import sys

N = int(sys.stdin.readline())
que = []

for _ in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push':
        que.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(que) >= 1:
            print(que.pop(0))
        else:
            print("-1")

    elif cmd[0] == 'size':
        print(len(que))

    elif cmd[0] == 'empty':
        if len(que) == 0:
            print("1")
        else:
            print("0")

    elif cmd[0] == 'front':
        if len(que) == 0:
            print("-1")
        else:
            print(que[0])

    elif cmd[0] == 'back':
        if len(que) == 0:
            print("-1")
        else:
            print(que[len(que)-1])