# Function to calculate sum of odd numbers from 1 to 100
def sum_odd_number():
    sum = 0 
    for i in range(1,101,2):
        sum+=i
    return sum
result = sum_odd_number()
print("sum of odd number = ",result)

def sumOfEvenNum(n):
    sum = 0
    for i in range(0,n+1,2):
        sum +=i
    return sum
n = int(input("enter how many even number sum :"))
print(sumOfEvenNum(n))