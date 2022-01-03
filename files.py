def read():
    numbers = [] # Creamos la lista
    with open("./archivos/numbers.txt",'r', encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Juan", "Miguel", "Martin", "Jhon"]
    with open("./archivos/numbers.txt", 'a', encoding="utf-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")
    
def main():
    # read()
    write()

if __name__ == "__main__":
    main()
