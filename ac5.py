
"""
Programação Estruturada
2024.1
AC5
 """
import random

def main():
    # Aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    # Monstruoso
    vida_monstruoso = random.randint(60, 80)
    ataque_monstruoso = random.randint(20, 30)

    rodada = 1

    print("Aventureiro vs. Monstruoso")

    while vida_aventureiro > 0 and vida_monstruoso > 0:
        print("Rodada", rodada)

        # Aventureiro ataca o monstruoso
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstruoso -= dano_aventureiro
        if vida_monstruoso <= 0:
            print("O Monstruoso morreu!")
            break
        print("O aventureiro atacou o monstruoso e causou", dano_aventureiro, "de dano")

        # Monstruoso ataca o aventureiro
        dano_monstruoso = random.randint(1, ataque_monstruoso)
        dano_monstruoso -= defesa_aventureiro
        if dano_monstruoso < 0:
            dano_monstruoso = 0
        vida_aventureiro -= dano_monstruoso
        if vida_aventureiro <= 0:
            print("O Aventureiro morreu!")
            break
        print("O monstruoso atacou o aventureiro e causou", dano_monstruoso, "de dano")

        rodada += 1

    print("Atributos finais:")
    print("Aventureiro - Vida:", vida_aventureiro, "Ataque:", ataque_aventureiro, "Defesa:", defesa_aventureiro)
    print("Monstruoso - Vida:", vida_monstruoso, "Ataque:", ataque_monstruoso)

main()
