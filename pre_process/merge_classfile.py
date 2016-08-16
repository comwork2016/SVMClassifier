# -*- coding: UTF-8 -*-

def merge_with_label(target_classpath, filepaths, label, tc_splitTag):
    frout = open(target_classpath,'w')
    for filepath in filepaths:
        fr = open(filepath, 'r')
        data = fr.read()
        import re
        p = re.compile("\s")  # replace all the blank character ,such as \t \n
        data = p.sub("", data)
        frout.write(data)
    frout.close()
    print "segments complete!"


def merge_classfile(dir_source,target_dir):
    import os.path
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    for classname in os.listdir(dir_source): # 列出目录下的所有文件和目录
        classpath = os.path.join(dir_source, classname)
        target_classpath = os.path.join(target_dir,classname)
        target_classpath = target_classpath + '.merge'
        filepaths = os.listdir(classpath)
        for i in range(len(filepaths)):
            filepaths[i] = os.path.join(classpath,filepaths[i])
        merge_with_label(target_classpath, filepaths, classname, "\t")#将该类别下的所有文件合并成一个文件