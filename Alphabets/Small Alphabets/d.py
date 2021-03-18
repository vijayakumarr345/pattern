# Small alphabet d using Function
def for_d():
    """ *'s printed in the Shape of Small d """
    for row in range(9):
        for col in range(6):
            if col ==5 or row in (4,8) and col !=0 or col ==0 and row in(5,6,7):
                print('*',end=' ')
            else:
                print(' ',end =' ')
        print()

def while_d():
    """ *'s printed in the Shape of Small d """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==5 or row in (4,8) and col !=0 or col ==0 and row in(5,6,7):
                print('*',end=' ')
            else:
                print(' ',end =' ')
            col+=1
        print()
        row +=1
  
