# Prosty kalkulator w Pythonie

def calculator():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    choice = input("Wybierz (1/2/3/4): ")

    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print("Wynik:", num1 + num2)
        elif choice == '2':
            print("Wynik:", num1 - num2)
        elif choice == '3':
            print("Wynik:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Wynik:", num1 / num2)
            else:
                print("Błąd: Dzielenie przez zero!")
        else:
            print("Nieprawidłowy wybór.")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość.")

calculator()
