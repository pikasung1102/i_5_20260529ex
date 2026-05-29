import random

def sign_up(member):
    print(('회원가입을 하시려면 가입하시려는 UID, UPW, UMAIL, UPHONE를 입력해 주세요.' ))
<<<<<<< HEAD
    UID = input('UserId: ')
=======
    UID = input('UserId: ').strip()
>>>>>>> ba4b80c (재업)
    if UID == "":
        print('아이디는 공백으로 만들 수 없습니다.')
        return
    if UID in member:
        print('동일한 아이디로는 가입할 수 없습니다.')
        return
    if not UID.isalnum():
        print('아이디에는 특수 문자를 사용할 수 없습니다.')
        return
    
    UPW = input('UserPw: ')
    UPW_confirm = input('UserPw Confirm (비밀번호 확인): ')
    if UPW != UPW_confirm:
        print('비밀번호가 일치하지 않습니다. 회원가입을 취소합니다.')
        return
    else:
        UEMAIL = input('UserEmail: ')
        UPHONE = input('UserPhone: ')

        print('회원가입이 완료되었습니다.')
        member[UID] = {
            'UID': UID,
            'UPW': UPW,
            'UEMAIL': UEMAIL,
            'UPHONE': UPHONE
                    }
    
    
    
def sign_in(member):
<<<<<<< HEAD
=======
    if not isinstance(member, dict):
        print("로그인 시스템에 오류가 발생했습니다. (회원 데이터가 올바르지 않습니다.)")
        return None
>>>>>>> ba4b80c (재업)
    print('로그인하실 UserID, UserPW를 입력해주세요. ')
    Login_ID = input('UserId: ')
    Login_PW = input('UserPw: ')
    if Login_ID in member: 
        if member [Login_ID] ['UPW'] == Login_PW:
            print('로그인이 완료되었습니다.')
            return Login_ID
                
        else:
            print('비밀번호가 틀렸습니다. ')  
            return None  
    else:
        print('회원님의 정보가 없습니다. ')
        return None

def sign_out(current_user):
    if current_user is None :
            print('현재 로그인되어있지 않습니다.')
            return None
            
    else:
        print(f'{current_user}님, 로그아웃 되었습니다.')
        return None

def modify_profile(member, current_user):
<<<<<<< HEAD
    if current_user is None :
        print('현재 로그인되어있지 않습니다.')
    else:
        selectedUpdateMenu = int(input('PW를 수정하시려면 1, EMAIL을 수정하시려면 2, PHONE을 수정하시려면 3, 전부 수정하시려면 4를 눌러주세요(ID는 변경 불가) '))
        if selectedUpdateMenu == 1:
            print(f'{current_user}님, 수정하실 PW를 입력해주세요.')
            New_PW = input('New_Pw: ')
            if member[current_user]['UPW'] == New_PW:
                print('기존과 동일한 비밀번호입니다.')
            else:
                member[current_user]['UPW'] = New_PW
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 2:
            print(f'{current_user}님, 수정하실 EMAIL를 입력해주세요.')
            New_EMAIL = input('New_Email: ')
            if member[current_user]['UEMAIL'] == New_EMAIL:
                    print('기존과 동일한 이메일입니다.')
            else:
                member[current_user]['UEMAIL'] = New_EMAIL
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 3:
            print(f'{current_user}님, 수정하실 PHONE를 입력해주세요.')
            New_PHONE = input('New_UPhone: ')
            if member[current_user]['UPHONE'] == New_PHONE:
                print('기존과 동일한 전화번호입니다.')
            else:
                member[current_user]['UPHONE'] = New_PHONE
                print('변경이 완료되었습니다.')

        elif selectedUpdateMenu == 4:
            print(f'{current_user}님, 수정하실 PW, EMAIL, PHONE를 입력해주세요.')
            new_pw = input('New_Pw: ')
            new_email = input('New_Email: ')
            new_phone = input('New_Phone: ')
            updated_fields = []

            if member[current_user]['UPW'] != new_pw:
                member[current_user]['UPW'] = new_pw
                updated_fields.append('비밀번호')
        
            if member[current_user]['UEMAIL'] != new_email:
                member[current_user]['UEMAIL'] = new_email
                updated_fields.append('이메일')
            
            if member[current_user]['UPHONE'] != new_phone:
                member[current_user]['UPHONE'] = new_phone
                updated_fields.append('전화번호')

            if updated_fields:
                print(f"[{', '.join(updated_fields)}] 변경이 완료되었습니다.")
            else:
                print("변경된 정보가 없습니다.")
        else:
            print("잘못된 메뉴 선택입니다.")
