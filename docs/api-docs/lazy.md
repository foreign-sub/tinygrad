<!-- markdownlint-disable -->

# <kbd>module</kbd> `lazy`




**Global Variables**
---------------
- **OPT**
- **LAZY**
- **REMOVE_MOVEMENT_NOPS**
- **MERGE_ELEMENTWISE_INTO_REDUCE**
- **SHUFFLE_MOVEMENT_OPS**
- **MERGE_ELEMENTWISE_OPS**
- **MERGE_ONE_REDUCE_INTO_ELEMENTWISE**
- **SHUFFLE_PAD_OPS**
- **PUSH_PERMUTES**
- **PUSH_CONTIGUOUS**
- **Device**

---

## <kbd>function</kbd> `get_weakop`

```python
get_weakop(op: 'LazyOp') → LazyOp
```






---

## <kbd>function</kbd> `get_single_root`

```python
get_single_root(root: 'LazyBuffer') → LazyBuffer
```






---

## <kbd>function</kbd> `get_movementroot`

```python
get_movementroot(root: 'LazyBuffer', allow_contiguous=False) → LazyBuffer
```






---

## <kbd>function</kbd> `get_movementroot_contiguous`

```python
get_movementroot_contiguous(x: 'LazyBuffer') → LazyBuffer
```






---

## <kbd>function</kbd> `replace_with_movement_ops`

```python
replace_with_movement_ops(
    y: 'Union[LazyOp, LazyBuffer]',
    ops: 'List[Tuple[MovementOps, Tuple[Any, ]]]'
) → LazyBuffer
```






---

## <kbd>function</kbd> `create_lazybuffer`

```python
create_lazybuffer(
    device: 'str',
    shape: 'Union[ShapeTracker, Tuple[int, ]]',
    optype: 'OpType',
    op: 'LazyOp',
    dtype: 'DType'
)
```






---

## <kbd>function</kbd> `elementwise_op`

```python
elementwise_op(
    op: 'Union[UnaryOps, BinaryOps]',
    *srcs: 'LazyBuffer',
    arg: 'Optional[Any]' = None
) → LazyBuffer
```






---

## <kbd>class</kbd> `LazyBuffer`




### <kbd>method</kbd> `__init__`

```python
__init__(
    device: 'str',
    st: 'ShapeTracker',
    optype: 'OpType',
    src: 'Union[LazyOp, RawBuffer]',
    dtype: 'DType'
)
```








---

### <kbd>method</kbd> `binary_op`

```python
binary_op(self: 'LazyBuffer', op: 'BinaryOps', y: 'LazyBuffer') → LazyBuffer
```





---

### <kbd>method</kbd> `cast`

```python
cast(self: 'LazyBuffer', arg: 'DType') → LazyBuffer
```





---

### <kbd>method</kbd> `const_like`

```python
const_like(val) → LazyBuffer
```





---

### <kbd>method</kbd> `contiguous`

```python
contiguous(self: 'LazyBuffer') → LazyBuffer
```





---

### <kbd>method</kbd> `fromCPU`

```python
fromCPU(x: 'ndarray') → LazyBuffer
```





---

### <kbd>method</kbd> `loadop`

```python
loadop(op, shape, dtype, device, arg=None, src=None) → LazyBuffer
```





---

### <kbd>method</kbd> `movement_op`

```python
movement_op(
    self: 'LazyBuffer',
    op: 'MovementOps',
    arg: 'Tuple[Any, ]'
) → LazyBuffer
```





---

### <kbd>method</kbd> `realize`

```python
realize(self: 'LazyBuffer') → LazyBuffer
```





---

### <kbd>method</kbd> `reduce_op`

```python
reduce_op(
    self: 'LazyBuffer',
    op: 'ReduceOps',
    new_shape: 'Tuple[int, ]'
) → LazyBuffer
```





---

### <kbd>method</kbd> `toCPU`

```python
toCPU()
```





---

### <kbd>method</kbd> `unary_op`

```python
unary_op(self: 'LazyBuffer', op: 'UnaryOps') → LazyBuffer
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
