import numpy as np


def distribuicao_normal(media, desvio_padrao, tamanho):
    return np.random.normal(media, desvio_padrao, tamanho)

def distribuicao_uniforme(limite_inferior, limite_superior, tamanho):
    return np.random.uniform(limite_inferior, limite_superior, tamanho)

def distribuicao_exponencial(taxa_ocorrencia, tamanho):
    return np.random.exponential(taxa_ocorrencia, tamanho)

def calcular_media(valores_media):
    return np.mean(valores_media)

def calcular_mediana(valores_mediana):
    return np.median(valores_mediana)

def calcular_variancia(valores_variancia):
    return np.var(valores_variancia)

def desvio_padrao(valores_std):    
    return np.std(valores_std)

def carregar_arquivo(caminho):
    lines = []
    with open(caminho, "r") as arquivo:
        for line in arquivo:
            values = line.strip().split(',')
            int_values = [int(val) for val in values]
            lines.append(int_values)
    return np.array([np.array(row) for row in lines], dtype='object')


def main():
    numeros = carregar_arquivo("Analise Estatisitca/dados.txt")
    print("numeros")
    
        
if(__name__ == '__main__'):
    main()
