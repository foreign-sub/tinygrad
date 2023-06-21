<!-- markdownlint-disable -->

# <kbd>module</kbd> `graph`




**Global Variables**
---------------
- **GRAPH**
- **PRUNEGRAPH**
- **GRAPHPATH**
- **cnts**
- **node_count**

---

## <kbd>function</kbd> `nm`

```python
nm(x)
```






---

## <kbd>function</kbd> `get_sop`

```python
get_sop(
    op: List[Union[UnaryOps, BinaryOps, ReduceOps, MovementOps, LoadOps, FusedOps]]
)
```






---

## <kbd>function</kbd> `str_dtype`

```python
str_dtype(dtyp)
```






---

## <kbd>function</kbd> `log_op`

```python
log_op(
    ret: LazyBuffer,
    ast: LazyOp,
    show_graph: Optional[bool] = None,
    phantom=False
)
```






---

## <kbd>function</kbd> `prune_graph`

```python
prune_graph()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
