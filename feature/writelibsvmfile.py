# -*- coding: UTF-8 -*-

def writelibsvminputfile(tfidf_dirpath,wordsdict_filepath,target_filepath):
    '格式化成libsvm的输入格式\
    lable1 index1:featureValue1 index2:featureValue2 index3:featureValue3 ...'
    fr = open(target_filepath,'w')
    from util import file_util
    wordsdict = file_util.read_wordsdict(wordsdict_filepath)
    import os
    for classname in os.listdir(tfidf_dirpath):
        classpath = os.path.join(tfidf_dirpath, classname)
        # 保存文件数目信息
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath, filename)
            doc_tfidf = file_util.read_tfidf(filepath)
            # 将字典中的词语保存
            line = classname[1:]+'\t' #去掉类名前面的字母
            for index in wordsdict:
                word = wordsdict[index]
                if word in doc_tfidf:
                    line = line + str(index) + ':' + str(doc_tfidf[word]) + '\t'
                #else:
                    #line = line + str(index) + ':' + str(0) + '\t'
            line = line.strip('\t') + '\n'
            fr.write(line.encode('utf-8'))
            print 'write file',filepath
    fr.close()

