inp=[None]*3
last_num=[]
for i in range(3):
    input_str=input()
    try:
        inp[i]=int(input_str)
        last_num=[inp[i], i]
    except:
        pass
all_num=[0]*3
for i in range(3):
    all_num[i]=last_num[0]+(i-last_num[1])
end=all_num[2]+1
if end%3==0 and end%5==0:
    print("FizzBuzz")
elif end%3==0:
    print("Fizz")
elif end%5==0:
    print("Buzz")
else:
    print(end)