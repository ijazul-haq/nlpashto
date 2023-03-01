# NLPashto – NLP Toolkit for Pashto
NLPashto is a python suite for supporting research and development in Pashto Natural Language Processing. NLPashto project is initiated at Shanghai Jiao Tong University, China

## Prerequisites
To use NLPashto you will need:
* Python 3.8+

## Installing NLPashto
You can install pashto from PyPi using this command
```bash
pip install nlpashto
```

## Using NLPashto

### Word Segmentation
```python
from nlpashto import word_tokenizer

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
print(tokenized)
['همدارنګه', 'تیره', 'شپه', 'او', 'ورځ', 'په', 'هیواد', 'کې', 'د', 'کرونا ویروس', 'له امله', '۵', 'تنه', 'مړه', 'شوي']
```
### POS Tagging
```python
from nlpashto import pos_tagger

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
tagged = pos_tagger(tokenized)
print(tagged) 
[['همدارنګه', 'RB'], ['تیره', 'JJ'], ['شپه', 'NNF'], ['او', 'CC'], ['ورځ', 'NNM'], ['په', 'IN'], ['هیواد', 'NNM'], ['کې', 'PT'], ['د', 'IN'], ['کرونا ویروس', 'NNP'], ['له امله', 'RB'], ['۵', 'NB'], ['تنه', 'NNS'], ['مړه', 'JJ'], ['شوي', 'VBDX']]
```

### Whitespace Correction (Proofing)

### Offensive Comments Detection

