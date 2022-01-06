import random
import time
import os
from typing import no_type_check

def presentation():
    DOORS = ['''
    
███╗░░░███╗░█████╗░███╗░░██╗████████╗██╗░░░██╗░░░░░░██╗░░██╗░█████╗░██╗░░░░░██╗░░░░░
████╗░████║██╔══██╗████╗░██║╚══██╔══╝╚██╗░██╔╝░░░░░░██║░░██║██╔══██╗██║░░░░░██║░░░░░
██╔████╔██║██║░░██║██╔██╗██║░░░██║░░░░╚████╔╝░█████╗███████║███████║██║░░░░░██║░░░░░
██║╚██╔╝██║██║░░██║██║╚████║░░░██║░░░░░╚██╔╝░░╚════╝██╔══██║██╔══██║██║░░░░░██║░░░░░
██║░╚═╝░██║╚█████╔╝██║░╚███║░░░██║░░░░░░██║░░░░░░░░░██║░░██║██║░░██║███████╗███████╗
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝

██████╗░██████╗░░█████╗░██████╗░██╗░░░░░███████╗███╗░░░███╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝████╗░████║
██████╔╝██████╔╝██║░░██║██████╦╝██║░░░░░█████╗░░██╔████╔██║
██╔═══╝░██╔══██╗██║░░██║██╔══██╗██║░░░░░██╔══╝░░██║╚██╔╝██║
██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗███████╗██║░╚═╝░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝
                                                                        
                                                                █▄▄ █▄█   █▀▀ █▀▄▀█ ▄█ █▀█
                                                                █▄█  █    █▀  █ ▀ █  █ ▀▀█

     ||===||===||===||      ||===||===||===||       ||===||===||===||
                 
     ||      1      ||      ||      2      ||       ||      3      ||

     ||            O||      ||            O||       ||            O||

     ||             ||      ||             ||       ||             ||

     ||             ||      ||             ||       ||             ||
    ==================      ==================     ==================   '''
    
    ,]
    print(DOORS[0])

def door_opened (door):
    DOOR = ['''
     ||===||===||===||
                 
     ||      1      ||

     ||            O||

     ||             ||

     ||             ||
    ===================  ''',
    '''
     ||===||===||===||
                 
     ||      2      ||

     ||            O||

     ||             ||

     ||             ||
    ===================  ''',
    '''
     ||===||===||===||
                 
     ||      3      ||

     ||            O||

     ||             ||

     ||             ||
    ===================  ''',
    ]
    print(DOOR[door - 1])

def door_pair(door1, door2):
    DOOR_PAIR = ['''
     ||===||===||===||      ||===||===||===||       

     ||     ''' + str(door1)+ '''       ||      ||      ''' + str(door2) + '''      || 

     ||            O||      ||            O||       

     ||             ||      ||             ||   

     ||             ||      ||             ||   
    ==================      ==================   '''
    ]
    print(DOOR_PAIR[0])

def doors_state():
    data = {
        "CASE 1" : [1,2,3],
        "CASE 2" : [3,2,1],
        "CASE 3" : [2,1,3],
        "CASE 4" : [2,3,1],
        "CASE 5" : [1,3,2],
        "CASE 6" : [3,1,2],
    }

    case_random = random.choice(list(data.values()))
    return case_random

def door_select():
    
    TITLE = ['''    
        █▀▀ █░░ █ █▀▀ █▀▀   █░█ █▄░█ ▄▀█   █▀█ █░█ █▀▀ █▀█ ▀█▀ ▄▀█
        ██▄ █▄▄ █ █▄█ ██▄   █▄█ █░▀█ █▀█   █▀▀ █▄█ ██▄ █▀▄ ░█░ █▀█
    
    ''',]
    
    selected = int(input(TITLE[0]))
    return selected


#########################################################################

def main():
    presentation()
    case_random = list(doors_state())
    price = random.choice(case_random) ## UBICACION DEL PREMIO
    answer = door_select() ## PUERTA ELEGIDA

    if answer == price:
        case_random.remove(answer)
        not_price = random.choice(case_random)
        case_random.remove(not_price)
        not_price_final = random.choice(case_random)
    elif answer != price:
        case_random.remove(answer)
        case_random.remove(price)
        not_price_final = random.choice(case_random)
        not_price = price
    else:
        pass
    # case_random.remove(answer) ## QUITAMOS EL ELEMENTO ELEGIDO
    # not_price = random.choice(case_random) ## ELEGIMOS UNA PUERTA CUALQUIERA
    # case_random.remove(not_price)
    last_select = not_price
    print("ELEGISTE LA PUERTA: " + str(answer))
    door_opened(answer)
    time.sleep(1.5)
    print("LA PUERTA " + str(not_price_final) + " NO TIENE EL PREMIO")
    door_opened(not_price_final)
    time.sleep(1)
    print("SOLO QUEDA LA PUERTA: " + str(answer) + " Y LA PUERTA: " + str(last_select))
    door_pair(answer, last_select)
    time.sleep(1)
    change = input("DESEAS CAMBIAR DE PUERTA? Y/N: ")

    if (change == 'Y') or (change == 'y'):
        answer = last_select
    elif (change == 'N') or (change == 'n'):
        answer = answer
    else:
        pass
    
    if answer == price:
        print("GANASTE!")
    else:
        print("PERDISTE :(")
    print("LA PUERTA GANADORA ES: " + str(price))
    door_opened(price)
if __name__ == "__main__":
    main()