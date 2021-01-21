def print_formatted(n):
    for i in range(1,n+1):
        print(int(i), end=" ") 
        print(hex(i).upper()[2:], end=" ")
        print(oct(i)[2:],end=" ") 
        print(bin(i)[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# print(str(i).rjust(len(str(bin(number)[2:])))+" "+str(oct(i)[2:]).rjust(len(str(bin(number)[2:])))+" "+str(hex(i)[2:]).upper().rjust(len(str(bin(number)[2:])))+" "+str(bin(i)[2:]).rjust(len(str(bin(number)[2:]))))
