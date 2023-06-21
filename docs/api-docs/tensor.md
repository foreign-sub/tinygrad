<!-- markdownlint-disable -->

# <kbd>module</kbd> `tensor`




**Global Variables**
---------------
- **pi**
- **device**


---

## <kbd>class</kbd> `Function`




### <kbd>method</kbd> `__init__`

```python
__init__(device: 'str', *tensors: 'Tensor')
```








---

### <kbd>classmethod</kbd> `apply`

```python
apply(*x: 'Tensor', **kwargs) → Tensor
```





---

### <kbd>method</kbd> `backward`

```python
backward(*args, **kwargs)
```





---

### <kbd>method</kbd> `forward`

```python
forward(*args, **kwargs)
```






---

## <kbd>class</kbd> `Tensor`




### <kbd>method</kbd> `__init__`

```python
__init__(
    data: 'Union[int, float, list, tuple, LazyBuffer, ndarray]',
    device='CUDA',
    dtype: 'Optional[DType]' = None,
    requires_grad: 'Optional[bool]' = None
)
```






---

#### <kbd>property</kbd> T





---

#### <kbd>property</kbd> device





---

#### <kbd>property</kbd> dtype





---

#### <kbd>property</kbd> ndim





---

#### <kbd>property</kbd> shape







---

### <kbd>method</kbd> `abs`

```python
abs()
```





---

### <kbd>method</kbd> `add`

