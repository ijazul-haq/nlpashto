import torch, os, joblib
from .utils import get_asset

class Tokenizer():
    def __init__(self):
        self.model_path=get_asset('tokenizer.sav')
        self.model=joblib.load(self.model_path)
    
    def tokenize(self,text=None):
        if(isinstance(text, str)): text=[text]
        text=[item.replace(" ",'') for item in text]
        def features(sentence, index):
            char = sentence[index]
            features = {
                'c': char,
                'is_first': index == 0,
                'is_last': index == len(sentence)-1
            }
            for n in range(1,5):
                features['prev_'+str(n)] = ''.join(sentence[index-n:index])
                features['next_'+str(n)] = ''.join(sentence[index+1:index+1+n]) 
            return features

        X_test =[[features(sent, index) for index in range(len(sent))] for sent in text]
        y_pred = self.model.predict(X_test)
        res=[''.join([c+t for c,t in zip(sent,pred)]) for sent, pred in zip(text,y_pred)]
        res=[item.replace('J','').replace('S', ' ').strip().split() for item in res]
        return res