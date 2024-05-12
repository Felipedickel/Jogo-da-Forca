[11:51, 11/05/2024] Joaquim: import os
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
    'paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuel…
[12:49, 11/05/2024] Joaquim: Vlw
[22:50, 11/05/2024] Joaquim: import tkinter as tk
from tkinter import messagebox
import random
import pygame
from pygame.locals import *

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela do Pygame
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400

# Cores
WHITE = (255, 255, 255)

# Inicializar a janela do Pygame
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Boneco da Forca')

class JogoForca:
    def _init_(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.categoria = ""
        self.palavra = ""
        self.palavra_escondida = ""
        self.letras_usadas = []
        self.tentativas_restantes = 10
        self.erros = 0

        self.label_categoria = tk.Label(root, text="")
        self.label_categoria.pack()

        self.label_palavra = tk.Label(root, text="")
        self.label_palavra.pack()

        self.label_letras_usadas = tk.Label(root, text="")
        self.label_letras_usadas.pack()

        self.label_tentativas = tk.Label(root, text="")
        self.label_tentativas.pack()

        self.entry_letra = tk.Entry(root)
        self.entry_letra.pack()

        self.button_adivinhar = tk.Button(root, text="Adivinhar", command=self.verificar_palpite)
        self.button_adivinhar.pack()

        self.button_novo_jogo = tk.Button(root, text="Novo Jogo", command=self.novo_jogo)
        self.button_novo_jogo.pack()

        self.button_sair = tk.Button(root, text="Sair", command=root.quit)
        self.button_sair.pack()

        self.novo_jogo()

    def novo_jogo(self):
        self.categoria = random.choice(list(categorias.keys()))
        self.palavra = random.choice(categorias[self.categoria])
        self.palavra_escondida = "_" * len(self.palavra)
        self.letras_usadas = []
        self.tentativas_restantes = 10
        self.erros = 0

        self.label_categoria.config(text=f"Categoria: {self.categoria}")
        self.atualizar_interface()

    def verificar_palpite(self):
        palpite = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if len(palpite) != 1 or not palpite.isalpha():
            messagebox.showinfo("Erro", "Por favor, digite apenas uma letra.")
            return

        if palpite in self.letras_usadas:
            messagebox.showinfo("Erro", "Você já tentou essa letra. Tente outra.")
            return

        self.letras_usadas.append(palpite)

        if palpite in self.palavra:
            self.palavra_escondida = self.revela_letra(self.palavra, self.palavra_escondida, palpite)
            if "_" not in self.palavra_escondida:
                messagebox.showinfo("Parabéns", f"Você acertou a palavra: {self.palavra}")
                self.novo_jogo()
        else:
            self.tentativas_restantes -= 1
            self.erros += 1
            if self.erros == 10:
                messagebox.showinfo("Game Over", f"Você esgotou todas as tentativas. A palavra era: {self.palavra}")
                self.novo_jogo()
            else:
                self.exibir_boneco()

        self.atualizar_interface()

    def revela_letra(self, palavra, palavra_escondida, letra):
        nova_palavra = ""
        for i in range(len(palavra)):
            if palavra[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += palavra_escondida[i]
        return nova_palavra

    def atualizar_interface(self):
        self.label_palavra.config(text=self.palavra_escondida)
        self.label_letras_usadas.config(text=f"Letras usadas: {', '.join(self.letras_usadas)}")
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restantes}")

    def exibir_boneco(self):
        # Desenhar partes do boneco da forca conforme os erros
        partes_boneco = [
            pygame.image.load('base_da_forca.png'),
            pygame.image.load('forca.png'),
            pygame.image.load('cabeca.png'),
            pygame.image.load('olhos.png'),
            pygame.image.load('boca.png'),
            pygame.image.load('tronco.png'),
            pygame.image.load('braco_esquerdo.png'),
            pygame.image.load('braco_direito.png'),
            pygame.image.load('perna_esquerda.png'),
            pygame.image.load('perna_direita.png')
        ]

        # Exibir a parte correspondente do boneco
        if self.erros <= len(partes_boneco):
            window_surface.blit(partes_boneco[self.erros - 1], (0, 0))
            pygame.display.update()

# Dicionário com as categorias e palavras
categorias = {
    'Frutas': ['abacaxi', 'morango', 'melancia', 'banana', 'uva', 'manga', 'abacate', 'pera', 'melão','mamao','amora','framboesa','laranja','limao','maracuja','tangerina','caju','jaca'],
    'Animais': ['cavalo', 'rinoceronte', 'elefante', 'girafa', 'leao', 'tigre', 'gato', 'cachorro','aguia','leao','leopardo','hiena','baleia','orca','golfinho','tubarao'],
    'Paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuela','paraguai','china','india','egito','ira','china','japao','alemanha','uruguai','canada','coreia do sul','coreia do norte','australia','espanha','portugal'],
    'Jogos': ['minecraft', 'fortnite', 'roblox', 'among us', 'fifa','tetris','zelda','mario','pokemon','sonic','pacman','gta','call of duty'],
    'Objetos': ['apontador', 'caneta', 'livro', 'cadeira', 'mesa','escada','mesa','espelho','controle','caneta','celular','caderno','lapis','borracha','caderno','livro','mochila','umidificador','microondas','geladeira','fogão','microondas','forno','geladeira']
}

# Inicializar a janela principal
root = tk.Tk()
app = JogoForca(root)
root.mainloop()
