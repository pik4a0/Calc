per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую планируете положить под проценты: "))
deposit = []

for bank, percent in per_cent.items():
    deposit.append(int(money * percent / 100))
max_per_cent = max(deposit)
print("При вложении суммы в размере: ",money,"денежных едениц","размер дохода с процентов за год составит: ",deposit)
print ("Максимальная сумма, которую вы можете заработать: ",max_per_cent,"денежных едениц")