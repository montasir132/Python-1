# def add_num():
#     add_num=[]
#     for i in range(5):
#         num = int(input(f"enter your number {i+1}: "))
#         add_num.append(num)
#     total = 0
#     total=sum(add_num)
#     print(total)
    
# add_num()

# def add_sum():
#     add_num=[]
#     print("enter your 5 number")
#     for i in range(5):
#         num = int(input(f"enter number {i+1}: "))
#         add_num.append(num)
#     total = 0
#     total = sum(add_num)
#     print(total)
    
# add_sum()


def add_num():
    add_list = []
    n = int(input("How many number you are input: "))
    print(f'Enter your {n} number')
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        add_list.append(num)
    total = sum(add_list)
    print(f"Your total sum: {total}")
# add_num()

def sumOfList(n):
    numbers = []
    for i in range(n):
        num = float(input(f"Enter your number {i+1} : "))
        numbers.append(num)
    return sum(numbers) 
n = int(input("Enter how many number you are input : "))
print(f"total sum: {sumOfList(n)}")
