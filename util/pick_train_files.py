# -*- coding: UTF-8 -*-

def getRandomSequence(bound):
    list = range(0,bound)
    import random
    random.shuffle(list)
    return list

def pick(inputPath, outputTrainPath, outputTestPath,trainfileratio):
    import os.path
    from shutil import copyfile
    if not os.path.exists(outputTrainPath):
        os.mkdir(outputTrainPath)
    if not os.path.exists(outputTestPath):
        os.mkdir(outputTestPath)
    for classname in os.listdir(inputPath): # 列出目录下的所有文件和目录
        classpath = os.path.join(inputPath, classname)
        target_trainclasspath = os.path.join(outputTrainPath,classname)
        target_testclasspath = os.path.join(outputTestPath,classname)
        if not os.path.exists(target_trainclasspath):
            os.mkdir(target_trainclasspath)
        if not os.path.exists(target_testclasspath):
            os.mkdir(target_testclasspath)
        filenames = os.listdir(classpath)
        filenum = len(filenames)
        shuffledIndex = getRandomSequence(filenum)
	    #first 60% files as train set
        trainEnd = int(filenum * trainfileratio)
        for i in range(0,trainEnd):
            filename = filenames[shuffledIndex[i]]
            filepath = os.path.join(classpath,filename)
            target_trainfilepath = os.path.join(target_trainclasspath,filename)
            copyfile(filepath,target_trainfilepath)
            print "copy file",filepath,"to",target_trainclasspath
        for i in range(trainEnd,filenum):
            filename = filenames[shuffledIndex[i]]
            filepath = os.path.join(classpath,filename)
            target_testfilepath = os.path.join(target_testclasspath,filename)
            copyfile(filepath,target_testfilepath)
            print "copy file",filepath,"to",target_testfilepath
    print "pickfile complete"