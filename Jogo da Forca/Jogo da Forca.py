# Importações
# ----------------------------------
import os
import customtkinter as ctk
import random as rnd
import time
from PIL import Image
os.system('cls')
# ----------------------------------
#Banco de Dados
letras_erradas = []
letras_acertadas = []
letras_usadas = []
categorias = {
'frutas': ['abacaxi', 'morango', 'melancia', 'banana', 'uva', 'manga', 'abacate', 'pera', 'melão','mamao','amora','framboesa','laranja','limao','maracuja','tangerina','caju','jaca'],
'animais': ['cavalo', 'rinoceronte', 'elefante', 'girafa', 'leao', 'tigre', 'gato', 'cachorro','aguia','leopardo','hiena','baleia','orca','golfinho','tubarao'],
'paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuela','paraguai','china','india','egito','ira','china','japao','alemanha','uruguai','canada','coreia do sul','coreia do norte','australia','espanha','portugal'],
'jogos': ['minecraft', 'fortnite', 'roblox', 'among us', 'fifa','tetris','zelda','mario','pokemon','sonic','pacman','gta','call of duty'],
'objetos': ['apontador', 'caneta', 'livro', 'cadeira', 'mesa','escada','mesa','espelho','controle','caneta','celular','caderno','lapis','borracha','caderno','livro','mochila','umidificador','microondas','geladeira','fogão','microondas','forno','geladeira']}
categoria = rnd.choice(list(categorias.keys()))
palavra = rnd.choice(categorias[categoria])
#-----------------------------------
#Funções
def newjane():
    janela.destroy()
def validar_entrada(event):
    valor = letra.get()
    if len(valor) >= 1:
        letra.delete(0)
def jogo (x, palavra):
    palavra_escondida = ''.join(['_ ' if char != ' ' else ' ' for char in palavra])
    re_ima = ctk.CTkImage(Image.open('Image\Parte 1.jpg'), size=(250, 250))
    re_ima = ctk.CTkLabel(janela_jogo, image=re_ima, text="")
    re_ima.place(x=350, y=100)
    font_dica = ctk.CTkFont(family="Arial Black", size=38, 
	weight="bold",underline=False, overstrike=False)
    dicas = ctk.CTkLabel(janela_jogo, text="Dica: "+ x or categoria , fg_color="transparent",
                         font=font_dica)
    dicas.place(x=330, y=20)
    font_pale_escon = ctk.CTkFont(family="Arial Black", size=38,
    weight="bold",underline=False, overstrike=False)
    pala_rel = ctk.CTkLabel(janela_jogo, text=palavra_escondida , fg_color="transparent",
                         font=font_pale_escon)
    pala_rel.place(x=330, y=360)
    def tra_ima (erros):
        if erros == 1:
            img1 = ctk.CTkImage(Image.open('Image\Parte 1.jpg'), size=(250, 250))
            re_ima.configure(image=img1)
        elif erros == 2:
            img2 = ctk.CTkImage(Image.open('Image\Parte 2.jpg'), size=(250, 250))
            re_ima.configure(image=img2)
        elif erros == 3:
            img3 = ctk.CTkImage(Image.open('Image\Parte 3.jpg'), size=(250, 250))
            re_ima.configure(image=img3)
        elif erros == 4:
            img4 = ctk.CTkImage(Image.open('Image\Parte 4.jpg'), size=(250, 250))
            re_ima.configure(image=img4)
        elif erros == 5:
            img5 = ctk.CTkImage(Image.open('Image\Parte 5.jpg'), size=(250, 250))
            re_ima.configure(image=img5)
        elif erros == 6:
            img6 = ctk.CTkImage(Image.open('Image\Parte 6.jpg'), size=(250, 250))
            re_ima.configure(image=img6)
        elif erros == 7:
            img7 = ctk.CTkImage(Image.open('Image\Parte 7.jpg'), size=(250, 250))
            re_ima.configure(image=img7)
        elif erros == 8:
            img8 = ctk.CTkImage(Image.open('Image\Parte 8.jpg'), size=(250, 250))
            re_ima.configure(image=img8)
        elif erros == 9:
            img9 = ctk.CTkImage(Image.open('Image\Parte 9.jpg'), size=(250, 250))
            re_ima.configure(image=img9)
        elif erros == 10:
            img10 = ctk.CTkImage(Image.open('Image\Parte 10.jpg'), size=(250, 250))
            re_ima.configure(image=img10)
        elif erros == 11:
            img11 = ctk.CTkImage(Image.open('Image\Parte 11.jpg'), size=(250, 250))
            re_ima.configure(image=img11)
    def acertar():
        dicas.destroy()
        font_congra = ctk.CTkFont(family="Arial Black", size=38,
        weight="bold",underline=True, overstrike=False)
        cong = ctk.CTkLabel(janela_jogo, text="Você Acertou!" , fg_color="transparent",
                            font=font_congra, text_color='#6BE659')
        cong.place(x=330, y=20)
    def errar():
        dicas.destroy() 
        font_err = ctk.CTkFont(family="Arial Black", size=38,
        weight="bold",underline=True, overstrike=False)
        erro = ctk.CTkLabel(janela_jogo, text="Você Errou!" , fg_color="transparent",
                            font=font_err, text_color='#F03425')
        erro.place(x=330, y=20)
    skip = ctk.CTkImage(Image.open('Image\skip1.png'), size=(70, 70))
    Pular = ctk.CTkButton(janela_jogo, image=skip, corner_radius=20, text=""
                          ,command=lambda: skip_jogo(dicas, pala_rel,errar,acertar ), fg_color="transparent",
                          hover_color='#ffffff', width=0,height=0)
    Pular.place(x=825, y=150)
    chutar = ctk.CTkButton(janela_jogo, text='Chutar', command=lambda:chut_tj(palavra),
                        width=130, height=45, border_width=3.5,
                        corner_radius=60)
    chutar.place(x = 415, y = 473)
    def chut_tj(palavra):
        v_palavras = palavras.get().lower()
        v_pala_re_se_esp = v_palavras.replace(" ", "")
        if v_pala_re_se_esp == palavra:
            acertar()
            categorias[categoria].remove(palavra)
        else:
            errar()
            tra_ima(11)
    v_letra = ''
    print(v_letra)
    def verifi_let():
        v_letra = letra.get().lower()
        if v_letra in letras_usadas:
            return
        letras_usadas.append(v_letra)
        if v_letra in palavra:
            letras_acertadas.append(v_letra)
            nova_palavra = ''
            palavra.replace(' ','')
            for char in palavra:
                if char in letras_acertadas:
                    nova_palavra += char + ' '
                else:
                    nova_palavra += '_ '
            pala_rel.configure(text=nova_palavra)
            letra_usa.configure(text= letras_usadas)
            if '_' not in nova_palavra:
                acertar()
                categorias[categoria].remove(palavra)
        else:
            letras_erradas.append(v_letra)
            letra_usa.configure(text= letras_usadas)
            erros = len(letras_erradas)
            tra_ima(erros + 1)
            if erros == 10:
                errar()
    certinho = ctk.CTkImage(Image.open('Image\Certin.png'), size=(20, 20))
    jogar_letra = ctk.CTkButton(janela_jogo, image=certinho, corner_radius=20, text=""
                    ,command=verifi_let, fg_color="#3282F6",
                    hover_color='#3282F6', width=40,height=45,
                    border_width=3.5)
    jogar_letra.place(x=335, y=473)
