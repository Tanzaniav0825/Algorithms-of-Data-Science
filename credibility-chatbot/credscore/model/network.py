import torch, torch.nn as nn
class CredScoreNet(nn.Module):
    def __init__(self,d_features=8,d_model=32):
        super().__init__(); self.net=nn.Sequential(nn.Linear(d_features,d_model),nn.ReLU(),nn.Linear(d_model,1))
    def forward(self,x):
        p=torch.sigmoid(self.net(x)).squeeze(-1); var=torch.full_like(p,0.05); return p,var
