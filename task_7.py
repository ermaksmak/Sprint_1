def run7():
    print("Введите целое положительное число")
    digit_root(int(input()))
def digit_root(num):
    print("Исходное число: ", num)
    while num > 9:
        num = sum(int(digit) for digit in str(num))
        print("Цифровой корень: ", num)
    return num