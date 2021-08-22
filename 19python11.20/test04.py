# P151 5.7
count = 1


def hanoi(n, stp, dst, mid):
    global count
    if n == 1:
        print(f"第{count}步:{1}环从 {stp} 杆移动到 {dst}")
        count += 1
    else:
        hanoi(n - 1, stp, mid, dst)
        print(f"第{count}步:{n}换从 {stp} 杆移动到 {dst}")
        count += 1
        hanoi(n - 1, mid, dst, stp)


hanoi(3, 'A', 'C', 'B')
