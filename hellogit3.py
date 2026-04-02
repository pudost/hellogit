print ("hellogit3")

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ Soma
- subtração
* Multiplicação
/ Divisão
5 Sair
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')
		
# Call calculate() outside of the function
calculate()

while True:
     string_digitada = input("Digite a Opção cooreta para Sair: ")
     if string_digitada.lower() == "5":
         print("Fim!")
         break
     if len(string_digitada) < 2:
         print("Opção Incorreta")
         continue
     print("Tente digitar \"5\"")
 