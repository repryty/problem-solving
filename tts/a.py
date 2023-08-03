# pip install gtts
from gtts import gTTS
말 = "안녕하세요"
말 = gTTS(text=말, lang="ko")
파일이름 = "a.mp3"
말.save(파일이름)

import playsound
playsound.playsound("a.mp3")

# pip install playsound==1.2.2
