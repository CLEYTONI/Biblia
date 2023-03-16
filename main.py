import requests
import json


Variavel = '''
Gn - Gênesis
Ex - Êxodo
Lv - Levítico
Nm - Números
Dt - Deuteronômio

Js - Josué
Jz - Juízes
Rt - Rute

1Sm - 1 Samuel
2Sm - 2 Samuel

1Rs - 1 Reis
2Rs - 2 Reis

1Cr - 1 Crônicas
2Cr - 2 Crônicas

Esd - Esdras
Ne - Neemias

Tb - Tobias
Jt - Judite
Est - Ester
1Mc - 1 Macabeus
2Mc - 2 Macabeus

Jó - Jó
Sl - Salmos
Pr - Provérbios
Ecl - Eclesiastes
Ct - Cânticos
Sb - Sabedoria
Eclo - Eclesiástico

Is - Isaías
Jr - Jeremias
Lm - Lamentações
Br - Baruc
Ez - Ezequiel
Dn - Daniel
Os - Oséias
Jl - Joel
Am - Amós
Ab - Abdias
Jn - Jonas
Mq - Miquéias
Na - Naum
Hab - Habacuc
Sf - Sofonias
Ag - Ageu
Zc - Zacarias
Ml - Malaquias

Mt - Mateus
Mc - Marcos
Lc - Lucas
Jo - João

At - Atos

Rm - Romanos
1Cor - 1 Coríntios
2Cor - 2 Coríntios
Gl - Gálatas
Ef - Efésios
Fl - Filipenses
Cl - Colossenses
1Ts - 1 Tessalonicenses
2Ts - 2 Tessalonicenses
1Tm - 1 Timóteo
2Tm - 2 Timóteo
Tt - Tito
Fm - Filemon

Hb - Hebreus
Tg - Tiago
1Pd - 1 Pedro
2Pd - 2 Pedro
1Jo - 1 João
2Jo - 2 João
3Jo - 3 João
Jd - Judas

Ap - Apocalipse'''.split('\n')

dicionario = {'Livros': []}

lista = []

for x in Variavel:
    if x == '' or x == ' ':
        continue
    y, z = tuple(x.split('-'))


    dicionario['Livros'].append(
        {
            z: y
         }
         )
        



with open('file.json', 'w') as file:
    json.dump(dicionario, file, indent=4)


print(dicionario)
'''
print(lista)

arg1 = None

for x, y in enumerate(lista):

    if x % 2 == 0 and not x == 0:
        dicionario[arg1] = y
    
    elif not x == 0:
        arg1 = y

    else:
        arg1 = y

# print(dicionario)'''