def skip_jogo(dicas, pala_rel):
    dicas.destroy()
    pala_rel.destroy()
    letras_acertadas.clear
    letras_erradas.clear
    letras_usadas.clear
    letra_usa.configure(text= letras_usadas)
    categoria = rnd.choice(list(categorias.keys()))
    palavra = rnd.choice(categorias[categoria])
    jogo(categoria, palavra)
# ----------------------------------
#Iniciar Janela Principal
# ----------------------------------
janela = ctk.CTk()
janela.title("Jogo da Forca")
janela._set_appearance_mode("light")
janela.geometry("1080x720")
janela.maxsize(width= 1080, height=720)
janela.resizable(width= False, height= False)
font_title = ctk.CTkFont(family="Arial Black", size=44, 
	weight="bold", underline=True, overstrike=False)
Texto = ctk.CTkLabel(janela, text="Jogo da Forca", fg_color="transparent", 
                     font=font_title)
Texto.place(x = 390, y = 70)
ima_log = Image.open('Image\Logo.png')
logo = ctk.CTkImage(ima_log, size=(250, 250))
logo = ctk.CTkLabel(janela, image=logo, text="")
logo.place(x = 435, y = 175)
Iniciar = ctk.CTkButton(janela, text='Jogar', command=newjane,
                        width=250, height=50, border_width=3.5,
                        corner_radius=60, )
Iniciar.place(x = 410, y = 450)
janela.mainloop()
#----------------------------------
#Janela do Jogo
#----------------------------------
janela_jogo = ctk.CTk()
janela_jogo.title("Jogo da Forca")
janela_jogo._set_appearance_mode("light")
janela_jogo.geometry("1080x720")
janela_jogo.maxsize(width= 1080, height=720)
janela_jogo.resizable(width= False, height= False)
letra = ctk.CTkEntry(janela_jogo, width=40, height=40)
letra.bind("<Key>", validar_entrada)
letra.place(x=347.5, y=430)
palavras = ctk.CTkEntry(janela_jogo, width=130, height=40)
palavras.place(x=415, y=430)
jogo(categoria, palavra)
font_anot = ctk.CTkFont(family="Roboto", size=21, 
	weight="bold", underline=False, overstrike=False)
anotações = ctk.CTkLabel(janela_jogo, text="Letras Usadas:", fg_color="transparent",
                         font=font_anot)
anotações.place(x=775,y=310)
font_le_us = ctk.CTkFont(family="Arial Black", size=36, 
	weight="bold",underline=False, overstrike=False)
letra_usa = ctk.CTkLabel(janela_jogo, text= letras_usadas, fg_color="transparent",
                         font= font_le_us, justify="left", wraplength=400)
letra_usa.place(x=710, y=350)
janela_jogo.mainloop()
#----------------------------------