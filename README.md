# Automizing-Excel-operations-using-Python
Why to do repetitive task again and again. Just write a python script and make life easier.

It's generally a time consuming task to fetch values from different tables and then perform calculations if you are using excel. It's even gets slow when you have large data. Getting images in a excel cell is a different challenge.

Here pandas comes to the rescue for calculation task.

--pip install pandas

Images formatting can be easily done by PIL.

--pip install Pillow.

Pasting images in Excel files can't be handled by Pandas itself that why I have used xlsxwriter create a writer instance using below code:

--pip install xlsxwriter

writer = pd.ExcelWriter('file.xlsx', engine='xlsxwriter')

