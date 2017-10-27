
import time 
import math
import operator
document = [0] * 99999
query = [0] * 99999
querylist = []
documentlist = []
queryDictlist = []
documenDictlist = []
number = 0
#caculate ni
#read query_list.txt save at querylist
fq = open('query_list.txt','r') 
for line in fq:
    querylist.append(line.rstrip('\n'))
#print(querylist)
fq.close()

#read document_list.txt save at documentlist
fd = open('doc_list.txt','r') 
for line in fd:
    documentlist.append(line.rstrip('\n'))
fd.close()

#read query
for qlist in querylist:
    dict={}

    #print(query[99998])
    fq = open(qlist,'r')
    for line in fq:
        result = []
        result.extend(list(line.split(' ')))
        #讀取每個term
        for n in range(len(result)) :
            if int(result[n]) != -1:
                #若dict裡沒有 則value設1,並count+1
                if dict.get(result[n]) == None :
                    dict[result[n]] = 1
                    number = int(result[n])
                    #統計該term出現在幾個query中
                    query[number] = query[number] + 1
                #反之加1
                else :
                    dict[result[n]] = dict.get(result[n]) + 1
    #term出現query(n)中的次數用dictionary存在list裡,每一個dictionary代表一個query
    queryDictlist.append(dict)
    fq.close()

#read document
for dlist in documentlist:
    dict={}
    fd = open(dlist,'r') 
    lines = fd.readlines()
    l_list = lines[3:]
    for l in l_list:
        result = []
        result.extend(list(list(l.split(' '))))
        #讀取每個term
        for n in range(len(result)) :
            if int(result[n]) != -1:
                #若dict裡沒有 則value設1,並count+1
                if dict.get(result[n]) == None :
                    dict[result[n]] = 1
                    number = int(result[n])
                    #統計該term出現在幾篇document中
                    document[number] = document[number] + 1
                #反之加1
                else :
                    dict[result[n]] = dict.get(result[n]) + 1
    #term出現document(n)中的次數用dictionary存在list裡,每一個dictionary代表一個document
    documenDictlist.append(dict)
    #print(documenDictlist)
    fd.close()
#print(document)

#fd = open('result.txt','w')
#fd.write('Query,RetrievedDocuments\n')
#讀取每個query
for que in range(len(queryDictlist)):
#    fd.write(querylist[que]+',')
    rank = {}
    d_q = queryDictlist[que]
    print(que)
    #讀取每個document
    for dict in range(len(documenDictlist)):
        sigma_q = 0
        sigma_d = 0
        sum = 0
        #print(len(documenDictlist))
        #讀取一個term
        d_dict = documenDictlist[dict]
        for key in d_q:
            wq = 0
            wd = 0
            number = int(key)
            #term對query的TF-IDF
            wq = (math.log(d_q.get(key ,0))+1) * math.log(1+len(queryDictlist)/query[number]+1)
            #wq = TF(d_q.get(key ,0)) * IDF(len(queryDictlist) ,query[number])
            #term對document的TF-IDF
            if(document[number] == 0):
                if(d_dict.get(key ,0) == 0):
                    wd = math.log(1)
                else:
                    wd = (math.log(d_dict.get(key ,0))+1 ) * math.log(1)
            else :
                if(d_dict.get(key ,0) == 0):
                    wd = math.log2(1+len(documenDictlist)/(document[number]))
                else :
                    wd = (math.log2(d_dict.get(key ,0))+1 ) * math.log(1+len(documenDictlist)/(document[number]))
            #wd = TF(d_dict.get(key ,0)) * IDF(len(documenDictlist) ,document[number])

            number = wq * wd
            sigma_q = sigma_q + (wq * wq)
            sigma_d = sigma_d + (wd * wd)
            #term值加總
            sum = sum + number
        #把document對query的值存在dictionary裡
        number = sum / math.sqrt( sigma_q ) / math.sqrt( sigma_d )
        documentlist[dict]
        rank[documentlist[dict]] = number
   #     if(que == 1):
   #         print(rank)

    #rank排序
    sorted_x = sorted(rank.items(), key=operator.itemgetter(1),reverse=True)
    if(que == 1):
        print(sorted_x)
        break
#    for str in sorted_x:
#        fd.write(str[0]+' ')
#    fd.write('\n')
#fd.close()

#timeclock1 = time.clock()
#timeclock2 = time.clock()
#print(timeclock2-timeclock1)
