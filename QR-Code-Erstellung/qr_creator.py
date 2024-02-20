import os
import pandas as pd
import qrcode


# Get the absolute path of the script
script_path = os.path.abspath(__file__)
# Extract the directory part of the path
script_directory = os.path.dirname(script_path)
# Change the working directory to the script's directory
os.chdir(script_directory)

# Read your DataFrame (replace 'QR.xlsx' with your actual file name)
#df = pd.read_excel("Anmeldeliste.xlsx")
df=pd.read_excel("Anmeldeliste.xlsx")
#print(df.head)
# Generate QR codes for each row in the fourth column
for index, row in df.iterrows():
    print(row)
    rowname=row[4]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(row[4])
    qr.make(fit=True)
    img = qr.make_image()
    img.save('output/'+str(rowname) + ".png")
