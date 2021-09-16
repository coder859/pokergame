import copy
from itertools import combinations


def decks(m, c):
    # Makes all possible hands

    a = list(m + c)
    d = []
    z = combinations(a, 5)
    for x in z:
        d.append(list(x))
    return d


def royal_flush(d):
    hand = []
    for x in d:
        x.sort()
        if x[0] % 20 == 10 and x[1] % 20 == 11 and x[2] % 20 == 12 and x[3] % 20 == 13 and x[4] % 20 == 14 \
                and int(x[0] / 20) == int(x[1] / 20) == int(x[2] / 20) == int(x[3] / 20) == int(x[4] / 20):
            hand = x
        else:
            continue
    if hand:
        return hand
    return False


def k4(d):
    b = []
    b1 = {}
    for x in d:
        for y in x:
            if y % 20 not in b1:
                b1[y % 20] = [y]
            else:
                if y not in b1[y % 20]:
                    b1[y % 20].append(y)
        if b1 not in b:
            b.append(copy.copy(b1))
        b1.clear()
    a = {}
    quad = []
    kind4 = []
    i = []
    for x in d:
        single = False
        for y in x:
            if y % 20 not in a:
                a[y % 20] = 1
            else:
                a[y % 20] += 1
        for y in a:
            if a[y] == 4:
                kind4.append(y)
                kind4.append(y)
                kind4.append(y)
                kind4.append(y)
            else:
                if not single:
                    single = True
                    i.append(y)
        if len(kind4 + i) == 5:
            quad.append(kind4 + i)
        kind4.clear()
        i.clear()
        a.clear()

    if len(quad) > 1:
        big = quad[0]
        flag = False
        for c in range(0, 5):
            for y in quad:
                if len(quad) == 1:
                    break
                if y[c] > big[c]:
                    big = y
                    if len(quad) == 1:
                        break
                elif y[c] < big[c]:
                    flag = True
                    if len(quad) == 1:
                        break
                else:
                    continue
                if not flag:
                    break
        a1 = {}
        count = 0
        target = {}
        big_counted = False
        for x in big:
            break
        x1 = big[-1]
        for y in b:
            if x in y and len(y[x]) == 4:
                g = y.get(x1)
                if g and len(y[x1]) == 1:
                    target = copy.copy(y)
                    break
                else:
                    continue
        hand = []
        while len(hand) != 5:
            for x in target:
                if len(target[x]) == 4:
                    hand = hand + target[x]
                    big_counted = True
                else:
                    if big_counted:
                        hand.append(x)
                        break
        return hand

    else:
        return False


def k3(d):
    b = []
    b1 = {}
    for x in d:
        for y in x:
            if y % 20 not in b1:
                b1[y % 20] = [y]
            else:
                if y not in b1[y % 20]:
                    b1[y % 20].append(y)
        if b1 not in b:
            b.append(copy.copy(b1))
        b1.clear()
    a = {}
    triple = []
    kind3 = []
    i = []
    for x in d:
        for y in x:
            if y % 20 not in a:
                a[y % 20] = 1
            else:
                a[y % 20] += 1
        if len(a) == 3:
            for y in a:
                if a[y] == 3:
                    kind3.append(y)
                    kind3.append(y)
                    kind3.append(y)
                elif a[y] == 1:
                    i.append(y)
        else:
            continue
        i.sort()
        if len(kind3 + i) == 5:
            triple.append(kind3 + i)
        kind3.clear()
        i.clear()
        a.clear()

    if len(triple) > 1:
        big = triple[0]
        flag = False
        for c in range(0, 5):
            for y in triple:
                if len(triple) == 1:
                    break
                if y[c] > big[c]:
                    big = y
                    if len(triple) == 1:
                        break
                elif y[c] < big[c]:
                    flag = True
                    if len(triple) == 1:
                        break
                else:
                    continue
                if not flag:
                    break
        a1 = {}
        count = 0
        target = {}
        big_counted = False
        for x in big:
            if x not in a1:
                a1[x] = 1
            else:
                a1[x] += 1
        for x in a1:
            count += 1
            for y in b:
                if x in y:
                    if count == 1:
                        if len(y[x]) == 3:
                            target = copy.copy(y)
    else:
        return False


def pair(d):
    p = []
    p1 = []
    i = []
    a = {}
    for x in d:
        single = False
        for y in x:
            if y % 20 not in a:
                a[y % 20] = 1
            else:
                a[y % 20] += 1
        for y in a:
            if y == 2:
                if not single:
                    single = True
                    p1.append(y)
                    p1.append(y)
            elif y == 1:
                i.append(y)
        i.sort()
        if len(p1 + i) == 5:
            p.append(p1 + i)
        p1.clear()
        i.clear()
        a.clear()

    if len(p) == 1:
        return p
    elif len(p) > 1:
        big = p[0]
        while len(p) != 1:
            for c in range(0, 5):
                for y in p:
                    if y == big:
                        continue
                    if y[c] > big[c]:
                        big = y
                        p.remove(y)
                    elif y[c] < big[c]:
                        p.remove(y)
        return big
    else:
        return False


