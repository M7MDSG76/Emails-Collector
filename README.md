# Emails Collector

Emails Collector is a Python program that collects emails from a text file and saves it into an excel file.

## Requirments 
pandas == 1.0.5\
path == 13.1.0 (from pathlib)

## Usage
```python
from Email_extractor import Text_spliter
 

# 1 - set file path.
# text_path => path to the text file.
text_path = 'emails0001.txt' 

# 2 - Declare Text_spliter object.
emails_list = Text_spliter(text_path, 'emails0001.xlsx', 'Emails', 'email')

# 3 - Convert the text into lines and saved it into list of lines.
# text_rows => the text file splited into lines and saved in list.
text_rows = emails_list.from_txt_to_list()

# 4 - Exctract emailes from text rows by removing the index from the rows.
#splited_rows => text_rows with cleaned emails.
splited_rows = emails_list.split_by_index(text_rows)

# 5 - Write the emails to excel file.
emails_list.to_excel(splited_rows)
```
### sample input (sample.txt)
```text
1 example@domain.com
2 example@domain.com
3 example@domain.com
4 example@domain.com
5 example@domain.com
. 
.
100  example@domain.com
1000     example@domain.com
```
### sample output(sample.xlsx)

|Email             |
|------------------|             
|example@domain.com|
|example@domain.com|
|example@domain.com|
|example@domain.com|
|. . .             |


## License
[MIT](https://choosealicense.com/licenses/mit/)