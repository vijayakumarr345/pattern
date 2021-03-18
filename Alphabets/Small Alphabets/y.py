# Small alphabet y using fucntion
def for_y():
    """ *'s printed in the shape of y """
    for row in range(5):
        for col in range(5):
            if row+col ==4 or row ==col and row <2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_y():
    """ *'s printed in the Shape of Small y """
    row =0
    while row <5:
        col =0
        while col <5:
            if row+col ==4 or row ==col and row <2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

