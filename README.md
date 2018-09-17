Simple Undersampler for Python 2.7
- A simple program for undersampling asymmetric data sets saved in CSV format

The purpose of this program is to make quick undersampled data sets
for training supervised classification models meant for classifying
asymmetric data (data with lots of occurrences of one label but fewer 
of others). This program reads CSV data sets and writes an undersampled 
set to a new CSV file.  The new set will contain a number of records
with each label proportional to the label with the lowest number of
records. Records with labels occurring at higher proportions will be 
selected at random from the original set and written to the output file.
