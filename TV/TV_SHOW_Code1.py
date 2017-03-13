import csv


f2 = file('TV_like.csv', 'r')
f3 = file('TV_output.csv', 'w')



c3 = csv.writer(f3)


for user in csv.reader(f2):
        f1 = file('TVshow_id.csv', 'r')
        for admin in csv.reader(f1):
                try:
                        if user[0]==admin[0]:
                                #print admin[1]
                                f3.write(admin[1]+"\n")
                except IndexError:
                        pass
        
              

f1.close()
f2.close()
f3.close()
