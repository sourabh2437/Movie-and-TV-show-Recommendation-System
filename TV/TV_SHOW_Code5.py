import csv
import operator
f1=file('TV_movie_score.csv','r')
csv1=csv.reader(f1)
sortedcsv=sorted(csv1,key=operator.itemgetter(1),reverse=True)
k=0
flag=0
for i in sortedcsv:
    f2=file('TVshow_id.csv','r')
    for j in csv.reader(f2):
        if i[0]==j[1]:
            print j[0]
            k=k+1
            if k==10:
                flag=1
                break
    if flag==1:
        break
    
