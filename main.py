# -*- coding: UTF-8 -*-

from util import *
from pre_process import *
from feature import *

if __name__ == '__main__':
    print "main entrance"
    # file_segment.writeSegmentsOfDir('./corpus','./outputs/segments')
    # calc_filenum.calc_filenum('./outputs/segments','./outputs/classfilenum.txt',True)
    # feature_extraction.construct_tmp_term_filenum_dic('./outputs/segments','./outputs/termfilenum.txt',True)
    # feature_extraction.calc_chiscore(writeToFile=True)
    # feature_extraction.extract_feature()
    # construct_dict.construct_dict('./outputs/features','./outputs/words.dict',True)
    # doc_statics.calc_all_tfidf('./outputs/segments')
    writelibsvmfile.writelibsvminputfile(tfidf_dirpath='./outputs/tfidf',wordsdict_filepath='./outputs/words.dict',target_filepath='./outputs/libsvminput')



