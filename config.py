import os

category = ("ERKEK") 
sub_category = ("Ayakkabı") 
product = ("Spor Ayakkabı")

#Dinamik olarak .json uzantılı dosyanın isminin oluşturulması.
json_file_name =f"{category}_{sub_category}_{product}.json"

#.json uzantılı dosyanın kaydedilecek dizin seçimi
data_directory =r"C:\Users\pc\Desktop\CASE\Data\Ürün Link Json"

json_file_path = os.path.join(data_directory, json_file_name)
print(json_file_path)
