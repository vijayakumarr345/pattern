# Small alphabet r using fucntion
def for_r():
    """ *'s printed in the shape of r """
    for row in range(5):
        for col in range(5):
            if col ==1 and row !=0 or row ==0 and col in (0,2,3) or row ==1 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_r():
    """ *'s printed in the Shape of Small r """
    row =0
    while row <5:
        col =0
        while col <5:
            if col ==1 and row !=0 or row ==0 and col in (0,2,3) or row ==1 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
   
