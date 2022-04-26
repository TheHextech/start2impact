import pandas as pd
import numpy as np
import os
from zipfile import ZipFile


def zip_extractor():
    """This function looks for zip files and extracts them in the same file path of this script, or in a folder provided 
    with an input. If the folder doesn't exist, it will be created with the provided name."""
    
    destination = input('Where do you want to put the extracted files?\nPress enter if you want to extract files in the current path: ').capitalize()

    if destination == '':
        pass
    elif destination not in os.listdir():
        os.mkdir(destination)

    for dirname, _, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if '.zip' in filename:
                with ZipFile(filename, "r") as zip:
                    zip.extractall(f'{destination}')

    print("Extraction: Done")
    
    
def csv_nan_reader():
    
    """This function search for .csv files in a target folder (provided by input), skipping 'checkpoint' files 
    and read them in pandas as DataFrame. Then for each file are printed out: 
    
    - filename and parental folder 
    - Dataframe shape 
    - number of total cells 
    - number of cells with missings 
    - % of missing data 
    - rows and columns containing missings 
    - rows and columns in original dataset 
    - rows and columns remained after drop 
    - the effect of dropping rows and columns in terms of remaining data and which is the best method.
    
    If a folder is empty or doesn't exist, this function will segnalate it."""
    
    target_folder = input('Write here folder name: ').capitalize()
    datano = 0

    # Check if the folder exist
    if os.path.isdir(target_folder):
        
        # Check if the folder is not empty
        if os.listdir(target_folder):
            
            for dirname, _, filenames in os.walk(target_folder):
                for filename in filenames:
                    if not 'checkpoint' in filename:
                        name, file_ext = os.path.splitext(filename)
                        
                        if '.csv' in file_ext:
                            
                            path = os.path.join(dirname, filename)
                            df = pd.read_csv(f'{path}')
                            
                            # Extract main information of the file and count Dataframes
                            datano += 1
                            print(f'\n\nDataframe No: {datano}')
                            print('_'*20+'Start'+'_'*20)
                            print(f'This is the Dataset "{filename}" from folder "{dirname}"')
                            print(filename,'shape',df.shape)
                            
                            # How many total missing values do we have?
                            total_cells = np.product(df.shape)
                            print('Total cells:', total_cells)
                            
                            total_missing = df.isnull().sum().sum()
                            print('Total cells with missings:', total_missing)
                            
                            # Count rows containing missing values and check what happens if you drop rows
                            rows_with_missing = df[df.isnull().any(axis=1)].index.to_list()
                            print('\nTotal lenght of missing rows:', len(rows_with_missing))
                            
                            if len(rows_with_missing) > 10:
                                print(f'Rows containing missing values:\n{rows_with_missing[:10]}...[{rows_with_missing[-1]}]')
                            else:
                                print('Rows containing missing values:\n',rows_with_missing)
                                
                            drop_rows = df.dropna()
                            rows_removal_perc = round((1-drop_rows.shape[0]/df.shape[0])*100,2)
                            print(f"\nRows in original dataset: {df.shape[0]}")
                            print(f"Rows remained after drop: {drop_rows.shape[0]}")
                            print('\nDropping rows with NaN removed',rows_removal_perc,'% of the data!')
                            print(f'Shape of Dataframe after rows manipulation: {drop_rows.shape}')
                            
                            # Count columns containing missing values and check what happens if you drop columns
                            cols_with_missing = [col for col in df.columns if df[col].isnull().any()]
                            print('\n\nTotal lenght of missing columns:', len(cols_with_missing))
                            
                            if len(cols_with_missing) > 5:
                                print(f'Columns containing missing values:\n{cols_with_missing[:5]}...[{cols_with_missing[-1]}]')                                
                            else:
                                print('Columns containing missing values:\n',cols_with_missing)
                                
                            drop_cols = df.dropna(axis=1)
                            cols_removal_perc = round((1-drop_cols.shape[1]/df.shape[1])*100,2)
                            print(f"\nColumns in original dataset: {df.shape[1]}")
                            print(f"Columns remained after drop: {drop_cols.shape[1]}")
                            print('\nDropping columns with NaN removed',cols_removal_perc,'% of the data!')
                            print(f'Shape of Dataframe after columns manipulation: {drop_cols.shape}\n\n')
                            
                            # Compare rows drop vs cols drop and print what is better
                            if rows_removal_perc < cols_removal_perc:
                                print(f"Dropping rows with NaN is the best approach.({rows_removal_perc}% vs {cols_removal_perc}%)\n\n")
                            elif rows_removal_perc > cols_removal_perc:
                                print(f"Dropping columns with NaN is the best approach.({cols_removal_perc}% vs {rows_removal_perc}%)\n\n")
                            else:
                                print("Dropping rows or columns produced the same output.")
                            print('-'*20+'End'+'-'*20+'\n\n')
                            
                        else:
                            print(f"\nI found a file with different extension from csv. '{name}' is a '{file_ext}' file.")
            
            print('\nAll Done.')
        
        else:
            print('\nThis folder is empty!')
    else:
        print("\nSelected folder doesn't exist in this path!")