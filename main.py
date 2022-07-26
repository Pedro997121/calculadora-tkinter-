from tkinter import *
from tkinter import ttk
import math


#Janelas

window = Tk()
window.title("Calculadora")
window.geometry("330x420")

window_frame = Frame(window, width=330, height=70,)
window_frame.grid(row=0, column=0)

window_frame2 = Frame(window, width=330, height=420, bg="white")
window_frame2.grid(row=1, column=0)

#label

input = StringVar()
label = Label(window_frame, textvariable=input, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Helvetica 26'), bg="white")
label.place(x=0, y=0)

#Funções

valores = ''
resultado = ''


def input_valor(valor):
    global valores
    valores += valor
    if input != "":
        input.set(valores)
    else:
        input.set(resultado)
    
    
def calcular():
    global valores
    resultado = eval(valores)
    valores = resultado
    input.set(resultado)
    
    
          
def calcular_raiz(valor):
    global valores
    global resultado
    valor = int(valor)
    valor = math.sqrt(valor)
    resultado = str(valor)
    valores = resultado
    input.set(resultado)
    
           
def apagar():
    global valores
    valores = ''
    input.set('')
    
    
    
#Botões

b0 = Button(window_frame2, text="0", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('0'), foreground="white", relief=RAISED, overrelief=RIDGE)
b0.place(x=85, y=280)

b1 = Button(window_frame2, text="1", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('1'), foreground="white", relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=210)

b2 = Button(window_frame2, text="2", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('2'), foreground="white", relief=RAISED, overrelief=RIDGE)
b2.place(x=85, y=210)

b3 = Button(window_frame2, text="3", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('3'), foreground="white", relief=RAISED, overrelief=RIDGE)
b3.place(x=170, y=210)

b4 = Button(window_frame2, text="4", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('4'), foreground="white", relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=140)

b5 = Button(window_frame2, text="5", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('5'), foreground="white", relief=RAISED, overrelief=RIDGE)
b5.place(x=85, y=140)

b6 = Button(window_frame2, text="6", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('6'), foreground="white", relief=RAISED, overrelief=RIDGE)
b6.place(x=170, y=140)

b7 = Button(window_frame2, text="7", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('7'), foreground="white", relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=70)

b8 = Button(window_frame2, text="8", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('8'), foreground="white", relief=RAISED, overrelief=RIDGE)
b8.place(x=85, y=70)

b9 = Button(window_frame2, text="9", width=8, height=3, bg="black",  font=("Helvetica"),command=lambda: input_valor('9'), foreground="white", relief=RAISED, overrelief=RIDGE)
b9.place(x=170, y=70)

bx = Button(window_frame2, text="*", width=8, height=3, font=("Helvetica"),command=lambda: input_valor('*'), foreground="white", relief=RAISED, overrelief=RIDGE, bg="grey")
bx.place(x=255, y=70)

bmais = Button(window_frame2, text="+", width=8, height=3, font=("Helvetica"),command=lambda: input_valor('+'), foreground="white", relief=RAISED, overrelief=RIDGE, bg="grey")
bmais.place(x=255, y=140)

bmenos = Button(window_frame2, text="-", width=8, height=3, font=("Helvetica"),command=lambda: input_valor('-'), foreground="white", relief=RAISED, overrelief=RIDGE, bg="grey")
bmenos.place(x=255, y=210)

bigual = Button(window_frame2, text="=", width=8, height=3, font=("Helvetica"),command=calcular, foreground="white", relief=RAISED, overrelief=RIDGE, bg="green")
bigual.place(x=255, y=280)

bporcentagem = Button(window_frame2, text="%", width=8, height=3,font=("Helvetica"),command=lambda: input_valor('%'), foreground="white", relief=RAISED, overrelief=RIDGE, bg="grey")
bporcentagem.place(x=255, y=0)

bapagar = Button(window_frame2, text="C", width=27, height=3, bg="black", font=("Helvetica"),command=apagar, foreground="white", relief=RAISED, overrelief=RIDGE)
bapagar.place(x=0, y=0)

bvirgula = Button(window_frame2, text=",", width=8, height=3, bg="grey", font=("Helvetica"),command=lambda: input_valor('%'), foreground="white", relief=RAISED, overrelief=RIDGE, )
bvirgula.place(x=170, y=280)

braiz = Button(window_frame2, text="√", width=8, height=3,font=("Helvetica"),command=lambda: calcular_raiz(valores), foreground="white", relief=RAISED, overrelief=RIDGE, bg="grey")
braiz.place(x=0, y=280)


window.mainloop()
