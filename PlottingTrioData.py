"""Plotting Trio Data"""

from csv import reader
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

with open('March_2018_Trio_Alt.csv', 'r') as f:
    data = list(reader(f))
    
Days = [0,1,2,3,4,5,6]
Initial_Frac = ['96-2-2','15-4-81','15-80-5','62-19-19']
communities = ['Constant','Alternating','Alternating2']
Dilution_schemes = ['3','1-5','2-4']

com = 'Constant'
dil_scheme = '3'

DR = [] #DR stands for Day Results
for IF in Initial_Frac:
    for j in [4,5,6]:
        colony_count = []
        for i in data[1::]:
            if i[0] == com and i[7] == IF and i[8] == dil_scheme:
                colony_count.append(float(i[j]))
                                
        DR.append(colony_count)

fig1 = plt.gcf()

def add(list1,list2):
    list3 = []
    for k in range(0,len(list1)):
        list3.append(list1[k]+list2[k])
    return list3

def mult(list1, list2):
    list3 = []
    for k in range(0,len(list1)):
        list3.append(list1[k]*list2[k])
    return list3

def div(list1, list2):
    list3 = []
    for k in range(0,len(list1)):
        list3.append(list1[k]/list2[k])
    return list3

i = 6 ##Change this to get different initial conditions

#title = 'Alternating Trio Starting \n Mostly Pv'
#save = '/Users/Billy/Desktop/%s' %(title)

npDR0 = DR[i] #Ea
npDR1 = DR[i+1] #Pp
npDR2 = DR[i+2] #Pv
DRtot = add(add(npDR0,npDR1),npDR2)
DR0frac = div(npDR0, DRtot) #Ea
DR1frac = div(npDR1, DRtot) #Pp
DR2frac = div(npDR2, DRtot) #Pv
    
plt.fill_between(Days, 0, add(add(DR1frac,DR0frac),DR2frac), facecolor='purple') #Pp
    
plt.fill_between(Days, 0, add(DR0frac,DR2frac),facecolor='orange')#Ea

plt.fill_between(Days, 0, DR2frac,facecolor='seagreen') #Pv
    
#error = np.sqrt((np.add(np.add(np.multiply(npDR0,npDR1), npDR0), npDR1) + 1)
#        /((np.add(npDR0,npDR1) + 2)**2 * (np.add(npDR0,npDR1) + 3)))
###Using Beta Distribution
#plt.errorbar(Days, plotDRfrac, yerr=error, color = 'red', ecolor = (0.6, 0.2, 0.1), lw = 4.0)
 
plt.grid(lw = 2.0)
plt.ylim(ymax = 1, ymin = 0)
plt.yticks(np.arange(0.0, 1.1, 0.5), fontsize=22)
plt.xticks(fontsize=22)
plt.xlabel('Time (Days)', fontsize=32)
plt.ylabel('Fractions', fontsize=32)
#plt.title(title, fontsize=22)
#plt.show()
fig1.savefig('/Users/Billy/Desktop/TrioConstPp.png', dpi=800)      
