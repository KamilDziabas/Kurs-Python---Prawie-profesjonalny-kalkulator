#Napisz program który będzie wykonywał 4 podstawowe operacje
#arytmetyczne: +,-,*,/

#Po wprowadzeniu dwóch liczb, użytkownik ma wybrać lub wprowadzić rodzaj
#operacji jaka ma zostać wykonana.
print("Podaj pierwszą liczbę")
a = int(input())
print("Podaj drugą liczbę")
b = int(input())
print("Jaką operację chcesz wykonać?")
operacja = input()
if operacja == "+":
    wynik = a + b
    print(wynik)
elif operacja == "-":
    wynik = a - b
    print(wynik)
elif operacja == "*":
    wynik = a * b
    print(wynik)
elif operacja == "/":
    wynik = a / b
    print(wynik)
else:
    print("Działanie nieprawidłowe")
