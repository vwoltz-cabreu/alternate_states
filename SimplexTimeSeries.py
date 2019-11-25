""" Plotting one simplex"""


from csv import reader
import ternary as tr
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

with open('March_2018_Trio_Alt.csv', 'r') as f:
    AverageThreeTrios = list(reader(f))

Days = [0,1,2,3,4,5,6]
Initial_Frac = ['96-2-2','15-4-81','15-80-5','62-19-19']
Initial_Frac_points = [(.96,.02,.02),(.15,0.04,.81),(.15,.8,.05),(.62,.19,.19)]
communities = ['Constant','Alternating','Alternating2']
Dilution_schemes = ['3','1-5','2-4']

com = 'Constant'
dil_scheme = ['1','2','3','4','5','6']
DF = '3'

DR = [] #DR stands for Day Results
for dil in [DF]:
    for k in range(len(Initial_Frac)):
        trajectory = []
        for i in AverageThreeTrios[1::]:
            if i[0] == com and i[7] == Initial_Frac[k] and i[8] == dil: #and i[9] == '6':
                ############   i[4] is Ea, i[5] is Pp, and i[6] is Pv
                trajectory.append((float(i[4]),float(i[5]),float(i[6])))
        #print(dil,Initial_Frac[k])
        DR.append(trajectory)

#print(DR)

figure, tax = tr.figure()
# Draw Boundary and Gridlines
my_axes_colors = {'l':'black', 'r':'black', 'b':'black'}
tax.boundary(linewidth=4, axes_colors=my_axes_colors)
#tax.gridlines(color="black", multiple=0.2)
# Set Axis labels and Title
fontsize = 32
#tax.set_title(title, fontsize=20)
#tax.left_corner_label("Pv", fontsize=fontsize,offset=0.1)
#tax.top_corner_label("Pp", fontsize=fontsize,offset=0.16)
#tax.right_corner_label("Ea", fontsize=fontsize,offset=0.1)
tax.clear_matplotlib_ticks()

def plot_on_simplex(DR, tax):
    for j in range(4):
        tax.plot(DR[j], linewidth=3, color='grey')
        #p1 = DR[j][0]
        last = DR[j][6]
        secondToLast = DR[j][5]
        avgEnd = ((last[0]+secondToLast[0])/2,(last[1]+secondToLast[1])/2,(last[2]+secondToLast[2])/2)
        print(avgEnd)
        #tax.scatter(p2, marker='o', color='grey', edgecolors='black')
        tax.scatter([avgEnd], s=130, marker='o', color='grey', edgecolors='black',zorder=10)
        tax.scatter([DR[j][0]], s=130, marker='o', color='black', edgecolors='black',zorder=1)
        #tax.line(p1, p2, linewidth=3., marker='s', color='grey', linestyle=":")
        
plot_on_simplex(DR, tax)

##### For Constant DF 3
if com == 'Constant' and DF == '3':
    ##State A
    tax.scatter([(0.5636672326000001, 0.008771929825, 0.42756083755)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)
    ##State B
    tax.scatter([(0.46164984189999997, 0.538350158105, 0.0)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)

##### For Alternating DF 2-4
if com == 'Alternating' and DF == '2-4':
    ##State A
    tax.scatter([(0.6445038423, 0.0, 0.3554961577)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)
    ##State B
    tax.scatter([(0.6336336989833333, 0.35629918692, 0.010067114093333334)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)

##### For Alternating DF 1-5
if com == 'Alternating' and DF == '1-5':
    ##State A
    tax.scatter([(0.718902439, 0.0, 0.281097561)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)
    ##State B
    tax.scatter([(0.47880647963333334, 0.5168541063166666, 0.0043394140400000005)], s=400, marker='o', color='blue', edgecolors='black',zorder=5)

        

ax = tax.get_axes()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
#plt.xlabel('Trio Constant\n'+r'Environment at $10^3$', fontsize=32)

tax.show()
figure.savefig('/Users/Billy/Desktop/TrioConst3.png', dpi=800)