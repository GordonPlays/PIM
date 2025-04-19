import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

# Janela principal
app = customtkinter.CTk()
app.geometry("600x500")
app.title('Login - UNIPA')

# Carregar imagem de fundo (se quiser usar um pattern ou cor sólida, pode trocar aqui)
img1 = ImageTk.PhotoImage(Image.open("./imagens/pattern.png"))
fundo = customtkinter.CTkLabel(master=app, image=img1)
fundo.pack(fill="both", expand=True)

# Frame central
frame = customtkinter.CTkFrame(master=fundo, width=340, height=380, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Logo e título
titulo = customtkinter.CTkLabel(master=frame, text="UNIPA", font=('Century Gothic', 32, 'bold'))
titulo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

subtitulo = customtkinter.CTkLabel(master=frame, text="Plataforma de Ensino", font=('Century Gothic', 16))
subtitulo.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

# Entradas de login
entry_user = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Usuário')
entry_user.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

entry_pass = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha', show='*')
entry_pass.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

# Esqueci senha
recuperar = customtkinter.CTkLabel(master=frame, text="Esqueceu a senha?", font=('Century Gothic', 12))
recuperar.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

# Botão de login
def login():
    app.destroy()
    w = customtkinter.CTk()
    w.geometry("1280x720")
    w.title('Bem-vindo(a)')
    l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    w.mainloop()

btn_login = customtkinter.CTkButton(master=frame, width=220, text="Entrar", command=login, corner_radius=8)
btn_login.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

app.mainloop()