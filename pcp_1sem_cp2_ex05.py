# verificar aprovação
def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False


#  Taxa de juros
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


# Cálculo da parcela
def calcular_parcela(valor, taxa, parcelas):
    pmt = valor * ((taxa * (1 + taxa)*parcelas) / ((1 + taxa)*parcelas - 1))
    return pmt


# Cálculo do valor total pago
def calcular_total(parcela, parcelas):
    return parcela * parcelas


# Cálculo dos juros pagos
def calcular_juros(total, valor):
    return total - valor


# Programa principal
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
valor = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite o número de parcelas (3 a 24): "))

# Verificando aprovação
if pode_aprovar(idade, renda, valor):

    taxa = definir_taxa(parcelas)

    parcela = calcular_parcela(valor, taxa, parcelas)

    total_pago = calcular_total(parcela, parcelas)

    juros = calcular_juros(total_pago, valor)

    print("\nEmpréstimo APROVADO!")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa aplicada: {taxa*100:.0f}% ao mês")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Valor total pago: R$ {total_pago:.2f}")
    print(f"Total de juros pagos: R$ {juros:.2f}")

else:
    print("\nEmpréstimo NEGADO!")