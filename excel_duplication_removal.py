import pandas as pd
excel_file_path = input("'Provide your excel file path for windows use this format e.g C:\\Users\\ABC\\file.xlsx \n")
df = pd.read_excel(excel_file_path, index_col=0)
# removing duplicates from excel file
df.drop_duplicates(subset=["What's your email address?", "What is the public key to your *BitClout*?"], keep="first", inplace=True)
df.to_excel(excel_file_path)