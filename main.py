from tkinter import *
import tkinter.font as font
import tkinter.messagebox

from objetos.Usuario import *
from login_functions import *

user = Usuario("", "")

# def login(username, password):

def sair():
    exit(0)


def tela_disciplinas(menu, logado):
    if logado:
        disciplinas_Font = font.Font(family='Constantia', size=5, weight='bold')
        menu.destroy()
        tela_disc = Tk()
        disciplinas_Font = font.Font(family='Constantia', size=15, weight='bold')
        tela_disc.title("Escolher disciplinas")
        tela_disc.geometry("1000x800+10+10")
        img = PhotoImage(file="Escolhadisciplina (3).png")
        limg = Label(tela_disc, i=img)
        limg.pack()

        Button(tela_disc, text="Conhecimentos Gerais", font=disciplinas_Font, bg="#86b8b1", borderwidth=10,
               command=lambda: questoes(tela_disc)).place(relx=0.3, rely=0.4,
                                                          anchor=CENTER,
                                                          relheight=0.1,
                                                          relwidth=0.3)
        Button(tela_disc, text="Ciências", font=disciplinas_Font, bg="#86b8b1", borderwidth=10).place(relx=0.75,
                                                                                                      rely=0.4,
                                                                                                      anchor=CENTER,
                                                                                                      relheight=0.1,
                                                                                                      relwidth=0.3)
        Button(tela_disc, text="História", font=disciplinas_Font, bg="#86b8b1", borderwidth=10).place(relx=0.53,
                                                                                                      rely=0.6,
                                                                                                      anchor=CENTER,
                                                                                                      relheight=0.1,
                                                                                                      relwidth=0.3)
        tela_disc.mainloop()
    else:
        tkinter.messagebox.showerror("error", "Não autenticado.")






def questoes(w2):
    w2.destroy()
    tela_questoes = Tk()
    var = IntVar() # Variavel controle RadioButton
    tela_questoes.title("Perguntas")
    tela_questoes.geometry("1000x800+10+10")
    img = PhotoImage(file="fundo.png")
    limg = Label(tela_questoes, i=img)
    limg.pack()
    radioFont = font.Font(family='Archivo black', size=15, weight='bold')
    labelFont = font.Font(family='Arial Black', size=15, weight='bold')
    R1 = Radiobutton(tela_questoes, text="2000", variable=var, value=1, font=radioFont)
    R1.place(relx=0.27, rely=0.33)

    R2 = Radiobutton(tela_questoes, text="2001", variable=var, value=2,
                     font=radioFont)
    R2.place(relx=0.27, rely=0.37)

    R3 = Radiobutton(tela_questoes, text="2002", variable=var, value=3,
                     font=radioFont)
    R3.place(relx=0.27, rely=0.41)

    R4 = Radiobutton(tela_questoes, text="2003", variable=var, value=4,
                     font=radioFont)
    R4.place(relx=0.27, rely=0.45)

    label = Label(tela_questoes, text='Em que ano derrubaram as Torres Gêmeas (World Trade Center)?', font=labelFont)
    label.place(relx=0.5, rely=0.3, anchor='s')


def tela_principal(logado):
       menu = Tk()
       menu.title('Projeto Quiz')
       menu.geometry("1000x800+10+10")

       img = PhotoImage(file="Perguntas_Respostas (1).png")
       limg = Label(menu, i=img)
       limg.pack()
       buttonFont = font.Font(family='Impact', size=20, weight='bold')

       Button(menu, text="Entrar", font=buttonFont, command=lambda: tela_disciplinas(menu, logado), bg="#b2d5ba",
              borderwidth=10).place(relx=0.5,
                                    rely=0.4,
                                    anchor=CENTER,
                                    relheight=0.1,
                                    relwidth=0.3)
       Button(menu, text="Sair", command=sair, font=buttonFont, bg="#b2d5ba", borderwidth=10).place(relx=0.5, rely=0.6,
                                                                                                    anchor=CENTER,
                                                                                                    relheight=0.1,
                                                                                                    relwidth=0.3)
       Button(menu, text="Cadastro / Login", command=lambda: login(menu), bg="#b2d5ba", borderwidth=7).place(relx=0.9,
                                                                                                             rely=0.9,
                                                                                                             anchor=CENTER,
                                                                                                             height=50,
                                                                                                             width=100)
       menu.mainloop()


def efetuar_login(usuario, senha, window_login):
    print("Usuario: " + usuario)
    print("Senha: " + senha)
    user_obj = Usuario(usuario, senha)
    if usuario_existe(user_obj):
        if verificar_senha(user_obj):
            tkinter.messagebox.showinfo("info", "Bem vinde, " + user_obj.usuario)
            window_login.destroy()
            tela_principal(True)
        else:
            tkinter.messagebox.showerror("info", "Senha incorreta.")
    else:
        criar_usuario(user_obj)
        tkinter.messagebox.showinfo("info", "Bem vinde, " + user_obj.usuario)
        window_login.destroy()
        logado = True
        tela_principal(True)


def login(menu):
    loginFont = font.Font(family='Constantia', size=5, weight='bold')
    menu.destroy()

    tela_login = Tk()
    tela_login.title("Login / Cadastro")
    tela_login.geometry("500x500")

    label_usuario = Label(tela_login, text='Usuário:', font=loginFont)
    label_usuario.place(relx=0.5, rely=0.4, anchor='s')

    campo_usuario = StringVar(None)
    usrIn = Entry(tela_login, textvariable=campo_usuario, width=50)
    usrIn.place(relx=0.5, rely=0.4, anchor='n')

    label_senha = Label(tela_login, text='Senha:', font=loginFont)
    label_senha.place(relx=0.5, rely=0.55, anchor='s')

    campo_senha = StringVar(None)
    senhaIn2 = Entry(tela_login, textvariable=campo_senha, width=50)
    senhaIn2.place(relx=0.5, rely=0.55, anchor='n')

    Button(tela_login, text="Entrar", font=loginFont, bg="#86b8b1", borderwidth=2,
           command=lambda: efetuar_login(campo_usuario.get(), campo_senha.get(), tela_login)).place(relx=0.5, rely=0.65,
                                                                            anchor=CENTER,
                                                                            relheight=0.04,
                                                                            relwidth=0.15)


tela_principal(False)
