menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def display_menu():
    print("-"*10, "MENU", "-"*10)
    for option in menu:
        print(f"{option}. {menu[option]["name"] : <9} // { menu[option]["price"] : >4}")
    print()

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = int(input("Select item number" + str(count) + "from 1 to 5: "))
        count += 1
        order.append(menu[item])
    return order

def print_order(order):
    print("You have ordered " + str(len(order)) + " items")
    items = [item["name"] for item in order]
    print(items)
    return order

def calculate_subtotal(order):
    pre_sum = [price["price"] for price in order]
    subtotal = sum(pre_sum)
    print('Calculating bill subtotal...')
    return round(subtotal, 2)

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    tax = subtotal*0.15
    return round(tax, 2)

def summarize_order(order):
    print_order(order)
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)

    item_names = [item["name"] for item in order]
    return item_names, total
          
    
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("The subtotal is: ", subtotal)

    tax = calculate_tax(subtotal)
    print("Total taxes are: ", tax)

    names, total = summarize_order(order)
    print(f"Order summary: Items: {names}, total {total}")
    


if __name__ == "__main__":
    main()