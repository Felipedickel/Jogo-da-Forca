# Importações
# ----------------------------------
import os
import backend as bk
import customtkinter as ctk
from PIL import Image
os.system('cls')
# ----------------------------------
#Iniciar Janela Principal
# ----------------------------------
janela = ctk.CTk()
janela.title("Jogo da Forca")
janela._set_appearance_mode("light")
janela.geometry("1050x650")
janela.maxsize(width= 1050, height=650)
janela.resizable(width= False, height= False)
y = "Jogo da Forca"
Texto = ctk.CTkLabel(janela, text=y, fg_color="transparent")
Texto.pack()
logo = ctk.CTkImage(Image.open('Image\Parte 1.png'), size=(170, 170))
image_label = ctk.CTkLabel(janela, image=logo, text="") 
image_label.pack(pady=50)
Iniciar = ctk.CTkButton(janela, text='Jogar')
Iniciar.pack()
janela.mainloop()
#----------------------------------