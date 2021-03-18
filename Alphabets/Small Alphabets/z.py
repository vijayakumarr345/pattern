# Small alphabet z using fucntion
def for_z():
    """ *'s printed in the shape of z """
    for row in range(5):
        for col in range(5):
            if row+col ==4 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_z():
    """ *'s printed in the Shape of Small z """
    row =0
    while row <5:
        col =0
        while col <5:
            if row+col ==4 or row%4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

