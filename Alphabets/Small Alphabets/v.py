# Small alphabet v using fucntion
def for_v():
    """ *'s printed in the shape of v """
    for row in range(5):
        for col in range(9):
            if row==col or row +col ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_v():
    """ *'s printed in the Shape of Small v """
    row =0
    while row <5:
        col =0
        while col <9:
            if row==col or row +col ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

