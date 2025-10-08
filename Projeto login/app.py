import customtkinter as ctk
import requests
#configuração de aparecia
ctk.set_appearance_mode('dark-blue')
#Criação das funções de funcionaçidades
def validar_login ():
    dados_de_login = {}
    dados_de_login["username"] = campo_usuario.get()
    dados_de_login["password"] = campo_senha.get()
    
    url = "https://dummyjson.com/auth/login"
    #Comunica com a api se os dados são iguais
    response = requests.post(url, json = dados_de_login)
    #Informa se o usuario e senha estão corretos
    if response.status_code == 200:
        resultado_login.configure(text = "Login realizado com sucesso!",text_color  = "green")
    else:
        resultado_login.configure(text = "falha no login", text_color = "red")
    print(response)
#Aqui voce deve controlar em qual página está o usuário
pagina = 1
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
#Label
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
#Campopara cadastrar usuario 
#iniciar a aplicação
app.mainloop()