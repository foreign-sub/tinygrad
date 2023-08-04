import mmap
import tempfile
from typing import Callable, Dict
from tinygrad.helpers import DType
from tinygrad.runtime.lib import RawBufferMapped
from tinygrad.ops import Interpreted, Op, UnaryOps, MovementOps

TMPFS_CACHE: Dict[str, mmap.mmap] = {}
class RawTmpFSBuffer(RawBufferMapped):
  def __init__(self, size, dtype: DType, device: str):
    device, self.cache_id = (device.split(",")[0], None if "," not in device else device.split(",")[1])
    if self.cache_id is not None and self.cache_id in TMPFS_CACHE: shm = TMPFS_CACHE[self.cache_id]
    else:
      tmp_file = tempfile.TemporaryFile(dir="/dev/shm")  # /dev/shm is a tmpfs mountpoint
      length=size * dtype.itemsize
      tmp_file.write(b'\x00' * length)
      tmp_file.flush()
      # MAP_LOCKED 0x02000 | MAP_POPULATE 0x08000
      shm = mmap.mmap(tmp_file.fileno(), length, flags=mmap.MAP_SHARED | 0x02000 | 0x08000, prot=mmap.PROT_READ | mmap.PROT_WRITE)
      shm.madvise(mmap.MADV_HUGEPAGE)
      tmp_file.close()
      if self.cache_id is not None: TMPFS_CACHE[self.cache_id] = shm

    super().__init__(size, dtype, shm)

  def __del__(self):
    if self.cache_id is None: self._buf.close()

  def _buffer(self): return memoryview(self._buf)

tmpfs_fxn_for_op: Dict[Op, Callable] = {UnaryOps.NOOP: lambda x: x, MovementOps.RESHAPE: lambda x, _: x}
TmpFSBuffer = Interpreted(RawTmpFSBuffer, tmpfs_fxn_for_op, to_underlying=lambda x: x, from_underlying=lambda x: x)
