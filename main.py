from time import sleep
total = clientMoney = 0
listing = ('001', 'Pencil', 1.75,
           '002', 'Rubber', 2,
           '003', 'Notebook', 15.90,
           '004', 'Case', 25,
           '005', 'Protractor', 4.20,
           '006', 'Compass', 9.99,
           '007', 'Backpack', 120.32,
           '008', 'Pens', 22.30,
           '009', 'Book', 34.90
           )
while True:
    print('-' * 40)
    print(f'\033[1m{"Price List":^40}\033[m')
    print('-' * 40)
    print(f'ID {"NAME":^10} {"PRICE":^45}')
    for pos in range(0, len(listing)):
        if pos % 3 == 0:
            print(f'{listing[pos]:.<6}', end='')
            print(f'{listing[pos+1]:.<28}', end='')
            print(f'${listing[pos+2]:>2.2f}')
    print('-' * 40)
    print(f'\033[1m{"Options":^40}\033[m')
    print('-' * 40)
    print('\033[1m1\033[m - Add items')
    print('\033[1m2\033[m - Show cart')
    print('\033[1m3\033[m - Checkout')
    print('\033[1m4\033[m - Exit')
    option = int(input('Option: '))
    if option == 1:
        itemID = str(input('Enter item ID: '))
        if itemID == listing[0]:
            converted = float(listing[2])
            total += converted
            sleep(1)
            print(f'You added {listing[1]} = \033[1;32m${listing[2]}\033[m')
            sleep(0.5)
        elif itemID == listing[3]:
            converted = float(listing[5])
            total += converted
            sleep(1)
            print(f'You added {listing[4]} = \033[1;32m${listing[5]}\033[m')
            sleep(0.5)
        elif itemID == listing[6]:
            converted = float(listing[8])
            total += converted
            sleep(1)
            print(f'You added {listing[7]} = \033[1;32m${listing[8]}\033[m')
            sleep(0.5)
        elif itemID == listing[9]:
            converted = float(listing[11])
            total += converted
            sleep(1)
            print(f'You added {listing[10]} = \033[1;32m${listing[11]}\033[m')
            sleep(0.5)
        elif itemID == listing[12]:
            converted = float(listing[14])
            total += converted
            sleep(1)
            print(f'You added {listing[13]} = \033[1;32m${listing[14]}\033[m')
            sleep(0.5)
        elif itemID == listing[15]:
            converted = float(listing[17])
            total += converted
            sleep(1)
            print(f'You added {listing[16]} = \033[1;32m${listing[17]}\033[m')
            sleep(0.5)
        elif itemID == listing[18]:
            converted = float(listing[19])
            total += converted
            sleep(1)
            print(f'You added {listing[19]} = \033[1;32m${listing[19]}\033[m')
            sleep(0.5)
        elif itemID == listing[21]:
            converted = float(listing[23])
            total += converted
            sleep(1)
            print(f'You added {listing[22]} = \033[1;32m${listing[23]}\033[m')
            sleep(0.5)
        elif itemID == listing[24]:
            converted = float(listing[26])
            total += converted
            sleep(1)
            print(f'You added {listing[25]} = \033[1;32m${listing[26]}\033[m')
            sleep(0.5)
        else:
            sleep(0.5)
            print('\033[1;31mID NOT FOUND\033[m')
        sleep(1.5)
    elif option == 2:
        print('-' * 40)
        print(f'\033[1m{"Cart":^40}\033[m')
        print('-' * 40)
        print(f'\nPURCHASE TOTAL: \033[1;32m${total}\033[m\n')
        sleep(2)
    elif option == 3:
        print('-' * 40)
        print(f'\033[1m{"Check":^40}\033[m')
        print('-' * 40)
        print(f'\nPURCHASE TOTAL: \033[1;32m${total}\033[m\n')
        while clientMoney < total:
            clientMoney = float(input('Enter your money: $'))
            if clientMoney >= total:
                clientChange = clientMoney - total
                if clientMoney > total:
                    sleep(0.5)
                    print(f'Here is your change: \033[1;32m${clientChange:.2f}\033[m')
                sleep(0.5)
                print('Thank you! Bye!')
                exit()
    elif option == 4:
        print('\033[1;31mShutting down...\033[m')
        sleep(1)
        exit()
        