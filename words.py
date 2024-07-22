text="""配(나눌 배)	信(믿을 신)	思(생각할 사)	遠(멀 원)	近(가까울 근)	強(강할 강)	卷(책 권)
雪(눈 설)	盛(왕성할 성)	螢(반딧불 형)	以(로서 이)	油(기름 유)	常(항상 상)	書 (글 서)
晝(낮 주)	寢(잘 침)	蛇(뱀 사)	旁(곁 방)	惶(두려울 황)	引(끌 인)	午(낮 오)
而(-하고 이)	捕(잡을 포)	擲(던질 척)	腹(배 복)	稍(조금 초)	優(나을 우)	壬(임)
沙(모래 사)	可(옳을 가)	命(목숨 명)	立(설 립)	名(이름 명)		
"""

import re

def separate_english_korean(text):
    # 결과를 저장할 두 개의 리스트
    english_words = []
    korean_words = []
    
    # 줄바꿈을 기준으로 문자열을 분리하여 각 줄을 처리
    lines = text.split('\n')
    for line in lines:
        Regular
        # 정규 표현식을 사용하여 영어 부분과 한국어 부분을 구분
        match = re.sub(r'\(([^)]+)\)', line, '')
        # if match:
        #     english, korean = match.groups()
        #     english_words.append(english.strip())
        #     korean_words.append(korean.strip())

    
    # return english_words, korean_words

print(re.sub(r'\(([^)]+)\)', '', text))
# english_words, korean_words = separate_english_korean(text)

# file = open('words.txt', 'w')
# content=""
# for i in range(len(english_words)):
#     content+=english_words[i]+"\t"+korean_words[i]+'\n'
# file.write(content)