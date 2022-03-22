'''
Developed by: @Mohammed Alghanmi
This file is responsible for extracting emailes from text and entering them into an excel file.

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

    # Convert a text file to list.
    def from_txt_to_list(self):
        
        # Open the txt file
        file = open(self.full_text_path, 'r')
        # This list is container of extracted emails.
        emails_list = []
        # number of lines in txt file
        line_num_count = 0
        
        # iterate through lines in txt fil
        for line in file:
            # append line to email list
            if line != '\n' and '@' in line:
                
                # append the email address to email_list
                emails_list.append(line)
                # increment line_num
                line_num_count += 1
                
        return emails_list

    def from_excel_to_list(self):
        df = pd.read_excel(self.excel_file_name, self.sheet_name)
        print(df)
        return df

    # This function should get the company name of the email address
    def exctract_company_name(email):
        company_name = email.split('@')
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

 # This function should get the company name of the email address
def exctract_company_name(email):
    spliter_by_at = email.split('@')
    
    dot_accurance = 0
    for i in spliter_by_at[1]:
        if i =='.':
            dot_accurance +=1
    print(dot_accurance)
    
    if dot_accurance >1 :
        company_name = spliter_by_at[1]
    else:   
        spliter_by_dot = spliter_by_at[1].split('.')
        company_name = spliter_by_dot[0]
    return company_name


def from_excel_to_list(excel_file_path, sheet_name ):
    df = pd.read_excel(excel_file_path, sheet_name)
    print(df)
    return df    

def main():
    
    
    # company = exctract_company_name('http://diyar.com/index.aspx?page=careers')
    
    # print(f'Comapny Name is: {company}\n')
    text_path = 'row_email_text_files\emails-0003 (indexed).txt' 

    # 2 - Declare Text_spliter object.
    emails = Text_spliter(text_path, 'emails0005.xlsx', 'Emails', 'Email')

    df = emails.from_excel_to_list()
    emails_list = []
    
    for email in df['Email']:
        emails_list.append(email)
    print(emails_list)
    # # 3 - Convert the text into lines and saved it into list of lines.
    # # text_rows => the text file splited into lines and saved in list.
    # text_rows = emails.from_txt_to_list()

    # # 4 - Exctract emailes from text rows by removing the index from the rows.
    # #splited_rows => text_rows with cleaned emails.
    # splited_rows = emails.split_by_index(text_rows)
    # emails.to_excel(splited_rows)
    # for email in splited_rows:
        
    #     print(f'email: {email}')
        
    #     company = exctract_company_name(email)
    #     if company == 'gmail' or company == 'yahoo' or company == 'hotmail' or company == 'outlook':
    #         company = 'None'
    #     print(f'Comapny Name is: {company}\n')
            
            
        
        

if __name__ == '__main__':
    
        main()
    
 
