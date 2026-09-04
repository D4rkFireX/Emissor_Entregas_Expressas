import os
#   PARA A INTERFACE
import tkinter as tk
#   PARA A GERAÇÃO DO PDF
from reportlab.pdfgen import canvas
#   PARA O TAMANHO DA FOLHA
from reportlab.lib.pagesizes import A4

def centralizar(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 3

    janela.geometry(f"{largura}x{altura}+{x}+{y}")
    
def limpar_campos(*campos):
    for campo in campos:
        campo.delete(0, tk.END)

def gerar_pdf(nome, endereco, cidade, uf, cep, cnpj):

    pdf = canvas.Canvas("destinatario.pdf", pagesize=A4)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(A4[0] / 2, 770, "Destinatário")

    #   NOME
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 750, "_" * 60)
    
    pdf.setFont("Helvetica", 18)
    pdf.drawString(100, 730, "Nome:")
    
    pdf.setFont("Helvetica", 18)
    pdf.drawString(152, 730, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 720, "_" * 60)
    
    #   ENDEREÇO
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 700, "_" * 40)
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 690, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 670, "_" * 40)
    
    #   CIDADE
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 650, "_" * 40)
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 640, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 620, "_" * 40)
    
    #   UF
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 600, "_" * 40)
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 590, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 570, "_" * 40)

    #   CEP
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 550, "_" * 40)
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 540, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 520, "_" * 40)

    #   CNPJ
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 500, "_" * 40)
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 490, nome)
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 470, "_" * 40)

    pdf.save()

    os.startfile("destinatario.pdf")

def interface():

    #   CRIAÇÃO DA JANELA
    janela = tk.Tk()

    #   CONFIGURAÇÕES GERAIS DA JANELA
    janela.title("Entregas RS")
    centralizar(janela, 600, 400)
    janela.resizable(False, False)

    #   TÍTULO DA APLICAÇÃO
    titulo = tk.Label(
        janela,
        text="Entregas RS Destinatário",
        font=("Arial", 16, "bold")
    )
    titulo.pack(pady=10)

    #   FRAME NOME
    frame_nome = tk.Frame(
        janela
    )
    frame_nome.pack(pady=10)

    nome_label = tk.Label(
        frame_nome,
        text="Nome: ",
        font=("Arial", 12)
    )
    nome_label.pack(side="left")

    nome_entrada = tk.Entry(
        frame_nome,
        width=40
    )
    nome_entrada.pack(side="right")

    #   FRAME ENDEREÇO
    frame_endereco = tk.Frame(
        janela
    )
    frame_endereco.pack(pady=10)

    endereco_label = tk.Label(
        frame_endereco,
        text="Endereço: ",
        font=("Arial", 12)
    )
    endereco_label.pack(side="left")

    endereco_entrada = tk.Entry(
        frame_endereco,
        width=40
    )
    endereco_entrada.pack(side="right")

    #   FRAME CIDADE
    frame_cidade_uf = tk.Frame(
        janela
    )
    frame_cidade_uf.pack(pady=10)

    cidade_label = tk.Label(
        frame_cidade_uf,
        text="Cidade: ",
        font=("Arial", 12)
    )
    cidade_label.pack(side="left")

    cidade_entrada = tk.Entry(
        frame_cidade_uf,
        width=40
    )
    cidade_entrada.pack(side="left")

    #   FRAME UF (INCLUSA NO FRAME DA CIDADE)
    frame_uf = tk.Frame(
        frame_cidade_uf
    )
    frame_uf.pack(side="right")

    uf_label = tk.Label(
        frame_uf,
        text="UF: ",
        font=("Arial", 12)
    )
    uf_label.pack(side="left")

    uf_entrada = tk.Entry(
        frame_uf,
        width=5
    )
    uf_entrada.pack(side="right")

    #   FRAME CEP
    frame_cep_cnpj = tk.Frame(
        janela
    )
    frame_cep_cnpj.pack(pady=10)

    cep_label = tk.Label(
        frame_cep_cnpj,
        text="CEP: ",
        font=("Arial", 12)
    )
    cep_label.pack(side="left")

    cep_entrada = tk.Entry(
        frame_cep_cnpj,
        width=15
    )
    cep_entrada.pack(side="left")

    #   FRAME CNPJ
    frame_cnpj = tk.Frame(
        frame_cep_cnpj
    )
    frame_cnpj.pack(pady=10)

    cnpj_label = tk.Label(
        frame_cnpj,
        text="CNPJ: ",
        font=("Arial", 12)
    )
    cnpj_label.pack(side="left")

    cnpj_entrada = tk.Entry(
        frame_cnpj,
        width=40
    )
    cnpj_entrada.pack(side="right")

    #   BOTÃO PDF
    botao = tk.Button(
        janela,
        text="Gerar PDF",
        font=("Arial", 10, "bold"),
        borderwidth=1,
        relief="solid",
        width=10,
        height=2,
        #   Lambda é importante pra não freezar o programa
        command=lambda: (
            gerar_pdf(
                nome_entrada.get(),
                endereco_entrada.get(),
                cidade_entrada.get(),
                uf_entrada.get(),
                cep_entrada.get(),
                cnpj_entrada.get()
            ),
            limpar_campos(
                nome_entrada,
                endereco_entrada,
                cidade_entrada,
                uf_entrada,
                cep_entrada,
                cnpj_entrada
            )
        )
    )
    botao.pack(pady=10)

    janela.mainloop()
