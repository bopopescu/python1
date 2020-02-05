"""
200 > 40%off           PC:ZOMATO
100 > 50% upto 150     PC:JUMBO
"""

amount = int(input("Enter an amount"))
promocode = input("Enter Promocode:")

print(">> your amount is",amount)
print(">> your promocode is:",promocode)

if amount > 200:
    if promocode == "zomato":
        amount = amount - (0.4*amount)
        print(">>ZOMATO Applied Successfully !! 40%off")
        print(">>Please Pay: \u20b9", amount)
    else:
        print(">> Try using ZOMATO to get 40% off")
elif amount > 100:
    if promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        else:
            amount = amount - discount
        print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
        print(">> Please Pay: \u20b9", amount)
    else:
        print(">> Try using JUMBO to get 50% OFF")
else:
    print(">> Please Pay: \u20b9", amount)
"""

# HW: Rectify the Use Case Above. Hint shared below:
#     You need to suggest correct promo code as well
if amount > 100:
    if promoCode == "ZOMATO" and amount > 200:
        pass
    elif promoCode == "JUMBO":
        passelif amount > 100:
    if promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        else:
            amount = amount - discount
        print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
        print(">> Please Pay: \u20b9", amount)
    else:
        print(">> Try using JUMBO to get 50% OFF")
else:
    print(">> Please Pay: \u20b9", amount)
"""

# HW: Rectify the Use Case Above. Hint shared below:
#     You need to suggest correct promo code as well
if amount > 100:
    if promoCode == "ZOMATO" and amount > 200:
        pass
    elif promoCode == "JUMBO":
        pass