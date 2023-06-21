<!-- markdownlint-disable -->

# <kbd>module</kbd> `state`




**Global Variables**
---------------
- **safe_dtypes**
- **inverse_safe_dtypes**

---

## <kbd>function</kbd> `safe_load`

```python
safe_load(fn: Union[Tensor, str]) → Dict[str, Tensor]
```






---

## <kbd>function</kbd> `safe_save`

```python
safe_save(tensors: Dict[str, Tensor], fn: str)
```






---

## <kbd>function</kbd> `get_state_dict`

```python
get_state_dict(
    obj,
    prefix: str = '',
    tensor_type=<class 'tinygrad.tensor.Tensor'>
) → Dict[str, Tensor]
```






---

## <kbd>function</kbd> `get_parameters`

```python
get_parameters(obj) → List[Tensor]
```






---

## <kbd>function</kbd> `load_state_dict`

```python
load_state_dict(model, state_dict, strict=True)
```






---

## <kbd>function</kbd> `torch_load`

```python
torch_load(fn: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
