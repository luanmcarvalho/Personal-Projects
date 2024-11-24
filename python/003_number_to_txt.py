numbers = ('zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')

while True:
    n = int(input("Choose a number between 0 and 10: "))
    if 0 <= n <= 10:
        break
print(f"The number you entered is {numbers[n]}.")
