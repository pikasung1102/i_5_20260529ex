from datetime import datetime
import config
from money_dummy import selectdumyInit



flag = True

bankAccount = []
currentMoney = 0


# def selectdumyInit():
def selectdumyInit():
    accountNumber = {
             'name': '홍길동',
             'bank': 'DW은행',
             'banknumber': '123-456789-012'
             }
    return accountNumber
    

def userSelectedMenuNum():
    selectMenu = int(input('1.입금   2.출금   3.조회   4.종료 '))
    return selectMenu

def usertimeLine():
    nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return nowTime

def usermemoLine():
    memo = f'[{nowTime}] \t {inMoney:<10} {0:<10} \t {inMoneyMemo:<8} \t{currentMoney:<10}'
    return memo

def usermemoSubLine():
    memo = f'[{nowTime}] \t {0:<10} {-subMoney:<10} \t {subMoneyMemo:<8} \t{currentMoney:<10}'
    return memo

def userReadNumber():
    if selectdumyInit == accountNumber['banknumber']:
        return selectdumyInit

while flag:

    selectMenu = userSelectedMenuNum()

    if selectMenu == config.MENU_DEPOSIT:
        
        print('=' *70)
        accountNumber = selectdumyInit()
        while True:
            inMoney = int(input('입금 금액: '))
            inMoneyMemo = input('입금 내용: ')
            currentMoney += inMoney
            
            if selectdumyInit() == userReadNumber():
                
                print(f'총 금액: {currentMoney}')
                print('=' *70)

            nowTime = usertimeLine()
            memo = usermemoLine()            
            bankAccount.append(memo)

            again = input('계속 입금을 진행하려면 1, 아니면 2를 입력하세요: ')

            if again == '2':
                break

    elif selectMenu == config.MENU_WITHDRAWAL:
        print('=' *70)
        accountNumber = selectdumyInit()
        while True:
            subMoney = int(input('출금 금액: '))
            subMoneyMemo = input('출금 내용: ')
            currentMoney -= subMoney

            if selectdumyInit() == userReadNumber():
                
                print(f'총 금액: {currentMoney}')
                print('=' *70)

            nowTime = usertimeLine()
            memo = usermemoSubLine()
            bankAccount.append(memo)
            
            again = input('계속 출금을 진행하려면 1, 아니면 2를 입력하세요: ')

            if again == '2':
                break

    elif selectMenu == config.MENU_INQUIRY:
        accountNumber = selectdumyInit()

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

