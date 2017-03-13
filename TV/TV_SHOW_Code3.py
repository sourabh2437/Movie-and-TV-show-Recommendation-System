import csv
import operator
#f1=file('actors_count.csv','r')
'''f5=file('top_actors.csv','w')
csv1=csv.reader(f1)
sortedcsv=sorted(csv1,key=operator.itemgetter(1),reverse=True)
for i in sortedcsv:
    f2=file('actors.csv','r')
    for j in csv.reader(f2):
        if i[0]==j[1]:
            output=''
            output=i[0]+","+i[1]
            #print output
            f5.write(output+"\n")
            #print j[0]+" = "+i[1]
            break
f1.close()
f2.close()
f5.close()

#print "\n"'''

f3=file('TV_genre_count.csv','r')
f6=file('TV_top_genre.csv','w')
csv2=csv.reader(f3)
sortedcsv2=sorted(csv2,key=operator.itemgetter(1),reverse=True)
for i in sortedcsv2:
    f4=file('genre.csv','r')
    for j in csv.reader(f4):
        if i[0]==j[1]:
            output=''
            output=i[0]+","+i[1]
            #print output
            f6.write(output+"\n")
          #  print j[0]+" = "+i[1]
            break
f3.close()
f4.close()
f6.close()   
