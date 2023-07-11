import random

with open('spisok','r') as file:
    lines = random.sample(list(file), 2)
print(*map(str.strip, lines))


def password (line1: str , line2: str):
    word1 = line1.strip().title()
    word2 = line2.strip().title()
    #password = f'{word1}{word2}'    
    return word1, word2


def trypass(word1, word2):
    try:
        word1[3]
        word2[3]
        (word1+word2)[7]
        if len(word1+word2) > 10:
            1/0
    except(IndexError, ZeroDivisionError):
        print('Пароль не подходит, давай заново.')
    else: 
        print(f'Пароль такой: {word1}{word2}')
    return


if __name__=='__main__':
    word1, word2 = password(lines[0], lines[1])
    trypass(word1, word2)
