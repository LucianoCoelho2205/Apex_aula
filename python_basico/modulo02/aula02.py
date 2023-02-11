n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2 

if media < 7:
    print('Aluno Reprovado!Sua media sera de: {:.1f}'.format(media))
else:
    print('Aluno Aprovado!Sua media sera de: {:.1f}'.format(media))    



