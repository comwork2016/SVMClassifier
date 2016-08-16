# -*- coding: UTF-8 -*-

def calc_filenum(segmentsdir,target_filenumpath="",writeToFile=False):
    filenum_dic = {}
    allfilenum = 0
    import os
    for classname in os.listdir(segmentsdir):
        classpath = os.path.join(segmentsdir, classname)
        # 保存文件数目信息
        filenum_dic[classname] = len(os.listdir(classpath))
        allfilenum = allfilenum + filenum_dic[classname]
    if writeToFile:
        from util import file_util
        if not os.path.exists(target_filenumpath):
            splitpath = os.path.split(target_filenumpath)
            if not os.path.exists(splitpath[0]):
                os.makedirs(splitpath[0])
        filenum_dic['all'] = allfilenum
        file_util.save_filenumdic(target_filenumpath, filenum_dic)
    print 'calc file number done!'
    return filenum_dic