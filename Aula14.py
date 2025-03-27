galera = []
dado = []
totalmai = 0
totalmen = 0

for c in range (0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmen += 1

print(f'Temos {totalmai} maiores e {totalmen} menores de idade.')


#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos.')