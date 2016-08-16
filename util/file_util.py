#_*_ coding: utf-8 _*_

#保存用于计算卡方检验值的字典
def save_term_filenum_dic(filepath,dic):
    fr = open(filepath,'w')
    for item in dic:
        record = item + '_--_'
        for classlabel in dic[item]:
            record = record + classlabel +':'+str(dic[item][classlabel]) +'\t'
        fr.write((record.strip('\t')+"\n").encode('utf-8'))
    fr.close()

#读取用于计算卡方检验值的字典
def read_term_filenum_dic(filepath):
    dic = {}
    fr = open(filepath,'r')
    for record in fr.readlines():
        records = record.decode('utf-8').strip('\n\t').split('_--_')
        term = records[0]
        if not term in dic:
            dic[term]={}
        class_filenum_records = records[1]
        class_filenums = class_filenum_records.split('\t')
        for class_filenum in class_filenums:
            str_split_class_filenum = class_filenum.split(':')
            classlabel = str_split_class_filenum[0]
            filenum = int(str_split_class_filenum[1])
            dic[term][classlabel] = filenum
    fr.close()
    print 'read term filenum dic done!'
    return dic

#保存文件数目字典
def save_filenumdic(filepath,dic):
    fr = open(filepath, 'w')
    for item in dic:
        record = item + ':' + str(dic[item])
        fr.write((record + "\n").encode('utf-8'))
    fr.close()

#读取文件数目字典
def read_filenumdic(filepath):
    dic = {}
    fr = open(filepath, 'r')
    for record in fr.readlines():
        records = record.decode('utf-8').split(':')
        dic[records[0]] = int(records[1])
    fr.close()
    return dic

#保存卡方分值的字典
def save_class_term_chiscore_dic(filepath,class_term_chiscore_dic):
    fr = open(filepath,'w')
    for classlabel in class_term_chiscore_dic:
        record = classlabel + ':'
        for term in class_term_chiscore_dic[classlabel]:
            print 'write chi score of',term,'in',classlabel
            record = record + term +'_--_'+str(class_term_chiscore_dic[classlabel][term]) +'\t'
        fr.write((record.strip('\t')+"\n").encode('utf-8'))
    fr.close()

#读取卡方分值的字典
def read_class_term_chiscore_dic(filepath):
    class_term_chiscore_dic = {}
    fr = open(filepath,'r')
    for record in fr.readlines():
        records = record.decode('utf-8').strip('\n\t').split(':',1)
        classlabel = records[0]
        if not classlabel in class_term_chiscore_dic:
            class_term_chiscore_dic[classlabel]={}
        term_chiscores_records = records[1].split('\t')
        for term_chiscore  in term_chiscores_records:
            term_chiscores = term_chiscore.split('_--_')
            term = term_chiscores[0]
            chiscore = float(term_chiscores[1])
            class_term_chiscore_dic[classlabel][term] = chiscore
    fr.close()
    print 'read chi score done!'
    return class_term_chiscore_dic

#保存提取出来的特征值
def save_featurelist(filepath,sorted_term_chiscore):
    fr = open(filepath, 'w')
    for term_score_tuple in sorted_term_chiscore:
        term = term_score_tuple[0]
        chiscore = term_score_tuple[1]
        fr.write(((term+'\t'+str(chiscore)).strip('\t') + "\n").encode('utf-8'))
    fr.close()

#保存词典
def save_wordsdict(target_wordset_path,wordsdict):
    fr = open(target_wordset_path,'w')
    for index in wordsdict:
        fr.write((str(index)+'\t'+wordsdict[index]+'\n').encode('utf-8'))
    fr.close()

#读取词典
def read_wordsdict(filepath):
    wordsdict = {}
    fr = open(filepath,'r')
    for line in fr.readlines():
        iw = line.strip('\n\t').split('\t')
        wordsdict[int(iw[0])] = iw[1]
    return wordsdict

#保存词频
def save_termfrequency(filepath,dict):
    fr = open(filepath,'w')
    for term in dict:
        fr.write((term+'\t'+str(dict[term])+'\n').encode('utf-8'))
    fr.close()
    print 'save tf done!'

#读取词频
def read_termfrequency(filepath):
    dict = {}
    fr = open(filepath,'r')
    for line in fr.readlines():
        tf = line.strip('\n\t').split('\t')
        dict[tf[0]] = int(tf[1])
    return dict

#保存tf-idf文档
def save_tfidf(filepath,dict):
    fr = open(filepath,'w')
    for term in dict:
        fr.write((term+'\t'+str(dict[term])+'\n').encode('utf-8'))
    fr.close()
    print 'save tf done!'

#读取词频
def read_tfidf(filepath):
    dict = {}
    fr = open(filepath,'r')
    for line in fr.readlines():
        tf = line.strip('\n\t').split('\t')
        dict[tf[0]] = float(tf[1])
    return dict