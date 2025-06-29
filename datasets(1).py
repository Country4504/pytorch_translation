
import jieba

from utils import normalizeString, cht_to_chs

SOS_token = 0 #起始符
EOS_token = 1 #終止符
Max_LENGTH = 10 #读取句子最大長度

class Lang:
    def __init__(self,name):
        self.name = name
        self.word2index = {}#记录对应词索引
        self.word2count = {}#记录词频
        self.index2word = {
         0:"SOS",1:"EOS"
        }
        self.n_words = 2

    #对词进行统计
    def addWord(self,word):
        if word not in self.word2index: #如果此不在统计表中，添加
            self.word2index[word] = self.n_words #词的索引第几种
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words +=1
        else:
            self.word2count[word] +=1

    #对句子的处理/分词
    def addSentence(self,sentence):
        for word in sentence.split(" "):
            self.addWord(word)


#文本解析
def readLines(lang1,lang2,path):
    lines = open(path, encoding='utf-8').readline()

    lang1_cls = Lang(lang1)
    lang2_cls = Lang(lang2)

    pairs = []
    for list in lines:
        list = list.split('\t')
        sentence1 = normalizeString(list[0])#处理英文句子
        sentence2 = cht_to_chs(list[1])#处理中文句子
        seg_list = jieba.cut(sentence2,cut_all=False)
        sentence2 = " ".join(seg_list)

        if len(sentence1.split(" ")) >Max_LENGTH:
            continue
        if len(sentence2.split(" "))>Max_LENGTH:
            continue

        pairs.append([sentence1,sentence2])#[["what are you ding","你 在 干 什么"]]

        lang1_cls.addSentence(sentence1)
        lang2_cls.addSentence(sentence2)

    return lang1_cls,lang2_cls,pairs

