# Small alphabet o using function
def for_o():
    """ *'s printed in the shape of o """
    for row in range(5):
        for col in range(5):
            if row%4 ==0 and col %4 !=0 or row%4 !=0 and col %4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_o():
    """ *'s printed in the Shape of Small o """
    row =0
    while row <5:
        col =0
        while col <5:
            if row%4 ==0 and col %4 !=0 or row%4 !=0 and col %4 ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
           
