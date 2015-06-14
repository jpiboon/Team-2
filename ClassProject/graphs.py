#ecosystemOutput
import numpy as np #used this for specificity
import matplotlib.pyplot as plt
from astropy.table import Table, Column
#you do not need to install anything for the Table
from read_template import ReadSpreadsheet
from ecosystem_solve import *

#input:
#   biomass (array)
#   species (list-string)
#   graphBoolean (list-boolean)
#output:
#   table
#   choice of graphs

#organization of this section:
#   a) table
#   b) bar graph, clustered by species
#   c) bar graph, clustered by input (only if 3 input given)
#   d) line graph
#all graphs are embedded in an if statement, initiated by user input (on excel template)

#variables used throughout this system:
userSpreadSheet = ReadSpreadsheet("project_template.xlsx")
graphSelection = userSpreadSheet.excelDataConvert(1)
#biomass = np.array([[3.,4.,5.],[6.,6.,8.],[4.,6.,8.],[5.,5.,5.],[3.,3.,3.]])
#use biomass from ecosystem_solve
species = userSpreadSheet.getSpeciesNames(1)
inputList = ['input1','input2','input3']
inputCount = np.shape(biomass)[1]

#######################################################################
#table: 
#t = Table() #redundant?

def createBiomassTable(species, biomass, inputCount):
    if inputCount == ():
        t = Table([tuple(species), biomass], names = ('species', 'biomass')) #simple table
        return t
    else:
        t = Table([tuple(species), biomass[:, 0]], names = ('species', 'biomass input1'))
        for col in range(inputCount - 1):
            t.add_column(Column(biomass[:, col + 1], name = 'biomass input%d' %(col + 2))) #simple table + more columns
        return t

'''
if shape((biomass)[1])==():
    t = Table([tuple(species), biomass],names = ('species', 'biomass'))
elif shape(biomass)[1]==2:
    t= Table([tuple(species),biomass[:,0], biomass[:,1]],names = ('species', 'biomass input1', 'biomass input2'))
elif shape(biomass)[1]==3:
    t= Table([tuple(species),biomass[:,0], biomass[:,1], biomass[:,2]],names = ('species', 'biomass input1', 'biomass input2', 'biomass input3'))'''

#test code for function
#x = createBiomassTable(species, biomass, inputCount)
#print x
########################################################################
#bargraph, organized by species
    
def barGraph(xData, xAxis, yData, yAxis, titlePlot, c, width, legendAxis):
    #did not work together for some reason
    if len(xData) != np.shape(biomass)[0]:
        if len(xData) != np.shape(biomass)[1]:
            print "The number of species does not match the number of rows in the biomass data."
    
    fig, ax = plt.subplots()    #There will be 3 different figures: ax, ay, az. - changed to just ax   
    ind = np.arange(len(xData))
    if len(xData) == np.shape(biomass)[0]: #to make second bar plot correctly, iterate through rows or columns?
        barsPerInput = np.shape(yData)[1]
    else:
        barsPerInput = np.shape(yData)[0]
    for barNumber in range(barsPerInput):
        if len(xData) == np.shape(biomass)[0]:
            plt.bar(ind + barNumber*width, biomass[:, barNumber], width, color = c[barNumber], label = legendAxis[barNumber])
        else:
            plt.bar(ind + barNumber*width, biomass[barNumber, :], width, color = c[barNumber], label = legendAxis[barNumber])
    plt.ylim(0.0, plt.ylim()[1])    #further define graph (keep below plotting lies)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(xData)
    plt.legend()
    ax.set_xlabel(xAxis)
    ax.set_ylabel(yAxis)
    ax.set_title(titlePlot)
    plt.show() #plt.draw = show multiple figures at once

#if graphSelection[0] == 1:# if bargraph1 was selected
    #barGraph(species, 'Species', biomass, 'Biomass', 'Biomass Bar Graph Organized by Species', 'rgb', 0.25, inputList)

'''
if graphSelection[0]==1:# if bargraph1 was selected
    fig, ax = plt.subplots()    #There will be 3 different figures: ax, ay, az.     
    
    plotList = biomass[:,0] #selects biomass and sort by inputs
    if np.shape(biomass)[1]==2:
        plotList2 = biomass[:,1]
    if np.shape(biomass)[1]==3:
        plotList2 = biomass[:,1]
        plotList3 = biomass[:,2]

    ax.set_ylabel('Biomass')    # set up graph
    ax.set_xlabel('Species')
    ax.set_title('Biomass Bar Graph Organized by Species')
    ind = np.arange(len(species))
    width = 0.25 #width of bar

    #plot graph. If statements to determin number of columns per species
    plt.bar(ind, plotList,  width, color='r',label= 'input1')
    if np.shape(biomass)[1]==2: # adds in 2nd column if 2 biomass
        plt.bar(ind+width, plotList2, width, color = 'b', label= 'input2')
    if np.shape(biomass)[1]==3: # adds in 3rd column if 3 biomass
        plt.bar(ind+width, plotList2, width, color = 'b',label= 'input2')
        plt.bar(ind+width+width, plotList3, width, color = 'y',label= 'input3')
        
    plt.ylim(0.0, plt.ylim()[1])    #further define graph (keep below plotting lies)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(species)
    plt.legend()

    plt.show() #plt.draw = show multiple figures at once '''

