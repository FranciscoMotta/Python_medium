def div(num):
    divisors = [i for i in range(1, num + 1) if num%i==0]
    print(divisors)

def main():
    num = int(input("Ingrese un numero: "))
    div(num)

if __name__ == "__main__":
    main()