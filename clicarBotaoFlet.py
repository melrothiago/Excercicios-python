import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo Clicar no Botão"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinha horizontalmente também

    def button_clicked(e):
        label.value = "Olá, você clicou no botão!"
        page.update()

    # Criação dos elementos
    label = ft.Text(value="Clique no botão abaixo.", text_align=ft.TextAlign.CENTER)
    botao = ft.ElevatedButton(text="Clique aqui", on_click=button_clicked)

    # Adicionando elementos ao layout principal (Column para centralizar tudo)
    page.add(
        ft.Column(
            [
                label,
                botao
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os elementos na vertical
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza na horizontal
        )
    )

ft.app(target=main)
