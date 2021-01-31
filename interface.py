from tkinter import *

app = Tk()
app.title('IQ Michels BOT')
app.geometry('290x200')
app.configure(background='#008080')

# anchor +> N Norte S south W Oeste E leste
Label(app, text='Login:',background='#dde',foreground='#000', anchor=W).place(x=10,y=10,width=50,height=20)

email=Entry(app)
email.place(x=60,y=10,width=200,height=20)

Label(app, text='Senha:',background='#dde',foreground='#000', anchor=W).place(x=10,y=40,width=50,height=20)

senha=Entry(app)
senha.place(x=60,y=40,width=200,height=20)


app.mainloop()
