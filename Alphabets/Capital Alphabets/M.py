# Capital Alphabet M using Function
def for_M():
    """ *'s printed in the Shape of Capital M """
    for row in range(9):
        for col in range(9):
            if col %8 ==0 or row -col ==0 and row <5 or col +row ==8 and row<5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_M():
    """ *'s printed in the Shape of Capital M """
    row =0
    while row <9:
        col =0
        while col <9:
            if col %8 ==0 or row -col ==0 and row <5 or col +row ==8 and row<5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

