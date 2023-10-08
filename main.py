from nlpashto.tokenization import Tokenizer
from nlpashto.word_segmentation import Segmenter
from nlpashto.pos_tagging import POSTagger
from nlpashto.sentiment_analysis import POLD
from nlpashto.utils import Cleaner

def run():
    txt='د تايلنډ د بانکاک سيام باراګون تجارتي مرکز کې د اکتوبر په درېيمې نېټې د ډزو پېښه وشوه، چې له امله يې اووه کسانو ته مرګژوبله واوښته.'
    segmenter = Segmenter()
    segmented = segmenter.segment([txt.split()])
    print(segmented)
    
if __name__ == '__main__':
    run()