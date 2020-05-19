from PIL import Image
import os
import pandas as pd
import numpy as np
def paste_image(data2):
    print("Pasting started")
    writer = pd.ExcelWriter('D:\demo\Consolidated_Report\Consolidated_file.xlsx', engine='xlsxwriter')
    data2.to_excel(writer, sheet_name='Sheet1',index=False)
    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    image_location=r"D:\demo\Images"
    worksheet.set_column('A:B',30)
    worksheet.set_column('C:E',20)
    for idx in range(len(data2['Component Product Code'])):
        for image in os.listdir(image_location):
            if data2['Component Product Code'][idx]==image.split(".j")[0]:
                print(data2['Component Product Code'][idx],image)
                image_url=image_location+'\\'+image
                i="E"+str(idx+2)
                # print(image_url)
                worksheet.set_row(idx+1, 50)
                try:
                    img=Image.open(image_url)
                    img.verify()
                    worksheet.insert_image(i, image_url,{'x_offset':1,'y_offset':1,'x_scale':1,'y_scale':1,'object_position': 2})
                    print(i)
                    break
                except(IOError,SyntaxError) as e:
                    print("bad file",image)
                    continue
    worksheet.set_column('D:D', None, None, {'hidden': True})
    print("Finished..!!")
    workbook.close()