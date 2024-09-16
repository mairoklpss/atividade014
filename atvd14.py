# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
n1 = float(input("digite a 1° nota: "))
n2 = float(input("digite a 2° nota: "))
n3 = float(input("digite a 3° nota: "))

# Calcular a média.
media = (n1 + n2 + n3)/3

# Para informar a condição do aluno.
if media >= 7:
    print(f"a média do(a) é {media:.2f}, portanto o(a) aluno(a) foi aprovado.")
elif media <= 5 or media < 7:
    print(f"a média do(a) é {media:.2f}, portanto o(a) aluno(a) está de recuperação.")
