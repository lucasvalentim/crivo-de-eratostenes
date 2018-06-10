def crivo_de_eratostenes(n):
    if n < 2:
        return []
    
    numeros = list(range(2, n + 1))
    
    i = 0
    
    while numeros[i] <= int(n ** 0.5):
        for multiplo in range(numeros[i] * 2, n + 1, numeros[i]):
            if multiplo in numeros:
                numeros.remove(multiplo)
        
        i += 1
        
    return numeros
