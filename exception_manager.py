def div(num):
    divisors = [i for i in range(1, num + 1) if num%i==0]
    print(divisors)

def main():
    try:
        num = int(input("Ingrese un numero: "))
        div(num)
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Debes ingresar un numero entero positivo")

if __name__ == "__main__":
    main()