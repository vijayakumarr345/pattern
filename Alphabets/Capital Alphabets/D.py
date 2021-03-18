# Capital Alphabet D using Function
def for_D():
    """ *'s printed in the Shape of Capital D """
    for row in range(9):
        for col in range(6):
            if col ==0 or row %8 == 0 and col!=5 or col ==5 and row %8 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_D():
    """ *'s printed in the Shape of Capital D """
    row =0
    while row<9:
        col =0
        while col <6:
            if col ==0 or row %8 == 0 and col!=5 or col ==5 and row %8 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col +=1
        print()
        row +=1

            
