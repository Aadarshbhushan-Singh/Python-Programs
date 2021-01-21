def collatz(num):
        sum=1
        while num>1:
                print(num)
                if num%2==0:
                        num=int(num/2)
                else:
                        num=num*3+1
                sum+=1
        print(1)
        print("Total Numbers: ",sum)
collatz(10)
