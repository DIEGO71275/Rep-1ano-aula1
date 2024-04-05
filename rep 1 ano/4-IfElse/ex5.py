lado1 = float(input("Digite o ângulo do primeiro lado: "))
lado2 = float(input("Digite o ângulo do segundo lado: "))
lado3 = float(input("Digite o ângulo do terceiro lado: "))

if lado1 == lado2 and lado2 == lado3:

    print ("É equilátero")

elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:

    print ("É isósceles")

else: 

    print ("É escaleno")