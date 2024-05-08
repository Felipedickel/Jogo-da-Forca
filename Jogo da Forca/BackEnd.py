import os
os.system('cls')

import random

def revela_letra(palavra, palavra_escondida, letra):
    nova_palavra = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra += letra
        else:
            nova_palavra += palavra_escondida[i]
    return nova_palavra

categorias = {
    'frutas': ['abacaxi', 'morango', 'melancia', 'banana', 'uva', 'manga', 'abacate', 'pera', 'melão','mamao','amora','framboesa','laranja','limao','maracuja','tangerina','caju','jaca'],
    'animais': ['cavalo', 'rinoceronte', 'elefante', 'girafa', 'leao', 'tigre', 'gato', 'cachorro','aguia','leao','leopardo','hiena','baleia','orca','golfinho','tubarao'],
    'paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuela','paraguai','china','india','egito','ira','china','japao','alemanha','uruguai','canada','coreia do sul','coreia do norte','australia','espanha','portugal'],
    'jogos': ['minecraft', 'fortnite', 'roblox', 'among us', 'fifa','tetris','zelda','mario','pokemon','sonic','pacman','gta','call of duty'],
    'objetos': ['apontador', 'caneta', 'livro', 'cadeira', 'mesa','escada','mesa','espelho','controle','caneta','celular','caderno','lapis','borracha','caderno','livro','mochila','umidificador','microondas','geladeira','fogão','microondas','forno','geladeira']
}

def jogar_forca():
    categoria = random.choice(list(categorias.keys()))
    palavra = random.choice(categorias[categoria])
    palavra_escondida = '_' * len(palavra)

    print(f'Dica: {categoria.capitalize()}')
    print(palavra_escondida)

    letras_usadas = []
    tentativas = 10

    print('---------------------------------')
    print('\n')
    print('Digite uma letra ou "sair" para sair. OBS: acentos foram retirados das palavras.')
    print('---------------------------------')
    print('\n')

    while tentativas > 0:
        letra = input('Digite uma letra:').lower()
        print('---------------------------------')
        print('\n')

        if letra == 'sair':
            print('Obrigado por jogar!\n')
            print('---------------------------------')
            break

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra. OBS:\n")
            print('---------------------------------')
            continue

        if letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra.\n")
            print('---------------------------------')
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            palavra_escondida = revela_letra(palavra, palavra_escondida, letra)
            print("A palavra agora é:", palavra_escondida,'\n')
            print('---------------------------------')
            if '_' not in palavra_escondida:
                print("Parabéns! Você acertou a palavra:", palavra,'\n')
                print('---------------------------------')
                break
        else:
            print("Essa letra não está na palavra.\n")
            print('---------------------------------')
            tentativas -= 1
            print(f"Agora você tem {tentativas} tentativas restantes.\n")
            print('---------------------------------')

        print(f'Letras usadas: {", ".join(letras_usadas)}\n')

    if tentativas == 0:
        print("Você esgotou todas as tentativas. A palavra era:", palavra,'\n')
        print('---------------------------------')

jogar_forca()
