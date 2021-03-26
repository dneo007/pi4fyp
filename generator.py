import csv
import numpy as np
import sys

def main():
    print("Starting", str(sys.argv[0]), "V1.0")
    inputfile = input('Input Filename: ')
    outputfile = input('Output Filename: ')
    print('Generating Filename:', str(inputfile))

    while True:
        with open (inputfile,'r') as csv_file:
            reader =csv.reader(csv_file)
        #    next(reader) # skip first row
            #print first 30 rows

            for row in reader:
                with open(outputfile, 'a') as csvnew:
                    rows = [ [row[0], row[1]]]
                    csvwriter = csv.writer(csvnew)
                    csvwriter.writerows(rows)

if __name__ == '__main__':
    main()
