# -*- coding: UTF-8 -*-
'''利用卡方检验进行特征提取'''

def getfiledic(filepath,classlable,dic):
    '对每个文件计算生成文档数目词典'
    import doc_statics
    doctf = doc_statics.calc_termfrequency(filepath)
    for term in doctf:
        if term in dic:
            if classlable in dic[term]:
                dic[term][classlable] = dic[term][classlable]+1
            else:
                dic[term][classlable] = 1
        else:
            dic[term] = {classlable:1}

def construct_tmp_term_filenum_dic(segmentsdir,target_dicpath='',writeTofile=False):
    '获取保存包含词语文档个数的临时词典，卡方检验时需要用到   \
    格式是：{term{c:docnum...},....}'
    tmp_term_filenum_dic = {}
    import os
    for classname in os.listdir(segmentsdir):
        classpath = os.path.join(segmentsdir,classname)
        #保存文件数目信息
        for filename in os.listdir(classpath):
            filepath = os.path.join(classpath,filename)
            getfiledic(filepath,classname,tmp_term_filenum_dic)
            print 'process',filepath
    #计算该词语在所有类别的文件中出现的次数
    for item in tmp_term_filenum_dic:
        count = 0
        for classname in tmp_term_filenum_dic[item]:
            count = count + tmp_term_filenum_dic[item][classname]
        tmp_term_filenum_dic[item]['allfilenum'] = count
    if writeTofile:
        from util import file_util
        file_util.save_term_filenum_dic(target_dicpath,tmp_term_filenum_dic)
        print 'construct tmp dict done!'
    return tmp_term_filenum_dic

def calcchi_for_term(term,classlabel_num_dic,class_filenum_dic,class_term_chiscore):
    '利用文档中包含的词语的个数计算卡方值 \
    形式为 {class{term:score},....}'
    # a：在这个分类下包含这个词的文档数量
    # b：不在该分类下包含这个词的文档数量
    # c：在这个分类下不包含这个词的文档数量
    # d：不在该分类下，且不包含这个词的文档数量
    # z1 = a*d - b*c
    # x2 = (z1 * z1 * float(N)) /( (a+c)*(a+b)*(b+d)*(c+d) )
    for classlabel in classlabel_num_dic:
        if classlabel == 'allfilenum':
            continue
        a = classlabel_num_dic[classlabel]
        b = classlabel_num_dic['allfilenum'] - classlabel_num_dic[classlabel]
        c = class_filenum_dic[classlabel] - a
        d = class_filenum_dic['all'] - class_filenum_dic[classlabel] - b
        z1 = a*d - b*c
        x2 = (z1*z1*class_filenum_dic['all'])/float(((a+b)*(a+c)*(b+d)*(c+d)))
        #保存分类词频的卡方值
        if not classlabel in class_term_chiscore:
            class_term_chiscore[classlabel] = {term:x2}
        else:
            class_term_chiscore[classlabel][term] = x2

def calc_chiscore(chidic_path='./outputs/termfilenum.txt',classfilenumpath='./outputs/classfilenum.txt',target_filepath='./outputs/chiscore.dict',writeToFile=False):
    '计算每个词语在每个分类下的卡方值   \
    class{term:score,....}'
    class_term_chiscore = {}
    from util import file_util
    tmp_term_filenum_dic = file_util.read_term_filenum_dic(chidic_path)
    class_filenum_dic = file_util.read_filenumdic(classfilenumpath)
    for term in tmp_term_filenum_dic:
        classlabel_num_dic = tmp_term_filenum_dic[term]
        calcchi_for_term(term,classlabel_num_dic,class_filenum_dic,class_term_chiscore)
        print 'calc chi score of ',term
    if writeToFile:
        file_util.save_class_term_chiscore_dic(target_filepath,class_term_chiscore)
    print 'calc chi score done!'
    return class_term_chiscore

def extract_feature(topN = 5000,target_dir='./outputs/features'):
    from util import  file_util
    import os
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    class_term_chiscore = calc_chiscore()
    for classlabel in class_term_chiscore:
        target_feature_path = os.path.join(target_dir,classlabel)
        target_feature_path = target_feature_path + '.feature'
        term_chisocre = class_term_chiscore[classlabel]
        sorted_term_chiscore = sorted(term_chisocre.iteritems(),key=lambda d:d[1],reverse=True)
        #保存所有的特征项
        file_util.save_featurelist(target_feature_path + '.all',sorted_term_chiscore)
        #保存topN个特征作为特征值
        file_util.save_featurelist(target_feature_path,sorted_term_chiscore[0:topN])
    print 'feature extract done!'


