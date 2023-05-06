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

## Downloading Models
Call the download() function and pass the "model name" as argument.
```bash
nlpashto.download('space_correct')
```
Valid model names: 'space_correct', 'pos_tag', 'word_segment', 'pold', 'snd'

If the model name was not specified, all the available models will be downloaded


## Basic Usage


### Space Correction
Space correction module can be used to correct the space-omission and space-insertion errors. It will remove extra spaces from the text and will insert space where necessary. It’s a beta version and only recommended if the input text is extremely noisy. 

```python
from nlpashto import space_correct

noisy_text = 'ه  م  د  ا  ر  ن  ګ ه ت ی ر ه ش پ ه ا وورځپههیوادکېدکروناویروسلهامله۵تنهمړهشوي'
corrected = space_correct(noisy_text)
print(corrected)
Output:: همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي
```


### Word Segmentatoin
```python
from nlpashto import word_segment

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
segmented_text = word_segment(text)
print(segmented_text)

Output:: ['همدارنګه', 'تیره', 'شپه', 'او', 'ورځ', 'په', 'هیواد', 'کې', 'د', 'کرونا ویروس', 'له امله', '۵', 'تنه', 'مړه', 'شوي']
```

### Part-of-speech (POS) Tagging
For further detail about the POS tagger and the corpus used for training please have a look at our paper [The Pashto Corpus and Machine Learning Model for Automatic POS Tagging](https://www.researchsquare.com/article/rs-2712906/v1)
```python
from nlpashto import pos_tag

text = 'همدارنګه تیره شپه او ورځ په هیواد کې د کرونا ویروس له امله ۵ تنه مړه شوي'
segmented_text = word_segment(text)
tagged = pos_tag(segmented_text)
print(tagged) 

Output:: [['همدارنګه', 'RB'], ['تیره', 'JJ'], ['شپه', 'NNF'], ['او', 'CC'], ['ورځ', 'NNM'], ['په', 'IN'], ['هیواد', 'NNM'], ['کې', 'PT'], ['د', 'IN'], ['کرونا ویروس', 'NNP'], ['له امله', 'RB'], ['۵', 'NB'], ['تنه', 'NNS'], ['مړه', 'JJ'], ['شوي', 'VBDX']]
```

### Offensive Language Detection
A fine-tuned BERT model for toxicity detection in Pashto text

```python
from nlpashto import pold

offensive_text = 'مړه یو کس وی صرف ځان شرموی او یو ستا غوندے جاهل وی چې قوم او ملت شرموی'
pold(text)

Output:: 1


normal_text = 'تاسو رښتیا وایئ خور 🙏'
pold(text)

Output:: 0
```

### Spammy Names Detection
A Naive Bayes classifier model that will predict whether the string of characters is a valid name or not. It can be used to identify spammy profile names on social media.

```python
from nlpashto import snd

not_a_name = 'مسافر لالی'
snd(not_a_name)

Output:: 0.2


valid_name = 'شاهد افريدی'
snd(text)

Output:: 1.0
```
