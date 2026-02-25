registros = []

elevadores = {"A": 0, "B": 0, "C": 0}
periodos = {"M": 0, "V": 0, "N": 0}
fluxo = {
    "A": {"M": 0, "V": 0, "N": 0},
    "B": {"M": 0, "V": 0, "N": 0},
    "C": {"M": 0, "V": 0, "N": 0}
}

while True:
    elevador = input("Informe o elevador (A, B, C) ou digite SAIR para encerrar: ").upper()

    if elevador == "SAIR":
        break

    if elevador not in ["A", "B", "C"]:
        print("Elevador inválido!")
        continue

    periodo = input("Período (M, V, N): ").upper()

    if periodo not in ["M", "V", "N"]:
        print("Período inválido!")
        continue

    registros.append((elevador, periodo))
    elevadores[elevador] += 1
    periodos[periodo] += 1
    fluxo[elevador][periodo] += 1


if len(registros) > 0:

    elevadores_validos = {k: v for k, v in elevadores.items() if v > 0}
    mais_usado = max(elevadores_validos, key=elevadores_validos.get)

    periodo_fluxo = max(fluxo[mais_usado], key=fluxo[mais_usado].get)

    # Período mais utilizado geral (ignora zero)
    periodos_validos = {k: v for k, v in periodos.items() if v > 0}
    periodo_mais_usado = max(periodos_validos, key=periodos_validos.get)

    valores_validos = list(periodos_validos.values())

    if len(valores_validos) > 1:
        mais = max(valores_validos)
        menos = min(valores_validos)

        total = sum(periodos.values())
        diferenca = ((mais - menos) / total) * 100
    else:
        diferenca = 0

    print("\nRESULTADOS:")
    print("Elevador mais utilizado:", mais_usado)
    print("Período de maior fluxo nesse elevador:", periodo_fluxo)
    print("Período mais utilizado geral:", periodo_mais_usado)
    print("Diferença percentual:", round(diferenca, 2), "%")

else:
    print("Nenhum dado foi inserido.")