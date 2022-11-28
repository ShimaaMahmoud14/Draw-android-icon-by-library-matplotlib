import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import*
#-------axis------
x1, x2 =0, 150
y1, y2 = 150,0
plt.axis([x1, x2, y1, y2])
plt.xticks(range(x1, x2, 10))
plt.yticks(range(y1, y2,-10))
plt.grid(True, alpha =.1)
axes = plt.gca()
axes.set_aspect(1)
#Draw Face
we = Wedge((65,55),30,180,0,facecolor='g', edgecolor ='g')
axes.add_patch(we)
# Draw Body   
tr = Rectangle((35, 58), 60,60,facecolor='g', edgecolor ='g')
axes.add_patch(tr)
for i in range(2):
    #Drawing eyes 
    cr = Circle((55+20*i,45),4,facecolor='w', edgecolor ='w')
    axes.add_patch(cr)
    #Drawing legs
    tr = Rectangle((44+30*i, 118), 10,20,facecolor='g', edgecolor ='g')
    axes.add_patch(tr) 
    we = Wedge((49.5+30*i,138),5,0,180,facecolor='g', edgecolor ='g')
    axes.add_patch(we)
    #Drawing hands
    tr = Rectangle((22+76*i, 70), 10,40,facecolor='g', edgecolor ='g')
    axes.add_patch(tr)
    we = Wedge((27.4+76*i,70),5,180,0,facecolor='g', edgecolor ='g')
    axes.add_patch(we)
    we = Wedge((27+76*i,110),5,0,180,facecolor='g', edgecolor ='g')
    axes.add_patch(we)
    #Drawing of the ears
    ell = Ellipse((89-50*i,24),1,15,angle=45-90*i,facecolor='g', edgecolor ='g')
    axes.add_patch(ell)     
plt.show()