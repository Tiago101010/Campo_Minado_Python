import customtkinter as ctk

#configuração de aparecia
ctk.set_appearance_mode('dark')
#Criação das funções de funcionaçidades
def validar_login ():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
        
    #Verificar se o usuario é Tiago e a senha 123456
    if usuario == "Tiago" and senha == "123456":
        resultado_login.configure(text = "Login realizado com sucesso!",text_color  = "green")
    else:
        resultado_login.configure(text = "falha no login", text_color = "red")

#criação da janela principal
app = ctk.CTk()
app.title("Sistema de login")
app.geometry("640x480")
#Criação dos campos
#Label
campo_usuario = ctk.CTkLabel(app, text = "Usuário:")
campo_usuario.pack(pady = 10)
#Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text = "Digite seu nome de usuário")
campo_usuario.pack(pady = 10)
#label
campo_senha = ctk.CTkLabel(app, text = "Senha:")
campo_senha.pack()
#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text = "Digite sua senha",show = "*")
campo_senha.pack(pady = 10)
#Button
botao_login = ctk.CTkButton(app, text = "Login", command = validar_login)
botao_login.pack(pady = 10)
#Campo fedeback de login
resultado_login = ctk.CTkLabel(app, text= "")
resultado_login.pack(pady = 10)
#iniciar a aplicação
app.mainloop()