def flush(d):
    a = []
    for x in d:
        if int(x[0] / 20) == int(x[1] / 20) == int(x[2] / 20) == int(x[3] / 20) == int(x[4] / 20):
            a.append(x)
    if len(a) == 1:
        return (x for x in a)
    elif len(a) > 1:
        big = a[0]
        big.sort(reverse=True)
        for c in range(0, 5):
            for y in a:
                y.sort(reverse=True)
                if y == big:
                    continue
                if y[c] > big[c]:
                    big = y
                    a.remove(y)
                elif y[c] < big[c]:
                    a.remove(y)
        return big
    else:
        return False


def straight(d):
    a = []
    b = 0
    for x in d:
        for y in x:
            x[x.index(y)] = y % 20
        x.sort()
        if x[0] % 20 == x[1] % 20 - 1 == x[2] % 20 - 2 == x[3] % 20 - 3 == x[4] % 20 - 4 or x == [2, 3, 4, 5, 14]:
            a.append(x)
            continue

    for x in a:
        if x[0] > b:
            b = x[0]
    for x in a:
        if x[0] == b:
            return x
    return False


def full_house(d):
    b = []
    b1 = {}
    for x in d:
        for y in x:
            if y % 20 not in b1:
                b1[y % 20] = [y]
            else:
                if y not in b1[y % 20]:
                    b1[y % 20].append(y)
        if b1 not in b:
            b.append(copy.copy(b1))
        b1.clear()
    a = {}
    full = []
    kind3 = []
    double = []
    for x in d:
        for y in x:
            if y % 20 not in a:
                a[y % 20] = 1
            else:
                a[y % 20] += 1
        for y in a:
            if a[y] == 3:
                kind3.append(y)
                kind3.append(y)
                kind3.append(y)
            elif a[y] == 2:
                double.append(y)
                double.append(y)
        if len(kind3 + double) == 5:
            full.append(kind3 + double)
        kind3.clear()
        double.clear()
        a.clear()

    if len(full) == 1:
        for x in full:
            break
        t = []
        hand = []
        for y in b:
            if len(y) != 2:
                continue
            else:
                t.append(y)
        for x in t:
            t[t.index(x)] = dict(reversed(list(x.items())))
            break
        for y in x:
            hand += x[y]
        return hand

    elif len(full) > 1:
        big = full[0]
        flag = False
        for c in range(0, 5):
            for y in full:
                if len(full) == 1:
                    break
                if y[c] > big[c]:
                    big = y
                elif y[c] < big[c]:
                    flag = True
                else:
                    continue
                if not flag:
                    break
        t = []
        for y in b:
            if len(y) != 2:
                continue
            else:
                t.append(y)
        hand = []
        flag = False
        for big in t:
            if True:
                break
        for x in t:
            t[t.index(x)] = dict(reversed(list(x.items())))
        for y in t:
            for h in big:
                for h1 in y:
                    if h1 > h:
                        big = copy.copy(y)
                        flag = True
                    break
        for x in big:
            hand += big[x]
        return hand
    else:
        return False


def tp(d):
    a = {}
    p2 = []
    p = []
    i = []
    for x in d:
        single = False
        for y in x:
            if y % 20 not in a:
                a[y % 20] = 1
            else:
                a[y % 20] += 1
        if len(a) == 3:
            for z in a:
                if a[z] == 2:
                    p.append(z)
                    p.append(z)
                if a[z] == 1:
                    if not single:
                        single = True
                        i.append(z)
        p.sort(reverse=True)
        if len(p + i) == 5:
            p2.append(p + i)
        p.clear()
        i.clear()
        a.clear()
    if len(p2) == 1:
        return [x for x in p2]
    elif len(p2) > 1:
        big = p2[0]
        while len(p2) != 1:
            for c in range(0, 5):
                for y in p2:
                    if y[c] == big[c]:
                        continue
                    if y[c] > big[c]:
                        big = y
                        p2.remove(y)
                    elif y[c] < big[c]:
                        p2.remove(y)
                        if len(p2) == 1:
                            return big
        return big
    else:
        return False


