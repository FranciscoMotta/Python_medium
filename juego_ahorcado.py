from os import read, times_result
import os
import random

def character_presentation(step):
    
    IMÁGENES_AHORCADO = ['''
        ||===||
        
             ||

             ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||

             ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
             ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
        (  )  ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
      /(  )  ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
      /(  )\ ||

             ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
      /(  )\ ||

        ()   ||

             ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
      /(  )\ ||

        ()   ||

       |      ||
    ==================''',
    '''
        ||===||
         |
       ('ʖ') ||
         v
      /(  )\ ||

        ()   ||

       |   | ||
    ==================''',
    '''
        ||===||
         |
       (xʖx) ||
         v
      /(  )\ ||

        ()   ||

       |   | ||
    ==================''',]
    print(IMÁGENES_AHORCADO[step])

def read_data_base():
    words = [] 
    with open("./archivos/data.txt", "r", encoding="utf-8") as data_set: # Leemos la base de datos
        for line in data_set: 
            words.append(line) # Agregamos a la lista
        return words

def presentation():
    TITLE = """
    
░█████╗░██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║███████║██║░░██║██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║
██╔══██║██╔══██║██║░░██║██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║
██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░
    

            ░██████╗░░█████╗░███╗░░░███╗███████╗
            ██╔════╝░██╔══██╗████╗░████║██╔════╝
            ██║░░██╗░███████║██╔████╔██║█████╗░░
            ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
            ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
            ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
            
                                            █▄▄ █▄█   █ █ █ █▀▀ ▀█▀ █▀█ █▀█
                                            █▄█  █    ▀▄▀ █ █▄▄  █  █▄█ █▀▄
    """
    print(TITLE)
    

def little_title():
    title = """
    █▀▀█ █░░█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀▄ █▀▀█ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ 
    █▄▄█ █▀▀█ █░░█ █▄▄▀ █░░ █▄▄█ █░░█ █░░█ 　 █░▀█ █▄▄█ █░▀░█ █▀▀ 
    ▀░░▀ ▀░░▀ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ 　 ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀
    """
    print(title)

def letter_choice():
    letter = input("ESCRIBA UNA LETRA: ")
    return letter

def happy_dummy():
    DUMMY = ['''
       ('ʖ') 
     m   v   m
     \/(  )\/
        ()   
       |   |   
      ==   ==
    ''',]
    print(DUMMY[0])
def main():
    words_data = read_data_base();
    select_word = random.choice(words_data)
    select_word = list(select_word)
    spaces = ["PALABRA SECRETA: "]
    correct_word = []
    presentation()
    estado = True
    for i in range(0, len(select_word)-1):
        correct_word.append("_ ")

    asnwers = "".join(spaces + correct_word)

    # Variables de desarrollo
    counter = 0
    state = True
    ok = False
    coincidence = 0
    chain = "".join(spaces)
    while(state):
        letter_local = letter_choice()
        for i in range(0, len(select_word)):
            if(select_word[i] == letter_local):
                correct_word[i] = letter_local
                ok = True
            else:
                pass
        if(not(ok)):
            counter+=1
            if counter >= 10:
                break
            else:
                pass
        else:
            pass

        for i in range(0,len(correct_word)):
            if select_word[i]==correct_word[i]:
                coincidence += 1
            else:
                pass
        if coincidence == len(correct_word):
            os.system("cls")
            little_title()
            asnwers = "".join(spaces + correct_word)
            print(asnwers)
            print("GANASTE!") 
            happy_dummy()
            break
        else:
            pass
        asnwers = "".join(spaces + correct_word)
        os.system("cls")
        little_title()
        print(character_presentation(counter))
        print(asnwers)
        print(str(coincidence) + str(len(correct_word)))
        ok = False
        coincidence = 0
    
    print("LA PALABRA RECRETA FUE: " + "".join(select_word))
if __name__ == "__main__":
    main()