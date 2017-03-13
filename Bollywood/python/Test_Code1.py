import csv


f2 = file('../user_input.csv', 'r')
f3 = file('../data/userLiked_moviesID.csv', 'w')



c3 = csv.writer(f3)


for user in csv.reader(f2):
        f1 = file('../data/Bollywood_movie_database.csv', 'r')
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
