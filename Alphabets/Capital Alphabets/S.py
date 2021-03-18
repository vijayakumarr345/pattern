# Capital Alphabet S using Function
def for_S():
    """ *'s printed in the Shape of Capital S """
    for row in range(9):
        for col in range(7):
            if row %4 ==0 and col %6 !=0 or col ==0 and row in(1,2,3) or col ==6 and row in (5,6,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_S():
    """ *'s printed in the Shape of Capital S """
    row =0
    while row <9:
        col =0
        while col <7:
            if row %4 ==0 and col %6 !=0 or col ==0 and row in(1,2,3) or col ==6 and row in (5,6,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

