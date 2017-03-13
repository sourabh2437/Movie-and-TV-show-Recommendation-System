import csv
import operator
f=file('../data/test1.csv','r')
actor=0
genre=0
rating=0
for row in csv.reader(f):
    a=row[0]
    b=row[1]
    c=row[2]
if a=='1' and b=='1':
    if c=='1':
        actor=0.3
        genre=0.2
        rating=0.5
    else:
        actor=0.7
        genre=0.3
        rating=0.1
if a=='1' and c=='0' and b=='0':
    actor=0.9
    genre=0
    rating=0.1
if a=='0' and c=='0' and b=='1':
    actor=0
    genre=0.9
    rating=0.1
if a=='0' and c=='1' and b=='0':
    actor=0.1
    genre=0.1
    rating=0.8
if a=='0' and c=='1' and b=='1':
    actor=0.1
    genre=0.4
    rating=0.8
if a=='1' and c=='1' and b=='0':
    actor=0.5
    genre=0
    rating=0.5

#print actor
#print genre
#print rating
f.close() 

f1=file('../data/Hollywood_movie_calc.csv','r')
f5=file('../data/movie_score.csv','w')


for row in csv.reader(f1):
    try:
        score=0
        flag=0
        new_row1=row[1].split(":")
        new_row2=row[2].split(":")
        #print new_row
        f4=file('../data/userLiked_moviesID.csv','r')
        for col in csv.reader(f4):
            #print col[0]
            if row[0]==col[0]:
                flag=1
                #print col[0]
                break
        if flag==0:
            
            for i in range(0,len(new_row1)):
                index=new_row1[i]
                #print 'index'+" "+index
                f2=file('../data/top_actors.csv','r')
                for j in csv.reader(f2):
                    #print j[0]
                    if index==j[0]:
                        #print j[1]
                        #print int(j[1])*(0.2)
                        score=score+int(j[1])*(actor)
                        #print score
                        break
            for k in range(0,len(new_row2)):
                index=new_row2[k]
                f3=file('../data/top_genre.csv','r')
                for l in csv.reader(f3):
                    if index==l[0]:
                        #print 'hi'
                        score=score+int(l[1])*(genre)
                        #print score
                        break
            #print int(row[3])
            score=score+float(row[3])*(rating)
            #print row[0]+" "+str(score)
            output=''
            output=row[0]+","+str(score)
            f5.write(output+"\n")
            
            #f2.close() 
    except IndexError:
        pass
f4.close()
f5.close()               
#f2.close()
f1.close()
           
             
   
