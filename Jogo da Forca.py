# Importações
# ----------------------------------
import os
import customtkinter as ctk
import random as rnd
from PIL import Image
os.system('cls')
# ----------------------------------
#Banco de Dados
categorias = {
'frutas': ['abacaxi', 'morango', 'melancia', 'banana', 'uva', 'manga', 'abacate', 'pera', 'melão','mamao','amora','framboesa','laranja','limao','maracuja','tangerina','caju','jaca'],
'animais': ['cavalo', 'rinoceronte', 'elefante', 'girafa', 'leao', 'tigre', 'gato', 'cachorro','aguia','leao','leopardo','hiena','baleia','orca','golfinho','tubarao'],
'paises': ['brasil', 'argentina', 'chile', 'colombia', 'uruguai','jamaica','venezuela','paraguai','china','india','egito','ira','china','japao','alemanha','uruguai','canada','coreia do sul','coreia do norte','australia','espanha','portugal'],
'jogos': ['minecraft', 'fortnite', 'roblox', 'among us', 'fifa','tetris','zelda','mario','pokemon','sonic','pacman','gta','call of duty'],
'objetos': ['apontador', 'caneta', 'livro', 'cadeira', 'mesa','escada','mesa','espelho','controle','caneta','celular','caderno','lapis','borracha','caderno','livro','mochila','umidificador','microondas','geladeira','fogão','microondas','forno','geladeira']}
#-----------------------------------
#Funções
def skip_jogo():
    print("jogo da forca")
def newjane():
    janela.destroy()
def chut_tj():
    print("jogo da forca")
def verifi_let():
    print("jogo da forca")
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
	weight="bold", slant="italic", underline=True, overstrike=False)
Texto = ctk.CTkLabel(janela, text="Jogo da Forca", fg_color="transparent", 
                     font=font_title, text_color='#444444')
Texto.place(x = 390, y = 70)
logo = ctk.CTkImage(Image.open('Image\Logo.png'), size=(250, 250))
logo = ctk.CTkLabel(janela, image=logo, text="")
logo.place(x = 435, y = 150)
Iniciar = ctk.CTkButton(janela, text='Jogar', command=newjane,
                        width=250, height=50, border_width=3.5,
                        corner_radius=60)
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
skip = ctk.CTkImage(Image.open('Image\skip1.png'), size=(70, 70))
Pular = ctk.CTkButton(janela_jogo, image=skip, corner_radius=20, text=""
                      ,command=skip_jogo, fg_color="transparent",
                      hover_color='#ffffff', width=0,height=0)
Pular.place(x=825, y=150)
Parte_um = ctk.CTkImage(Image.open('Image\Parte 1.jpg'), size=(250, 250))
Parte_um = ctk.CTkLabel(janela_jogo, image=Parte_um, text="")
Parte_um.place(x=350, y=100)
letra = ctk.CTkEntry(janela_jogo, width=40, height=40)
letra.place(x=347.5, y=430)
palavra = ctk.CTkEntry(janela_jogo, width=130, height=40)
palavra.place(x=415, y=430)
chutar = ctk.CTkButton(janela_jogo, text='Chutar', command=chut_tj,
                        width=130, height=45, border_width=3.5,
                        corner_radius=60)
chutar.place(x = 415, y = 473)
certinho = ctk.CTkImage(Image.open('Image\Certin.png'), size=(20, 20))
jogar_letra = ctk.CTkButton(janela_jogo, image=certinho, corner_radius=20, text=""
                      ,command=verifi_let, fg_color="#3282F6",
                      hover_color='#3282F6', width=40,height=45,
                      border_width=3.5)
jogar_letra.place(x=335, y=473)
anotações = ctk.CTkLabel(janela_jogo, text="Anotações:", fg_color="transparent")
anotações.place(x=775,y=310)
ano_tebox = ctk.CTkTextbox(janela_jogo, width=205, height=280, fg_color='#D4D4D4')
ano_tebox.place(x=780, y=350)
teste1 = ctk.CTkEntry(janela_jogo, width=300, height=55, placeholder_text="Espaço para dica, e comunicação")
teste1.place(x=330, y=20)
teste2 = ctk.CTkEntry(janela_jogo, width=325, height=55, placeholder_text="Espaço para a Palavra")
teste2.place(x=330, y=360)
janela_jogo.mainloop()
#----------------------------------