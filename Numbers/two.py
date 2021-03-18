# Shape of number 2 using fucntions
def for_2():
    """ *'s printed in the shape of number 2 """
    for row in range(9):
        for col in range(9):
            if row ==8 or row+col ==8 and row  !=0 or row ==0 and col%8 !=0 or row ==1 and col ==0 or row ==2 and col ==0:
                print('*',end =' ')
            else:
                print(' ',end=' ')
        print()

def while_2():
    """ *'s printed in the shape of number 2 """
    row =0
    while row<9:
        col =0
        while col <9:
            if row ==8 or row+col ==8 and row  !=0 or row ==0 and col%8 !=0 or row ==1 and col ==0 or row ==2 and col ==0:
                print('*',end =' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1
    

