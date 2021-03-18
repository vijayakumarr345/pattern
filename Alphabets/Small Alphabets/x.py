# Small alphabet x using fucntion
def for_x():
    """ *'s printed in the shape of small x """
    for row in range(5):
        for col in range(5):
            if row ==col or row+col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_x():
    """ *'s printed in the Shape of Small x """
    row =0
    while row <5:
        col =0
        while col <5:
            if row ==col or row+col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
              

