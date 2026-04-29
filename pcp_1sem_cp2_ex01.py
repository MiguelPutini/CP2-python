estado_origem = int(input("Digite o código do estado (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))


peso_quilos = peso_toneladas * 1000

if 10 <= codigo_carga <= 20:
    preco_por_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_por_kg = 250
else:
    preco_por_kg = 340

preco_carga = peso_quilos * preco_por_kg

if estado_origem == 1:
    porcentagem_imposto = 0.35
elif estado_origem == 2:
    porcentagem_imposto = 0.25
elif estado_origem == 3:
    porcentagem_imposto = 0.15
elif estado_origem == 4:
    porcentagem_imposto = 0.05
else:
    porcentagem_imposto = 0.0

valor_imposto = preco_carga * porcentagem_imposto

valor_total = preco_carga + valor_imposto

print("-" * 30)
print(f"Peso em quilos: {peso_quilos} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")