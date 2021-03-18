# Capital Alphabet O using Function
def for_O():
    """ *'s printed in the Shape of Capital O """
    for row in range(9):
        for col in range(9):
            if row%8 !=0 and col %8 ==0 or row %8 ==0 and col %8 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_O():
    """ *'s printed in the Shape of Capital O """
    row =0
    while row <9:
        col =0
        while col <9:
            if row%8 !=0 and col %8 ==0 or row %8 ==0 and col %8 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1






