from autograd.Tensor import Tensor, Dependency
import numpy as np


def tanh(tensor: Tensor):
    data = np.tanh(tensor.data)
    requires_grad = tensor.requires_grad

    if requires_grad:
        def grad_fn(grad: np.ndarray) -> np.ndarray:
            return grad * (1 - data * data)
        depends_on = [Dependency(tensor, grad_fn)]
    else:
        depends_on = []

    return Tensor(data, requires_grad, depends_on)
