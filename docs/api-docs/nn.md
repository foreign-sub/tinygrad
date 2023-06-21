<!-- markdownlint-disable -->

# <kbd>module</kbd> `nn`





---

## <kbd>function</kbd> `Conv1d`

```python
Conv1d(
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True
)
```






---

## <kbd>class</kbd> `BatchNorm2d`




### <kbd>method</kbd> `__init__`

```python
__init__(sz, eps=1e-05, affine=True, track_running_stats=True, momentum=0.1)
```









---

## <kbd>class</kbd> `Conv2d`




### <kbd>method</kbd> `__init__`

```python
__init__(
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    dilation=1,
    groups=1,
    bias=True
)
```









---

## <kbd>class</kbd> `ConvTranspose2d`




### <kbd>method</kbd> `__init__`

```python
__init__(
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    output_padding=0,
    dilation=1,
    groups=1,
    bias=True
)
```









---

## <kbd>class</kbd> `Linear`




### <kbd>method</kbd> `__init__`

```python
__init__(in_features, out_features, bias=True)
```









---

## <kbd>class</kbd> `GroupNorm`




### <kbd>method</kbd> `__init__`

```python
__init__(
    num_groups: int,
    num_channels: int,
    eps: float = 1e-05,
    affine: bool = True
)
```









---

## <kbd>class</kbd> `InstanceNorm`




### <kbd>method</kbd> `__init__`

```python
__init__(num_features: int, eps: float = 1e-05, affine: bool = True)
```









---

## <kbd>class</kbd> `LayerNorm`




### <kbd>method</kbd> `__init__`

```python
__init__(
    normalized_shape: Union[int, Tuple[int, ]],
    eps: float = 1e-05,
    elementwise_affine: bool = True
)
```









---

## <kbd>class</kbd> `LayerNorm2d`




### <kbd>method</kbd> `__init__`

```python
__init__(
    normalized_shape: Union[int, Tuple[int, ]],
    eps: float = 1e-05,
    elementwise_affine: bool = True
)
```









---

## <kbd>class</kbd> `Embedding`




### <kbd>method</kbd> `__init__`

```python
__init__(vocab_size: int, embed_size: int)
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
