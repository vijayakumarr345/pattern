# Capital Alphabet Q using Function
def for_Q():
    """ *'s printed in the Shape of Capital Q """
    for row in range(9):
        for col in range(7):
            if row not in (0,7,8) and col %6 ==0 or row %7 ==0 and col %6!=0 or row ==8 and col ==6:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_Q():
    """ *'s printed in the Shape of Capital Q """
    row =0
    while row <9:
        col =0
        while col <7:
            if row not in (0,7,8) and col %6 ==0 or row %7 ==0 and col %6!=0 or row ==8 and col ==6:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

