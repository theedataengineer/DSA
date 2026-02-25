# Store apples's stock price for 5 days and answer
# 1. What was the price on day 1
# 2. What was the price on day 3

stock_price=[298,305,320,301,292]
print(stock_price[0]) # Stock price on day 1
print(stock_price[2]) # Stock price on day 3


# Store apple's stock price from March 4 to March 7 and answer
# 1. What was the price on March 7
# 2. What was the price on March 5

stock_price ={
    'March 4': 298,
    'March 5': 305,
    'March 6': 320,
    'March 7': 301
}

print(f"The price on March 7 was", stock_price['March 7'])
print(f"The price on March 5 was", stock_price['March 5'])


# Memory Layout of the two Data Structures!

# 1. Array or List - Numbers stored in a continous location.
# 2. Hash Table - Dictionaries store data in a hash map. A key(hash function) and a given element.





# Example of a program whose time complexity is 0(n)

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers


numbers=[2,5,8,9]
print(get_squared_numbers(numbers))



## 0(1) Example

def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe


# 0(n^2) - time = a*n^2+b

numbers=[3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i] , " is a duplicate")
            break