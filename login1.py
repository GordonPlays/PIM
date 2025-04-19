import tkinter as tk
from tkinter import messagebox

# Dados fictícios para simular um login (pode ser substituído por leitura de arquivo ou banco de dados)
usuarios = {
    "admin": "1234",
    "joao": "senha123"
}

# Função de login
def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        janela.destroy()
        abrir_tela_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Janela de login
janela = tk.Tk()
janela.title("Login - UNIPA")
janela.geometry("300x200")

label_titulo = tk.Label(janela, text="Login UNIPA", font=("Arial", 14))
label_titulo.pack(pady=10)

label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(janela)
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

btn_login = tk.Button(janela, text="Entrar", command=realizar_login)
btn_login.pack(pady=10)

# Função da próxima janela
def abrir_tela_principal():
    nova_janela = tk.Tk()
    nova_janela.title("Bem-vindo")
    nova_janela.geometry("400x200")
    label = tk.Label(nova_janela, text="Bem-vindo à plataforma UNIPA!", font=("Arial", 16))
    label.pack(expand=True)
    nova_janela.mainloop()

janela.mainloop()