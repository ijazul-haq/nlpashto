# NLPashto – NLP Toolkit for Pashto
![GitHub](https://img.shields.io/github/license/ijazul-haq/nlpashto) ![GitHub contributors](https://img.shields.io/github/contributors/ijazul-haq/nlpashto) ![code size](https://img.shields.io/github/languages/code-size/ijazul-haq/nlpashto)

NLPashto is a Python suite for Pashto Natural Language Processing, initiated at Shanghai Jiao Tong University. 

## Prerequisites
To use NLPashto you will need:
* Python 3.8+

## Installing NLPashto
NLPashto can be installed from PyPi using this command
```bash
pip install nlpashto
```

## Using NLPashto

### Sentence Tokenizer
```python
from nlpashto import sentence_tokenizer
sentences_list = sentence_tokenizer(content)
tagged = pos_tagger(tokenized)
```

### Word Tokenizer
```python
from nlpashto import word_tokenizer

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
print(tokenized)
['همدارنګه', 'تیره', 'شپه', 'او', 'ورځ', 'په', 'هیواد', 'کې', 'د', 'کرونا ویروس', 'له امله', '۵', 'تنه', 'مړه', 'شوي']
```

### Whitespace Tokenizer (Proofing)
Whitespace Tokenizer can be used as a proofing tool to remove the space-omission and space-insertion errors. It will remove extra spaces from the text and will insert space where necessary. It’s a beta version and only recommended if the input text is extremely noisy. 

```python
from nlpashto import tokenizer

noisy_text = 'ه  م  د  ا  ر  ن  ګ ه ت ی ر ه ش پ ه ا وورځپههیوادکېدکروناویروسلهامله۵تنهمړهشوي'
corrected = tokenizer(noisy_text)
print(corrected)
همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي
```

### Part-of-speach (POS) Tagging
For further detail about the POS tagger and the corpus used for training please have a look at our paper [The Pashto Corpus and Machine Learning Model for Automatic POS Tagging](https://www.researchsquare.com/article/rs-2712906/v1)
```python
from nlpashto import pos_tagger

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
tokenized = word_tokenizer(text)
tagged = pos_tagger(tokenized)
print(tagged) 
[['همدارنګه', 'RB'], ['تیره', 'JJ'], ['شپه', 'NNF'], ['او', 'CC'], ['ورځ', 'NNM'], ['په', 'IN'], ['هیواد', 'NNM'], ['کې', 'PT'], ['د', 'IN'], ['کرونا ویروس', 'NNP'], ['له امله', 'RB'], ['۵', 'NB'], ['تنه', 'NNS'], ['مړه', 'JJ'], ['شوي', 'VBDX']]
```

### Offensive Language Detection
Coming soon…
