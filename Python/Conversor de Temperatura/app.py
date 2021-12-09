from tkinter import *

# FUNCOES
def Conversao():
    global final
    G_Fahrenheit = float(caixa_text.get()) # pegando um valor da textbox e convertendo em float
    G_Celcius = (G_Fahrenheit - 32) * (5 / 9)
    final.set(str(round(G_Celcius,1)) + ' °C')
# GUI
tela = Tk()
tela.title('Conversor')
# OUTROS
final = StringVar()
# FRAMES
# WIDGETS
orientacao = Label(tela, text='Digite abaixo um falor em °F:')
caixa_text = Entry(tela)
resultados = Label(tela, textvariable=final)
botao_conv = Button(tela, text='Converta', command=Conversao)
# LAYOUTS
orientacao.grid()
caixa_text.grid()
resultados.grid()
botao_conv.grid()
# END GUI
tela.mainloop()
