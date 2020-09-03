import torch.nn as nn
import torch

def KLDLoss(mu, logvar):
    return -0.5 * torch.mean(torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), axis=(1, 2, 3)))

class Loss(nn.Module):
    def __init__(self, dic):
        super(Loss, self).__init__()
        self.w_kl = dic['w_kl']

    def forward(self, target, inp, mu, covar):

        L_kl = KLDLoss(mu, covar)

        L_recon = torch.mean(torch.abs(inp - target))

        Loss = L_kl * self.w_kl + L_recon

        return Loss, L_recon, L_kl
