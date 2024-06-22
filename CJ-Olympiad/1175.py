inp=int(input())

bands=["mouse", "cow", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "chicken", "dog", "pig"]

#5: cow
#3: pig
band=inp%12

print(bands[band-4])