=======
    if current_user is None:
        print('현재 로그인되어있지 않습니다.')
        return

    selectedUpdateMenu = int(input('PW를 수정하시려면 1, EMAIL을 수정하시려면 2, PHONE을 수정하시려면 3, 전부 수정하시려면 4를 눌러주세요(ID는 변경 불가): '))
    
    if selectedUpdateMenu == 1:
        print(f'{current_user}님, 수정하실 PW를 입력해주세요.')
        New_PW = input('New_Pw: ')
        if member[current_user]['UPW'] == New_PW:
            print('기존과 동일한 비밀번호입니다.')
        else:
            member[current_user]['UPW'] = New_PW
            print('변경이 완료되었습니다.')

    elif selectedUpdateMenu == 2:
        print(f'{current_user}님, 수정하실 EMAIL를 입력해주세요.')
        New_EMAIL = input('New_Email: ')
        if member[current_user]['UEMAIL'] == New_EMAIL:
            print('기존과 동일한 이메일입니다.')
        else:
            member[current_user]['UEMAIL'] = New_EMAIL
            print('변경이 완료되었습니다.')

    elif selectedUpdateMenu == 3:
        print(f'{current_user}님, 수정하실 PHONE를 입력해주세요.')
        New_PHONE = input('New_UPhone: ')
        if member[current_user]['UPHONE'] == New_PHONE:
            print('기존과 동일한 전화번호입니다.')
        else:
            member[current_user]['UPHONE'] = New_PHONE
            print('변경이 완료되었습니다.')

    elif selectedUpdateMenu == 4:
        print(f'{current_user}님, 수정하실 PW, EMAIL, PHONE를 입력해주세요.')
        New_PW = input('New_Pw: ')
        New_EMAIL = input('New_Email: ')
        New_PHONE = input('New_Phone: ')

        if member[current_user]['UPW'] == New_PW:
            print('기존과 동일한 비밀번호가 포함되어 있어 수정을 취소합니다.')
            return

        if member[current_user]['UEMAIL'] == New_EMAIL:
            print('기존과 동일한 이메일이 포함되어 있어 수정을 취소합니다.')
            return

        if member[current_user]['UPHONE'] == New_PHONE:
            print('기존과 동일한 전화번호가 포함되어 있어 수정을 취소합니다.')
            return

        member[current_user]['UPW'] = New_PW
        member[current_user]['UEMAIL'] = New_EMAIL
        member[current_user]['UPHONE'] = New_PHONE
        
        print('---')
        print("[비밀번호, 이메일, 전화번호] 전체 변경이 완료되었습니다.")    
    else:
        print("잘못된 번호를 입력하셨습니다.")
>>>>>>> ba4b80c (재업)

def user_delete(member, current_user):
    if current_user is None :
        print('현재 로그인되어있지 않습니다.')
        return current_user
    else:
        password = f'{random.randint(0, 9999):04d}'
        print('탈퇴를 위해 패스워드를 입력받겠습니다. 아래에 나온 패스워드를 입력해주세요. ')
        print(f'Password: {password}')
        User_input = input('password: ')
        if User_input == password:
            del member[current_user]
            print('회원 탈퇴가 완료되었습니다. ')
            return None
        else:
            print('인증 번호가 일치하지 않아 탈퇴할 수 없습니다..')
<<<<<<< HEAD
            return current_user
=======
            return current_user
        
def print_all_members(member):
    if not member:
        print('등록된 회원이 없습니다.')
        return
    else:
        print('회원 전체 목록')
        print('\t===============================================================================================================')
        for uid in member:
            user_info = member[uid]
            print(f"[{user_info['UID']}] 님의 정보")
            print(f" - 비밀번호: {user_info['UPW']}")
            print(f" - 이메일: {user_info['UEMAIL']}")
            print(f" - 전화번호: {user_info['UPHONE']}")
            print('\t===============================================================================================================')
>>>>>>> ba4b80c (재업)
