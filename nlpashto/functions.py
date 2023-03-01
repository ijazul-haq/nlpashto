from nlpashto.utils import features_segmenter, features_pos, preprocess
import pickle, os

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

def pos_tagger(text):
    X_test = [features_pos(text, index) for index in range(len(text))]
    path_ = os.path.join(os.path.dirname(__file__), "pos_tagger.sav")
    model = pickle.load(open(path_, 'rb'))
    y_pred = model.predict_single(X_test)
    text_ = []
    for c, t in zip(text, y_pred):
        text_.append([c,t])
    return text_