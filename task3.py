def pipeline(value, functions):
    result = value
    for fn in functions:
        result = fn(result)
    return result

def add_tax(price):
    return price * 1.18

def round_price(price):
    return round(price, 2)

funcs1 = [add_tax, lambda x: x - 5, round_price]
result1 = pipeline(100, funcs1)
print("Ardicilliq 1 neticesi:", result1)

funcs2 = [lambda x: x - 5, add_tax, round_price]
result2 = pipeline(100, funcs2)
print("Ardicilliq 2 neticesi:", result2)

print("Izah: Funksiyalarin yeri deyisende netice ferqli olur, cunki birinci halda 18% vergi 100 uzerine gelir ve sonra 5 cixilir. Ikinci halda ise evvelce 5 cixilib 95 qalir, sonra 95 uzerine vergi hesablanir.")
