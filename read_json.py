import json


def read_json(arg):
    with open('file.json', encoding='utf-8') as file:
        json_file = json.load(file)

    for x in json_file['Livros']:
        try:
            for y, z in x.items():
                if y.strip() == arg:
                    return z.strip().lower()
        
        except KeyError:
            print('Não Encontrado')

if __name__ == '__main__':
    variavel = 'Gênesis'
    read_json(variavel)