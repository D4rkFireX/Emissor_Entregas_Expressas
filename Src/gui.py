import tkinter as tk
from funcoes import centralizar, processar_formulario

def interface():

    #   CRIAÇÃO DA JANELA
    janela = tk.Tk()

    #   CONFIGURAÇÕES GERAIS DA JANELA
    janela.title("Entregas Expressas RS")
    centralizar(janela, 600, 340)
    janela.resizable(False, False)

    icone = tk.PhotoImage(file="img/favicon.png")
    janela.iconphoto(True, icone)

    #   TÍTULO DA APLICAÇÃO
    titulo = tk.Label(
        janela,
        text="Destinatário",
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
        text="Endereço:",
        font=("Arial", 12)
    )
    endereco_label.pack(side="left")
    
    endereco_entrada = tk.Entry(
        frame_endereco,
        width=40
    )
    endereco_entrada.pack(side="left")
    
    #   FRAME CEP
    frame_cep = tk.Frame(
        frame_endereco
    )
    frame_cep.pack(side="left")
    
    cep_label = tk.Label(
        frame_cep,
        text="CEP:",
        font=("Arial", 12)
    )
    cep_label.pack(side="left")
    
    cep_entrada = tk.Entry(
        frame_cep,
        width=12
    )
    cep_entrada.pack(side="left")

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

    #   FRAME TELEFONE
    frame_telefone_cnpj = tk.Frame(
        janela
    )
    frame_telefone_cnpj.pack(pady=10)

    telefone_label = tk.Label(
        frame_telefone_cnpj,
        text="Telefone: ",
        font=("Arial", 12)
    )
    telefone_label.pack(side="left")

    telefone_entrada = tk.Entry(
        frame_telefone_cnpj,
        width=18
    )
    telefone_entrada.pack(side="left")

    #   FRAME CNPJ
    frame_cnpj = tk.Frame(
        frame_telefone_cnpj
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
        width=26
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
        command=lambda: processar_formulario(
            nome_entrada,
            endereco_entrada,
            cep_entrada,
            cidade_entrada,
            uf_entrada,
            telefone_entrada,
            cnpj_entrada
        )
    )
    botao.pack(side="top", pady=14)

    janela.mainloop()
