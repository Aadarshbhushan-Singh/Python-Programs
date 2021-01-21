def exception_function():
	n=int(input())
	for i in range(n):
		try:
			list_numbers=list(map(int, input().split()[:2]))
			print(list_numbers[0]//list_numbers[1])
		except Exception as error:
			print("Error Code:",error)
exception_function()

''''This below code can also be tried'''

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)