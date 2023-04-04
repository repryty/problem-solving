### 연락처 관리 프로그램 ###

import time
menu=0
friends=["김김김", "박박박", "무열왕","카이저 빌헬름 II"]
while menu!=9:
    time.sleep(0.7)
    print("============================")
    time.sleep(0.1)
    print("1. 친구 목록 출력")
    time.sleep(0.1)
    print("2. 친구 추가") #append
    time.sleep(0.1)
    print("3. 친구 삭제") #remove
    time.sleep(0.1)
    print("4. 친구 이름 변경") # = tkdyd
    time.sleep(0.1)
    print("9. 종료")
    time.sleep(0.2)
    
    menu= int(input(">> "))
    if menu == 1:
        time.sleep(0.5)
        for i in range(len(friends)):
            print(f"{i+1}. {friends[i]}")
            time.sleep(0.1)
        print(".\n.")
    elif menu==2:
        time.sleep(0.2)
        new_friend=input("이름을 입력하시오: \n>> ")
        friends.append(new_friend)
        time.sleep(0.3)
        print("성공적으로 처리되었습니다\n")
    elif menu==3:
        time.sleep(0.1)
        del_friend=input("삭제할 대상을 입력하시오:\n>> ")
        time.sleep(0.3)
        if del_friend in friends: friends.remove(del_friend)
        else: 
            time.sleep(0.8)
            print("문제가 발생했습니다.")
        print("성공적으로 처리되었습니다.")
    elif menu==4:
        time.sleep(0.05)
        newname=input("변경할 이름을 입력하시오:\n>> ")
        time.sleep(0.2)
        target=input("변경할 대상을 지정하시오:\n>> ")
        time.sleep(0.4)
        if target in friends: friends[friends.index(target)]=newname
        else: 
            time.sleep(0.8)
            print("문제가 발생했습니다.")
        print("성공적으로 처리되었습니다")
    elif menu==9:
        break