#some code written with ChatGPT 
#edited by Group 3
#parse through results files quickly

import pandas as pd
import re

def output(inputText):

    # Read the input CSV file into a DataFrame
    df = pd.read_csv(inputText)

    # Convert the "fasta headers" column to a string data type
    df['Fasta headers'] = df['Fasta headers'].astype(str)

    # Get the "fasta headers" column from the DataFrame
    fasta_headers = df['Fasta headers']

    # Define a regular expression pattern to match the "GN=" field
    gn_pattern = r'GN=([^ ]+)'

    # Initialize empty lists to store the extracted values
    between_spaces_list = []
    gn_list = []

    # Loop over the fasta headers and extract the desired information
    for header in fasta_headers:
        # Convert the header to a string data type if it is a float
        if isinstance(header, float):
            header = str(header)

        # Split the header on spaces
        parts = header.split()

        # Get the text between the first and second spaces, if it exists
        between_spaces = ''
        if len(parts) > 1:
            between_spaces = parts[1]

        # Get the text after "GN="
        gn_match = re.search(gn_pattern, header)
        gn = ''
        if gn_match:
            gn = gn_match.group(1)

        # Append the extracted values to the respective lists
        between_spaces_list.append(between_spaces)
        gn_list.append(gn)

    # Create two new DataFrames from the extracted values
    between_spaces_df = pd.DataFrame({'Between Spaces': between_spaces_list})
    gn_df = pd.DataFrame({'GN': gn_list})

    # Concatenate the "between spaces" and "GN" DataFrames
    result_df = pd.concat([between_spaces_df, gn_df], axis=1)

    return result_df



if __name__ == '__main__':
    df1 = output('proteinGroups_AB.csv')
    df2 = output('proteinGroups_SB.csv')
    
    
    # Merge the two dataframes on their common column
    merged_df = pd.merge(df1, df2, on=['Between Spaces','GN'], how='inner')
    
    # Write the resulting dataframe to an output CSV file
    merged_df.to_csv('outputSameGenes.csv', index=False)