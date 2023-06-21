<!-- markdownlint-disable -->

# <kbd>module</kbd> `mlops`






---

## <kbd>class</kbd> `Contiguous`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x)
```






---

## <kbd>class</kbd> `Cast`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x, dtype)
```






---

## <kbd>class</kbd> `Sin`







---

### <kbd>method</kbd> `backward`

```python
backward(grad: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Relu`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Log`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Exp`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Sum`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, new_shape: Tuple[int, ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Max`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, new_shape: Tuple[int, ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Equal`







---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Maximum`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Add`







---

### <kbd>method</kbd> `backward`

```python
backward(
    grad_output: LazyBuffer
) → Tuple[Optional[LazyBuffer], Optional[LazyBuffer]]
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Sub`







---

### <kbd>method</kbd> `backward`

```python
backward(
    grad_output: LazyBuffer
) → Tuple[Optional[LazyBuffer], Optional[LazyBuffer]]
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer)
```






---

## <kbd>class</kbd> `Mul`







---

### <kbd>method</kbd> `backward`

```python
backward(
    grad_output: LazyBuffer
) → Tuple[Optional[LazyBuffer], Optional[LazyBuffer]]
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer)
```






---

## <kbd>class</kbd> `Pow`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer)
```






---

## <kbd>class</kbd> `Div`







---

### <kbd>method</kbd> `backward`

```python
backward(
    grad_output: LazyBuffer
) → Tuple[Optional[LazyBuffer], Optional[LazyBuffer]]
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, y: LazyBuffer) → LazyBuffer
```






---

## <kbd>class</kbd> `Expand`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, shape: Tuple[int, ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Reshape`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output)
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, shape: Tuple[int, ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Permute`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, order: Tuple[int, ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Pad`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, arg: Tuple[Tuple[int, int], ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Shrink`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, arg: Tuple[Tuple[int, int], ]) → LazyBuffer
```






---

## <kbd>class</kbd> `Flip`







---

### <kbd>method</kbd> `backward`

```python
backward(grad_output: LazyBuffer) → LazyBuffer
```





---

### <kbd>method</kbd> `forward`

```python
forward(x: LazyBuffer, axis: Tuple[int, ])
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
