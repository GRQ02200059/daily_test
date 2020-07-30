import os ,sys
import jieba ,codecs,math
import jieba.posseg as pseg
import jieba
names={}
relationships={}
linesnames=[]

excludes = {'王朝','北莽','北凉','王府','龙虎山','北凉军','王妃','西楚','老皇帝',
            '西垒壁','徐家','封王','徐家铁','靖安王','燕敕','赵家天子','赵室'
            ,'徐家军','金刚','龙象军','澹台','老祖宗','祖师爷','吴家剑','羽衣卿',
            '白莲先生','小娘子','老道士','王世子','佩剑','马夫','春雷',
            '安静','丹婴','西蜀','王八蛋','小姑娘','凤字营','老天爷',
            '老夫','青羊宫','羊皮裘','武大帝','王氏','靖安','马嵬','养剑'
            ,'白马义','慕容桐','慕容','洪骠','王大石','鱼龙','宋貂儿',
            '老先生','小宗师','呼延','拓跋','耶律东','慕容龙','春秋剑',
            '清凉山','秦帝陵','雪山庄','雪莲城','卢氏','左骑军'}
with codecs.open("雪中悍刀行.txt",'r',encoding='utf-8')as f:
    for line in f.readlines():
        poss=pseg.cut(line)
        linesnames.append([])
        for w in poss:

            if w.flag!="nr" or len(w.word)<2 or w.word in excludes:
                continue

            elif w.word == '白狐儿脸' :
                real_word = '南宫仆射'
            elif w.word=='北凉王' or w.word=='王爷' or w.word=='老凉王':
                real_word='徐骁'
            elif w.word=='黄蛮':
                real_word='徐龙象'
            elif w.word=='师叔祖':
                real_word="洪洗象"
            elif w.word=='凤年' or w.word=='小王爷' or w.word=='徐奇' or w.word=='徐公子':
                real_word="徐凤年"
            elif w.word=='老黄':
                real_word='黄阵图'
            elif w.word=='禄球儿':
                real_word='褚禄山'
            elif w.word=='董胖子':
                real_word='董卓'
            elif w.word=='李老头' or w.word=='老剑神':
                real_word='李淳罡'
            elif w.word=='姜姒':
                real_word='姜泥'
            elif w.word=='曹官子':
                real_word='曹长卿'
            elif w.word=='木剑' or w.word=='游侠':
                real_word='温华'
            elif w.word=='裴王妃' :
                real_word='裴南苇'
            elif w.word == '白衣僧':
                real_word = '李当心'

            else:
                real_word = w.word
            print(real_word)
            linesnames[-1].append(real_word)
            if names.get(real_word) is None:
                names[real_word]=0
                relationships[real_word]={}
            names[real_word]+=1


with codecs.open("sanguo_node.txt","w",'gbk')as f:
    f.write("Id Label Weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")

for line in linesnames:
   # print(line)
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
               # print(name1,name2)
                relationships[name1][name2]=1
            else:
                relationships[name1][name2]=relationships[name1][name2]+1

with codecs.open("sanguo_edge.txt","w","gbk")as f:
    f.write("Source Target Weight\r\n")
    for name,edges in relationships.items():
        for v,w in edges.items():
            if w>25:
                f.write(name+" "+v+" "+str(w)+"\r\n")