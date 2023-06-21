<!-- markdownlint-disable -->

# <kbd>module</kbd> `nn.optim`





---

## <kbd>function</kbd> `AdamW`

```python
AdamW(params: List[Tensor], lr=0.001, b1=0.9, b2=0.999, eps=1e-08, wd=0.01)
```






---

## <kbd>function</kbd> `Adam`

```python
Adam(params: List[Tensor], lr=0.001, b1=0.9, b2=0.999, eps=1e-08)
```






---

## <kbd>class</kbd> `Optimizer`




### <kbd>method</kbd> `__init__`

```python
__init__(params: List[Tensor])
```








---

### <kbd>method</kbd> `realize`

```python
realize(extra=None)
```





---

### <kbd>method</kbd> `zero_grad`

```python
zero_grad()
```






---

## <kbd>class</kbd> `SGD`




### <kbd>method</kbd> `__init__`

```python
__init__(
    params: List[Tensor],
    lr=0.001,
    momentum=0,
    weight_decay=0.0,
    nesterov=False
)
```








---

### <kbd>method</kbd> `realize`

```python
realize(extra=None)
```





---

### <kbd>method</kbd> `step`

```python
step() → None
```





---

### <kbd>method</kbd> `zero_grad`

```python
zero_grad()
```






---

## <kbd>class</kbd> `LAMB`




### <kbd>method</kbd> `__init__`

```python
__init__(
    params: List[Tensor],
    lr=0.001,
    b1=0.9,
    b2=0.999,
    eps=1e-06,
    wd=0.0,
    adam=False
)
```








---

### <kbd>method</kbd> `realize`

```python
realize(extra=None)
```





---

### <kbd>method</kbd> `step`

```python
step() → None
```





---

### <kbd>method</kbd> `zero_grad`

```python
zero_grad()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
