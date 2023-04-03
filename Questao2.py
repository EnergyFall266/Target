
anterior = 0
posterior = 1
numInform = 90
aux = 0
while numInform>aux:
    aux = anterior + posterior
    if numInform == aux:
        print("numero pertencente")
        exit(1)
    anterior = posterior
    posterior = aux
print("numero nao pertencente")