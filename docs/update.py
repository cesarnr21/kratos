'''
write a script that will convert excel sheets to 
markdown tables that can written into a file
'''

import pandas as pd
from pathlib import Path
import numpy as np


'''
TODO:
* what happens if a file is already exits,
    maybe just add the table to a certain section

* add Heading to table

* the format needs to be imporoved

* one idea: https://stackoverflow.com/questions/73236051/converting-excel-sheet-to-markdown-table-with-breaks-between-multiple-lines-in-a

* add a git precommit hook to update the Markdown file
'''

def main():
    dir_path = Path(__file__).parent
    excel_file = dir_path / 'bill_of_materials.xlsx'
    markdown_file = dir_path / 'bill_of_materials.md'

    data = pd.read_excel(excel_file, sheet_name='parts list').replace(np.nan, '', regex=True).to_markdown()

    # print(data)
    with open(markdown_file, 'w+') as file:
        file.write((data))
        print(f'{markdown_file} updated')


if __name__ == '__main__':
    main()
