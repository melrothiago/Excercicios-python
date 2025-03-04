import flet as ft
import random

def main(page: ft.Page):
    page.title = "Jogo Estilo Candy Crush"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    grid_size = 8
    tabuleiro = []
    pontos = 0

    # Lista de imagens para as peças
    pecas_imagens = [
        "circle.png",    # Substitua pelo caminho correto das suas imagens
        "square.png",
        "triangle.png"
    ]

    # Função para criar uma peça com uma imagem
    def criar_peca(imagem_src, posicao, selecionada=False):
        border_color = ft.Colors.PURPLE if selecionada else None
        return ft.Container(
            content=ft.Image(
                src=imagem_src,
                width=40,
                height=40,
                fit=ft.ImageFit.CONTAIN
            ),
            width=40,
            height=40,
            border=ft.border.all(4, border_color) if border_color else None,
            on_click=lambda e: mover_peca(posicao)
        )

    # Função para criar uma peça aleatória
    def criar_peca_aleatoria(posicao):
        imagem_src = random.choice(pecas_imagens)
        return criar_peca(imagem_src, posicao)

    # Função para verificar combinações
    def verificar_combinacoes():
        combinacoes_encontradas = False
        # Verifica combinações em linhas
        for i in range(grid_size):
            for j in range(grid_size - 2):
                if (tabuleiro[i].controls[j].content.src == tabuleiro[i].controls[j+1].content.src == tabuleiro[i].controls[j+2].content.src):
                    remover_combinacao_linha(i, j, j+1, j+2)
                    combinacoes_encontradas = True
        # Verifica combinações em colunas
        for j in range(grid_size):
            for i in range(grid_size - 2):
                if (tabuleiro[i].controls[j].content.src == tabuleiro[i+1].controls[j].content.src == tabuleiro[i+2].controls[j].content.src):
                    remover_combinacao_coluna(i, j, i+1, i+2)
                    combinacoes_encontradas = True
        return combinacoes_encontradas

    # Função para remover a combinação em linha e atualizar o tabuleiro
    def remover_combinacao_linha(linha, col1, col2, col3):
        nonlocal pontos

        # Incrementa o contador de pontos
        pontos += 1
        contador_pontos.value = f"Pontos: {pontos}"
        page.update()

        # Remover peças
        tabuleiro[linha].controls[col1].content.src = None
        tabuleiro[linha].controls[col2].content.src = None
        tabuleiro[linha].controls[col3].content.src = None

        # Fazer as peças descerem
        for i in range(linha, 0, -1):
            tabuleiro[i].controls[col1].content.src = tabuleiro[i-1].controls[col1].content.src
            tabuleiro[i].controls[col2].content.src = tabuleiro[i-1].controls[col2].content.src
            tabuleiro[i].controls[col3].content.src = tabuleiro[i-1].controls[col3].content.src

        # Gerar novas peças no topo
        tabuleiro[0].controls[col1] = criar_peca_aleatoria((0, col1))
        tabuleiro[0].controls[col2] = criar_peca_aleatoria((0, col2))
        tabuleiro[0].controls[col3] = criar_peca_aleatoria((0, col3))

        page.update()

    # Função para remover a combinação em coluna e atualizar o tabuleiro
    def remover_combinacao_coluna(linha1, col, linha2, linha3):
        nonlocal pontos

        # Incrementa o contador de pontos
        pontos += 1
        contador_pontos.value = f"Pontos: {pontos}"
        page.update()

        # Remover peças
        tabuleiro[linha1].controls[col].content.src = None
        tabuleiro[linha2].controls[col].content.src = None
        tabuleiro[linha3].controls[col].content.src = None

        # Fazer as peças descerem
        for i in range(linha3, 2, -1):
            tabuleiro[i].controls[col].content.src = tabuleiro[i-3].controls[col].content.src

        # Gerar novas peças no topo
        for i in range(3):
            tabuleiro[i].controls[col] = criar_peca_aleatoria((i, col))

        page.update()

    # Função para mover a peça
    def mover_peca(posicao):
        nonlocal tabuleiro
        if not hasattr(mover_peca, "peca_selecionada"):
            mover_peca.peca_selecionada = None

        linha, coluna = posicao

        if mover_peca.peca_selecionada is None:
            mover_peca.peca_selecionada = posicao
            tabuleiro[linha].controls[coluna] = criar_peca(tabuleiro[linha].controls[coluna].content.src, posicao, True)
        else:
            linha1, coluna1 = mover_peca.peca_selecionada
            linha2, coluna2 = posicao

            # Verifica se a peça clicada está adjacente à peça selecionada
            if (abs(linha1 - linha2) == 1 and coluna1 == coluna2) or (abs(coluna1 - coluna2) == 1 and linha1 == linha2):
                # Troca de posições
                tabuleiro[linha1].controls[coluna1], tabuleiro[linha2].controls[coluna2] = tabuleiro[linha2].controls[coluna2], tabuleiro[linha1].controls[coluna1]

                # Atualiza a página
                page.update()
                
                # Verificar e remover combinações
                while verificar_combinacoes():
                    page.update()
            
            # Remove o contorno da peça selecionada
            tabuleiro[linha1].controls[coluna1] = criar_peca(tabuleiro[linha1].controls[coluna1].content.src, (linha1, coluna1))
            mover_peca.peca_selecionada = None

    # Contador de pontos
    contador_pontos = ft.Text(value=f"Pontos: {pontos}", size=18)

    for i in range(grid_size):
        linha = []
        for j in range(grid_size):
            # Seleciona uma imagem aleatória para a peça
            linha.append(criar_peca_aleatoria((i, j)))
        tabuleiro.append(ft.Row(linha, alignment=ft.MainAxisAlignment.CENTER))

    # Layout principal com contador de pontos e tabuleiro
    layout_principal = ft.Row(
        [
            ft.Container(content=contador_pontos, width=100, padding=10),
            ft.Column(tabuleiro, alignment=ft.MainAxisAlignment.CENTER)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Adiciona o layout principal à página
    page.add(layout_principal)

ft.app(target=main)
