# Capital Alphabet E using Function
def for_E():
    """ *'s printed in the Shape of Capital E """
    for row in range(9):
        for col in range(6):
            if col ==0 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_E():
    """ *'s printed in the Shape of Capital E """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col += 1
        print()
        row +=1


