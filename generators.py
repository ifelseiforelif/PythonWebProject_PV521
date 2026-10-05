def even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number #перетворює функцію на генератор: числа повертаються по одному, а не створюється весь список у пам’яті.


# Приклад використання
for number in even_numbers(1, 10):
    print(number)


#генератор не створює всі результати одразу, а видає їх по одному, коли вони потрібні
generator = even_numbers(1, 10)

while True:
    answer = input("Отримати наступне парне число? (так/ні): ")

    if answer == "ні":
        break

    if answer == "так":
        try:
            print(next(generator))
        except StopIteration:
            print("Парні числа закінчилися.")
            break