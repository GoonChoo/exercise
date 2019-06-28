

# 2
def ex_2():
    with open('INPUT.TXT') as i:
        s = i.readline()
        n = int(s.split()[0])
        if n > 0:
            sum_n = sum(range(n+1))
        else:
            sum_n = sum(range(1, n-1, -1))
        with open('OUTPUT.TXT', 'w') as o:
            o.write(str(sum_n))


# 3
def ex_3():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            for s in i:
                n = int(s.split()[0])
                o.write(str(n*n) + '\n')


def ex_35():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            n = int(i.readline().split()[0])
            for _ in range(n):
                s = i.readline().split()
                n = int(s[0])
                m = int(s[1])
                res = int(19*m + (n + 239)*(n + 366)/2)
                o.write(str(res) + '\n')



def ex_62():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()[0]
            row = int(n[1])
            index = ord(n[0]) - 64
            print(row, index)
            x = row % 2
            y = index % 2
            answer = ''
            if (x == 0 and y == 0) or (x > 0 and y > 0):
                answer = 'BLACK'
            elif (x > 0 and y == 0) or (x == 0 and y > 0):
                answer = 'WHITE'
            o.write(answer)


def ex_66():
    """
    p -> a
    l -> z
    m -> q
    112 -> 97
    108 -> 122
    109 -> 113
    """
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            c = s.split()[0]
            keyboard = 'qwertyuiopasdfghjklzxcvbnmq'
            o.write(keyboard[keyboard.find(c)+1])


def ex_149():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            i.readline()
            array = i.read().split()
            array.reverse()
            for c in array:
                o.write('{c} '.format(c=c))


def ex_324():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            if s[0] == s[3] and s[1] == s[2]:
                o.write('YES')
            else:
                o.write('NO')


def ex_529():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            n = i.readline().split()
            x1 = int(n[0])
            y1 = int(n[1])
            x2 = int(n[2])
            y2 = int(n[3])
            from math import sqrt
            o.write('{0:.5f}'.format(sqrt((x2-x1)**2 + (y2-y1)**2)))


# 561
def ex_561():
    with open('INPUT.TXT') as f_input:
        f_input.readline()
        towers = []
        for n in f_input:
            towers.append([int(x) for x in n.split()])
        towers_value = []
        for tower in towers:
            towers_value.append(get_tower_value(tower[1:]))
            print(towers_value[-1])


def get_tower_value(tower: list)->int:
    base = tower[0]
    return pow(base, get_pow_from_tower(tower[1:]))


def get_pow_from_tower(tower_pows: list)->int:
    if not len(tower_pows):
        return 1
    if len(tower_pows) == 1:
        return tower_pows[0]
    else:
        return pow(tower_pows[0], get_pow_from_tower(tower_pows[1:]))
# 561


def ex_597():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            r1 = int(n[0])
            r2 = int(n[1])
            r3 = int(n[2])
            if r1 >= (r2 + r3):
                o.write('YES')
            else:
                o.write('NO')


# 678
def ex_678():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            state_1 = 1
            state_2 = 0
            state_3 = 0
            for c in s:
                if c == 'A':
                    state_1, state_2 = state_2, state_1
                elif c == 'B':
                    state_3, state_2 = state_2, state_3
                elif c == 'C':
                    state_1, state_3 = state_3, state_1
            answer = 0
            if state_1:
                answer = '1'
            elif state_2:
                answer = '2'
            elif state_3:
                answer = '3'
            o.write(answer)
# 678


def ex_685():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            a = [int(x) for x in n[0:3]]
            b = [int(x) for x in n[3:6]]
            a.sort()
            b.sort()
            res = sum([x*y for x, y in zip(a, b)])
            o.write(str(res))


def ex_697():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            n = i.read().split()
            l = int(n[0])
            w = int(n[1])
            h = int(n[2])
            from math import ceil
            r = ceil((2*l*h + 2*w*h)/16)
            o.write(str(r))


def ex_756():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            a = int(n[0]) - 1
            b = int(n[1]) - 1
            o.write(str(a*b))


def ex_757():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            c = int(n[0]) // 2
            h = int(n[1]) // 6
            ox = int(n[2])
            o.write(str(min(c, h, ox)))


def ex_777():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            n = i.readline().split()
            s = int(n[0]) - 1
            t = int(n[1]) - 1
            if s > t:
                res = (12 - s) + t
            else:
                res = t - s
            o.write(str(res))


def ex_819():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            a = int(n[0])
            b = int(n[1])
            c = int(n[2])
            s = 2*(a*b) + 2*(a*c) + 2*(b*c)
            v = a*b*c
            o.write(str(s) + ' ' + str(v))


def ex_854():
    from enum import Enum

    class ConditionerState(Enum):
        freeze = 1
        heat = 2
        auto = 3
        fan = 4

    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            n = i.readline().split()
            t_room = n[0]
            t_cond = n[1]
            state = ConditionerState[i.readline()]
            if state == freeze:



def ex_892():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            month = int(n[0])
            if month < 1 or month > 12:
                o.write('Error')
                return
            if 1 <= month <= 2 or month == 12:
                o.write('Winter')
            elif 3 <= month <= 5:
                o.write('Spring')
            elif 6 <= month <= 8:
                o.write('Summer')
            elif 9 <= month <= 11:
                o.write('Autumn')


# 907
def ex_907():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            w = int(n[0])
            h = int(n[1])
            r = int(n[2])
            if r*2 > w or r*2 > h:
                o.write('NO')
            else:
                o.write('YES')
# 907


# 929
def ex_929_tests():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            for s in i:
                n = int(s.split()[0])
                x = n // 6
                y = n % 6
                if y:
                    y = 7 - y
                min_sum = x + y
                o.write(str(n) + ' -> ' + str(min_sum) + ' ' + str(n * 6) + '\n')


# 970
def ex_970():
    with open('INPUT.TXT') as i:
        with open('OUTPUT.TXT', 'w') as o:
            s = i.readline()
            n = s.split()
            a1 = int(n[0])
            a2 = int(n[1])
            a3 = int(n[2])
            if (a1 + a2 == a3) or (a3 + a2 == a1) or (a1 + a3 == a2):
                o.write('YES')
            else:
                o.write('NO')
# 970


# зепуск тестов, в одном файле все тестовые данные, разделенные новой строкой
def start(func, sep):
    with open('INPUT_TEST.TXT') as i:
        with open('OUTPUT_TEST.TXT', 'w') as o:
            text = i.read()
            tests = text.split(sep)
            for ts in tests:
                ts = ts.strip()
                if len(ts) == 0:
                    continue
                with open('INPUT.TXT', 'w') as input_file:
                    input_file.write(ts)
                func()
                with open('OUTPUT.TXT') as output_file:
                    a = output_file.read()
                    o.write(a + '\n')


if __name__ == '__main__':
    start(ex_854, ';')
