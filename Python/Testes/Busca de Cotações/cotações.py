import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotações['text'] = texto

janela = Tk()
janela.title('Cotação das moedas')
janela.geometry("340x200")

texto_orientação = Label(janela, text='Clique no botão abaixo para ver as cotações das moedas!')
texto_orientação.grid(column=0, row=0, padx=10, pady=10)

texto_orientação2 = Label(janela, text='Clique agora')
texto_orientação2.grid(column=0, row=1)

botao = Button(janela, text='Buscar cotações', command=pegar_cotacoes)
botao.grid(column=0, row=2)

texto_cotações = Label(janela, text="")
texto_cotações.grid(column=0, row=3)

janela.mainloop()
