<!-- markdownlint-disable -->

# API Overview

## Modules

- [`graph`](./graph.md#module-graph)
- [`helpers`](./helpers.md#module-helpers)
- [`jit`](./jit.md#module-jit)
- [`lazy`](./lazy.md#module-lazy)
- [`mlops`](./mlops.md#module-mlops)
- [`nn`](./nn.md#module-nn)
- [`nn.image`](./nn.image.md#module-nnimage)
- [`nn.optim`](./nn.optim.md#module-nnoptim)
- [`ops`](./ops.md#module-ops)
- [`state`](./state.md#module-state)
- [`tensor`](./tensor.md#module-tensor)

## Classes

- [`helpers.Context`](./helpers.md#class-context)
- [`helpers.ContextVar`](./helpers.md#class-contextvar)
- [`helpers.DType`](./helpers.md#class-dtype): DType(priority, itemsize, name, np, sz)
- [`helpers.GlobalCounters`](./helpers.md#class-globalcounters)
- [`helpers.ImageDType`](./helpers.md#class-imagedtype)
- [`helpers.Timing`](./helpers.md#class-timing)
- [`helpers.dtypes`](./helpers.md#class-dtypes): dtypes(bool: 'Final[DType]' = dtypes.bool, float16: 'Final[DType]' = dtypes.half, float32: 'Final[DType]' = dtypes.float, float64: 'Final[DType]' = dtypes.double, int8: 'Final[DType]' = dtypes.char, int32: 'Final[DType]' = dtypes.int, int64: 'Final[DType]' = dtypes.long, uint8: 'Final[DType]' = dtypes.uchar, uint32: 'Final[DType]' = dtypes.uint, uint64: 'Final[DType]' = dtypes.ulong, _half4: 'Final[DType]' = dtypes.half4, _float4: 'Final[DType]' = dtypes.float4)
- [`jit.TinyJit`](./jit.md#class-tinyjit)
- [`lazy.LazyBuffer`](./lazy.md#class-lazybuffer)
- [`mlops.Add`](./mlops.md#class-add)
- [`mlops.Cast`](./mlops.md#class-cast)
- [`mlops.Contiguous`](./mlops.md#class-contiguous)
- [`mlops.Div`](./mlops.md#class-div)
- [`mlops.Equal`](./mlops.md#class-equal)
- [`mlops.Exp`](./mlops.md#class-exp)
- [`mlops.Expand`](./mlops.md#class-expand)
- [`mlops.Flip`](./mlops.md#class-flip)
- [`mlops.Log`](./mlops.md#class-log)
- [`mlops.Max`](./mlops.md#class-max)
- [`mlops.Maximum`](./mlops.md#class-maximum)
- [`mlops.Mul`](./mlops.md#class-mul)
- [`mlops.Pad`](./mlops.md#class-pad)
- [`mlops.Permute`](./mlops.md#class-permute)
- [`mlops.Pow`](./mlops.md#class-pow)
- [`mlops.Relu`](./mlops.md#class-relu)
- [`mlops.Reshape`](./mlops.md#class-reshape)
- [`mlops.Shrink`](./mlops.md#class-shrink)
- [`mlops.Sin`](./mlops.md#class-sin)
- [`mlops.Sub`](./mlops.md#class-sub)
- [`mlops.Sum`](./mlops.md#class-sum)
- [`nn.BatchNorm2d`](./nn.md#class-batchnorm2d)
- [`nn.Conv2d`](./nn.md#class-conv2d)
- [`nn.ConvTranspose2d`](./nn.md#class-convtranspose2d)
- [`nn.Embedding`](./nn.md#class-embedding)
- [`nn.GroupNorm`](./nn.md#class-groupnorm)
- [`nn.InstanceNorm`](./nn.md#class-instancenorm)
- [`nn.LayerNorm`](./nn.md#class-layernorm)
- [`nn.LayerNorm2d`](./nn.md#class-layernorm2d)
- [`nn.Linear`](./nn.md#class-linear)
- [`optim.LAMB`](./nn.optim.md#class-lamb)
- [`optim.Optimizer`](./nn.optim.md#class-optimizer)
- [`optim.SGD`](./nn.optim.md#class-sgd)
- [`ops.ASTRunner`](./ops.md#class-astrunner)
- [`ops.BinaryOps`](./ops.md#class-binaryops): An enumeration.
- [`ops.Compiled`](./ops.md#class-compiled)
- [`ops.FlopCounter`](./ops.md#class-flopcounter)
- [`ops.FusedOps`](./ops.md#class-fusedops): An enumeration.
- [`ops.Interpreted`](./ops.md#class-interpreted)
- [`ops.LazyOp`](./ops.md#class-lazyop): LazyOp(op, src, arg)
- [`ops.LoadOps`](./ops.md#class-loadops): An enumeration.
- [`ops.ReduceOps`](./ops.md#class-reduceops): An enumeration.
- [`ops.UnaryOps`](./ops.md#class-unaryops): An enumeration.
- [`tensor.Function`](./tensor.md#class-function)
- [`tensor.Tensor`](./tensor.md#class-tensor)

## Functions

- [`graph.get_sop`](./graph.md#function-get_sop)
- [`graph.log_op`](./graph.md#function-log_op)
- [`graph.nm`](./graph.md#function-nm)
- [`graph.prune_graph`](./graph.md#function-prune_graph)
- [`graph.str_dtype`](./graph.md#function-str_dtype)
- [`lazy.create_lazybuffer`](./lazy.md#function-create_lazybuffer)
- [`lazy.elementwise_op`](./lazy.md#function-elementwise_op)
- [`lazy.get_movementroot`](./lazy.md#function-get_movementroot)
- [`lazy.get_movementroot_contiguous`](./lazy.md#function-get_movementroot_contiguous)
- [`lazy.get_single_root`](./lazy.md#function-get_single_root)
- [`lazy.get_weakop`](./lazy.md#function-get_weakop)
- [`lazy.replace_with_movement_ops`](./lazy.md#function-replace_with_movement_ops)
- [`nn.Conv1d`](./nn.md#function-conv1d)
- [`image.image_conv2d`](./nn.image.md#function-image_conv2d)
- [`image.image_dot`](./nn.image.md#function-image_dot)
- [`optim.Adam`](./nn.optim.md#function-adam)
- [`optim.AdamW`](./nn.optim.md#function-adamw)
- [`ops.get_buffers`](./ops.md#function-get_buffers)
- [`ops.get_lazyop_info`](./ops.md#function-get_lazyop_info)
- [`ops.get_lazyops`](./ops.md#function-get_lazyops)
- [`ops.map_buffers`](./ops.md#function-map_buffers)
- [`state.get_parameters`](./state.md#function-get_parameters)
- [`state.get_state_dict`](./state.md#function-get_state_dict)
- [`state.load_state_dict`](./state.md#function-load_state_dict)
- [`state.safe_load`](./state.md#function-safe_load)
- [`state.safe_save`](./state.md#function-safe_save)
- [`state.torch_load`](./state.md#function-torch_load)


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
