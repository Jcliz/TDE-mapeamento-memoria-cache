#função que executa o cálculo do MRU
def executar_mru(sequencia, quadros):
    #declaração de variáveis
    cache = []
    uso_recente = []
    historico = []

    #loop que percorre cada endereço na sequência
    for endereco in sequencia:
        #dicionário que armazena o estado atual do cache
        estado = {
            'endereco': endereco,
            'resultado': '',
            'cache_depois': []
        }

        #se o endereço já está no cache, é um acerto
        if endereco in cache:
            estado['resultado'] = 'ACERTO'
            #atualiza a ordem de uso: remove da posição atual e adiciona ao final (mais recente)
            uso_recente.remove(endereco)
            uso_recente.append(endereco)
            estado['cache_depois'] = cache.copy()
        else:
            #se não, é uma falha e o novo endereço é adicionado
            estado['resultado'] = 'FALHA'

            #se estiver faltando espaço para completar os 8 quadros, 
            # o endereço é adicionado ao final
            if len(cache) < quadros:
                cache.append(endereco)
                uso_recente.append(endereco)
            else:
                #encontra o endereço mais recentemente usado (último da lista)
                mru_endereco = uso_recente[-1]
                #localiza sua posição no cache
                indice_mru = cache.index(mru_endereco)
                #substitui o endereço mais usado pelo novo
                cache[indice_mru] = endereco

                #atualiza a ordem de uso: remove o mais usado e adiciona o novo ao final
                uso_recente.pop(-1)
                uso_recente.append(endereco)

            #atualiza o estado do cache após a modificação
            estado['cache_depois'] = cache.copy()

        #adiciona o estado atual ao histórico
        historico.append(estado)

    return historico

#declaração das sequências que vão ser testadas
sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]

#variável utilizada para armazenar as sequências em uma lista 
# (facilita a exibição dos resultados)
sequencias = [sequencia_a, sequencia_b, sequencia_c]

#loop para exibição dos resultados
for i in range(3):
    print(f"\nSequência {i + 1}:")
    historico = executar_mru(sequencias[i], 8)

    print("Passo | Endereço | Cache | Resultado")
    print("-" * 60)

    for estado in historico:
        print(f"{historico.index(estado) + 1} | {estado['endereco']} | {estado['cache_depois']} | {estado['resultado']}\n")