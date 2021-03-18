# Capital Alphabet H using Function
def for_H():
    """ *'s printed in the Shape of Capital H """
    for row in range(9):
        for col in range(6):
            if col %5 ==0 or row ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_H():
    """ *'s printed in the Shape of Capital H """
    row =0
    while row <9:
        col =0
        while col<6:
            if col %5 ==0 or row ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col +=1
        print()
        row +=1

