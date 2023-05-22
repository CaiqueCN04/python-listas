lista= [100,150,1000,200,300] 
carros=["up","fusca","celta","ka","corsinha"]  
def acha_maior(lista):
    maior=lista[0]
    indice_maior=0
    for i in range(len(lista)):
        print(f"agora vou testar a lista{i}, ou seja, {lista[i]}>{maior}")
        if lista[i]>maior:
            print(f"vou trocar {maior} por{lista[i]}")
            maior= lista[i]
            indice_maior=i
    return indice_maior
precos= [100,150,1000,200,300] 
carros=["up","fusca","celta","ka","corsinha"]
local_maior= acha_maior(precos)
print(f"no fim o mais caro é {carros [local_maior]} e custa {precos[local_maior]}")