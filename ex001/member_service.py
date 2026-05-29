from module_ex_001 import user_delete
from module_ex_001 import sign_up
from module_ex_001 import sign_in
from module_ex_001 import sign_out
from module_ex_001 import modify_profile
<<<<<<< HEAD
=======
from module_ex_001 import print_all_members
import config
>>>>>>> ba4b80c (재업)
member = {}
current_user = None

while True:
<<<<<<< HEAD
    print("\n--- 메뉴를 선택하세요 ---")
    try:
        selectedMenuNum = int(input('1.회원가입    2.로그인    3.로그아웃     4.회원 정보 수정    5. 회원 탈퇴, 99. 종료'))
    except ValueError:
        print("숫자만 입력 가능합니다.")
        continue
    if selectedMenuNum == 1:
        member = sign_up(member)
        

    elif selectedMenuNum == 2:
        current_user = sign_in(member)

    elif selectedMenuNum == 3:
        current_user = sign_out(current_user)

    elif selectedMenuNum == 4:
        modify_profile(member, current_user)


    elif selectedMenuNum == 5:
        current_user = user_delete(member, current_user)

    elif selectedMenuNum == 99:
        print('프로그램을 종료합니다.')
        break
    else:
        print("없는 메뉴입니다. 다시 선택해주세요.")
=======
    print("\n==============================")
    if current_user is None:
        print(f" 상태: 오프라인")
        print(" 1.회원가입  2.로그인, 6. 전체 회원 출력  99.종료")
    else:
        print(f" 상태: {current_user}님 로그인 중")
        print(" 3.로그아웃  4.회원 정보 수정  5.회원 탈퇴  99.종료")
    print("==============================")

    try:
        selectedMenuNum = int(input('원하시는 메뉴 번호를 입력하세요: '))
    except ValueError:
        print("숫자만 입력 가능합니다.")
        continue
    
    if current_user is None:
        if selectedMenuNum == config.SIGN_UP:
            sign_up(member)
        elif selectedMenuNum == config.SIGN_IN:
            sign_in(member)
        elif selectedMenuNum == config.PRINT_ALL_MEMBERS:
            print_all_members(member)
        elif selectedMenuNum == config.EXIT:
            print('프로그램을 종료합니다.')
            break
        else:
            print("로그인 전에는 이용할 수 없는 메뉴이거나 없는 번호입니다.")

    else:
        if selectedMenuNum == config.SIGN_OUT:
            sign_out(current_user)
        elif selectedMenuNum == config.MODIFY_PROFILE:
            modify_profile(member, current_user)
        elif selectedMenuNum == config.USER_DELETE:
            user_delete(member, current_user)
        elif selectedMenuNum == config.EXIT:
            print('프로그램을 종료합니다.')
            break
        else:
            print("로그인 중에는 이용할 수 없는 메뉴이거나 없는 번호입니다.")
>>>>>>> ba4b80c (재업)
