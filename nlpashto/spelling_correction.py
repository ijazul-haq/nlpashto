import numpy as np
import pickle
from .utils import preprocess

MODEL_PATH = "models/space_correct.sav"

def extract_features(sentence, index):
    char = sentence[index]
    features = {
        'c': char,
        'is_first': index == 0,
        'is_last': index == len(sentence)-1
    }
    for n in range(1,5):
        features['prev_'+str(n)] = ''.join(sentence[index-n:index+1])
        features['next_'+str(n)] = ''.join(sentence[index+1:index+n+2]) 
    return features

def space_correct(text):
    text = preprocess(text)
    text = [sentence.replace(' ','') for sentence in text]
    features = []
    for sentence in text:
        features.append([extract_features(sentence, index) for index in range(len(sentence))])

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    labels = model.predict(features)
    corrected_text = []
    for sentence, labels_ in zip(text, labels):
        corrected_sentence = ''
        for char, label in zip(sentence, labels_):
            corrected_sentence = corrected_sentence + char + label
        corrected_sentence = corrected_sentence.strip(' S')
        corrected_sentence = corrected_sentence.replace('J', '')
        corrected_sentence = corrected_sentence.split('S')
        corrected_text.append(corrected_sentence)
    return corrected_text
