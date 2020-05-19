import requests
import pandas as pd
from time import sleep
import socket
socket.getaddrinfo('localhost', 8080)
def downloads(output_data):
    output_data=pd.DataFrame(output_data)
    print("length",len(output_data))
    for index in range(len(output_data)):
        print(index)
        image_path=r"D:\demo\Images"+"\\"+str(output_data["Component Product Code"][index])+".jpg"
        with open(image_path, 'wb') as handle:
            response = requests.get(output_data.SKU_url[index], stream=True,timeout=30)
            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        sleep(1)
    print("Images have been Downloaded!")