from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

# Definindo o tamanho fixo da janela
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

class MyApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label_resultado = Label(text="Resultado: ", font_size='24sp', size_hint=(1, 0.2))
        self.layout.add_widget(self.label_resultado)

        # Layout para os botões numéricos e de operações
        self.buttons_layout = GridLayout(cols=4, size_hint=(1, 0.8), spacing=0)

        # Adicionando botões numéricos e de operações na última coluna
        botoes = [
            ('7', self.adicionar_numero), ('8', self.adicionar_numero), ('9', self.adicionar_numero), ('+', self.definir_operacao),
            ('4', self.adicionar_numero), ('5', self.adicionar_numero), ('6', self.adicionar_numero), ('-', self.definir_operacao),
            ('1', self.adicionar_numero), ('2', self.adicionar_numero), ('3', self.adicionar_numero), ('*', self.definir_operacao),
            ('C', self.limpar), ('0', self.adicionar_numero), ('=', self.calcular), ('/', self.definir_operacao)
        ]

        for (texto, acao) in botoes:
            self.buttons_layout.add_widget(Button(text=texto, on_press=acao, font_size='20sp', size_hint=(1, 1)))

        self.layout.add_widget(self.buttons_layout)

        self.input = ""
        self.operador = ""
        self.num1 = ""
        self.num2 = ""

        return self.layout

    def adicionar_numero(self, instance):
        self.input += instance.text
        self.label_resultado.text = self.input

    def limpar(self, instance):
        self.input = ""
        self.operador = ""
        self.num1 = ""
        self.num2 = ""
        self.label_resultado.text = "Resultado: "

    def definir_operacao(self, instance):
        if self.input:
            self.num1 = self.input
            self.operador = instance.text
            self.input = ""
            self.label_resultado.text = self.operador

    def calcular(self, instance):
        try:
            if self.operador and self.input:
                self.num2 = self.input
                num1 = float(self.num1)
                num2 = float(self.num2)
                resultado = self.realizar_operacao(num1, num2, self.operador)
                self.label_resultado.text = f"Resultado: {resultado}"
                self.input = ""
                self.operador = ""
                self.num1 = ""
                self.num2 = ""
        except ValueError:
            self.label_resultado.text = "Erro: Entrada inválida."

    def realizar_operacao(self, num1, num2, operador):
        if operador == "+":
            return num1 + num2
        elif operador == "-":
            return num1 - num2
        elif operador == "*":
            return num1 * num2
        elif operador == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erro: Não é possível dividir por zero."
        else:
            return "Erro: Operação inválida."

if __name__ == "__main__":
    MyApp().run()
