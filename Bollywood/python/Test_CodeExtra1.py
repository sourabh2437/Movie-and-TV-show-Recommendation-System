import csv
import operator
f1=file('../data/actors_count.csv','r')
f5=file('../data/top_actors_name.csv','w')
csv1=csv.reader(f1)
sortedcsv=sorted(csv1,key=operator.itemgetter(1),reverse=True)
num=0
flag=0
for i in sortedcsv:
    f2=file('../data/Bollywood_actor_database.csv','r')
    for j in csv.reader(f2):
        if i[0]==j[1]:
            output=''
            output=i[0]+","+i[1]
            print j[0]
            num=num+1
            if num==5:
                flag=1
                break
            f5.write(j[0]+" "+i[1]+"\n")
            #print j[0]+" = "+i[1]
            break
    if flag==1:
        break
f1.close()
f2.close()
f5.close()
