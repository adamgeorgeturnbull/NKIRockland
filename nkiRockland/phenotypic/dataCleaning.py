# functions to clean the phenotypic data before merging

def delEmptyRows(path, variables):
    
    # delete rows that contain no information
    # path variable defines location of phenotypic data files, COINs download usually called 'assessment_data'
    # variables defines the specific files you want to clean
    
    import os
    import pandas as pd
    from glob import glob
    
    os.chdir(path) # change path to location of data
    files = sorted(glob('*')) # get list of data files
    
    for v in variables: # loop through each desired file
        print("cleaning %s file" % v)
        file = [s for s in files if v in s]
        if len(file) > 1:
            print("Warning, multiple files for variable %s" % v) # check that there is only one file for this variable
        file = file[0]
        if df.iloc[0][0] == 'ID': # check if first line contains repeat headers
            df = df.iloc[1:] # remove repeat headers
        df_zero = df.fillna(value=0)
        c = df.columns.get_loc("Days since first enrollment")
        df_zero = df_zero.iloc[:,c+1:]
        