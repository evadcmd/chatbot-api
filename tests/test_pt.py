import torch


def test_dim():
    x = torch.arange(12).type(torch.float32)
    print(x)
    y = x.view(-1, 4)
    print(y)
