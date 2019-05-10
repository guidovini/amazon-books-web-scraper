# ─── LIBRARIES ──────────────────────────────────────────────────────────────────
import pandas as pd
import os, os.path


# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from variables import output_path, fieldnames, input_path, books_to_scrape
from file_generation import filter_asin_from_url_list, read_input_file


# ─── PROGRAM ────────────────────────────────────────────────────────────────────
def read_initial_values():
    print('Running initial validation')

    url_list = read_input_file(input_path, books_to_scrape)
    asin_list = filter_asin_from_url_list(url_list)

    ## Filter repeated values from the input
    input_df = pd.DataFrame(asin_list, columns=['ASIN'])
    filtered_input = input_df.groupby('ASIN').size().reset_index(name='STATUS')

    ## Find repeated values from the input
    repeated_input_values = filtered_input[filtered_input['STATUS'] > 1]

    if os.path.isfile(output_path): 
        print('Scanning database')
        db = pd.read_csv(output_path, usecols=['ASIN', 'STATUS'])

        if ~db.empty or (len(db) == 0): 
            print('Database found with ' + str(len(db)) + ' records.')

            ## Find repeated values from the DB
            repeated_values = db[db['ASIN'].isin(filtered_input['ASIN'])]

            ## Find new values after filtering: repeated values from the input, and repeated values from the DB
            values = pd.concat([
                                db.drop('STATUS', axis=1), 
                                filtered_input.drop('STATUS', axis=1)
                               ]).drop_duplicates(keep=False)

            new_values = filtered_input[filtered_input['ASIN'].isin(values['ASIN'])]

            if repeated_values.empty: 
                print('------------\nRepeated values not found')

            else:    
                print('------------')
                print(str(len(repeated_values)) + ' repeated values found')
                # update_status(repeated_values, repeated_input_values)

                print('------------')
                if new_values.empty: 
                    print('No new values')
                    return [], repeated_values, repeated_input_values
                
                else:
                    print('These values will be send to processing\n', new_values)
                    return new_values, repeated_values, repeated_input_values  

        else:
            print('Original file is empty')

    else:
        print('Database not found, creating new file')
    

    return filtered_input, pd.DataFrame(), repeated_input_values



def update_status(r_values, r_input_values):
    # To prevent that pesky warning
    repeated_values = r_values.copy()
    repeated_input_values = r_input_values.copy()

    repeated_values.reset_index(drop=True)
    repeated_values.set_index('ASIN', inplace=True)
    repeated_input_values.set_index('ASIN', inplace=True)

    db = pd.read_csv(output_path)
    db.set_index('ASIN', inplace=True)

    if len(repeated_input_values) > 0:
        # Minus 1 because r_input_values already counts the + 1
        repeated_input_values.loc[:,'STATUS'] -= 1
        repeated_values = repeated_values.add(repeated_input_values, fill_value=0)
    
    if len(repeated_values) > 0:
        repeated_values.loc[:,'STATUS'] += 1

    nd = pd.concat([repeated_values, repeated_input_values])      
    nd = nd[~nd.index.duplicated(keep='first')] 

    db.update(nd)
    # db.to_csv(output_path, float_format='%.f')
    db.to_csv(output_path) 


def write_csv_file(file_path, extracted_data):
    new_df = pd.DataFrame(extracted_data, columns=fieldnames)

    if os.path.isfile(file_path):
        old_df = pd.read_csv(file_path)
        df = pd.concat([new_df, old_df], sort=False)
    else:
        df = new_df

    df.set_index('ASIN', inplace=True)
    # df.to_csv(file_path, float_format='%.f')
    df.to_csv(output_path) 
