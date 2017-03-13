import csv
import operator
f3=file('../data/TV_genre_count.csv','r')
f6=file('../data/TV_top_genre.csv','w')
csv2=csv.reader(f3)
sortedcsv2=sorted(csv2,key=operator.itemgetter(1),reverse=True)
num=0
flag=0
for i in sortedcsv2:
    f4=file('../data/genre.csv','r')
    for j in csv.reader(f4):
        if i[0]==j[1]:
            output=''
            output=i[0]+","+i[1]
            print j[0]
            num=num+1
            if num==3:
                flag=1
                break
            f6.write(j[0]+" "+i[1]+"\n")
          #  print j[0]+" = "+i[1]
            break
    if flag==1:
        break
f3.close()
f4.close()
f6.close()   
