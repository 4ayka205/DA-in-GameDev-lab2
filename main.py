import gspread
import numpy as np
gc = gspread.service_account(filename='unitydatascience-438110-e40c83e26224.json')
sh = gc.open("UnitySheets")
hp = np.random.randint(0, 50, 11)
mon = list(range(1,11))
i = 0
while i <= len(mon):
    i += 1
    if i == 0:
        continue
    else:
        sh.sheet1.update(('A' + str(i)), str(i))
        sh.sheet1.update(('B' + str(i)), str(hp[i-1]))
        print(hp[i-1])