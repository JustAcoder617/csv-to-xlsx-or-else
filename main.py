import pandas as pd

def ler_ex(arquivo):
    df=pd.read_excel(arquivo)
    return df

def ler_csv(arquivo):
    df=pd.read_csv(arquivo)
    return df

choice=int(input("Qual o tipo do seu arquivo? (1. Execel 2. Csv)"))
if choice==1:
    choice=str(input("Digite o caminho do seu arquivo: "))
    file="a"
    try:
        file=ler_ex(choice)
    except FileNotFoundError:
        print("Arquivo não encontrado! ")
        exit(1)
    escolha=int(input("Arquivo encontrado! gostaria de transformar em formato CSV? (1. sim 2.não)"))
    if escolha==1:
        file.to_csv("Dados_em_Csv.Csv", index=False)
        linhas, colunas=file.shape
        print(f" Pronto! criei um arquivo chamado Dados_em_Csv.csv, com os dados da sua planilha em csv. Sua planinha tem {linhas} linhas e {colunas} colunas.")
        exit(0)
    if escolha==2:
        linhas, colunas=file.shape
        print(f" O arquivo tem {linhas} linhas e {colunas}!")
        exit(0)
        
if choice==2:
    choice=str(input("Digite o caminho do seu arquivo: "))
    file="a"
    try:
        file=ler_csv(choice)
    except FileNotFoundError:
        print(" Arquivo não encontrado!")
        exit(1)
    escolha=int(input("Arquivo encontrado! gostaria de tranformar em formatado Excel? (1.sim 2.não)"))
    if escolha==1:
        file.to_excel("Dados_em_excel.xlsx", index=False)
        linhas, colunas=file.shape
        print(f"Pronto! criei o arquivo Dados_em_excel.xlsx com seus dados! o arquivo tem {linhas} linhas e {colunas} colunas!")
        exit(0)
    if escolha==2:
        linhas, colunas=file.shape
        print(f"O arquivo  tem {linhas} linahs e {colunas} colunas.")
        exit(0)