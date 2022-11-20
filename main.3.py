student = int(input("количество человек: "))

price = 0

print("Вводимо ціни за 1 шт.")

print("приставка: ")

pen = float(input())

flag = True

while flag == True:

    print("Вибираємо покупки: ")

    print("1.приставка;")

    print("0.Заверишити покупки")

    print("Введіть номер товару: ")

    change = int(input())

    if change == 1:
        price += pen

    if change == 0:
        flag = False

    if change != 1 and change != 2 and change != 3 and change != 0:
        print("Error")

price_class = price * student

print("Ціна 1 приставки = ", price)

print("Ціна всех приставок = ", price_class)

if price_class >= 500:

    price_class_discount = 0.0

    if price_class >= 500 and price_class < 1000:
        print("Вам доступна знижка 10%")

        price_class_discount = (price_class * 10) / 100;

        print("Цiна зi знижкою = ", price_class_discount)

    if price_class >= 1000 and price_class < 2000:
        print("Вам доступна знижка 15%")

        price_class_discount = (price_class * 15) / 100;

        print("Цiна зi знижкою = ", price_class_discount)

    if price_class >= 2000 and price_class < 3000:
        print("Вам доступна знижка 20%")

        price_class_discount = (price_class * 20) / 100;

        print("Цiна зi знижкою = ", price_class_discount)

    if price_class >= 3000 and price_class < 5000:
        print("Вам доступна знижка 25%")

        price_class_discount = (price_class * 25) / 100;

        print("Цiна зi знижкою = ", price_class_discount)

    if price_class >= 5000:
        print("Вам доступна знижка 30%")

        price_class_discount = (price_class * 30) / 100;

        print("Цiна зi знижкою = ", price_class_discount)

else:

    print("Знижка вiдсутня. Ви не досягли мiнiмального порогу цiни.")