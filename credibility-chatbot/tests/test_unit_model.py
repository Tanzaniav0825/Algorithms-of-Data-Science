import torch
from credscore.model.network import CredScoreNet
def test_forward_shapes():
 m=CredScoreNet(d_features=8); x=torch.randn(4,8); p,v=m(x); assert p.shape==(4,) and v.shape==(4,) and (p>=0).all() and (p<=1).all() and (v>0).all()
