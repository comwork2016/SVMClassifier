# -*- coding: UTF-8 -*-
import os
import chardet

def fileToUTF8(filename_source,filename_target):
    if os.path.exists(filename_target) or not os.path.exists(filename_source):
        return
    fr_source = open(filename_source)
    contents_source = fr_source.read()
    sourceEncode = chardet.detect(contents_source)['encoding'] # get sourceEncode
    if not sourceEncode:
        return
    contents_target = unicode(contents_source,sourceEncode,errors='ignore').encode('utf-8')
    fr_target = open(filename_target,'w')
    fr_target.write(contents_target)
    fr_source.close()
    fr_target.close()
    os.remove(filename_source)
    print 'transfer',filename_source,'to',filename_target,'done!'

def convertDirtoUTF8(dir_source,dir_target):
    if not os.path.exists(dir_target):
        os.mkdir(dir_target)
    for classname in os.listdir(dir_source): # 列出目录下的所有文件和目录
        classpath = os.path.join(dir_source, classname)
        target_classpath = os.path.join(dir_target,classname)
        if not os.path.exists(target_classpath):
            os.mkdir(target_classpath)
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath,filename)
            target_filename = os.path.join(target_classpath,filename)
            fileToUTF8(filepath,target_filename)
        if len(os.listdir(classpath))==0:
            os.removedirs(classpath)