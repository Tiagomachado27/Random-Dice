import random

dice_nr = input("Quantos dados quer lançar? ")
dice_shape = input("Quantos lados têm os dados? ")

repeat = ("")


for x in range(int(dice_nr)):
    print(random.randint(1, int(dice_shape)))
while True :
    repeat = input("Deseja lançar outra vez?\n"  "(Pressione 's' para lançar outra vez)")
    if repeat == "s":
        for x in range(int(dice_nr)):
            print(random.randint(1, int(dice_shape)))
    else:
        close = input("Pressione Enter para fechar o programa.")
        break
