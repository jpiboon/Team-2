import numpy as np
import xlrd
import unicodedata

'''
f = raw_input("Hello, user. "
    "\n\n Please download a template file at xxx. Complete the form with " +
    "your own data input and select the graph type for data output." + 
    "\n\n Then, please type in the path to your saved file and press 'Enter': ")

# How is the user accessing file? Call file in command line, main file should refer to other files (template)?
# Regardless of template access we still want file embedded in project folder
# README.md: Package requirements

# uploadFile = open(f, 'r') '''

class ReadSpreadsheet(object):
    
    # The constructor passes in the name of the Excel file ONLY.
    def __init__(self, excelFile):
        self.excelFile = excelFile
        # Open the workbook; preliminary actions   
        self.workbook = xlrd.open_workbook(self.excelFile) # Book class

    def getSheetNames(self):
        sheetNames = self.workbook.sheet_names()
        for i, element in enumerate(sheetNames):
            element = unicodedata.normalize('NFKD', element).encode("ascii", "ignore")
            sheetNames[i] = element
        return sheetNames
        
    def getWantedSheet(self, numSheet):
        sheetNames = self.getSheetNames()
        return self.workbook.sheet_by_name(sheetNames[numSheet]) # We will be using multiple sheets
        
    def excelDataConvert(self, usedSheet): 
        worksheet = self.getWantedSheet(usedSheet)
        
        graphOptions = ["Bar Graph (x-axis: Input)", 
                        "Bar Graph (x-axis: Species)", 
                        "Linear Graph"]
        nOptions = len(graphOptions)
        graphBoolean = []
        offset = 15
        for row in range(nOptions):
            booleanCell = worksheet.cell(row + offset, 1)
            booleanCell = booleanCell.value
            if booleanCell.lower() == "yes":
                graphBoolean.append(1)
            elif booleanCell.lower() == "no":
                graphBoolean.append(0)
            else:
                print "The %s option did not have a 'yes' or 'no' answer" %(graphOptions[row])
                return [0]*nOptions
        return graphBoolean
        
    def getSpeciesNames(self, usedSheet):
        worksheet = self.getWantedSheet(usedSheet)
        offset = 1
        speciesNames = []
        for row in range(5):
            species = worksheet.cell(row + offset, 0)
            species = str(species.value)
            speciesNames.append(species)
        return speciesNames
    
    # How to make this more general
    # Format input dataset into columns
    def getBiomassProduced(self, usedSheet):
        worksheet = self.getWantedSheet(usedSheet) 
        return np.array(worksheet.col_values(1, 1, 6))
    
    def getBiomassConsumed(self, usedSheet):
        worksheet = self.getWantedSheet(usedSheet)
        return np.array(worksheet.col_values(2, 1, 6))
        
    def getReductionBiomass(self, usedSheet):
        worksheet = self.getWantedSheet(usedSheet) 
        return np.array(worksheet.col_values(3, 1, 6))
        
    def getAdditionBiomass(self, usedSheet):
        worksheet = self.getWantedSheet(usedSheet) 
        return np.array(worksheet.col_values(4, 1, 6))
        
        '''
        # Graph option selection
        inputBarGraphCell = firstSheet.cell(0,0)         
        speciesBarGraphCell = firstSheet.cell(0,0)
        linearGraphCell = firstSheet.cell(0,0)
        graphSelection = [inputBarGraphCell, speciesBarGraphCell, linearGraphCell]  '''
        
    # excelDataConvert("project_template.xlsx", "User Input")
        
    # If we do multiple inputs (3), if input 2 is blank, stop reading there for input 3 as well