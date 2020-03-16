import random

dice_nr = input("Quantos dados quer lançar? ")
dice_shape = input("Quantos lados têm os dados? ")

for x in range(int(dice_nr)):
    print(random.randint(1, int(dice_shape)))