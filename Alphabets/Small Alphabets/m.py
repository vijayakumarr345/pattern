# Small alphabet m using function
def for_m():
    """ *'s printed in the shape of m """
    for row in range(5):
        for col in range(9):
            if col %4 ==0 and row !=0 or row ==0 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_m():
    """ *'s printed in the Shape of Small m """
    row =0
    while row <5:
        col =0
        while col <9:
            if col %4 ==0 and row !=0 or row ==0 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
  


