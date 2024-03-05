"""
Model training and testing
"""
__author__ = "boblyx"
import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0,1],
                           [1,2],
                           [2,0]], dtype=torch.long)

x = torch.tensor([[0,0], [1,1],[1,0]], dtype=torch.float) # Node feature - coordinates

shape = [3]

data = Data(pos=x, edge_index = edge_index.t().contiguous(), shape = shape)
data.validate(raise_on_error = True)
print(data);
