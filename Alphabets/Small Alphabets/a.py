# Small alphabet a using Function
def for_a():
    """ *'s printed in the Shape of Small a """
    for row in range(9):
        for col in range(5):
            if col ==4 and row !=0 or row %4 ==0 and col %4 !=0 or col ==0 and row not in (0,3,4,8) : 
                print('*',end =' ')
            else:
                print(' ',end=' ')
        print()

def while_a():
    """ *'s printed in the Shape of Small a """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==4 and row !=0 or row %4 ==0 and col %4 !=0 or col ==0 and row not in (0,3,4,8) : 
                print('*',end =' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

