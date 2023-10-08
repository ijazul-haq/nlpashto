import re, emoji
from .pashto import pashto

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
        self.alphabits=pashto['alphabits']
        self.numbers=pashto['numbers']
        self.punctuations=pashto['punctuations']
        pass
    def clean(self,text=None, split_into_sentences=True, remove_emojis=True, normalize_nums=True, remove_puncs=False,  special_chars=[]):
        sentence_delimiters='.۔'
        sentences=[]
        if(split_into_sentences==True):
            text=text.strip(sentence_delimiters)
            sentences=re.split(fr'{"|".join(re.escape(char) for char in sentence_delimiters)}', text)
        else:sentences=[text.strip()]
        cleaned_sentences=[]
        for sentence in sentences:
            allowed_chars=self.alphabits+self.numbers+special_chars
            if(normalize_nums):
                map_table = sentence.maketrans(normalize_numbers)
                sentence = sentence.translate(map_table)
            else:
                arabic_numbers=[key for key in normalize_numbers]
                allowed_chars+=arabic_numbers
                
            if(remove_puncs==False):
                allowed_chars+=self.punctuations
            sentence = [c if ((c in allowed_chars) or (remove_emojis == False and emoji.is_emoji(c))) else ' ' for c in sentence]
            if(remove_emojis==False):sentence=[' '+c+' ' if emoji.is_emoji(c) else c for c in sentence]
            sentence = ''.join(sentence)
            sentence = re.sub(f'[^{"|".join(re.escape(char) for char in self.alphabits)}]+', lambda c: " " + c[0] + " ", sentence)
            sentence = re.sub(' +', ' ', sentence)
            sentence=sentence.strip()
            cleaned_sentences.append(sentence)
        cleaned_sentences=cleaned_sentences if split_into_sentences==True else cleaned_sentences[0]
        return cleaned_sentences
    