```python
add(x: 'Union[Tensor, float]', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `arange`

```python
arange(stop, start=0, step=1, **kwargs)
```





---

### <kbd>method</kbd> `assign`

```python
assign(x) → Tensor
```





---

### <kbd>method</kbd> `avg_pool2d`

```python
avg_pool2d(kernel_size=(2, 2), stride=None)
```





---

### <kbd>method</kbd> `backward`

```python
backward()
```





---

### <kbd>method</kbd> `batchnorm`

```python
batchnorm(
    weight: 'Optional[Tensor]',
    bias: 'Optional[Tensor]',
    mean: 'Tensor',
    invstd: 'Tensor'
) → Tensor
```





---

### <kbd>method</kbd> `cast`

```python
cast(dtype: 'DType') → Tensor
```





---

### <kbd>method</kbd> `cat`

```python
cat(*args, dim=0)
```





---

### <kbd>method</kbd> `ceil`

```python
ceil(self: 'Tensor') → Tensor
```





---

### <kbd>method</kbd> `celu`

```python
celu(alpha=1.0)
```





---

### <kbd>method</kbd> `chunk`

```python
chunk(num, dim)
```





---

### <kbd>method</kbd> `clip`

```python
clip(min_, max_)
```





---

### <kbd>method</kbd> `contiguous`

```python
contiguous()
```





---

### <kbd>method</kbd> `conv2d`

```python
conv2d(
    weight: 'Tensor',
    bias: 'Optional[Tensor]' = None,
    groups=1,
    stride=1,
    dilation=1,
    padding=0
) → Tensor
```





---

### <kbd>method</kbd> `conv_transpose2d`

```python
conv_transpose2d(
    weight: 'Tensor',
    bias: 'Optional[Tensor]' = None,
    groups=1,
    stride=1,
    dilation=1,
    padding=0,
    output_padding=0
) → Tensor
```





---

### <kbd>method</kbd> `cos`

```python
cos()
```





---

### <kbd>method</kbd> `cumsum`

```python
cumsum(axis=0)
```





---

### <kbd>method</kbd> `deepwalk`

```python
deepwalk()
```





---

### <kbd>method</kbd> `detach`

```python
detach()
```





---

### <kbd>method</kbd> `div`

```python
div(x: 'Union[Tensor, float]', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `dot`

```python
dot(w: 'Tensor') → Tensor
```





---

### <kbd>method</kbd> `dropout`

```python
dropout(p=0.5) → Tensor
```





---

### <kbd>method</kbd> `element_size`

```python
element_size() → int
```





---

### <kbd>method</kbd> `elu`

```python
elu(alpha=1.0)
```





---

### <kbd>method</kbd> `empty`

```python
empty(*shape, **kwargs)
```





---

### <kbd>method</kbd> `eq`

```python
eq(x) → Tensor
```





---

### <kbd>method</kbd> `exp`

```python
exp()
```





---

### <kbd>method</kbd> `expand`

```python
expand(shape, *args) → Tensor
```





---

### <kbd>method</kbd> `eye`

```python
eye(dim, **kwargs)
```





---

### <kbd>method</kbd> `flatten`

```python
flatten(start_dim=0)
```





---

### <kbd>method</kbd> `flip`

```python
flip(axis, *args) → Tensor
```





---

### <kbd>method</kbd> `float`

```python
float() → Tensor
```





---

### <kbd>method</kbd> `floor`

```python
floor(self: 'Tensor') → Tensor
```





---

### <kbd>method</kbd> `full`

```python
full(shape: 'Tuple[int, ]', fill_value, **kwargs)
```





---

### <kbd>method</kbd> `full_like`

```python
full_like(tensor, fill_value, dtype: 'Optional[DType]' = None, **kwargs)
```





---

### <kbd>method</kbd> `gelu`

```python
gelu()
```





---

### <kbd>method</kbd> `glorot_uniform`

```python
glorot_uniform(*shape, **kwargs) → Tensor
```





---

### <kbd>method</kbd> `half`

```python
half() → Tensor
```





---

### <kbd>method</kbd> `hardswish`

```python
hardswish()
```





---

### <kbd>method</kbd> `hardtanh`

```python
hardtanh(min_val=-1, max_val=1)
```





---

### <kbd>method</kbd> `is_floating_point`

```python
is_floating_point() → bool
```





---

### <kbd>method</kbd> `kaiming_uniform`

```python
kaiming_uniform(*shape, a: 'float' = 0.01, **kwargs) → Tensor
```





---

### <kbd>method</kbd> `layernorm`

```python
layernorm(axis=-1, eps: 'float' = 1e-05) → Tensor
```





---

### <kbd>method</kbd> `leakyrelu`

```python
leakyrelu(neg_slope=0.01)
```





---

### <kbd>method</kbd> `linear`

```python
linear(weight: 'Tensor', bias: 'Optional[Tensor]' = None)
```





---

### <kbd>method</kbd> `log`

```python
log()
```





---

### <kbd>method</kbd> `log_softmax`

```python
log_softmax(axis=-1)
```





---

### <kbd>method</kbd> `manual_seed`

```python
manual_seed(seed=None)
```





---

### <kbd>method</kbd> `matmul`

```python
matmul(x: 'Tensor', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `max`

```python
max(axis=None, keepdim=False)
```





---

### <kbd>method</kbd> `max_pool2d`

```python
max_pool2d(kernel_size=(2, 2), stride=None, dilation=1)
```





---

### <kbd>method</kbd> `maximum`

```python
maximum(x: 'Union[Tensor, float]') → Tensor
```





---

### <kbd>method</kbd> `mean`

```python
mean(axis=None, keepdim=False)
```





---

### <kbd>method</kbd> `min`

```python
min(axis=None, keepdim=False)
```





---

### <kbd>method</kbd> `minimum`

```python
minimum(x: 'Union[Tensor, float]') → Tensor
```





---

### <kbd>method</kbd> `mish`

```python
mish()
```





---

### <kbd>method</kbd> `mul`

```python
mul(x: 'Union[Tensor, float]', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `nbytes`

```python
nbytes() → int
```





---

### <kbd>method</kbd> `numel`

```python
numel() → int
```





---

### <kbd>method</kbd> `numpy`

```python
numpy() → ndarray
```





---

### <kbd>method</kbd> `ones`

```python
ones(*shape, **kwargs)
```





---

### <kbd>method</kbd> `ones_like`

```python
ones_like(tensor, **kwargs)
```





---

### <kbd>method</kbd> `pad`

```python
pad(arg: 'Tuple[Tuple[int, int], ]') → Tensor
```





---

### <kbd>method</kbd> `pad2d`

```python
pad2d(padding: 'Union[List[int], Tuple[int, ]]')
```





---

### <kbd>method</kbd> `permute`

```python
permute(order, *args) → Tensor
```





---

### <kbd>method</kbd> `pow`

```python
pow(x: 'Union[Tensor, float]', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `quick_gelu`

```python
quick_gelu()
```





---

### <kbd>method</kbd> `rand`

```python
rand(*shape, **kwargs)
```





---

### <kbd>method</kbd> `randn`

```python
randn(*shape, dtype: 'Optional[DType]' = None, **kwargs) → Tensor
```





---

### <kbd>method</kbd> `realize`

```python
realize() → Tensor
```





---

### <kbd>method</kbd> `reciprocal`

```python
reciprocal()
```





---

### <kbd>method</kbd> `relu`

```python
relu()
```





---

### <kbd>method</kbd> `relu6`

```python
relu6()
```





---

### <kbd>method</kbd> `repeat`

```python
repeat(repeats)
```





---

### <kbd>method</kbd> `reshape`

```python
reshape(shape, *args) → Tensor
```





---

### <kbd>method</kbd> `rsqrt`

```python
rsqrt()
```





---

### <kbd>method</kbd> `scaled_uniform`

```python
scaled_uniform(*shape, **kwargs) → Tensor
```





---

### <kbd>method</kbd> `sequential`

```python
sequential(ll: 'List[Callable[[Tensor], Tensor]]')
```





---

### <kbd>method</kbd> `shrink`

```python
shrink(arg: 'Tuple[Tuple[int, int], ]') → Tensor
```





---

### <kbd>method</kbd> `sigmoid`

```python
sigmoid()
```





---

### <kbd>method</kbd> `sign`

```python
sign()
```





---

### <kbd>method</kbd> `silu`

```python
silu()
```





---

### <kbd>method</kbd> `sin`

```python
sin()
```





---

### <kbd>method</kbd> `slice`

```python
slice(arg: 'Sequence[Optional[Tuple[int, int]]]') → Tensor
```





---

### <kbd>method</kbd> `softmax`

```python
softmax(axis=-1)
```





---

### <kbd>method</kbd> `softplus`

```python
softplus(beta=1)
```





---

### <kbd>method</kbd> `softsign`

```python
softsign()
```





---

### <kbd>method</kbd> `sqrt`

```python
sqrt()
```





---

### <kbd>method</kbd> `square`

```python
square()
```





---

### <kbd>method</kbd> `stack`

```python
stack(tensors, dim=0)
```





---

### <kbd>method</kbd> `std`

```python
std(axis=None, keepdim=False, correction=1)
```





---

### <kbd>method</kbd> `sub`

```python
sub(x: 'Union[Tensor, float]', reverse=False) → Tensor
```





---

### <kbd>method</kbd> `sum`

```python
sum(axis=None, keepdim=False)
```





---

### <kbd>method</kbd> `swish`

```python
swish()
```





---

### <kbd>method</kbd> `tan`

```python
tan()
```





---

### <kbd>method</kbd> `tanh`

```python
tanh()
```





---

### <kbd>method</kbd> `to`

```python
to(device: 'str')
```





---

### <kbd>method</kbd> `to_`

```python
to_(device: 'str')
```





---

### <kbd>method</kbd> `transpose`

```python
transpose(ax1=1, ax2=0) → Tensor
```





---

### <kbd>method</kbd> `tril`

```python
tril(k: 'int' = 0) → Tensor
```





---

### <kbd>method</kbd> `triu`

```python
triu(k: 'int' = 0) → Tensor
```





---

### <kbd>method</kbd> `uniform`

```python
uniform(*shape, low=-1.0, high=1.0, **kwargs) → Tensor
```





---

### <kbd>method</kbd> `unsqueeze`

```python
unsqueeze(dim)
```





---

### <kbd>method</kbd> `where`

```python
where(
    self: 'Tensor',
    input_: 'Union[Tensor, float]',
    other: 'Union[Tensor, float]'
)
```





---

### <kbd>method</kbd> `zeros`

```python
zeros(*shape, **kwargs)
```





---

### <kbd>method</kbd> `zeros_like`

```python
zeros_like(tensor, **kwargs)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
