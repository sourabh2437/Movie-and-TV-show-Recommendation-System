import csv

'''
actors_count=[]
for i in range(270):
    actors_count.append(0)
for row in csv.reader(f1):
    f2=file('TVshow_Database.csv','r')
    for j in csv.reader(f2):
        try:
            if row[0]==j[0]:
                new_row=[]
                new_row=j[1].split(":")
                for i in range(0,len(new_row)):
                  #  print new_row[i]
                    index=int(new_row[i])
                    #print new_row[0] +" "+new_row[1]
                    #index=int(new_row[int(i)])
                    #print index
                    actors_count[index]=actors_count[index]+1   
                        
        except IndexError:
            pass
f4=file('actors_count.csv','w')
l= len(actors_count)               
#for i in actors_count:
 #   print i
for i in range(1,l):
    try:
        output=''
        output=str(i)+","
        output=output+str(actors_count[i])
        f4.write(output)
        #print output
        f4.write("\n")
    except IndexError:
        pass


f1.close()
f2.close()'''

### End of part 1, now part 2

genre_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
f1=file('TV_output.csv','r')
for row in csv.reader(f1):
    f2=file('TVshow_Database.csv','r')
    for j in csv.reader(f2):
        try:
            if row[0]==j[0]:
                new_row=[]
                new_row=j[1].split(":")
                for i in range(0,len(new_row)):
                  #  print new_row[i]
                    index=int(new_row[i])
                    #print new_row[0] +" "+new_row[1]
                    #index=int(new_row[int(i)])
                    #print index
                    genre_count[index]=genre_count[index]+1   
                        
        except IndexError:
            pass
f5=file('TV_genre_count.csv','w')
l= len(genre_count)               
#for i in actors_count:
 #   print i
for i in range(1,l):
    try:
        output=''
        output=str(i)+","
        output=output+str(genre_count[i])
        f5.write(output)
        #print output
        f5.write("\n")
    except IndexError:
        pass


f1.close()
f2.close()
#f4.close()
f5.close()
