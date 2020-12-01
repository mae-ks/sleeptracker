from sleeptrack import *

def randomizer(file1, file2):
    emo = []
    hoursss = []
    if get_filesize(file2) != 0:
        with open(file2, 'w') as _:
            pass
    for _ in emodays.keys():
        with open(file1, 'a') as txt:
            hour = random.randint(1, 10)
            em = emotion(hour, markov)
            emo.append(em)
            hoursss.append(hour)
            txt.write(str(hour) + ' ' + str(em) + '\n')
    i = 0
    with open(file2, 'a') as txt:
        for key, val in emodays.items():
            e = emo[i]
            h = hoursss[i]
            val = int(e) * '#'
            i += 1
            txt.write(key + ' : ' + val + ' ' + str(h) + ' hr\n')

randomizer('maindat.txt', 'emodays.txt')