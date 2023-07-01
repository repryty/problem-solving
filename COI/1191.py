howmuch = input()
food = 0
other = 0
for i in range(int(howmuch)):
    inp = input().split()
    if inp[0] == "0":
        food += int(inp[1])
    other += int(inp[1])
end1 = food / other
end = end1 * 100
print("%.2f" % end)
