import numpy as np
import pickle
from .utils import preprocess
import keras
from keras.utils import pad_sequences

MODEL_DIR = "models/"
MODEL_NAME ="pold.h5"
TOKENIZER = 'tokenizer.pickle'
SEQ_LEN = 100
def extract_features(text):
    with open(MODEL_DIR+TOKENIZER, 'rb') as f:
        tokenizer = pickle.load(f)
    seq = tokenizer.texts_to_sequences(text)
    seq_padded = pad_sequences(seq, maxlen=SEQ_LEN)
    return seq_padded

def pold(text):
    seq_padded = extract_features([text])
    model = keras.models.load_model(MODEL_DIR+MODEL_NAME)
    preds = model.predict(seq_padded, verbose=0)
    preds = np.rint(preds.flatten())
    return preds
