import os
import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#   FUNÇÕES

#   CENTRALIZA JANELA
def centralizar(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 3

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

#   LIMPA CAMPO
def limpar_campos(*campos):
    for campo in campos:
        campo.delete(0, tk.END)

#   VALIDA DADOS
def validar_dados(nome, endereco, cep, cidade, uf, telefone, cnpj):

    erros = []
    
    if not nome:
        erros.append("O nome é obrigatório!")
        
    if not endereco:
        erros.append("O endereço é obrigatório!")
        
    if not cep:
        erros.append("O CEP é obrigatório!")
    
    if not cidade:
        erros.append("A cidade é obrigatório!")

    if not uf:
        erros.append("A UF é obrigatório!")

    if not telefone:
        erros.append("O telefone é obrigatório!")

    if not cnpj:
        erros.append("O CNPJ é obrigatório!")

    return erros

#   GERA PDF
def gerar_pdf(nome, endereco, cep, cidade, uf, telefone, cnpj):

    pdf = canvas.Canvas("destinatario.pdf", pagesize=A4)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(A4[0] / 2, 770, "Destinatário")

    #   NOME
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 754, "_" * 60)

    pdf.setFont("Helvetica", 18)
    pdf.drawString(100, 730, "Nome:")

    pdf.setFont("Helvetica", 16)
    pdf.drawString(160, 730, nome)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 722, "_" * 60)

    #   ENDEREÇO
    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, 694, "Endereço:")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(176, 694, endereco)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 682, "_" * 60)

    #   CEP
    pdf.setFont("Helvetica", 16)
    pdf.drawString(426, 694, cep)

    #   CIDADE
    pdf.setFont("Helvetica", 18)
    pdf.drawString(100, 654, "Cidade:")

    pdf.setFont("Helvetica", 16)
    pdf.drawString(170, 654, cidade)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 642, "_" * 60)

    #   UF
    pdf.setFont("Helvetica", 18)
    pdf.drawString(436, 654, "UF:")

    pdf.setFont("Helvetica", 18)
    pdf.drawString(470, 654, uf)

    #   TELEFONE
    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, 614, "Telefone: ")

    pdf.setFont("Helvetica", 16)
    pdf.drawString(172, 614, telefone)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 602, "_" * 60)

    #   CNPJ/CPF
    pdf.setFont("Helvetica", 16)
    pdf.drawString(300, 614, "CNPJ:")

    pdf.setFont("Helvetica", 16)
    pdf.drawString(350, 614, cnpj)

    pdf.save()

    os.startfile("destinatario.pdf")

#   PROCESSA FORMULÁRIO
def processar_formulario(nome, endereco, cep, cidade, uf, telefone, cnpj):

    valor_nome = nome.get().strip()
    valor_endereco = endereco.get().strip()
    valor_cep = cep.get().strip()
    valor_cidade = cidade.get().strip()
    valor_uf = uf.get().strip()
    valor_telefone = telefone.get().strip()
    valor_cnpj = cnpj.get().strip()

    erros = validar_dados(
        valor_nome,
        valor_endereco,
        valor_cep,
        valor_cidade,
        valor_uf,
        valor_telefone,
        valor_cnpj
    )

    if erros:
        messagebox.showerror(
            "Dados Inválidos",
            "\n".join(erros)
        )
        return

    gerar_pdf(
        valor_nome,
        valor_endereco,
        valor_cep,
        valor_cidade,
        valor_uf,
        valor_telefone,
        valor_cnpj
    )

    limpar_campos(
        nome,
        endereco,
        cep,
        cidade,
        uf,
        telefone,
        cnpj
    )
