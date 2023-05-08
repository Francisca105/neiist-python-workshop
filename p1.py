def eh_sensivel(string):
    vogais = ["a", "e", "i", "o", "u"]
    if string[0] in vogais or string[-1] in vogais or string.count("a") < 2 or sum([ord(char) for char in string]) > 1200:
        return False
    return True


# def cifra_palavra(string, inteiro):
#     res = ""

#     if len(string.split()) > 1:
#         raise ValueError("erro")
#     for e in string: # 97 -> 122 | 65 -> 90
#         e = ord(e)
#         #print(e, e + inteiro)

#         def auxiliar(min, max, e, inteiro):
#             if (e+inteiro) < max:
#                 return e+inteiro
#             while e <= max:
#                 e += 1
#                 inteiro -= 1
#             e = min + inteiro
#             return e

#         if 122 >= e >= 97:    
#             valor = e + inteiro
#             res += str()
#         if 90 >= e >= 65:
            
#             valor =  auxiliar(65, 90, e , inteiro)
#             res += str(valor)
#             print(valor)
#         else:
#             raise ValueError("unknown")
#         return valor
    
# print(cifra_palavra("abc", 5))

def cifra_palavra(string, inteiro):
    res = []
    for c in string:
        o = ord(c)

        def auxiliar(o, inteiro, min, max):
            if ord(min) <= o <= ord(max):
                if (o + inteiro) > ord(max):
                    while o <= ord(max):
                        o += 1
                        inteiro -= 1
                    o = ord(min) + inteiro
                else:
                    o = o + inteiro
                return o
            return False

        auxiliado1 = auxiliar(o, inteiro, "a", "z")
        auxiliado2 = auxiliar(o, inteiro, "A", "Z")

        if auxiliado1:
            res.append(auxiliado1)
        if auxiliado2:
            res.append(auxiliado2)

    resultado = ""
    for n in res:
        resultado+=chr(n)
    return resultado

#print(cifra_palavra("zaokasdpk", 3))

def cifra_mensagem(frase, n):
    res = []
    for p in frase.split() :
        res.append(cifra_palavra(p,n))
    return " ".join(res) 

print(cifra_mensagem("macaco zaokasdpk", 3))
#print(cifra_palavra("macaco zaokasdpk", 3))
