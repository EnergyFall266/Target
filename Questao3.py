import json

with open("dados.json",encoding='utf-8') as dadosFile:
    dados = json.load(dadosFile)

menor = 1.7976931348623157e+308
maior = 0
total = 0
count = 0
numDiasFaturSuper = 0

for i in dados:
    if i['valor']<menor:
        menor = i['valor']
    if i['valor']>maior:
        maior = i['valor']

for j in dados:
    if j['valor'] != 0:
        total = total + j['valor']
        count = count + 1

mediaMensal = total/count

for k in dados:
    if k['valor']>mediaMensal:
        numDiasFaturSuper = numDiasFaturSuper +1

print(f'Menor valor de faturamento: {menor}')
print(f'Maior valor de faturamento: {maior}')
print(f'Numero de dias que o faturamento diario foi superior ao mensal: {numDiasFaturSuper}')