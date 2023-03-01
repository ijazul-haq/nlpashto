# NLPashto – NLP Toolkit for Pashto
NLPashto is a python suite for Pashto Natural Language Processing. The project is initiated by a PhD scholar at Shanghai Jiao Tong University. 
A sample of the Pashto Corpus is available [here](https://github.com/ijazul-haq/pashto_pos) that is used to train some of the models in NLPashto.

## Prerequisites
To use NLPashto you will need:
* Python 3.8+

## Installing NLPashto
NLPashto can be installed from PyPi using this command
```bash
pip install nlpashto
```

## Using NLPashto

### Word Segmentation
```bash
from nlpashto import word_tokenizer

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
print(tokenized)
```
Output: ['همدارنګه', 'تیره', 'شپه', 'او', 'ورځ', 'په', 'هیواد', 'کې', 'د', 'کرونا ویروس', 'له امله', '۵', 'تنه', 'مړه', 'شوي']
### POS Tagging
```python
from nlpashto import pos_tagger

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
tagged = pos_tagger(tokenized)
print(tagged) 
[['همدارنګه', 'RB'], ['تیره', 'JJ'], ['شپه', 'NNF'], ['او', 'CC'], ['ورځ', 'NNM'], ['په', 'IN'], ['هیواد', 'NNM'], ['کې', 'PT'], ['د', 'IN'], ['کرونا ویروس', 'NNP'], ['له امله', 'RB'], ['۵', 'NB'], ['تنه', 'NNS'], ['مړه', 'JJ'], ['شوي', 'VBDX']]
```
Output: [['همدارنګه', 'RB'], ['تیره', 'JJ'], ['شپه', 'NNF'], ['او', 'CC'], ['ورځ', 'NNM'], ['په', 'IN'], ['هیواد', 'NNM'], ['کې', 'PT'], ['د', 'IN'], ['کرونا ویروس', 'NNP'], ['له امله', 'RB'], ['۵', 'NB'], ['تنه', 'NNS'], ['مړه', 'JJ'], ['شوي', 'VBDX']]

### Whitespace Correction (Proofing)

### Offensive Comments Detection
Coming soon…
