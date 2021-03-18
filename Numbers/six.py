# Shape of number 6 using functions
def for_6():
    """ *'s printed in the shape of number 6 """
    for row in range(9):
        for col in range(5):
            if col ==0 and row%8 !=0 or row%4 ==0 and col%4 !=0 or col ==4 and row not in (0,2,3,4,8):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_6():
    """ *'s printed in the shape of number 6 """
    row =0
    while row<9:
        col =0
        while col <5:
            if col ==0 and row%8 !=0 or row%4 ==0 and col%4 !=0 or col ==4 and row not in (0,2,3,4,8):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1
    

