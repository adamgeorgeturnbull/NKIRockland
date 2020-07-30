def mergeData(path):

    # combine variables into single data sheet
    # path variable defines location of phenotypic data files, COINs download usually called 'assessment_data'
    
    import os
    import pandas as pd
    from glob import glob
    
    os.chdir(path) # change path to location of data
    files = sorted(glob('*')) # get list of data files
    
    data = [pd.read_csv(f) for f in files]
    
    IDs = []   
    for d in data:
        if d.iloc[0][0] == 'ID': # check if first line contains repeat headers
            d = d.iloc[1:] # remove repeat headers
        IDs.append(set(d['Anonymized ID']))
    result = set(IDs[0]) 
    for currSet in IDs[1:]: 
        result.intersection_update(currSet) 
    
    keys = ['Anonymized ID', 'Subject Type', 'Sub Study Label', 'Visit']
    df = pd.DataFrame(columns=keys)
    for d in data:
        if d.iloc[0][0] == 'ID': # check if first line contains repeat headers
            d = d.iloc[1:] # remove repeat headers
        d = d[d['Anonymized ID'].isin(result)]
        d = d.replace(to_replace=['V1','V2'], value='VA')
        d = d.replace(to_replace=['V1REP','V2REP'], value='VA-REP')
        cols = [x for x in d.columns if x not in df.columns or x in keys]
        df = pd.merge(df, d[cols], on=keys, how='outer', suffixes=['',''])  
    
    df.to_csv('../master/master_data_all_timepoints.csv', index=False)
    
    