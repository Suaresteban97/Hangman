from random import randint
from os import system

#Leemos el archivo data, luego reemplazamos los espacios por un string vacío convirtiendo
# cada una de las líneas en una lista, aquí usamos list comprehension.
def read():
    with open("./sources/data.txt", "r") as f:
        words = [i.replace("\n", "") for i in f]
    return words

def normalize(s): # Remueve los acentos
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
def comparison(word, line):
    draw()
    print(f'                  Encuentra la palabra: ' + ' '.join(line) + f' tiene {len(word)} letras \n')
    word = list(normalize(word))
    line = list(line)
    user = ''
    attemps = 10
    while word != line:
        print(f'\nIntentos: {attemps}')
        user = input('Ingresa una sola letra: ')
        assert len(user) == 1, 'Ingresaste más de una línea'
        assert user.isalpha(), 'Solo puedes ingresar letras'
           
        if attemps >= 1:
            for i in range(0, len(word)):
                if word[i] == user:
                    line[i] = word[i]
        attemps = attemps - 1        
        
        print(' '.join(line))
        
        if attemps == 0:
            print(f'\n¡Perdiste!, no lograste adviniar la palabra, era: ' + ''.join(word))
            break
        elif word == line:
            print(f'Ganaste descubriste toda la palabra: ' + ''.join(word))
            break
        
    reinicio()

def reinicio():
    choose = int(input("""
        ¿Deseas jugar nuevamente (escribe el número y presiona enter)?
        1. Sí
        2. No
        -"""))
    if choose == 1:
        system('clear')
        run()         
    else: 
        print('Gracias por jugar')
        quit()    
        
    

def draw():
    print("""
        ***  ***  ********  *****    ***  ***********  *****    ********  ********  *****    ***
       ***  ***  ********  ******   ***  ***********  ******   ********  ********  ******   *** 
      ********  **   ***  *** ***  ***  ***          *** ***  ***  ***  **   ***  *** ***  ***  
     ********  ********  ***  *** ***  ***  ******  ***  *** ***  ***  ********  ***  *** ***
    ***  ***  ***  ***  ***   ******  ***  ** ***  ***   ******  ***  ***  ***  ***   ****** 
   ***  ***  ***  ***  ***    *****  ***********  ***    *****  ***  ***  ***  ***    *****  
                                 ¡VAMOS A JUGAR AHORCADO!
""")

def run():
    words = read() 
    index = randint(0, len(words))
    word = words[index]
    line = '_' * len(word)
    comparison(word, line)
    
if __name__ == '__main__':
    run()
