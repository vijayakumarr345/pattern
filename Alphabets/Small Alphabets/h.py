# Small alphabet h using function
def for_h():
    """ *'s printed in the Shape of small h """
    for row in range(9):
        for col in range(6):
            if col ==0 or  row ==4 and col !=5 or col ==5 and row > 4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_h():
    """ *'s printed in the Shape of Small h """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or  row ==4 and col !=5 or col ==5 and row > 4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
  
