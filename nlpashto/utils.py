import re
from nlpashto.char_replace import char_replace

def features_segmenter(sentence, index):
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
        'next_2': ''.join(sentence[index+2:index+3]),
    }
    return features


def features_pos(sentence, index):
    token = sentence[index]
    prev_1 = ''.join(sentence[index-1:index])
    next_1 = ''.join(sentence[index+1:index+2])
    prev_2 = '' if(index<2) else ''.join(sentence[index-2:index-1])
    next_2 = ''.join(sentence[index+2:index+3])
    
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
        'prev_2': prev_2,
        
        'next_1': next_1,
        'next_1_len': len(next_1),
        'next_1_pfx_1': '' if (not next_1 or len(next_1)<3) else next_1[0],       
        'next_1_pfx_2': '' if (not next_1 or len(next_1)<4) else next_1[:2],       
        'next_1_sfx_1': '' if (not next_1 or len(next_1)<3) else next_1[-1],       
        'next_1_sfx_2': '' if (not next_1 or len(next_1)<4) else next_1[-2:],       
        'next_2': next_2,
      }
    return features


def preprocess(c):
    special_char_dict = {}
    for r in char_replace:
        old, new = r[0], r[1]
        special_char_dict[old] = new
    
    alphabits = 'اب پ ت ټ ث ج چ ح خ څ ځ دډذرړزژږس ش ښ ص ض ط ظ ع غ ف ق ک ګ ل م ن ڼ ں وؤ ه ۀ ي ې ی ےۍئء'
    punc = '٪.،.\n'
    digits = '۰۱۲۳۴۵۶۷۸۹'
    uk = 'ـ'

    map_table = c.maketrans(special_char_dict)
    c = c.translate(map_table)
    c = c.replace(uk, '')
    
    res = [ele if (ele in alphabits) or (ele in digits) or (ele in punc) else  ' ' for ele in c]
    c = ''.join(res)
    
    c = re.sub("["+digits+"]+", lambda ele: " " + ele[0] + " ", c)

    c = c.replace('\n', ' ').replace('۔', '.')
    c = re.sub('\.+', '.', c)
    c = re.sub('،+', '،', c)
    c = re.sub('، ،', '،', c)
    c = re.sub('٪+', '٪', c)
    c = re.sub('٪ ٪', '٪', c)
    c = re.sub(' +', ' ', c)
    c = c.strip(' ،.').replace('.','\n')
    c = re.sub('\n+', '\n', c)
    return c