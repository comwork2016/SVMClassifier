# -*- coding: UTF-8 -*-

def calc_termfrequency(segspath,target_dir='./outputs/tf',writeToFile = False):
    '计算文件中的词频'
    fr = open(segspath, 'r')
    data = fr.read().decode('utf-8')
    fr.close()
    doctf = {}
    segs = data.split('\n')
    for seg in segs:
        seg = seg.strip(' \n\t')
        if len(seg) == 0: #词语长度>0
            continue
        times = doctf.get(seg)
        if times:
            doctf[seg] = times + 1
        else:
            doctf[seg] = 1
    if writeToFile:
        import os
        class_filename = os.path.split(segspath)
        classname = os.path.split(class_filename[0])[1]
        filename = class_filename[1]
        target_filename = os.path.join(target_dir,classname)
        if not os.path.exists(target_filename):
            os.makedirs(target_filename)
        target_filename = os.path.join(target_filename,filename)
        print classname,filename,target_filename
        from util import file_util
        file_util.save_termfrequency(target_filename,doctf)
    return doctf

def calc_tfidf(doctf,term_filenum_dic,allfilenum,target_filename='',writeToFile = False):
    '计算文件中的词频'
    doc_tfidf = {}
    import math
    for term in doctf:
        idf = math.log(allfilenum / float(1 + term_filenum_dic[term]['allfilenum']))
        doc_tfidf[term] = doctf[term] * idf
    if writeToFile:
        from util import file_util
        file_util.save_tfidf(target_filename,doc_tfidf)
    return doctf

def calc_all_tfidf(segmentsdir,term_filenum_dic_path='./outputs/termfilenum.txt',classfilenumpath='./outputs/classfilenum.txt'):
    import os
    from util import file_util
    term_filenum_dic = file_util.read_term_filenum_dic(term_filenum_dic_path)
    allfilenum = file_util.read_filenumdic(classfilenumpath)['all']
    for classname in os.listdir(segmentsdir):
        classpath = os.path.join(segmentsdir, classname)
        # 保存文件数目信息
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath, filename)
            target_filename = os.path.join('./outputs/tfidf',classname)
            if not os.path.exists(target_filename):
                os.makedirs(target_filename)
            target_filename = os.path.join(target_filename,filename)
            doctf = calc_termfrequency(filepath)
            doc_tfidf = calc_tfidf(doctf, term_filenum_dic, allfilenum, target_filename=target_filename, writeToFile=True)