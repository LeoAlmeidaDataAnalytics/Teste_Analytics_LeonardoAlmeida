from datetime import datetime, timedelta

from numpy import random
import pandas as pd


# Configuração inicial
num_registros = 100  # Número de registros no dataset
inicio_periodo = datetime(2023, 1, 1)
fim_periodo = datetime(2023, 12, 31)

# Listas para gerar dados aleatórios
produtos_categorias = [
    {"produto": "Notebook", "categoria": "Eletrônicos"},
    {"produto": "Smartphone", "categoria": "Eletrônicos"},
    {"produto": "Camiseta", "categoria": "Vestuário"},
    {"produto": "Tênis", "categoria": "Vestuário"},
    {"produto": "Mesa", "categoria": "Móveis"},
    {"produto": "Cadeira", "categoria": "Móveis"},
    {"produto": "Geladeira", "categoria": "Eletrodomésticos"},
    {"produto": "Micro-ondas", "categoria": "Eletrodomésticos"}
]

# Função para gerar uma data aleatória no período
def gerar_data_aleatoria(inicio, fim):
    delta = fim - inicio
    dias_aleatorios = random.randint(0, delta.days)
    return inicio + timedelta(days=dias_aleatorios)

# Gerar os dados
dados = []
for i in range(1, num_registros + 1):
    produto_categoria = random.choice(produtos_categorias)
    quantidade = random.randint(1, 21)  # Quantidade de 1 a 20
    preco = round(random.uniform(10, 5001), 2)  # Preço entre R$10 e R$5000
    data_venda = gerar_data_aleatoria(inicio_periodo, fim_periodo)
    
    dados.append({
        "id": i,
        "data": data_venda.strftime("%Y-%m-%d"),
        "produto": produto_categoria["produto"],
        "categoria": produto_categoria["categoria"],
        "quantidade": quantidade,
        "preço": int(preco)
    })

# Criar o DataFrame
dataset = pd.DataFrame(dados)

# Visualizar o dataset
print(dataset)
print(type(preco))

# criando o dataset como csv e o separador como ;
#dataset.to_csv('data_clean.csv', index=False, sep=';')