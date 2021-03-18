# Capital Alphabet W using Function
def for_W():
    """ *'s printed in the Shape of Capital W """
    for row in range(9):
        for col in range(9):
            if col%8 ==0 or row+col ==8 and row>3 or row -col ==0 and row >3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_W():
    """ *'s printed in the Shape of Capital W """
    row =0
    while row <9:
        col =0
        while col <9:
            if col%8 ==0 or row+col ==8 and row>3 or row -col ==0 and row >3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

