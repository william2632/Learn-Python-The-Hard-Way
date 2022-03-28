#!/usr/bin/python
#   python FHLB_List_Header.py D:\powershell\processes.csv
#   python FHLB_List_Header.py D:\powershell\processes10M.csv
import sys
import os
import pandas as pd
import csv

def main(argv):
    if(len(argv)!=2):
        print("--------------------------------Error:")
        print("need 1 parameters: fileName")
        return(1)

    filePath=str(argv[1])
    print("--------------------------------Info:")
    print('input file name as:', filePath)

    try:
        df = pd.read_csv(filePath,nrows=101)
        print("--------------------------------Info:")
        print("input file existing verified:",filePath)
        #for col in df.columns: print(col)
        #print(df.keys())

        df2 = pd.read_csv(filePath, usecols=[0])
        nRecords= "{:,}".format(len(df2))
        print("--------------------------------Info: total number of records in the file: ",nRecords)

        print("--------------------------------Info: sample records:")
        print(df.head())

        head, tail = os.path.splitext(filePath)
        outputFileHeader=head+"_header"+tail
        df.to_csv(outputFileHeader, index=False, quoting=csv.QUOTE_NONNUMERIC)     #, encoding='utf-8'
        print("--------------------------------Info: also created sample file: ",outputFileHeader)

        
    except FileNotFoundError:
        print("--------------------------------Error:")
        print('File is not present:',filePath)
        return(3)
    except UnicodeDecodeError:
        print("--------------------------------Error:")
        print('File UnicodeDecodeError:',filePath)
        return(4)
    except IOError as e:
        print("--------------------------------Error:")
        print('read CSV file error:',e)
        return(5)

    return(0)


if __name__ == "__main__":
   main(sys.argv)