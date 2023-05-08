import numpy as np
import pickle
from .utils import preprocess

MODEL_PATH = "models/segmenter.sav"

def extract_features(sentence, index):
    token = sentence[index]
    prev_1 = ''.join(sentence[index-1:index+1])
    next_1 = ''.join(sentence[index+1:index+2])
    
    features = {
        'token': token,
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'length': len(token),
        'is_numeric': token.isdigit(),
        'pfx_1': token[0] if(len(token) > 2) else '',
        'pfx_2': token[:2] if(len(token) > 3) else '',
        'pfx_3': token[:3] if(len(token) > 4) else '',
        'sfx_1': token[-1] if(len(token) > 2) else '',
        'sfx_2': token[-2:] if(len(token) > 3) else '',
        'sfx_3': token[-3:] if(len(token) > 4) else '',
        
        'prev_1': prev_1,
        'prev_1_len': len(prev_1),
        'prev_1_pfx_1': '' if (not prev_1 or len(prev_1)<3) else prev_1[0],
        'prev_1_pfx_2': '' if (not prev_1 or len(prev_1)<4) else prev_1[:2],
        'prev_1_sfx_1': '' if (not prev_1 or len(prev_1)<3) else prev_1[-1],
        'prev_1_sfx_2': '' if (not prev_1 or len(prev_1)<4) else prev_1[-2:],
        'prev_2': '' if(index<2) else ''.join(sentence[index-2:index-1]),
        
        'next_1': next_1,
        'next_1_len': len(next_1),
        'next_1_pfx_1': '' if (not next_1 or len(next_1)<3) else next_1[0],       
        'next_1_pfx_2': '' if (not next_1 or len(next_1)<4) else next_1[:2],       
        'next_1_sfx_1': '' if (not next_1 or len(next_1)<3) else next_1[-1],       
        'next_1_sfx_2': '' if (not next_1 or len(next_1)<4) else next_1[-2:],       
        'next_2': ''.join(sentence[index+2:index+3])
      }
    return features

def segment_words(text):
    text = preprocess(text)
    text = [sentence.split() for sentence in text]
    features = []
    for sentence in text:
        features.append([extract_features(sentence, index) for index in range(len(sentence))])

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    labels = model.predict(features)
    segmented_text = []
    for sentence, labels_ in zip(text, labels):
        segmented_sentence = ''
        for token, label in zip(sentence, labels_):
            segmented_sentence = segmented_sentence + token + label
        segmented_sentence = segmented_sentence.strip(' SB')
        segmented_sentence = segmented_sentence.replace('S', ' ').split('B')
        segmented_text.append(segmented_sentence)
    return segmented_text
