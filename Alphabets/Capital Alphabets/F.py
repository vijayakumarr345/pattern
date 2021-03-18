# Capital Alphabet F using Function
def for_F():
    """ *'s printed in the Shape of Capital F """
    for row in range(8):
        for col in range(5):
            if col ==0 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_F():
    """ *'s printed in the Shape of Capital F """
    row =0
    while row <8:
        col =0
        while col <5:
            if col ==0 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col +=1
        print()
        row +=1

            
