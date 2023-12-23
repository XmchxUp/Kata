def v1():
    MAX_N = 1005

    N, V = map(int, input().split())

    volumes = [0] * MAX_N
    weights = [0] * MAX_N

    for i in range(1, N + 1):
        v, w = map(int, input().split())
        volumes[i] = v
        weights[i] = w
    dp = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            if j < volumes[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - volumes[i]] + weights[i])
    print(dp[N][V])

def v2():
    N, V = map(int, input().split())
    dp = [0] * (V + 1)

    for _ in range(N):
        v, w = map(int, input().split())
        for j in range(V, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + w)

    print(dp[V])
    pass
v2()
