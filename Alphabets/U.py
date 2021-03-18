# Capital Alphabet U using Function
def for_U():
    """ *'s printed in the Shape of Capital U """
    for row in range(9):
        for col in range(7):
            if row !=8 and col %6 ==0 or row ==8 and col %6 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_U():
    """ *'s printed in the Shape of Capital U """
    row =0
    while row <9:
        col =0
        while col <7:
            if row !=8 and col %6 ==0 or row ==8 and col %6 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

