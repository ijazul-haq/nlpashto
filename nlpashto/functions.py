from nlpashto.utils import features_segmenter, features_pos, basic_preprocessing, preprocess, features_tokenizer
import pickle, os

def tokenizer(text):
    text = preprocess(text)
    text = text.replace(' ', '')
    X_test = [features_tokenizer(text, index) for index in range(len(text))]
    path_ = os.path.join(os.path.dirname(__file__), "tokenizer.sav")
    model = pickle.load(open(path_, 'rb'))
    y_pred = model.predict_single(X_test)
    text_ = ''
    for c, t in zip(text, y_pred):
        text_ = text_ + c + t 
    text_ = text_.strip(' J').replace('S', ' ')
    text_ = text_.replace('J', '')
    return text_

def word_tokenizer(text):
    text = preprocess(text)
    text = text.split()
    X_test = [features_pos(text, index) for index in range(len(text))]
    path_ = os.path.join(os.path.dirname(__file__), "segmenter.sav")
    model = pickle.load(open(path_, 'rb'))
    y_pred = model.predict_single(X_test)
    text_ = ''
    for c, t in zip(text, y_pred):
        text_ = text_ + c + t 
    text_ = text_.strip(' SB')
    text_ = text_.replace('S', ' ').split('B')
    return text_

def sentence_tokenizer(text):
    text = basic_preprocessing(text)
    text = text.split('.')
    return text

def pos_tagger(text):
    X_test = [features_pos(text, index) for index in range(len(text))]
    path_ = os.path.join(os.path.dirname(__file__), "pos_tagger.sav")
    model = pickle.load(open(path_, 'rb'))
    y_pred = model.predict_single(X_test)
    text_ = []
    for c, t in zip(text, y_pred):
        text_.append([c,t])
    return text_

