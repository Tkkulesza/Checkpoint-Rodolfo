# PROJETO CHECKPOINT RODOLFO - NOTA FINAL DO ANO

# PRIMEIRO SEMESTRE

# Notas CheckPoints
cp1 = float(input("Digite o seu CheckPoint 1: "))
cp2 = float(input("Digite o seu CheckPoint 2: "))
cp3 = float(input("Digite o seu CheckPoint 3: "))

# Notas Challenges
cs1 = float(input("Digite o seu Challenge 1: "))
cs2 = float(input("Digite o seu Challenge 2: "))

# Notas Global Solutions
gs1 = float(input("Digite a sua nota do Global Solution 1: "))

# Removendo a nota de checkpoint mais baixa (usar somente 2 melhores CPs)
cp_top2 = cp1 + cp2 + cp3 - min(cp1, cp2, cp3)
print(f"CPs considerados (sem menor CP): {cp_top2:.1f}")
print(f"CSs considerados: {cs1:.1f} e {cs2:.1f}")
print(f"GS considerado: {gs1:.1f}")

# Cálculo simplificado do primeiro semestre
# CP_top2 + CS1 + CS2 + GS1, dividido pelos 5 itens (2 CP + 2 CS + 1 GS)
nota_sm1 = (cp_top2 + cs1 + cs2 + gs1) / 5
print(f"A sua média do primeiro semestre é: {nota_sm1:.2f}")



# SEGUNDO SEMESTRE

# Notas CheckPoints
cp4 = float(input("Digite o seu CheckPoint 4: "))
cp5 = float(input("Digite o seu CheckPoint 5: "))
cp6 = float(input("Digite o seu CheckPoint 6: "))

# Notas Challenges do segundo semestre
cs3 = float(input("Digite o seu Challenge 3: "))
cs4 = float(input("Digite o seu Challenge 4: "))

gs3 = float(input("Digite a sua nota do Global Solution 3: "))
gs4 = float(input("Digite a sua nota do Global Solution 4: "))

# Removendo a nota de checkpoint mais baixa do segundo semestre
cp_top2_2s = cp4 + cp5 + cp6 - min(cp4, cp5, cp6)
print(f"CPs considerados (sem menor CP): {cp_top2_2s:.1f}")
print(f"CSs considerados: {cs3:.1f} e {cs4:.1f}")
print(f"GSs considerados: {gs3:.1f} e {gs4:.1f}")

# Cálculo simplificado do segundo semestre
# CP_top2 + CS3 + CS4 + GS3 + GS4, dividido pelos 6 itens (2 CP + 2 CS + 2 GS)
nota_sm2 = (cp_top2_2s + cs3 + cs4 + gs3 + gs4) / 6
print(f"A sua média do segundo semestre é: {nota_sm2:.2f}")

# Calculando a nota final do ano
nota_final_total = (nota_sm1 * 0.4) + (nota_sm2 * 0.6)
print(f"A sua nota final total é: {nota_final_total:.2f}")

# Verificando se o aluno passou de ano, ficou de exame ou não passou de ano
if nota_final_total < 4:
    print("Infelizmente você não passou de ano, estude mais para o próximo semestre!!")
elif nota_final_total >= 4 and nota_final_total < 6:
    print("Você ficou de exame, estude mais para a recuperação!!")
else:
    print("Parabéns, você passou de ano!!")