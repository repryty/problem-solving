#입력값 x 출력값 x

def hello():
    print("HI!")

#입력값 1 출력값 x

def hallo(name="park"):
    print(f"안녕! {name}")

#입력값 2 출력값 x

def hola(name1, name2):
    print(f"아녕! {name1}, 그리고 {name2}")

#입력값 2 출력값 o

def 덧셈(num1, num2):
    return num1+num2

def 뺄셈(num1, num2):
    return num1-num2

def 곱셈(num1, num2):
    return num1*num2

def 나눗셈(num1, num2):
    return num1/num2

def is_prime(n):
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

def password(n):
    source = "abcdefghijklmnopqrstuvwxyzaÂĂćåÃÅċʤĖÉʣʥʥɘɤɧʮĪ1234567890-`~+_/!@#$%^&*()=젉곏됎렭펿녨햵휽헑萬國高櫻李崔九野㕧䐖고양이와그옆의강아지는말했다왜냐하면요것은태스트이자뻘지시기때무내"
    end=""
    import random
    for i in range(n):
        locate = random.randrange(len(source)) #위치확인
        end+=source[locate]
    return end
