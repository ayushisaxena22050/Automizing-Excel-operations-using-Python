import os
import pandas as pd
from Download_images import downloads
from paste_images_into_excel import paste_image

if __name__ =='__main__':
    input_path = r"D:\demo\Sales_data"
    output_path = r"D:\demo\Consolidated_Report"
    for file in os.listdir(input_path):
        if file.endswith(".xlsx"):
            bundle = pd.read_excel(r"D:\demo\Sales_data\sample File.xlsx", sheet_name="bundle")

            simple = pd.read_excel(r"D:\demo\Sales_data\sample File.xlsx", sheet_name="Simple")

            sales_data = pd.read_excel(r"D:\demo\Sales_data\sample File.xlsx", sheet_name="Sale data")
            mapping_file = pd.read_csv(r'D:\demo\DATATABLE CHANNEL ITEM TYPE 10-1-19.csv')
            sales_data = sales_data.reset_index()
            sales_data.loc[sales_data.Sku.isin(mapping_file['Channel Product Id']), 'Sku'] = mapping_file['SKU Code']
            simple_final = sales_data.merge(simple, right_on="Sku", left_on="Sku")[["Sku", "Sales", "Bundle/single_x"]]
            # print(simple_final)

            bundle_final = sales_data.merge(bundle, left_on="Sku", right_on="Product Code")[
                ["Sku", "Sales", "Component Product Code", "Component Quantity", "Component Price", "Bundle/single"]]
            bundle_final["Sales_Quantity"] = bundle_final["Component Quantity"] * bundle_final["Sales"]

            bundle_final["Sales_price"] = bundle_final["Component Price"] * bundle_final["Sales_Quantity"]
            Total_data = bundle_final[["Component Product Code", "Sales_Quantity", "Bundle/single"]]
            simple_final.columns = Total_data.columns
            output_data = pd.concat([Total_data, simple_final], axis=0)
            data2 = output_data.groupby("Component Product Code").agg('sum').reset_index()
            data2.to_csv(r'D:\'data2.csv')

            data2['Item_Name'] = data2.merge(simple, right_on="Sku", left_on="Component Product Code")['Item Name']
            data2 = data2.sort_values(by='Sales_Quantity', ascending=False)
            data2["SKU_url"] = str("https://cdn.shopify.com/s/files/1/0912/9966/files/") + data2["Component Product Code"] + str("_thumb.JPG?v=1577958450")
            data2["Product_Image"] = ""

            data2=data2.reset_index()
            data2=data2[['Component Product Code', 'Item_Name','Sales_Quantity','SKU_url','Product_Image']]
            print("First Part Done..!!")
    downloads(data2)
    paste_image(data2)