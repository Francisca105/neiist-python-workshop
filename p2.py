test = {
    "Helena Teixiera": [1.595, {
        "velocidade": 3,
        "forca": 7,
        "inteligencia": 10,
        "carisma": 4,
    }],
    "Rogério Colaco": [1.70, {
        "velocidade": 9,
        "forca": 5,
        "inteligencia": 8,
        "carisma": 0,
    }]
}
dicionario = {
    "velocidade": 3,
    "altura": 1.69,
    "forca": 7,
    "ALTURA": 2.0
}

def calcula_pontuacao(atr):
    v = atr.values()
    maior = max(v)
    menor = min(v)
    soma = 0
    for n in v:
        soma += (maior-n)
    return soma / (11-menor)

def valor_requisitos(l, dic):
    pont = 0
    if dic["ALTURA"] > l[0] > dic["altura"]:
        pont += 1
    for i in l[1]:
        if i == "ALTURA" or i == "altura":
            pass

        if i in dic.keys():
            min = dic[i]
            value = l[1][i]

            pont += 1 if value >= min else 0
    return pont


def escolhe_espiao(espioes, reqs):
    r = {}
    nome = ""
    p = 0
    for espiao in espioes:

        valor = valor_requisitos(espioes[espiao], reqs)
        if p < valor:
            p = valor
            nome = espiao
        elif p == valor and calcula_pontuacao(espioes[espiao][1]) > calcula_pontuacao(espioes[nome][1]):
            nome = espiao
    return nome
        

print(escolhe_espiao(test, dicionario))