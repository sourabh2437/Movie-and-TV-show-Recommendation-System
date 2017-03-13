import csv
import operator

f1=file('../data/TVshow_Database.csv','r')
f5=file('../data/TV_movie_score.csv','w')


for row in csv.reader(f1):
    try:
        score=0
        flag=0
        #new_row1=row[1].split(":")
        new_row2=row[1].split(":")
        #print new_row
        f4=file('../data/TV_output.csv','r')
        for col in csv.reader(f4):
            #print col[0]
            if row[0]==col[0]:
                flag=1
                #print col[0]
                break
        if flag==0:
            for k in range(0,len(new_row2)):
                index=new_row2[k]
                f3=file('../data/TV_top_genre.csv','r')
                for l in csv.reader(f3):
                    if index==l[0]:
                        #print 'hi'
                        score=score+int(l[1])*(0.8)
                        #print score
                        break
            #print int(row[3])
            score=score+float(row[2])*(0.2)
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
           
             
   
