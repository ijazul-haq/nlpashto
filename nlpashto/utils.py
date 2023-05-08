import re
from .helpers import alphabits, digits, char_replace, diacritics
uk = 'ـ'
punc = '٪.،؟'

def preprocess(c):
    special_char_dict = {}
    for r in char_replace:
        old, new = r[0], r[1]
        special_char_dict[old] = new
    
    map_table = c.maketrans(special_char_dict)
    c = c.translate(map_table)
    c = c.replace(uk, '')
    
    res = [ele if (ele in alphabits) or (ele in digits) or (ele in punc) else  ' ' for ele in c]
    c = ''.join(res)
    c = re.sub("["+digits+"]+", lambda ele: " " + ele[0] + " ", c)
    c = c.replace('\n', ' ')
    c = re.sub('\.+', '.', c)
    c = re.sub('،+', '،', c)
    c = re.sub('٪+', '٪', c)
    c = c.replace('، ،', '،').replace('٪ ٪', '٪')
    c = re.sub(' +', ' ', c)
    c = c.strip(' ،.')
    c = re.split('؟|\.', c)
    return c


def download(model_name=''):
    models = ['space_correct', 'pos_tag', 'word_segment', 'pos_tag', 'pold', 'snd']
    if(model_name!=''):
        if(model_name in models):
            models = [model_name]
        else: 
            print('Resource name is invalid')
            return

    import os
    import requests
    
    for model_name in models:
        MODELS_DIR = 'models/'
        SAVE_PATH = f"{MODELS_DIR+model_name}.sav"
        MODEL_URL = f'https://github.com/ijazul-haq/nlpashto/raw/main/nlpashto/models/{model_name}.sav'

        if os.path.exists(SAVE_PATH):
            print(f"Model already exists at {SAVE_PATH}. Skipping download.")
            return
        try:
            if (not os.path.exists(MODELS_DIR)): os.makedirs(MODELS_DIR)
            print('Downloading...')
            response = requests.get(MODEL_URL, stream=True, timeout=180)
            response.raise_for_status()
            r = requests.get(MODEL_URL, stream = True)
            with open(SAVE_PATH, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: f.write(chunk)

            print(f"Model downloaded and saved to {SAVE_PATH}.")
        except Exception as e:
            raise Exception(f"Failed to download model from {MODEL_URL}: {e}")
        
