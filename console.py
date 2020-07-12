import math
from hashlib import sha256
from multiprocessing import Pool
from pprint import pprint 

PASSWORD_SALT = "NeverChangeIt:)"
cores = 4
pk = "d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e"

wordlist = open("/usr/share/wordlists/rockyou.txt", "r",  encoding="utf-8", errors='ignore').readlines()

def pwd_find(start, end):
    for word_inx in range(start, end):
        password = wordlist[word_inx].strip()
        tmp = sha256(f'{password}{PASSWORD_SALT}'.encode()).hexdigest()
        cand_pk = sha256(f'10.255.0.2{tmp}'.encode()).hexdigest()

        if cand_pk == pk:
            print(password)
            p.terminate()
            p.join()
        else:
            pass


break_points = []

for i in range(cores):
    break_points.append({"start": math.ceil(len(wordlist)/cores * i), "end": math.ceil(len(wordlist)/cores * (i + 1))})


if __name__ == "__main__":
    p = Pool(cores)
    for i in break_points:
        a = p.apply_async(pwd_find, kwds=i, args=tuple())
    print("Done!")
    p.close()
    p.join()







