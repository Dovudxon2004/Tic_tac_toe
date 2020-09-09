x='x'
y='y'
z=' '
a=1
tic=[[z,z,z],[z,z,z],[z,z,z]]
print(tic[0])
print(tic[1])
print(tic[2])


def winner():
    global a
    if tic[0][0]==tic[1][1]==tic[2][2]==x or tic[0][2]==tic[1][1]==tic[2][0]==x:
        print('player 1 wins')
        a=0
    elif tic[0][0]==tic[1][1]==tic[2][2]==y or tic[0][2]==tic[1][1]==tic[2][0]==y:
        print('player 2 wins')
        a=0
    for elem in range(3):
        if tic[elem][0]==tic[elem][1]==tic[elem][2]==x or tic[0][elem]==tic[1][elem]==tic[2][elem]==x:
            print('player 1 wins')
            a=0
        elif tic[elem][0]==tic[elem][1]==tic[elem][2]==y or tic[0][elem]==tic[1][elem]==tic[2][elem]==y:    
            print('player 2 wins')    
            a=0
        
        

def play1():
    go1=input('row,col ')
    go1=go1.split(',')
    while tic[(int(go1[0])-1)][(int(go1[1])-1)]!=z:
        go1=input('try again: row,col ')
        go1=go1.split(',')
    tic[(int(go1[0])-1)][(int(go1[1])-1)]=x
    print(tic[0])
    print(tic[1])
    print(tic[2])


def play2():
    go2=input('row,col ')
    go2=go2.split(',')
    while tic[(int(go2[0])-1)][(int(go2[1])-1)]!=z:
        go2=input('try again: row,col ')
        go2=go2.split(',')
    tic[(int(go2[0])-1)][(int(go2[1])-1)]=y
    print(tic[0])
    print(tic[1])
    print(tic[2])        


def main():
    t=0
    while t<9:
        t=t+1
        play1()
        winner()
        if a==0:
            break
        if t==9:
            break
        t=t+1
        play2()
        winner()
        if a==0:
            break
        if t==9:
            break
    if a==1:
        print(' it was draw')

if __name__ == "__main__":
    main()
        
