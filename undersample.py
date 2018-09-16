#simple undersampler for Python 2.7
#This program reads CSV data sets and writes an undersampled set
#to a new CSV file.  The new set will contain a number of records
#in each class proportional to the label with the lowest number of
#records selected at random from the original set.
import csv
import random

def main():
    #declarations
    #**** Stuff you should change to run! ****
    #change input and output file names here
    inFileName = 'InputFileName.csv'
    outFileName = 'OutputFileName.csv'
    #set catFld to row number that defines category labels
    catFld = 8
    #**** End of stuff you should change! ****
    lineCt = 0
    catCtDict = {}
    firstLn = True
    minPerct = 0
    minCategory = ''
    randNum = 0
    inFile = open(inFileName)
    inRdr = csv.reader(inFile)
    outFile = open(outFileName, 'wb')
    outWtr = csv.writer(outFile)

    print "Let's undersample some data!"
    #count total items, & number of items in each category
    for row in inRdr:
        if firstLn:
            firstLn = False
        else:
            lineCt += 1
            if row[catFld] not in catCtDict:
                catCtDict[row[catFld]] = 1
            else:
                catCtDict[row[catFld]] += 1
    #end for
    inFile.seek(0)

    minCategory = minCat(catCtDict)
    minPerct = minPct(catCtDict, lineCt)
    firstLn = True
    for row in inRdr:
        randNum = random.randint(1, 100)
        if firstLn:
            firstLn = False
            outWtr.writerow(row)
        else:
            if row[catFld] == minCategory:
                outWtr.writerow(row)
            else:
                if randNum <= minPerct:
                    outWtr.writerow(row)
    #end for
    
    inFile.close()
    outFile.close()
    print 'Finshed undersampling!'
    raw_input('press Enter to quit')
#end main

#determine min category in dict and calc percent
#d = dictionary & c = total count, returns percent min
def minPct(d, c):
    firstVal = True
    for cat in d:
        if firstVal:
            firstVal = False
            minCt = d[cat]
        elif minCt > d[cat]:
            minCt = d[cat]
    #end for
    return int((float(minCt)/c*100))          
#end minPct

#returns minimum category, d = dictionary
def minCat(d):
    firstVal = True
    for cat in d:
        if firstVal:
            firstVal = False
            minCt = d[cat]
            minCat = cat
        elif minCt > d[cat]:
            minCt = d[cat]
            minCat = cat
    #end for
    return minCat
#end minCat

if (__name__ == '__main__'):
    main()
