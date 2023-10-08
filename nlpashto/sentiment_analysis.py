import torch, os
from transformers import pipeline
if torch.cuda.is_available():device = torch.device("cuda")
else:device = torch.device("cpu")

class POLD():
    def __init__(self): 
        self.pipe=pipeline(model='ijazulhaq/pold')
    def predict(self,text=None):
        preds=self.pipe(text)
        preds=[int(item['label'].split('_')[1]) for item in preds]
        return preds