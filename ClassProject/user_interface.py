import os
from graphs import *

def userInterface():
    print ("\n\n Please download a template file at tinyurl.com/CSE490Final. Save the file as 'userInput.xlsx', complete " +
        "the form with your own data input and select the graph type for data output, as specified " +
        "in the template.")
    
    userInput = raw_input("\n\n If you would like some more explicit directions on how to do this, type" +
        " 'explain' and press 'Enter'. Press 'Enter' if you are ready " +
        "to have your Excel file read. What would you like to do?: ")
    
    def helpTemplate(userInput):
        if userInput.lower() == 'explain':
           print "\n\n If the template is not available online, then a copy of the file is provided"
           print "in the same folder as this software. Use this instead. Directions are also provided"
           print "within the template itself."
    
    helpTemplate(userInput)
    
    print ("\n\n Please type in the directory to your saved file " +
        "and press 'Enter.'")
    
    userInput = raw_input("If you would like some more directions on this, type 'explain' and " +
        "press 'Enter'. What would you like to do?: ")
    
    def helpCommand (userInput):
        if userInput.lower() =='explain':
            print ("\n\n To find the location of your directory: find the corresponding folder icon," +
            "right click, and click on 'Properties' (at the very bottom). In the tab 'General'," +
            "copy what comes after 'Location.' It should look something" +
            "like, 'C:\Users:\yourName\Downloads'." +
            "\n\n Input required: The full directory (that looks something" +
            " like , 'C:\Users\yourName\Downloads'. Do not specify the file" +
            "at the end of the directory (userInput.xlsx).")
    
    helpCommand(userInput)
    
    userInput = raw_input ("\n\n Please type in the directory to your saved file " +
        "and press 'Enter.': ")
    
    try:
        os.chdir(userInput)
    
    except:
        print "\n\n The directory given did not work."
        userInput = raw_input ("Please try again (attempt 2/3): ")
        try:
                os.chdir(userInput)
        except:
            print "\n\n The directory given did not work."
            userInput = raw_input ("Please try again (last attempt): ")
            try:
                os.chdir(userInput)
            except IOError:
                print "Sorry, you maxed out your attempts. Execute this file to try again."
            except WindowsError:
                print "Sorry, your file cannot be found."
    
    #os.chdir(userInput)
    #open("userInput.xlsx") as f:
    
    with open("project_template.xlsx") as f:
        currTable = createBiomassTable(species, biomass, inputCount)
        print currTable
        
        if graphSelection[0] == 1:# if bargraph1 was selected
            barGraph(species, 'Species', biomass, 'Biomass', 'Biomass Bar Graph Organized by Species', 'rgb', 0.25, inputList)
    
        if graphSelection[1] == 1: ######### if bargraph2 was selected
            barGraph(inputList, 'Input', biomass, 'Biomass', 'Biomass Bar Graph Organized by Input', 'rgbyc', 0.15, species)
    
        if graphSelection[2] == 1: # if linegraph was selected
            lineGraph(inputList, 'Input', biomass, 'Biomass', 'Biomass Line Graph', species)
    
    f.close()