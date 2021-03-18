# Capital Alphabet B using Fuction
def for_B():
    """ *'s printed in the Shape of Capital B """
    for row in range(9):
        for col in range(5):
            if col ==0  or row%4 ==0 and col%4 !=0 or col ==4 and row%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_B():
    """ *'s printed in the Shape of Capital B """
    row =0
    while row<9:
        col =0
        while col<5:
            if col ==0  or row%4 ==0 and col%4 !=0 or col ==4 and row%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col +=1
        print()
        row +=1

