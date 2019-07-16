# Traductor Español-Koruño.
# (C) 2019 fpedraza
# licencia: GNU GPL

import re

# inicialización de variables
dict=           {}
suffix =        ['neno','chorbo']
question =      '¿Oistes?'
surprise =      ['¡Buah neno!', '¡Que muvi!' ]
esp2kor_dict=   'esp2kor.dict.txt'
idx =           0


def load_dict():
    global dict
    with open(esp2kor_dict) as f:
        for line in f:
            try:
                (key, val) = line.split(':')
                dict[key] = val.lower().strip()
            except:
                print("no se ha conseguido leer la línea")

def add_suffix(i,k=0):
    # añadir a cada frase el sufijo apropiado, neno o chorbo
    i+=', '+suffix[k]+'.'
    return i

def add_question(i):
    # las preguntas en Koruño siempre debe iniciarse con ¿Oistes?
    i=re.sub('(\¿.*\?)', r'¿Oistes? \1',i)
    return i

def add_surprise(i):
    # añadir  a las oraciones con !¡ la expresión de sorpresa apropiada
    i=re.sub('(\¡.*\!)', surprise[0]+r' \1 '+surprise[1] ,i)
    return i

# programa principal
print("Traductor Español-Koruño")

try:
    load_dict()
except:
    print("no se ha encontrado el diccionario")
    exit()


inp=input("Texto a traducir: ")
sentences=inp.split(sep='.')

print("\nTraducción:\n")
for i in sentences:
    if len(i) > 1:
        i=add_question(i)
        i=add_surprise(i)
        if i.find('?')<0 and i.find('!')<0:
            i=add_suffix(i,idx%2)
            idx+=1

        for key in dict.keys():
            i=re.sub(key, dict[key],i,flags=re.IGNORECASE)

        i=i.strip()
        print(i)
    

