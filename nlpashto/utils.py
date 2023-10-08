import re, emoji, requests, os
from .pashto import alphabits,diacritics,numbers,punctuations,specials,sentence_delimiters
version='0.0.16'

normalize_numbers = {
    '0': '۰',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹',
    '٠': '۰',
    '١': '۱',
    '٢': '۲',
    '٣': '۳',
    '٤': '۴',
    '٥': '۵',
    '٦': '۶',
    '٧': '۷',
    '٨': '۸',
    '٩': '۹'
}

class Cleaner():
    def __init__(self):
        pass
    def clean(self,text=None, split_into_sentences=True, remove_emojis=True, normalize_nums=True, remove_puncs=False, remove_special_chars=True,  special_chars=[]):
        sentences=[]
        if(split_into_sentences==True):
            assert isinstance(text, str), 'If input text is List, "split_into_sentences" should be False'
            text=text.strip(sentence_delimiters)
            sentences=re.split(fr'{"|".join(re.escape(char) for char in sentence_delimiters)}', text)
        else:sentences=[text.strip()]
        cleaned_sentences=[]
        for sentence in sentences:
            allowed_chars=alphabits+diacritics+numbers+special_chars
            if(normalize_nums):
                map_table = sentence.maketrans(normalize_numbers)
                sentence = sentence.translate(map_table)
            else:
                arabic_numbers=[key for key in normalize_numbers]
                allowed_chars+=arabic_numbers
                
            if(remove_puncs==False):allowed_chars+=punctuations
            if(remove_special_chars==False):allowed_chars+=specials

            sentence = [c if ((c in allowed_chars) or (remove_emojis == False and emoji.is_emoji(c))) else ' ' for c in sentence]
            if(remove_emojis==False):sentence=[' '+c+' ' if emoji.is_emoji(c) else c for c in sentence]
            sentence = ''.join(sentence)
            sentence = re.sub(f'[^{"|".join(re.escape(char) for char in alphabits)}]+', lambda c: " " + c[0] + " ", sentence)
            sentence = re.sub(' +', ' ', sentence)
            sentence=sentence.strip()
            cleaned_sentences.append(sentence)
        cleaned_sentences=cleaned_sentences if split_into_sentences==True else cleaned_sentences[0]
        return cleaned_sentences
    
def get_asset(asset_name=None, force_download=False):
    target_directory = os.path.join(os.path.expanduser("~"), ".nlpashto")
    os.makedirs(target_directory, exist_ok=True)
    asset_path = os.path.join(target_directory, asset_name)
    if os.path.exists(asset_path):
        if(force_download):
            download(asset_name, asset_path)
            return asset_path
        else: return asset_path
    else:
        download(asset_name, asset_path)
        return asset_path
    
def download(asset_name, asset_path):
    print('Downloading...')
    download_url = f'https://github.com/ijazul-haq/nlpashto/releases/download/{version}/{asset_name}'
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(asset_path, 'wb') as file:
            file.write(response.content)
        return True
    else: print(f'Failed to download {asset_name}. Status code: {response.status_code}')