def straight_flush(d):
    s = []
    for x in d:
        if int(x[0] / 20) == int(x[1] / 20) == int(x[2] / 20) == int(x[3] / 20) == int(x[4] / 20) and \
                x[0] % 20 == x[1] % 20 - 1 == x[2] % 20 - 2 == x[3] % 20 - 3 == x[4] % 20 - 4 or x == [2, 3, 4, 5,
                                                                                                       14]:
            s.append(x)
    if len(s) == 1:
        return [x for x in s]
    elif len(s) > 1:
        big = s[0]
        big.sort(reverse=True)
        for c in range(0, 5):
            for y in s:
                y.sort(reverse=True)
                if y == big:
                    continue
                if y[c] > big[c]:
                    big = y
                    s.remove(y)
                elif y[c] < big[c]:
                    s.remove(y)
        return big
    else:
        return False


def high_card(d):
    big = d[0]
    big.sort(reverse=True)
    for c in range(0, 5):
        for x in d:
            x.sort(reverse=True)
            if x == big:
                continue
            if x[c] > big[c]:
                big = x
                d.remove(x)
            elif x[c] < big[c]:
                d.remove(x)
    return big


def compare(c):
    h = []
    hand = []
    players = []
    h1 = []
    hand1 = []
    breaker = False
    for x in c:
        players.append(x[0])
        hand.append(x[1])
        h.append(x[2])

    for x1 in h:
        for y1 in x1:
            hand1.append(y1 % 20)
        hand1x = copy.copy(hand1)
        h1.append(hand1x)
        hand1.clear()

    big = h1[0]
    for count in range(0, 5):
        for y in h1:
            if y[count] > big[count]:
                if len(h1) == 2:
                    big = y
                    breaker = True
                    break
        if breaker:
            break
    i = h[h1.index(big)]
    for x in c:
        if x[2] != i:
            c.remove(x)
    return c


l = []
t = []
a = {}
m = 0
m1 = []
hands = {1: "High Card", 2: "Pair", 3: "Two Pair", 4: "Three of a Kind", 5: "Straight", 6: "Flush", 7: "Full House",
         8: "Four of a Kind", 9: "Straight Flush", 10: "Royal Flush"}
cards = {2: "S2", 3: "S3", 4: "S4", 5: "S5", 6: "S6", 7: "S7", 8: "S8", 9: "S9", 10: "S10", 11: "SJ", 12: "SQ",
         13: "SK", 14: "SA",
         22: "C2", 23: "C3", 24: "C4", 25: "C5", 26: "C6", 27: "C7", 28: "C8", 29: "C9", 30: "C10", 31: "CJ", 32: "CQ",
         33: "CK", 34: "CA",
         42: "H2", 43: "H3", 44: "H4", 45: "H5", 46: "H6", 47: "H7", 48: "H8", 49: "H9", 50: "H10", 51: "HJ", 52: "HQ",
         53: "HK", 54: "HA",
         62: "D2", 63: "D3", 64: "D4", 65: "D5", 66: "D6", 67: "D7", 68: "D8", 69: "D9", 70: "D10", 71: "DJ", 72: "DQ",
         73: "DK", 74: "DA"}
CompareHands = []
# individual cards, ordered by the player:
card_groups = [[63, 43], [25, 45]]
# cards on the table:
common = [42, 65, 23, 2, 5]
# [3, 3], [5, 5]
# [2, 14, 3, 2, 5]

# makes the player id, hand type, and hand.
for x in card_groups:
    d = decks(x, common)
    t.append(card_groups.index(x) + 1)
    if royal_flush(d):
        t.append(10)
        t.append(royal_flush(d))
    else:
        if straight_flush(d):
            t.append(9)
            t.append(straight_flush(d))
        else:
            if k4(d):
                t.append(8)
                t.append(k4(d))
            else:
                if full_house(d):
                    t.append(7)
                    t.append(full_house(d))
                else:
                    if flush(d):
                        t.append(6)
                        t.append(flush(d))
                    else:
                        if straight(d):
                            t.append(5)
                            t.append(straight(d))
                        else:
                            if k3(d):
                                t.append(4)
                                t.append(k3(d))
                            else:
                                if tp(d):
                                    t.append(3)
                                    t.append(tp(d))
                                else:
                                    if pair(d):
                                        t.append(2)
                                        t.append(pair(d))
                                    else:
                                        t.append(1)
                                        t.append(high_card(d))
    t1 = copy.deepcopy(t)
    l.append(t1)
    t.clear()

for x in l:
    a[x[0]] = x[1]

for x in l:
    for y in x:
        if x.index(y) == 1:
            if y < m:
                l.remove(x)

if len(l) == 1:
    print(
        f"The winner is Player {str(l[0][0])}! His hand was a {str(hands[l[0][1]])}. His actual hand was {str(l[0][2])}.")
else:
    for x in l:
        CompareHands.append(x)
    c = compare(CompareHands)
    print(f"The winner(s) are {str(c)[1:-1]}!")