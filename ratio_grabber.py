import Russell_2000_CSV as R2 
import csv

#To read in data
def reader(address, x):
    with open(address,"r") as data:
        read_in = csv.reader(data,delimiter=',')
        #for skip in range(2): #skips the first two rows
        #    next(read_in)
       	names = next(read_in)
        #print(type(names))
        print("Grabbed column names are %s" % names[:2])
        for row in read_in:
        	#x.append(float(row[0])) #grab the first column 
            #y.append(float(row[1])) #grab the second column
            if row[1] != 'NM':
                rv = float(row[1])
                if rv >= 7.:
            	   good = str(row[0]) + ":"+ str(row[1]) #concatenate name and P/E ratio of company 
            	   x.append(good)

    print(x)
    print(type(a))
    print("Processed %d lines." % len(x))

if __name__ == "__main__":
    g_r = []
    print("Grabbing best P/E ratios based on 3 or less...\n")
    #R2.R2000_data() #if you need to grab the data again. Automatically creates our .csv file
    reader("Russell_2000.csv",g_r)