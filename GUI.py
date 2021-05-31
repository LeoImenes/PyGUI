import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key=('nome'))],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key=('idade'))],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key=("Gmail")),sg.Checkbox('Outlook',key=("Outlook")),sg.Checkbox('Yahoo',key=("Yahoo")),],
            [sg.Text("Aceita cartão")],
            [sg.Radio('Sim','Cartoes',key='sim'),sg.Radio('Não','cartoes',key='nao')],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30,20))]
            ]
        #Janela
        self.janela = sg.Window("Dados do usuario").layout(layout)
        
       

    def Iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()
            nome=self.values['nome']
            idade=self.values['idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartaoS= self.values['sim']
            aceita_cartaoN= self.values['nao']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita Yahoo: {aceita_yahoo}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita cartão: {aceita_cartaoS}')
            print(f'Não aceita cartão: {aceita_cartaoN}')
            print('---'*17)
        

tela=TelaPython()
tela.Iniciar()        
    
            
            
            
    
    
        
    
