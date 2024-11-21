MOD = 10**9 + 7

    # Задание 1
def Task1():
    print("============== Задание #1 ==============\n")

    t = int(input("Введите количество наборов данных: "))
    for i in range(t):
        n = int(input(f"Введите {i+1}-й набор данных: "))
        print(f"Результат #{i+1}: {Task1_Formula(n)}")

    print("\n========================================\n\n")

def Task1_Formula(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += (i & j)
            result %= MOD
    return result

    # Run
if __name__ == "__main__":
    Task1()
