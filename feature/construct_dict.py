# -*- coding: UTF-8 -*-

'''
构建词典
'''

def appenddictfromfile(filepath,word_set):
    fr = open(filepath,'r')
    for line in fr.readlines():
        term = line.decode('utf-8').strip('\t\n').split('\t')[0]
        word_set.add(term)
    fr.close()

def construct_dict(class_features_dir='./outputs/features',target_wordset_path = './outputs/words.dict',writeToFile = False):
    '根据各种分类中提取的特征来构建词典'
    import os
    import re
    word_set = set()
    for classname in os.listdir(class_features_dir):
        if re.match(r'.+\.feature$', classname):  # 网址
            class_features_filepath = os.path.join(class_features_dir,classname)
            appenddictfromfile(class_features_filepath,word_set)
    wordsdict = {}
    index=1
    for word in word_set:
        wordsdict[index] = word
        index = index + 1
    if writeToFile:
        from util import file_util
        file_util.save_wordsdict(target_wordset_path,wordsdict)
    return wordsdict



