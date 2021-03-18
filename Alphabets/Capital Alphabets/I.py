# Capital Alphabet I using Function
def for_I():
    """ *'s printed in the Shape of Capital I """
    for row in range(9):
        for col in range(5):
            if row %8 ==0 or col ==2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_I():
    """ *'s printed in the Shape of Capital I """
    row =0
    while row <9:
        col =0
        while col <5:
            if row %8 ==0 or col ==2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

            


