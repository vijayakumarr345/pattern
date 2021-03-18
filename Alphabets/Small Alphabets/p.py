# Small alphabet p using function
def for_p():
    """ *'s printed in the shape of p """
    for row in range(9):
        for col in range(5):
            if col ==0 or row in (1,5) and col !=4 or col ==4 and row in (2,3,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_p():
    """ *'s printed in the Shape of Small p """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==0 or row in (1,5) and col !=4 or col ==4 and row in (2,3,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

