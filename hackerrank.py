# from collections import Counter
# no_of_shoes = int(input())
# shoes_lst = map(int, input().split())
# no_of_customers = int(input())

# shoes = Counter(shoes_lst)
# income = 0
# for i in range(no_of_customers):
#     size, price = map(int, input().split())
#     if shoes[size]:
#         income+= price
#         shoes[size]-1
# print(income)

# n = eval(input("Enter a number: "))
# if n%2==1:
#     print("The number is odd")
# else:
#     print("The number is even")


n = int(input())
for i in range(1, n):
        print(i, end = "")