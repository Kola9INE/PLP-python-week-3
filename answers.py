def calculate_discount(price:float, discount:float):
    if discount <= 20:
        print('The discount cannot be applied at this discount rate')
        return price
    else:
        print("Calculating discount...")
        disc_rate  = price * discount/100
        return price - disc_rate

if __name__ == '__main__':
    original_price = input("Enter original price here: ")
    discount = input("Enter discount percent here: ")
    try:
        original_price = float(original_price)
        discount = float(discount)
        print(calculate_discount(
            price = original_price,
            discount=discount
        ))
    except:
        print(original_price)