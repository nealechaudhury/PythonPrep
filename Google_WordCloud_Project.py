""" Wordcloud project - wordcloud creates a picture of ow often a word appears"""
import re
from collections import Counter as cnt


def _retL(_L=[]):
    """ Use generator"""
    for i in _L:
        yield i


def clean(_str="", _p=[] ):
#def clean(_str=""):

    #punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    #_p = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    _l = list(_str)
    for punc in _p:
        #print (punc)
        if punc in _l:
            #print (f'{punc} is in {_l}')
            #print (f'{punc} is in {_l}')
            _x=_l.index(punc)
            #print (_x)
            #_l.pop(_l.index(punc))
            _l[:] = [item for item in _l if item != punc]
    # _newstr = ''.join(repr(e) for e in _l)
    # print(str(_newstr))
    # return _newstr
    #print (_l)
    _newstr = ''
    for i in _l:
        _newstr = _newstr + i
    return _newstr

if __name__ == "__main__":
    punctuations = """!()-[]{};:'’"\,<>./?@#$%^&*_—~"""
    uninteresting_words = [
        "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",
    ]

    # Read in a string - use context manager to do so:
    _file = "C:\\Users\\neale\\Downloads\\1184-0.txt"
    #print(_file)
    _wc=[]
    _mylines = [line.strip() for line in open(_file, "r+", encoding="utf-8")]
    for i, w in enumerate(_retL(_mylines)):
        _l = w.split()
        #print("-------------------------------")
        #print(f"{i} -> {w}")
        #print(_l, type(_l), len(_l))
        if len(_l) > 0:
            for str in _retL(_l):
                #     print(f'Before : {str}')
                #     ## Chack if there is a punctuation mark in this string
                #print(f"Before : {str} \nAfter clean  : {clean(str, punctuations )}")
                _retval = clean(str, punctuations)
                #print(f"Before : {str} \nAfter clean  : {_retval}")
                #print(f"Before : {str} \nAfter {clean(str)}")
                #print(f'IS --> {_retval} in --> {uninteresting_words}')
                if _retval.isalpha():
                    _retval_lc = _retval.lower()
                    if _retval_lc not in uninteresting_words:
                        _wc.append(_retval)

    _wcSubmit={}
    print (_wc)
    _cnt=cnt(_wc)
    for i in _wc:
        _wcSubmit[i]=_cnt[i]

    print (_wcSubmit)