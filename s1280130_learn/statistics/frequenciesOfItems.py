import pandas as pd
import sys

class frequenciesOfItems():
        """
            Storing the complete transactions of the database/input file in a database variable
        """
        def __init__(self,inputFile,sep="\t"):
                self.iFile=inputFile
                self.sep=sep
                
        def countFre(self):
            """
                Storing the complete transactions of the database/input file in a database variable
            """
            
            with open(self.iFile, 'r', encoding='utf-8') as f:
                Database= {}
                for line in f:
                        line.strip()
                        temp = [i.rstrip() for i in line.split(self.sep)]
                        temp = [x for x in temp if x]
                        for i in temp:
                            if i not in Database.keys():
                                Database[i]=1
                            else:
                                Database[i]+=1
            return Database


if __name__=="__main__":
    if len(sys.argv)==2 or len(sys.argv)==3:
            if len(sys.argv)==2:
                x=frequenciesOfItems(sys.argv[1])
                data=x.countFre()
            if len(sys.argv)==3:
                x=frequenciesOfItems(sys.argv[1],sys.argv[2])
                data=x.countFre()
    else:
        print("err")
