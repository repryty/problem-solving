from PIL import Image, ImageDraw, ImageFont
import textwrap

# 이후 사용 편의를 위하여 함수 형태로 만들었습니다.
def make_image(message):

    # Image size
    W = 640
    H = 640
    bg_color = 'rgb(214, 230, 245)' # 아이소프트존
    
    # font setting
    font = ImageFont.truetype('NanumSquareRoundR.ttf', size=28)
    font_color = 'rgb(0, 0, 0)' # or just 'black'
		# 원래 윈도우에 설치된 폰트는 아래와 같이 사용 가능하나,
		# 아무리 해도 한글 폰트가 사용이 안 되어.. 같은 폴더에 다운받아 놓고 사용함.
		# font = ImageFont.truetype("arial.ttf", size=28)
    
    image =Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)
    
    # Text wraper to handle long text
	# 40자를 넘어갈 경우 여러 줄로 나눔
    lines = textwrap.wrap(message, width=40)
  
    # start position for text
    x_text = 50
    y_text = 50
    
    # 각 줄의 내용을 적음
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height
        # height는 글씨의 높이로, 한 줄 적고 나서 height만큼 아래에 다음 줄을 적음
        
    # 안에 적은 내용을 파일 이름으로 저장
    image.save('{}.png'.format(message))
    
# 실행
make_image("I like!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11") 