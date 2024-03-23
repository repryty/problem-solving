N,K=map(int, input().split())
queue=list(range(1, N+1))

end=[]
while len(queue)>0:
    for i in range(K):
        queue.append(queue.pop(0))
    end.append(str(queue.pop()))
print("<"+", ".join(end)+">")