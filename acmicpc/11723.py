import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x)+"\n")
set_1=set()
for _ in range(int(input())):
    inp = input()
    if " " in inp:
        cmd, ctx = inp.split()
        ctx = int(ctx)
    else:
        cmd=inp
    if cmd == "add":
        set_1.add(ctx)
    elif cmd == "remove":
        if ctx in set_1:
            set_1.remove(ctx)
    elif cmd == "check":
        if ctx in set_1:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if ctx in set_1:
            set_1.remove(ctx)
        else:
            set_1.add(ctx)
    elif cmd == "all\n":
        set_1 = {i for i in range(1, 21)}
    elif cmd == "empty\n":
        set_1 = set()