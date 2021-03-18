# Shape of number 0 using fucntions
def for_0():
    """ *'s printed in the shape of number 0 """
    for row in range(9):
        for col in range(5):
            if row%8 ==0 and col%4 !=0 or row%8 !=0 and col%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_0():
    """ *'s printed in the shape of number 0 """
    row =0
    while row<9:
        col =0
        while col<5:
            if row%8 ==0 and col%4 !=0 or row%8 !=0 and col%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1
    

