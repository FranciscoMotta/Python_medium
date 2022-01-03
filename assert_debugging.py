def div(num):
    divisors = [i for i in range(1, num + 1) if num%i==0]
    print(divisors)

def main():
    num = int(input("Ingrese un numero: "))
    assert num >= 0, "Debes ingresar un numero positivo"
    div(int(num))

if __name__ == "__main__":
    main()