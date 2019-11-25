""" Simplex Plots for Trio Trajectories"""

from csv import reader
from matplotlib import pyplot as plt
from matplotlib import gridspec as gsp
import numpy as np
import ternary as tr
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

with open('March_2018_Trio_Alt.csv', 'r') as f:
    AverageThreeTrios = list(reader(f))

with open('Trio_Exp_Constant_Trios_End.csv', 'r') as f:
    ConstantTrios = list(reader(f))
 
###############################################################################
#### Sample trajectory plot
#figure, tax = tr.figure(scale=1.0)
#tax.boundary()
#tax.gridlines(multiple=0.2, color="black")
#tax.set_title("Plotting of sample trajectory data", fontsize=20)
#points = []
#### Load some data, tuples (x,y,z)
#for p in [(1,0,0),(.9,0.05,0.05),(.8,0.15,0.05),(.7,0.2,0.1),(.6,0.3,0.1),(.5,0.35,0.15),(.4,0.4,0.2),(0.33,0.33,0.33)]:
#    points.append(p)
#points2 = []
#for q in [(0.8,0.1,0.1),(0.6,0.35,0.5),(0.3,0.58,0.12),(0.2,0.6,0.2),(0.2,0.45,0.35),(0.22,0.35,0.43),(0.3,0.25,0.45),(0.37,0.25,0.38),(0.35,0.35,0.3),(0.33,0.33,0.33)]:
#    points2.append(q)
#### Plot the data
#tax.plot(points, linewidth=2.0, label="Curve")
#tax.plot(points2, linewidth=2.0, label="Curve2")
#tax.legend()
#tax.show()

###############################################################################

Days = [0,1,2,3,4,5,6]
Initial_Frac = ['96-2-2','15-4-81','15-80-5','62-19-19']
Initial_Frac_points = [(.96,.02,.02),(.15,0.04,.81),(.15,.8,.05),(.62,.19,.19)]
communities = ['Constant','Alternating','Alternating2']
Dilution_schemes = ['3','1-5','2-4']

com = 'Constant'
dil_scheme = ['1','2','3','4','5','6']

DR = [] #DR stands for Day Results
for dil in dil_scheme:
    for k in range(len(Initial_Frac)):
        trajectory = [Initial_Frac_points[k]]
        for i in ConstantTrios[1::]:
            if i[0] == com and i[7] == Initial_Frac[k] and i[8] == dil and i[9] == '5':
                ############   i[4] is Ea, i[5] is Pp, and i[6] is Pv
                trajectory.append((float(i[4]),float(i[5]),float(i[6])))
        #print(dil,Initial_Frac[k])
        DR.append(trajectory)
#print(DR)
#print(len(DR))
def plot_on_simplex(DR, tax, d):
    for j in range(4):
        tax.plot(DR[j+d], linewidth=1.4, color='black')
        #p1 = DR[j][0]
        last = DR[j+d][1]
        #tax.scatter(p2, marker='o', color='grey', edgecolors='black')
        tax.scatter([last], marker='o', color='black', edgecolors='black', zorder=10)
        #tax.line(p1, p2, linewidth=3., marker='s', color='grey', linestyle=":")

fig = plt.figure(figsize=(21, 3))
gs = gsp.GridSpec(2, 6, height_ratios=[5, 1])
gs.update(wspace=0.4, hspace=0.02)

my_axes_colors = [{'l':'black', 'r':'blue', 'b':'black'}, {'l':'red', 'r':'blue', 'b':'blue'} ,
                  {'l':'red', 'r':'blue', 'b':'blue'} , {'l':'black', 'r':'blue', 'b':'black'} ,
                  {'l':'black', 'r':'blue', 'b':'black'} , {'l':'black', 'r':'blue', 'b':'black'} ]

d=0
for i in range(0,6,1):
    figure, tax = tr.figure(ax = plt.subplot(gs[0,i:i+1]))
    # Draw Boundary and Gridlines
    tax.boundary(linewidth=1.5, axes_colors=my_axes_colors[i])
    #tax.gridlines(color="black", multiple=0.2)
    # Set Axis labels and Title
    fontsize = 20
    #tax.set_title(title, fontsize=20)
#    if i == 0:
#        tax.left_corner_label("Pv", fontsize=fontsize,offset=0.35)
#        tax.top_corner_label("Pp", fontsize=fontsize,offset=0.16)
#        tax.right_corner_label("Ea", fontsize=fontsize,offset=0.35)
    tax.clear_matplotlib_ticks()
    
    plot_on_simplex(DR, tax, d)
    
    ax = tax.get_axes()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    d += 4

LowerAx = plt.subplot(gs[1,:])
x = np.linspace(1,6,100)
y = np.linspace(0,1,100)
plt.fill_between(x, y, 0, facecolor='grey')
plt.ylim((0,1))
plt.xlim((0.7,6.3))
plt.yticks([])
LowerAx.spines['left'].set_visible(False)
LowerAx.spines['right'].set_visible(False)
LowerAx.spines['top'].set_visible(False)
plt.xticks(fontsize = 16)
plt.xlabel('Log(Dilution Factor)', fontsize = 22)
plt.subplots_adjust(bottom=0.35)

plt.show()

#fig.savefig("/Users/Billy/Desktop/ConstantTrios.png", dpi=800, box_inches="tight")