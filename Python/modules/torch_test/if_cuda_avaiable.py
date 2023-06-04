import torch

# 判断cuda是否可用
cuda_available = torch.cuda.is_available()

print(cuda_available)

x = torch.randn((4, 4), requires_grad=True)
y = 2 * x
z = y.sum()

print(z.requires_grad)

z.backward()

print(x.grad)