#########################################################################
# bargraphs by input

#if graphSelection[1] == 1: ######### if bargraph2 was selected
    #barGraph(inputList, 'Input', biomass, 'Biomass', 'Biomass Bar Graph Organized by Input', 'rgbyc', 0.15, species)

'''
if graphSelection[1]==1: ######### if bargraph2 was selected
    inputList = ['input1', 'input2', 'input3']

    species1 = biomass[0,:] # make matrix by species 
    species2 = biomass[1,:] # this grpah uses the same format as above, so instead of having the data
    species3 = biomass[2,:] # organized by inputs to cluster bars by species, the data is clustered by
    species4 = biomass[3,:] # species to be clustered by inputs.
    species5 = biomass[4,:]

    # this build in function needs 3 "heights," and therefore will only
    # be available with 3 inputs
    if np.shape(biomass)[1]==3:
        fig, ay = plt.subplots()
        ay.set_ylabel('Biomass') #set up graph
        ay.set_xlabel('Input')
        ay.set_title('Biomass Bar Graph Organized by Input')
        ind = np.arange(inputCount)
        width = 0.15

        #plot graph (provide labels for legend
        plot21 = plt.bar(ind, species1,  width, color='r', label= 'species1')
        plot22 = plt.bar(ind+width, species2,  width, color='b', label= 'species2')
        plot23 = plt.bar(ind+width+width, species3,  width, color='g', label= 'species3')
        plot24 = plt.bar(ind+width+width+width, species4,  width, color='y', label= 'species4')
        plot25 = plt.bar(ind+width+width+width+width, species5,  width, color='c', label= 'species5')
        plt.ylim(0.0, plt.ylim()[1])
        plt.legend()

        ay.set_xticks(ind+width)    #show rest of graph
        ay.set_xticklabels(inputList)
        plt.show()
    else:
        print "A graph clustered by input can only be graphed with 3 inputs"'''


##########################################################################
# line graph by input

def lineGraph(xData, xAxis, yData, yAxis, titlePlot, legendAxis):
    ax = plt.subplot()    
    ax.set_xlabel(xAxis)
    ax.set_ylabel(yAxis)
    ax.set_title(titlePlot)
    
    yCount = []
    for i in range(len(xData)): #create yCount for general case
        yCount.append(i + 1)
    for lineNumber in range(len(legendAxis)):
        plt.plot(yCount, biomass[lineNumber, :], marker = 'o', label = legendAxis[lineNumber])
    
    plt.ylim(0.0, plt.ylim()[1]+1) #adjusting x and y legends 
    plt.xlim(0.0, 4)
    ax.set_xticks(np.arange(0, 4, 1))
    plt.legend()
    
    plt.show()  # display graph

# lineGraph(inputList, 'Input', biomass, 'Biomass', 'Biomass Line Graph', species)
  
'''  
if graphSelection[2]==1: # If linegraph was selected
    az = plt.subplot()

    #determine number of inputs (for graph axis purposes)
    if np.shape(biomass)[1]==1:
        inputList = ['input1']
        yCount=[1]
    if np.shape(biomass)[1]==2:
        inputList = ['input1', 'input2']
        yCount=[1,2];
    if np.shape(biomass)[1]==3:
        inputList = ['input1', 'input2', 'input3']
        yCount = [1,2,3];

    species1 = biomass[0,:] # addes in biomass per species
    species2 = biomass[1,:]
    species3 = biomass[2,:]
    species4 = biomass[3,:]
    species5 = biomass[4,:]

    az.set_ylabel('Biomass')    #setting up graph
    az.set_xlabel('Input')
    az.set_title('Biomass Line Graph')

    #plot graph, and assign labels for legend
    plt.plot(yCount,species1, marker='o', label= 'species1')
    plt.plot(yCount,species2, marker='o', label= 'species2')
    plt.plot(yCount,species3, marker='o', label= 'species3')
    plt.plot(yCount,species4, marker='o', label= 'species4')
    plt.plot(yCount,species5, marker='o', label= 'species5')

    plt.ylim(0.0, plt.ylim()[1]+1) #adjusting x and y legends 
    plt.xlim(0.0, 4)
    az.set_xticks(np.arange(0, 4, 1))
    plt.legend()
    
    plt.show()  # display graph'''
