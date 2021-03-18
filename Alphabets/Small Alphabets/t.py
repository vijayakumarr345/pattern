# Small alphabet t using fucntion
def for_t():
    """ *'s printed in the shape of small t """
    for row in range(9):
        for col in range(5) :
            if col ==2 or row ==7 and col ==3 or row ==6 and col ==4 or row ==2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_t():
    """ *'s printed in the Shape of Small t """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==2 or row ==7 and col ==3 or row ==6 and col ==4 or row ==2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
   
