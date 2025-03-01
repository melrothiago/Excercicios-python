from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    
    def build(self):
        self.title = "Salute!"

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label_instrucao = Label(text="Qual o seu nome?", font_size='20sp')
        self.layout.add_widget(self.label_instrucao)

        self.textinput = TextInput(hint_text="Digite seu nome aqui", font_size='18sp', multiline=False)
        self.layout.add_widget(self.textinput)

        self.botao = Button(text="Confirmar", font_size='18sp')
        self.botao.bind(on_press=self.exibir_saudacao)
        self.layout.add_widget(self.botao)

        self.label_resultado = Label(text="", font_size='20sp')
        self.layout.add_widget(self.label_resultado)

        return self.layout

    def exibir_saudacao(self, instance):
        
        nome = self.textinput.text
        if nome.strip():  
            self.label_resultado.text = f"Olá, {nome}!"
        else:
            self.label_resultado.text = "Por favor, insira seu nome."

if __name__ == "__main__":
    MyApp().run()
