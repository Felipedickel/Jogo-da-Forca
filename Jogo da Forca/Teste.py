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
    'frutas': ['abacaxi', 'morango', 'melancia', 'banana', 'uva', 'manga', 'abacate', 'pera', 'melão','mamão','amora','framboesa','laranja','limao','maracuja','tangerina','caju','jaca'],
    'animais': ['cavalo', 'rinoceronte', 'elefante', 'girafa', 'leao', 'tigre', 'gato', 'cachorro','águia','leão','leopardo','hiena','baleia','orca','golfinho','tubarão'],
    'paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuela','paraguai','china','india','egito','irã','china','japão','alemanha','uruguai','canada','coreia do sul','coreia do norte','australia','espanha','portugal'],
    'jogos': ['minecraft', 'fortnite', 'roblox', 'among us', 'fifa','tetris','zelda','mario','pokemon','sonic','pacman','gta','call of duty'],
    'objetos': ['apontador', 'caneta', 'livro', 'cadeira', 'mesa','escada','mesa','espelho','controle','caneta','celular','caderno','lapis','borracha','caderno','livro','mochila','umidificador','microondas','geladeira','fogão','microondas','forno','geladeira']
}

categoria = random.choice(list(categorias.keys()))
palavra = random.choice(categorias[categoria])
palavra_escondida = '_' * len(palavra)

print(f'Dica: {categoria.capitalize()}')
print(palavra_escondida)

letras_usadas = []
print('---------------------------------')
print('\n')
print('Digite uma letra ou "sair" para sair . OBS : caso queira uma letra com acento digite o acento junto . Ex.: á, ã.: ')
print('---------------------------------')
print('\n')
while True:
    letra = input('Digite uma letra:').lower()
    print('---------------------------------')
    print('\n')

    if letra == 'sair':
        print('Obrigado por jogar!','\n')
        print('---------------------------------')
        break

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.OBS :",'\n')
        print('---------------------------------')
        continue

    if letra in letras_usadas:
        print("Você já tentou essa letra. Tente outra.", '\n')
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
        print("Essa letra não está na palavra.",'\n')
        print('---------------------------------')
        print("A palavra continua sendo :", palavra_escondida,'\n')
        print('---------------------------------')
    print(f'Letras usadas: {", ".join(letras_usadas)}', '\n')
  