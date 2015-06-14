#ecosystemSolver with functions
import numpy as np
from read_template import ReadSpreadsheet

#input:
#   biomassProducedColumn1,2,3 (array) At least one necessary for all. 
#   biomassConsumedColumn1,2,3   (array)
#   reductionBiomassColumn1,2,3  (array)
#   additionBiomassColumn1,2,3   (array)
#output:
#   biomass (array)

#biomassProducedColumn1 = array([0.76, 0.405, 2.25, 3.41, 4.4])
#biomassConsumedColumn1 = array([24.35, 2.602, 12, 25, 22])
#reductionBiomassColumn1 = array([0.0006, 0, 0.0094, 0, 0])
#additionBiomassColumn1 = array([0, 0, 0, 0, 0])

#biomassProducedColumn2 = array([0.3, 20, 0.9, 3.0,24.0])
#biomassConsumedColumn2 = array([40, 24.5, 3.09, 15, 0])
#reductionBiomassColumn2 = array([5, 2, 20, 50, 0])
#additionBiomassColumn2 = array([3, 5, 18, 30, 0])

userSpreadSheet = ReadSpreadsheet("project_template.xlsx")

biomassProducedColumn1 = userSpreadSheet.getBiomassProduced(1)
biomassConsumedColumn1 = userSpreadSheet.getBiomassConsumed(1)
reductionBiomassColumn1 = userSpreadSheet.getReductionBiomass(1)
additionBiomassColumn1 = userSpreadSheet.getAdditionBiomass(1)

biomassProducedColumn2 = userSpreadSheet.getBiomassProduced(2)
biomassConsumedColumn2 = userSpreadSheet.getBiomassConsumed(2)
reductionBiomassColumn2 = userSpreadSheet.getReductionBiomass(2)
additionBiomassColumn2 = userSpreadSheet.getAdditionBiomass(2)

biomassProducedColumn3 = userSpreadSheet.getBiomassProduced(3)
biomassConsumedColumn3 = userSpreadSheet.getBiomassConsumed(3)
reductionBiomassColumn3 = userSpreadSheet.getReductionBiomass(3)
additionBiomassColumn3 = userSpreadSheet.getAdditionBiomass(3)

#Our linear food chain does not have fractions in the diet percentage as it is
#all ones. This allows us to neglect this parameter as n*1 =n

def biomassCalculator (biomassProducedColumn, biomassConsumedColumn, reductionBiomassColumn, additionBiomassColumn):
    biomassConsumedColumn = np.delete(biomassConsumedColumn,4)
    linearEquationsPart1= np.diag(biomassProducedColumn) #make diagnal matrix of biomassProducedColumn
    linearEquationsPart2 = np.diag(biomassConsumedColumn, k=-1) # make off diagnal matrix of biomassConsumedColumn
    linearEquations = linearEquationsPart1 + (-1*linearEquationsPart2) # add the two diagnal matrix together to set up to solve the system of equations
    equationSolutions = reductionBiomassColumn -additionBiomassColumn
    biomass = []
    biomass = np.linalg.solve(linearEquations,equationSolutions) #solve system of equations
    biomass = np.reshape(biomass, (5,1))
    return biomass

biomass1 = biomassCalculator(biomassProducedColumn1, biomassConsumedColumn1, reductionBiomassColumn1, additionBiomassColumn1)
biomass2 = biomassCalculator(biomassProducedColumn2, biomassConsumedColumn2, reductionBiomassColumn2, additionBiomassColumn2)
biomass3 = biomassCalculator(biomassProducedColumn3, biomassConsumedColumn3, reductionBiomassColumn3, additionBiomassColumn3)

#append all calculated sets of biomasses into one matrix
biomass = np.append(biomass1, biomass2, axis=1) 
biomass = np.append(biomass, biomass3, axis=1)

'''
#if input1 == True:########## if there is input 2, rewrite to fit
biomassConsumedColumn1 = np.delete(biomassConsumedColumn1,4)#remove last column

linearEquationsPart11= np.diag(biomassProducedColumn1) #make diagnal matrix of biomassProducedColumn
linearEquationsPart12 = np.diag(biomassConsumedColumn1, k=-1) # make off diagnal matrix of biomassConsumedColumn
linearEquations1 = linearEquationsPart11 + linearEquationsPart12 # add the two diagnal matrix together to set up to solve the system of equations
equationSolutions1 = additionBiomassColumn1-reductionBiomassColumn1 #complete system of equations

biomass1 = []
biomass1 = np.linalg.solve(linearEquations1,equationSolutions1) #solve system of equations
biomass = biomass1

#if input2 == True: ########## if there is input 2, rewrite to fit
#same process as above, but slightly different variable names
biomassConsumedColumn2 = np.delete(biomassConsumedColumn2,4)
linearEquationsPart21= np.diag(biomassProducedColumn2)
linearEquationsPart22 = np.diag(biomassConsumedColumn2, k=-1)
linearEquations2 = linearEquationsPart21 + linearEquationsPart22
equationSolutions2 = additionBiomassColumn2-reductionBiomassColumn2
biomass2 = []
biomass2 = np.linalg.solve(linearEquations2,equationSolutions2)
biomass =np.concatenate((biomass1,biomass2))
biomass=np.reshape(biomass,(5,2))

#if input3 == True: ########## if there is input 3, rewrite to fit
#same process as above, but slightly different variable names
biomassConsumedColumn3 = np.delete(biomassConsumedColumn3,4)
linearEquationsPart31= np.diag(biomassProducedColumn3) 
linearEquationsPart32 = np.diag(biomassConsumedColumn3, k=-1)
linearEquations3 = linearEquationsPart31 + linearEquationsPart32
equationSolutions3 = additionBiomassColumn3-reductionBiomassColumn3
biomass3 = []
biomass3 = np.linalg.solve(linearEquations3,equationSolutions3)
biomass =np.concatenate((biomass1,biomass2, biomass3))
biomass=np.reshape(biomass,(5,3))'''