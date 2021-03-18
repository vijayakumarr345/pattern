# Small alphabet w using fucntion
def for_w():
    """ *'s printed in the shape of w """
    for row in range(5):
        for col in range(9):
            if col% 8 ==0 or row+col ==4 or col -row ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_w():
    """ *'s printed in the Shape of Small w """
    row =0
    while row <5:
        col =0
        while col <9:
            if col% 8 ==0 or row+col ==4 or col -row ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
while_w()
