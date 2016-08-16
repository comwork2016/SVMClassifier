# -*- coding: UTF-8 -*-

def readStopTerm():
    stop_term_set = set()
    fr = open('./files/stopterm.txt')
    for term in fr.readlines():
        term = term.strip().decode("utf-8")# 解码成为Unicode形式
        stop_term_set.add(term)
    return stop_term_set

def initnlpir():
    import pynlpir
    pynlpir.open()
    pynlpir.nlpir.ImportUserDict('./files/userdic.txt')
    return pynlpir

def segments(filepath,nlpir):
    segments = []
    fr = open(filepath)
    data = fr.read()
    import re
    p = re.compile("\s")  # replace all the blank character ,such as \t \n
    data = p.sub("", data)
    segs = nlpir.segment(data)
    return segs

def writeSegmentsToFile(filepath,target_filepath,nlpir,stop_term_set):
    import re
    frsegs = open(target_filepath, 'w')
    segs = segments(filepath,nlpir)
    for seg in segs:
        item = seg[0].lower() #统一转换成小写形式
        if item not in stop_term_set:
            if re.match(r'^https?:/{2}\w.+$', item):  #网址
                item = u'@HTTP'
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", item): #邮箱地址
                item = u'@EMAIL'
            if item == u'numeral':
                item = '@NUMBER'  #将数字统一替换成@NUMBER
            if item == u'string':
                item = '@STRING'
            if item == u'time word':
                item = '@DATA'
            frsegs.write((item +'\n').encode('utf-8')) #以utf-8编码保存
    frsegs.close()
    print "write segments of",filepath,"to",target_filepath

def writeSegmentsOfDir(dir_source,dir_target):
    import os
    if not os.path.exists(dir_target):
        os.mkdir(dir_target)
    nlpir = initnlpir()#分词工具初始化
    stop_term_set = readStopTerm()#读取停用词
    for classname in os.listdir(dir_source): # 列出目录下的所有文件和目录
        classpath = os.path.join(dir_source, classname)
        target_classpath = os.path.join(dir_target,classname)
        if not os.path.exists(target_classpath):
            os.mkdir(target_classpath)
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath,filename)
            target_filename = os.path.join(target_classpath,filename)
            writeSegmentsToFile(filepath,target_filename,nlpir,stop_term_set)
    nlpir.close()

