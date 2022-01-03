from typing import Sequence


def main():
    # squares = []
    # for i in range(1,101):
    #     if i%3 != 0:
    #         squares.append(i**2)
    # print(squares)
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    #      elementos para cada interable  condicion
    # para cada i que va de 1 - 101 se guarda solo los datos que no son
    # divisibles entre 3
    print(squares)
    MAX = 99999
    multiplos = [i for i in range(1, MAX) if ((i%4==0) and (i%6==0) and(i%9==0))]
    print(multiplos)
if __name__ == '__main__':
    main()