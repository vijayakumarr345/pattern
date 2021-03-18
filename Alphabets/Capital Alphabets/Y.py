# Capital Alphabet Y using Function
def for_Y():
    """ *'s printed in the Shape of Capital Y """
    for row in range(9):
        for col in range(9):
            if row==col and row < 5 or row +col ==8 and row <5 or col==4 and row >3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_Y():
    """ *'s prined in the Shape of Capital Y """
    row =0
    while row <9:
        col =0
        while col <9:
            if row==col and row < 5 or row +col ==8 and row <5 or col==4 and row >3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

