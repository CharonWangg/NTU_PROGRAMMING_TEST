from skimage import measure
import numpy as np
import itertools
import queue
import pandas as pd

#1.

# B R B R B
# R B R B R
# B R B R B
# R B R B R
# B R B R B

#2.
def evaluation(grid):
    totalPenalty = []
    (label_image,num) = measure.label(grid,connectivity=1,return_num=True)
    bbox = measure.regionprops(label_image)
    penalty = []
    #print(np.max(label_image))
    for i in range(num):
        area = bbox[i].area
        if area > 1:
            penalty.append(area)
    totalPenalty.append(sum(penalty))
    # for i in range(1,6):
    #     temp = np.copy(grid)
    #     temp[temp!=i] = 0
    #     #temp[temp==i] = 1
    #     label_image = measure.label(temp, connectivity=1)
    #     bbox = measure.regionprops(label_image)
    #     penalty = []
    #     #print(np.max(label_image))
    #     for i in range(np.max(label_image)):
    #         area = bbox[i].area
    #         penalty.append(area)
    #     totalPenalty.append(sum(penalty))
    return sum(totalPenalty)


num = {}
num['red'] = 139
num['blue'] = 1451
num['green'] = 977
num['white'] = 1072
num['yellow'] = 457

bead = {'red':1,'blue':2,'green':3,'white':4,'yellow':5}

colorList = []
for i in itertools.permutations(['red','blue','green','white','yellow'],5):
    colorList.append([i])

grid = np.zeros((64,64))
allGrid = {}
res = {}
for id,L in enumerate(colorList):
    L = L[0]
    Q = queue.Queue()
    color1 = L[0]
    color2 = L[1]
    Q.put(L[2])
    Q.put(L[3])
    Q.put(L[4])
    flag = 0
    grid = np.zeros((64, 64))

    for i in range(64):
        for j in range(64):
            #print((i+1)*(j+1))
            if (i+1)%2:
                if (64*(i)+j+1)%2 == 1 or flag == 1:
                    grid[i, j] = bead[color1]
                    num[color1] = num[color1] - 1
                    if num[color1] == 0:
                        try:
                            color1 = Q.get(block=False)
                        except:
                            flag = 2

                if (64*(i)+j+1)%2 == 0 or flag == 2:
                    grid[i, j] = bead[color2]
                    num[color2] = num[color2] - 1
                    if num[color2] == 0:
                        try:
                            color2 = Q.get(block=False)
                        except:
                            flag = 1
            else:
                if (64*(i)+j+1)%2 == 1 or flag == 1:
                    grid[i, j] = bead[color2]
                    num[color2] = num[color2] - 1
                    if num[color2] == 0:
                        try:
                            color2 = Q.get(block=False)
                        except:
                            flag = 1

                if (64*(i) +j+1)%2 == 0 or flag == 2:
                    grid[i, j] = bead[color1]
                    num[color1] = num[color1] - 1
                    if num[color1] == 0:
                        try:
                            color1 = Q.get(block=False)
                        except:
                            flag = 2

    allGrid[id] = grid
    res[id] = evaluation(grid)
print(res)
print(colorList[min(res,key=res.get)])
pd.DataFrame(allGrid[min(res,key=res.get)]).to_csv('q5.csv')




