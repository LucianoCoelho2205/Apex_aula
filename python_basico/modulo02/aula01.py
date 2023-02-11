idade = int(input('qual a sua idade? '))

if idade >= 18:
    print('o aluno tem 18')
elif idade <= 18:
    print('o aluno tem menor que 18')
elif idade == 18:
    print('o aluno tem 18')  
elif idade != 18:
    print('o aluno te a idade diferente de 18')           
elif idade > 18:
    print('o aluno tem maior que 18')
else:
    print('o aluno tem menos que 18')

