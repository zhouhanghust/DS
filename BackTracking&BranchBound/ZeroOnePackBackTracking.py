# -- coding:utf-8 --


def backtrackZOP(w, v, c):
    n = len(w)
    x = [False] * n
    bestV = 0              # 最高价值
    curW = 0               # 当前物品重量
    curV = 0               # 当前物品价值
    bestx = None           # 最好x

    def backtrack(i):
        # i:开始位置
        # x:物品
        nonlocal bestV, curW, curV, x, bestx
        if i >= n:  # 边界条件
            if bestV < curV:
                bestV = curV
                bestx = x[:]    # 这种方式相当于copy，不会让bestx指向x
        else:  # 更新
            if curW + w[i] <= c:
                x[i] = True
                curW += w[i]
                curV += v[i]
                backtrack(i + 1)
                curW -= w[i]
                curV -= v[i]
            x[i] = False
            backtrack(i + 1)

    backtrack(0)
    return bestV,bestx


if __name__ == "__main__":
    c = 10
    w = [2, 2, 6, 5, 4]  # 每个物品重量
    v = [6, 3, 5, 4, 6]  # 每个物品价值
    bestV, bestx = backtrackZOP(w,v,c)
    print(bestV)
    print(bestx)










