
import config
import moduleEx


flag = True

bankAccount = []
currentMoney = 0



while flag:

    selectMenu = moduleEx.userSelectedMenuNum()

    if selectMenu == config.MENU_DEPOSIT:
        
        print('=' *70)
        accountNumber = moduleEx.selectdumyInit()
        while True:
            inMoney = int(input('입금 금액: '))
            inMoneyMemo = input('입금 내용: ')
            currentMoney += inMoney
            
                
            print(f'총 금액: {currentMoney}')
            print('=' *70)

            nowTime = moduleEx.usertimeLine()
            memo = moduleEx.usermemoLine(nowTime, inMoney, inMoneyMemo, currentMoney )           
            bankAccount.append(memo)

            again = input('계속 입금을 진행하려면 1, 아니면 2를 입력하세요: ')

            if again == '2':
                break

    elif selectMenu == config.MENU_WITHDRAWAL:
        print('=' *70)
        accountNumber = moduleEx.selectdumyInit()
        while True:
            subMoney = int(input('출금 금액: '))
            subMoneyMemo = input('출금 내용: ')
            currentMoney -= subMoney

            accountNumber = moduleEx.selectdumyInit()
                    
                
            print(f'총 금액: {currentMoney}')
            print('=' *70)

            nowTime = moduleEx.usertimeLine()
            memo = moduleEx.usermemoSubLine(nowTime, subMoney, subMoneyMemo, currentMoney)
            bankAccount.append(memo)
            
            again = input('계속 출금을 진행하려면 1, 아니면 2를 입력하세요: ')

            if again == '2':
                break

    elif selectMenu == config.MENU_INQUIRY:
        accountNumber = moduleEx.selectdumyInit()

        inputAccount = input('계좌번호 입력: ')
        if inputAccount == accountNumber["banknumber"]:
      
            print('=' *75)
            print(f'{"날짜&시간":<20} {"입금":<10} {"출금":<10} {"내역":<10} {"잔액":<10}')
            print('=' *75)
            for history in bankAccount:
                    print(history)

            print('=' *75)
                   
            break
       
        else:
            print('입력하신 계좌정보가 없습니다.')
            

    elif selectMenu == config.EXIT:
        flag = False

