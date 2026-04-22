
cp1 = float(input("Digite a nota da 1ª CP: "))
cp2 = float(input("Digite a nota da 2ª CP: "))
cp3 = float(input("Digite a nota da 3ª CP: "))
sp1 = float(input("Digite a nota da 1ª Sprint: "))
sp2 = float(input("Digite a nota da 2ª Sprint: "))
gs = float(input("Digite a nota da GS: "))

if cp1 <= cp2 and cp1 <= cp3:
    menor_nota = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor_nota = cp2
else:
    menor_nota = cp3

media_bloco = (cp1 + cp2 + cp3 - menor_nota + sp1 + sp2) / 4


mediapeso_40 = media_bloco * 0.4

mediapeso_60 = gs * 0.6

media_final = mediapeso_40 + mediapeso_60

print("-" * 30)
print(f"Menor nota de CP descartada: {menor_nota}")
print(f"Média do bloco (CPs + SPs): {media_bloco:.2f}")
print(f"Pontos acumulados (40%): {mediapeso_40:.2f}")
print(f"Pontos da GS (60%): {mediapeso_60:.2f}")
print(f"MÉDIA FINAL SEMESTRAL: {media_final:.2f}")