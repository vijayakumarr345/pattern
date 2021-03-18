# Small alphabet j using function
def for_j():
    """ *'s printed in the Shape of small j """
    for row in range(9):
        for col in range(4):
            if col == 2 and row not in (1,8) or col ==1 and row in (2,8) or col ==0 and row ==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_j():
    """ *'s printed in the Shape of Small j """
    row =0
    while row <9:
        col =0
        while col <4:
            if col == 2 and row not in (1,8) or col ==1 and row in (2,8) or col ==0 and row ==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

