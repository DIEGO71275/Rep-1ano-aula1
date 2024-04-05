#ENTRADA
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

#PROCESSAMENTO

SomaNotas = nota1 + nota2 + nota3 + nota4
CalcMedia = SomaNotas / 4

#SAÍDA

if CalcMedia >= 6:

    print("Passou")

elif CalcMedia >= 5 and CalcMedia <6: 

    print("Recuperação")

else:

    print("Reprovado")
