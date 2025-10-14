def executar_fifo(sequencia, quadros):
    indice_mais_antigo = 0
    cache = []
    acertos = 0
    falhas = 0
    historico = []

    for endereco in sequencia:
        estado = {
            'endereco': endereco,
            'cache_antes': cache.copy(),
            'resultado': '',
            'cache_depois': []
        }

        if endereco in cache:
            acertos += 1
            estado['resultado'] = 'ACERTO'
            estado['cache_depois'] = cache.copy()
        else:
            falhas += 1
            estado['resultado'] = 'FALHA'

            if len(cache) < quadros:
                cache.append(endereco)
            else:
                cache[indice_mais_antigo] = endereco
                indice_mais_antigo = (indice_mais_antigo + 1) % quadros

            estado['cache_depois'] = cache.copy()

        historico.append(estado)

    return acertos, falhas, historico


sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]

sequencias = [sequencia_a, sequencia_b, sequencia_c]

for i in range(3):
    print(f"\nSequência {i + 1}:")
    acertos, falhas, historico = executar_fifo(sequencias[i], 8)

    print("Passo | Endereço | Cache | Resultado")
    print("-" * 60)

    for estado in historico:
        print(f"{historico.index(estado) + 1} | {estado['endereco']} | {estado['cache_depois']} | {estado['resultado']}\n")
