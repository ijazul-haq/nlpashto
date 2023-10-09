import re, emoji, requests, os
from .pashto import alphabits,numbers,punctuations,specials,sent_delimiters,diacritics, aesthetics, unknown
version='0.0.23'

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
    def _clean_token(self, token):
        url_chars =['http','//']
        if(re.search(f"[{'|'.join(re.escape(char) for char in url_chars)}]", token)):
            token=''
        elif(token[0]=='@' and len(token)>1):
            token=''
        elif(token[0]=='#' and len(token)>1):
            token=''
        return token
        
    def clean(self,text=None, split_into_sentences=True, remove_emojis=True, normalize_nums=True, remove_puncs=False, remove_special_chars=True,  special_chars=[],split_special_chars=True, remove_diacritics=False, sentence_delimiters=[]):
        assert (isinstance(text,list) or isinstance(text, str)), 'input text should be string or list'
        sentence_delimiters=sentence_delimiters or sent_delimiters
        sentences=[]
        if(split_into_sentences==True):
            if(isinstance(text, list)):
                sub_sentences = []
                for sent in text:
                    sub_sents=re.split(fr'{"|".join(re.escape(char) for char in sentence_delimiters)}', sent)
                    sub_sentences.extend(sub_sents)
                sentences.extend(sub_sentences)
            else:
                sub_sentences=re.split(fr'{"|".join(re.escape(char) for char in sentence_delimiters)}', text)
                sentences.extend(sub_sentences)
        else:
            if(isinstance(text, list)):sentences=text
            else:sentences=[text]
        
        cleaned_sentences=[]
        for sentence in sentences:
            sentence = re.sub(f"[{''.join(re.escape(char) for char in aesthetics+unknown)}]", '', sentence)
            tokenized_sentence=sentence.split()
            tokenized_sentence=[self._clean_token(token) for token in tokenized_sentence]
            sentence=' '.join(tokenized_sentence)
            
            allowed_chars=alphabits+numbers+special_chars+diacritics
            if(normalize_nums):
                map_table = sentence.maketrans(normalize_numbers)
                sentence = sentence.translate(map_table)
            else:
                arabic_numbers=[key for key in normalize_numbers]
                allowed_chars+=arabic_numbers           
            
            if(remove_puncs==False):allowed_chars+=punctuations
            if(remove_special_chars==False):allowed_chars+=specials
            
            # Remove diacritics
            if(remove_diacritics):          
                sentence = re.sub(f"[{''.join(re.escape(char) for char in diacritics)}]", '', sentence)
            
            # The main filter
            sentence = [c if ((c in allowed_chars) or (remove_emojis == False and emoji.is_emoji(c))) else ' ' for c in sentence]
            sentence = ''.join(sentence)
            
            # Remove repeated chars
            sentence = re.sub(f'((?!["{"|".join(re.escape(char) for char in alphabits+numbers)}"]).)\\1+', '\\1', sentence)
            
            # Split special chars
            if(split_special_chars):
                sentence = re.sub(f"[^{re.escape(''.join(alphabits+numbers+diacritics))}]", ' \\g<0> ', sentence)
            
            # Remove repeated chars
            sentence = re.sub(f'((?!["{"|".join(re.escape(char) for char in alphabits+numbers)}"]).)\\1+', '\\1', sentence)
            sentence=sentence.strip()
            if(len(sentence)>0):cleaned_sentences.append(sentence)
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
        print('Downloaded Successfully!')
    else: print(f'Failed to download {asset_name}. Status code: {response.status_code}')