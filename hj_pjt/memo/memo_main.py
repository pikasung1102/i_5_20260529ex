import memo_config
import memo_DB
from datetime import datetime
import memo_read_config
from memo_service import MemoService
from memo_dumy import memoDummyInit

flag = True

if memo_config.DEV_MOD:
    memoDummyInit()

memoService = MemoService(memo_DB.userMemoList)

while flag:
    selectedMenuNum = int(input('1.작성 2.조회 3.수정 4.삭제 99.종료 '))
    
    if selectedMenuNum == memo_config.MEMO_WRITE:
        userMemo = input('메모하실 내용을 입력하세요. ')
        
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        memoInfo = {
            '작성시간': now,
            '메모내용': userMemo
        }
        memo_DB.userMemoList.append(memoInfo)

        print('메모가 저장되었습니다.')

    elif selectedMenuNum == memo_config.MEMO_READ:
        print('---------------------메모 조회 선택 메뉴---------------------')
        memoReadMenuNum = int(input('menu: 1.최신순 조회     2.오래된순 조회     3.월별 조회 '))

        if memoReadMenuNum == memo_read_config.MEMO_READ_LATEST:
           memoService.readLatest()

        elif memoReadMenuNum == memo_read_config.MEMO_READ_OLDEST:
            memoService.readOldest()

        elif memoReadMenuNum == memo_read_config.MEMO_READ_MONTH:
            memoService.readMonth()
           
    elif selectedMenuNum == memo_config.MEMO_UPDATE:
        memoService.showMemoList()

        modifyNum = int(input('수정할 메모 번호 입력: '))
        newMemo = input('새로운 메모 입력: ')

        memoService.modifyMemo(modifyNum, newMemo)

        print('메모 수정이 완료되었습니다')
        
    elif selectedMenuNum == memo_config.MEMO_DELETE:
        memoService.showMemoList()

        deleteNum = int(input('삭제할 메모 번호 입력: '))

        deletedMemo = memoService.deleteMemo(deleteNum)
        
        print(f'{deletedMemo} 메모가 삭제되었습니다.')

    elif selectedMenuNum == memo_config.MEMO_EXIT:
        print('종료합니다.')
        flag = False
