import pandas as pd
def frequenciesOfItems(inputFile,sep):
        """
            Storing the complete transactions of the database/input file in a database variable


        """
        Database = {}
        with open(inputFilee, 'r', encoding='utf-8') as f:
              for line in f:
                    line.strip()
                    temp = [i.rstrip() for i in line.splitsep)]
                    temp = [x for x in temp if x]
                    for i in temp:
                      if i not in Database.keys():
                        Database[i]=1
                      else:
                        Datbase[i]+=1
        return Database
