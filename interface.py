from tkinter import *

def login():
    #Invocando Função
    login = Tk()
    #Definindo Nome Janela
    login.title('Yellow Trader BOT')
    #Definindo Dimensões tela
    login.geometry('300x200')
    #Definindo cor Background
    login.configure(background='#FFFF00')
    login.resizable(False, False)
    
    

    # anchor +> N Norte S south W Oeste E leste
    Label(login, text='Login',background='#dde',foreground='#000', anchor=W).place(x=10,y=10,width=100,height=20)

    email=Entry(login)
    email.place(x=70,y=10,width=200,height=20)

    Label(login, text='Senha',background='#dde',foreground='#000', anchor=W).place(x=10,y=40,width=100,height=20)

    senha=Entry(login)
    senha.place(x=70,y=40,width=200,height=20)

    autenticar = Button(login, text=('ENTRAR'))
    autenticar.pack()


    login.mainloop()

    return email, senha

login()