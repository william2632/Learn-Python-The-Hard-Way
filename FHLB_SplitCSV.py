#!/usr/bin/python
#   python FHLB_SplitCSV.py D:\powershell\processes.csv BasePriority
#   python FHLB_SplitCSV.py D:\powershell\processes10M.csv BasePriority
import sys
import os
import pandas as pd
import csv
import time

def num_commas(number):
    return ("{:,}".format(number))

def main(argv):
    if(len(argv)!=3):
        print("--------------------------------Error:")
        print("need 2 parameters: fileName keyColumnName")
        return(1)

    filePath=str(argv[1])
    keyColumnName=str(argv[2])
    print("--------------------------------Info:")
    print('input file name as:', filePath)
    print('Key column name as:', keyColumnName)

    #if not path.exists(filePath):

    try:
        df = pd.read_csv(filePath,nrows=20)
        print("--------------------------------Info:")
        print("input file existing verified:",filePath)
        #for col in df.columns: print(col)
        #print(df.keys())
        if keyColumnName in df.columns :
            print("--------------------------------Info:")
            print("input key column existing verified:",keyColumnName)
        else:
            print("--------------------------------Error:")
            print('Error: The key column does not exist in the CSV file:',keyColumnName)
            return(2)

        #startT = time.time()
        df = pd.read_csv(filePath, usecols = [0])
        #endT = time.time()
        #print(endT - startT)
        pTlen=len(df)
        print("--------------------------------Info: total number of records in the input file: ",num_commas(pTlen))

        #### split into 3 CSV files based on the key column value:
        head, tail = os.path.splitext(filePath)
        outputFileName001=head+"_001"+tail
        outputFileName002=head+"_002"+tail
        outputFileName003=head+"_003"+tail

        outputFileName001_Flag=0
        outputFileName002_Flag=0
        outputFileName003_Flag=0

        pTlen001=0
        pTlen002=0
        pTlen003=0
        print("--------------------------------Info: start split to 3 files:")
        startT = time.time()
        with pd.read_csv(filePath, chunksize=500000) as reader:
            for df_chunk  in reader:
                part001 = df_chunk[ df_chunk[keyColumnName] < 6 ]
                part002 = df_chunk[ (df_chunk[keyColumnName] >= 6) & (df_chunk[keyColumnName] <= 10) ]
                part003 = df_chunk[ df_chunk[keyColumnName] > 10 ]

                plen001=len(part001)
                plen002=len(part002)
                plen003=len(part003)
                pTlen001+=plen001
                pTlen002+=plen002
                pTlen003+=plen003
                print("--------------------------------Info: processed: ",num_commas(pTlen001+pTlen002+pTlen003))

                if(plen001>0 and outputFileName001_Flag==0):
                    part001.to_csv(outputFileName001,index=False, quoting=csv.QUOTE_NONNUMERIC)     #, encoding='utf-8',quoting: QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3)       initial write
                    outputFileName001_Flag=1
                elif(plen001>0 and outputFileName001_Flag>0):
                    part001.to_csv(outputFileName001,index=False, header=False, quoting=csv.QUOTE_NONNUMERIC, mode='a')                  # append write

                if(plen002>0 and outputFileName002_Flag==0):
                    part002.to_csv(outputFileName002,index=False, quoting=csv.QUOTE_NONNUMERIC)     #, encoding='utf-8')       initial write
                    outputFileName002_Flag=1
                elif(plen002>0 and outputFileName002_Flag>0):
                    part002.to_csv(outputFileName002,index=False, header=False, quoting=csv.QUOTE_NONNUMERIC, mode='a')                  # append write
                
                if(plen003>0 and outputFileName003_Flag==0):
                    part003.to_csv(outputFileName003,index=False, quoting=csv.QUOTE_NONNUMERIC)     #, encoding='utf-8')       initial write
                    outputFileName003_Flag=1
                elif(plen003>0 and outputFileName003_Flag>0):
                    part003.to_csv(outputFileName003,index=False, header=False, quoting=csv.QUOTE_NONNUMERIC, mode='a')                  # append write
        endT = time.time()
        print("--------------------------------Info: splited to 3 files, cost {p:5.2f} seconds. ".format(p=endT - startT))

        df001 = pd.read_csv(outputFileName001, usecols = [0])
        print("--------------------------------Info: total number of records in the 1st file: ",outputFileName001,":",num_commas(len(df001)))
        df002 = pd.read_csv(outputFileName002, usecols = [0])
        print("--------------------------------Info: total number of records in the 2nd file: ",outputFileName002,":",num_commas(len(df002)))
        df003 = pd.read_csv(outputFileName003, usecols = [0])
        print("--------------------------------Info: total number of records in the 3rd file: ",outputFileName003,":",num_commas(len(df003)))
        print("--------------------------------Info: total number of records splited files: ", num_commas(len(df001)+len(df002)+len(df003)))
        if(pTlen!=(len(df001)+len(df002)+len(df003))):
            print("--------------------------------Error: number of records in input file:",num_commas(pTlen)," not equal number of records in splited files:",num_commas(len(df001)+len(df002)+len(df003)))

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