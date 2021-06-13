# import sys
# sys.stdin = open('input/조이스틱.txt', 'r')

DICT = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9,
        'K': 10,'L': 11,'M': 12,'N': 13,'O': 12,'P': 11,'Q': 10,'R': 9,'S': 8,'T': 7,
        'U': 6,'V': 5,'W': 4,'X': 3,'Y': 2,'Z': 1}

def solution(name):
    name.strip('"')
    name = list(name)
    result = DICT.get(name.pop(0))
    if name:
        name = name[::-1] if name[0] == 'A' else name
        for i in name:
            result += DICT.get(i) + 1

        return result
    else:
        return result


print(solution("AZAAAZ"))