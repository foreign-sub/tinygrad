<!-- markdownlint-disable -->

# <kbd>module</kbd> `ops`




**Global Variables**
---------------
- **shape_fxn_for_op**
- **InterpretedFlopCounter**

---

## <kbd>function</kbd> `get_buffers`

```python
get_buffers(op: 'LazyOp') → List[Any]
```






---

## <kbd>function</kbd> `get_lazyops`

```python
get_lazyops(op: 'LazyOp') → List[LazyOp]
```






---

## <kbd>function</kbd> `map_buffers`

```python
map_buffers(real_srcs: 'Dict[Any, Any]', x: 'Any') → LazyOp
```






---

## <kbd>function</kbd> `get_lazyop_info`

```python
get_lazyop_info(ast: 'LazyOp') → FlopCounter
```






---

## <kbd>class</kbd> `UnaryOps`
An enumeration. 





---

## <kbd>class</kbd> `BinaryOps`
An enumeration. 





---

## <kbd>class</kbd> `ReduceOps`
An enumeration. 





---

## <kbd>class</kbd> `FusedOps`
An enumeration. 





---

## <kbd>class</kbd> `LoadOps`
An enumeration. 





---

## <kbd>class</kbd> `LazyOp`
LazyOp(op, src, arg) 





---

## <kbd>class</kbd> `Interpreted`




### <kbd>method</kbd> `__init__`

```python
__init__(
    buffer,
    fxn_for_op: 'Dict[Op, Callable]',
    from_lazybuffer=<function Interpreted.<lambda> at 0x7f62d8d2bb80>,
    to_underlying=<function Interpreted.<lambda> at 0x7f62d8d2bc10>,
    from_underlying=None
)
```








---

### <kbd>method</kbd> `exec_ast`

```python
exec_ast(ast: 'LazyOp', output=None, context=None, **kwargs)
```






---

## <kbd>class</kbd> `FlopCounter`




### <kbd>method</kbd> `__init__`

```python
__init__(tup: 'Tuple[Tuple[int, ], DType, int]')
```








---

### <kbd>method</kbd> `consume_flops`

```python
consume_flops()
```






---

## <kbd>class</kbd> `ASTRunner`




### <kbd>method</kbd> `__init__`

```python
__init__(
    name,
    prg,
    global_size: 'Optional[List[int]]' = None,
    local_size: 'Optional[List[int]]' = None,
    op_estimate=0,
    mem_estimate=0,
    display_name: 'Optional[str]' = None,
    runtime_args: 'Optional[dict]' = None
)
```








---

### <kbd>method</kbd> `build`

```python
build(runtime)
```





---

### <kbd>method</kbd> `exec`

```python
exec(bufs) → Optional[float]
```






---

## <kbd>class</kbd> `Compiled`




### <kbd>method</kbd> `__init__`

```python
__init__(
    buffer: 'Type[RawBuffer]',
    codegen,
    runtime,
    synchronize=<function Compiled.<lambda> at 0x7f62d8d4f0d0>
)
```








---

### <kbd>method</kbd> `exec_ast`

```python
exec_ast(ast: 'LazyOp', output, **kwargs)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
