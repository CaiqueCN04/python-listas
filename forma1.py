lista= [100,150,1000,200,300] 
carros=["up","fusca","celta","ka","corsinha"]  
maior=lista[0]
indice_maior=0
for i in range(len(lista)):
    print(f"agora vou testar a lista{i}, ou seja, {lista[i]}>{maior}")
    if lista[i]>maior:
        print(f"vou trocar {maior} por{lista[i]}")
        maior= lista[i]
        indice_maior=i
print(f"no fim o mais caro é {carros[indice_maior]} e custa {lista[indice_maior]}")


#pode ser usado na global para fazer indice de paises que mais usam e os que menos usam
#para os menos usam apenas mudar i if e a variaveis respectivas
