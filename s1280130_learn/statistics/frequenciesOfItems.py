import pandas as pd
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
            Database = {}
            with open(self.iFile, 'r', encoding='utf-8') as f:
                  for line in f:
                        line.strip()
                        temp = [i.rstrip() for i in line.split(self.sep)]
                        temp = [x for x in temp if x]
                        for i in temp:
                          if i not in Database.keys():
                            Database[i]=1
                          else:
                            Datbase[i]+=1
            return Database

if __name__=="__main__":
        x=frequenciesOfItems("PM24HeavyPollutionRecordingSensors.csv","\t")
        data=x.countFre()
