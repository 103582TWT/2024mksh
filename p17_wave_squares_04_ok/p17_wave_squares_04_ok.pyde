# p17_wave_squares_04_ok
a = [
     [1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1], # 三個1,四個2,四個1,四個2,1
     [2,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2],
     [2,2,1,1,1,2,2,2,2,1,1,1,1,2,2,2],
     [2,2,2,1,1,1,2,2,2,2,1,1,1,1,2,2],
     [1,2,2,2,1,1,1,1,2,2,2,2,2,1,1,2],
     [1,1,2,2,2,1,1,1,1,1,2,2,2,2,1,1],
     [1,1,1,2,2,2,1,1,1,1,1,2,2,2,2,1],
     [1,1,1,1,2,2,2,1,1,1,1,1,2,2,2,2],
     [1,1,1,2,1,2,2,1,1,1,1,1,1,2,2,1],
     [2,1,1,1,2,1,2,2,2,1,1,1,1,1,2,2],
     [2,2,1,1,1,2,1,2,2,2,1,1,1,1,1,2],
     [2,2,2,1,1,1,2,1,2,2,2,1,1,1,1,1],
     [2,2,2,2,1,1,1,2,1,2,2,2,1,1,1,1],
     [1,2,2,2,2,1,1,1,1,1,2,2,2,1,1,1],
     [1,1,2,2,2,2,1,1,1,1,1,2,2,2,1,1],
     [1,1,1,2,2,2,2,1,1,1,1,1,2,2,2,1]]

size(480, 480)
for i in range(len(a)):
    for j in range(16):
            if (i+j)%2==1:fill(255) #白色
            else: fill(0) #黑色
            rect(j*30,i*30, 30, 30)
            if(i+j)%2==1:fill(0) #黑色
            else: fill(255) #白色
            if a[i][j]==1:
                rect(j*30+2, i*30+2, 9, 9)
                rect(j*30+19, i*30+19, 9, 9)
            else:
                rect(j*30+19, i*30+2, 9, 9)
                rect(j*30+2, i*30+19, 9, 9)
