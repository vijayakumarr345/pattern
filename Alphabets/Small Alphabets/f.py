# Small alphabet f  using function
def for_f():
    """ *'s printed in the Shape of Small f """
    for row in range(9):
        for col in range(5):
            if col ==1 and row !=0 or row ==0 and col not in (0,1) or row ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_f():
    """ *'s printed in the Shape of Small f """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==1 and row !=0 or row ==0 and col not in (0,1) or row ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1


