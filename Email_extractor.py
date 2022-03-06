'''
This file is responsible for extracting emailes from text and entering them into an excel file.
inputs are:
    - Text file.
    Example text:
    1 email1

    2 email2

    3 email3

    4 email4
    etc...

Process Flow:
    1 - Set the directory path.
    2 - Set the file path in the directory.
    3 - set the full file path.
    4 - Convert the text into lines and saved it into list of lines.
    5 - Exctract emailes from text rows by removing the index from the rows.
    6 - Write the emails to excel file.
    
Outputs are:
    - excel file contain cleaned emails.

Create Date: 2/25/2022, 9:23 PM.
'''

import pandas as pd


class Text_spliter:
    def __init__(self, full_text_path: str, excel_file_name: str, sheet_name: str, col_name: str):
        self.full_text_path = full_text_path
        self.excel_file_name = excel_file_name
        self.sheet_name = sheet_name
        self.col_name = col_name
        pass  
     
    # split text by index number.
    def split_by_index(self, strings_list):
        # cleaned_emails is a list of email addresses that were cleaned from the email list
        cleaned_emails = []

        # iterate over emails in the email_list
        for i, e in enumerate(strings_list):

            # add the email[i] to cleaned_emails after replacing the order numberand all whitespaces.
            cleaned_emails.append(strings_list[i].replace(str(i + 1), '').strip())

            # print cleaned_emails
            # print('email No: {}\n email address: {}'.format(i+1, cleaned_emails[i]))

        return cleaned_emails


    # write the list to excel.
    def to_excel(self, strings_list):
        # put emails into DataFrame.
        emailes_df = pd.DataFrame(strings_list, columns=[self.col_name])
        # Set DataFrame name.
        emailes_df.name = self.sheet_name
        # write emails_df to excel.
        emailes_df.to_excel(self.excel_file_name,self.sheet_name, index=False)
        print(f'Emails has been written to {self.excel_file_name}.xlsx/sheet: {self.sheet_name}.')


    # This function count number of lines in txt file
    def from_txt_to_list(self):
        # Open the txt file
        file = open(self.full_text_path, 'r')
        # This list is container of extracted emails.
        emails_list = []
        # number of lines in txt file
        line_num = 0
        # iterate through lines in txt fil
        for line in file:
            # append line to email list
            if line != '\n':
                # append the email address to email_list
                emails_list.append(line)
                # increment line_num
                line_num += 1

        # print the total number of lines.
        # print("line_num: {}. \n lingth of email_list: {}".format(
        #   line_num, len(email_list)))
        return emails_list


 
