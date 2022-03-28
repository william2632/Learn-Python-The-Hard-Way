#!/usr/bin/python
#   python FHLB_List_Unique_Value.py D:\powershell\processes.csv BasePriority
#   python FHLB_List_Unique_Value.py D:\powershell\processes10M.csv BasePriority
import sys
import pandas as pd

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

        df = pd.read_csv(filePath, usecols = [keyColumnName])
        nRecords= "{:,}".format(len(df))
        print("--------------------------------Info: total number of records in the file: ",nRecords)
        
        # Add count to column of interest
        df['count'] = df.groupby(keyColumnName)[keyColumnName].transform('count')
        # only keep unique values in column of interest
        df.drop_duplicates(subset=[keyColumnName], inplace = True)
        sorted_df = df.sort_values(by=[keyColumnName])
        
        print("--------------------------------Info: unique value for ",keyColumnName)
        print(sorted_df.to_string(index=False))
        #print(df.to_csv(sep=',', index=False))

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