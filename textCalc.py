from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label_resultado = Label(text="Resultado: ")
        self.layout.add_widget(self.label_resultado)
        
        self.num1_input = TextInput(hint_text="Digite um número real")
        self.layout.add_widget(self.num1_input)
        
        self.num2_input = TextInput(hint_text="Digite outro número real")
        self.layout.add_widget(self.num2_input)

        self.operador_input = TextInput(hint_text="Digite a operação matemática desejada (+, -, *, /)")
        self.layout.add_widget(self.operador_input)
        
        self.button_calcular = Button(text="Calcular")
        self.button_calcular.bind(on_press=self.calcular)
        self.layout.add_widget(self.button_calcular)

        return self.layout
    
    def calcular(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            operador = self.operador_input.text

            resultado = self.realizar_operacao(num1, num2, operador)
            self.label_resultado.text = f"Resultado: {resultado}"
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
