# https://programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    round_time = list()
    city_num = len(t)
    city_count = [[0, 0] for _ in range(city_num)]
    this_time = 0
    next_time = 1
    total_gold = total_siver = 0
    for x in t:
        round_time.append(x * 2)

    while True:
        this_time += next_time

        for x in range(city_num):
            t[x] += next_time
            if t[x] == round_time[x]:
                t[x] = 0
                city_count[x][0] += 1
                if g[x] >= w[x]:
                    total_gold += w[x]
                    g[x] -= w[x]
                else:
                    total_gold += g[x]
                    g[x] = 0
                    if w[x] - g[x] < s[x]:
                        total_siver += (w[x] - g[x])
                        s[x] -= (w[x] - g[x])
                    else:
                        total_siver += s[x]
                        s[x] = 0

                if total_gold > a:
                    remain_gold = total_gold - a
                    for y in range(len(city_count)):
                        if city_count[y][1] != 0 and s[y] != 0:
                            if remain_gold < city_count[y][1] and s[y] >= remain_gold:
                                total_gold -= remain_gold
                                total_siver += remain_gold
                                s[y] -= remain_gold
                                city_count[y][1] -= remain_gold
                                g[y] += remain_gold
                                remain_gold = 0
                            elif remain_gold >= city_count[y][1] and s[y] >= city_count[y][1]:
                                total_gold -= city_count[y][1]
                                total_siver += city_count[y][1]
                                remain_gold -= city_count[y][1]
                                s[y] -= city_count[y][1]
                                g[y] += city_count[y][1]
                                city_count[y][1] = 0
                                city_count[y][0] -= 1
                            elif city_count[y][1] > remain_gold > s[y]:
                                total_gold -= s[y]
                                total_siver += s[y]
                                remain_gold -= s[y]
                                city_count[y][1] -= s[y]
                                g[y] += s[y]
                                s[y] = 0
                            elif remain_gold >= city_count[y][1] and s[y] < remain_gold:
                                if city_count[y][1] <= s[y]:
                                    total_gold -= city_count[y][1]
                                    total_siver += city_count[y][1]
                                    remain_gold -= city_count[y][1]
                                    s[y] -= city_count[y][1]
                                    g[y] += city_count[y][1]
                                    city_count[y][1] = 0
                                    city_count[y][0] -= 1
                                else:
                                    total_gold -= s[y]
                                    total_siver += s[y]
                                    remain_gold -= s[y]
                                    city_count[y][1] -= s[y]
                                    g[y] += s[y]
                                    s[y] = 0

                        if city_count[y][0] != 0 and s[y] != 0:
                            if remain_gold < w[y] and remain_gold < s[y]:
                                total_gold -= remain_gold
                                total_siver += remain_gold
                                s[y] -= remain_gold
                                g[y] += remain_gold
                                city_count[y][1] = w[y] - remain_gold
                            elif remain_gold > w[y] and s[y] >= w[y]:
                                total_gold -= w[y]
                                total_siver += w[y]
                                s[y] -= w[y]
                                g[y] += w[y]
                                city_count[y][0] -= 1
                            elif remain_gold > w[y] > s[y]:
                                total_gold -= s[y]
                                total_siver += s[y]
                                city_count[y][1] = w[y] - s[y]
                                g[y] += s[y]
                                s[y] = 0
                            elif w[y] > remain_gold > s[y]:
                                total_gold -= s[y]
                                total_siver += s[y]
                                city_count[y][1] = w[y] - s[y]
                                g[y] += s[y]
                                s[y] = 0

        if (total_gold >= a and total_siver >= b): break

    return this_time