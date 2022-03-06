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
import os
from pathlib import Path


# split text by index number.
def split_by_index(strings_list):
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
def to_excel(strings_list):
    # put emails into DataFrame.
    emailes_df = pd.DataFrame(strings_list, columns=['email_address'])
    sheet_name = 'Emails'
    # Set DataFrame name.
    emailes_df.name = sheet_name
    # write emails_df to excel.
    emailes_df.to_excel(f'{emailes_df.name}-0005.xlsx', index=False)
    print(f'Emails has been written to {emailes_df.name}.')


# This function count number of lines in txt file
def from_txt_to_list(full_text_path):
    # Open the txt file
    file = open(full_text_path, 'r')
    # This list is container of extracted emails.
    email_list = []
    # number of lines in txt file
    line_num = 0
    # iterate through lines in txt fil
    for line in file:
        # append line to email list
        if line != '\n':
            # append the email address to email_list
            email_list.append(line)
            # increment line_num
            line_num += 1

    # print the total number of lines.
    # print("line_num: {}. \n lingth of email_list: {}".format(
    #   line_num, len(email_list)))
    return email_list


def main():
    # 1 - Set the directory path.
    # BASE_DIR => File directory path in the system.
    BASE_DIR = Path(__file__).resolve().parent.parent 
    
    # 2 - Set the file path in the directory.
    # text_path_in_dir => text file path withen the directory.
    text_path_in_dir ='schadualed_email/row_email_text_files/emails-0003 (indexed).txt'
    
    # 3 - set the full file path.
    # full_text_path => full path to the text file.
    full_text_path = os.path.join(BASE_DIR, text_path_in_dir).replace('\\','/')
    
    # 4 - Convert the text into lines and saved it into list of lines.
    # text_rows => the text file splited into lines and saved in list.
    text_rows = from_txt_to_list(full_text_path)
    
    # 5 - Exctract emailes from text rows by removing the index from the rows.
    #splited_rows => text_rows with cleaned emails.
    splited_rows = split_by_index(text_rows)
    
    # 6 - Write the emails to excel file.
    to_excel(splited_rows)


if __name__ == '__main__':

    main()
