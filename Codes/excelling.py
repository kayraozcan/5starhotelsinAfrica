
import csv
with open('africa.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "NumberOf5StarHotels", "id"])
    writer.writerow(["Algeria","24", "DZA"])
    writer.writerow(["Angola","3","AGO"])
    writer.writerow(["Botswana","18", "BWA"])
    writer.writerow(["Burkina Faso","2", "BFA"])
    writer.writerow(["Burundi","1", "BDI"])
    writer.writerow(["Cabo Verde","12"])
    writer.writerow(["Cameroon","3", "CMR"])
    writer.writerow(["Central African Republic","6", "CAF"])
    writer.writerow(["Chad","3", "TCD"])
    writer.writerow(["Comoros","20"])
    writer.writerow(["Congo Democratic Republic","7", "COD"])
    writer.writerow(["Congo Republic","4", "COG"])
    writer.writerow(["Cote dIvoire","5", "CIV"])
    writer.writerow(["Egypt","60", "EGY"])
    writer.writerow(["Ethiopia","9", "ETH"])
    writer.writerow(["Gabon","4", "GAB"])
    writer.writerow(["Gambia","6", "GMB"])
    writer.writerow(["Ghana","4", "GHA"])
    writer.writerow(["Guinea","2", "GIN"])
    writer.writerow(["Guinea Bissau","1", "GNB"])
    writer.writerow(["Kenya","60", "KEN"])
    writer.writerow(["Lesotho","24", "LSO"])
    writer.writerow(["Liberia","11", "LBR"])
    writer.writerow(["Libya","4", "LBY"])
    writer.writerow(["Madagascar","6", "MDG"])
    writer.writerow(["Malawi","2", "MWI"])
    writer.writerow(["Mali","3", "MLI"])
    writer.writerow(["Mauiritius","43"])
    writer.writerow(["Mauritania","0", "MRT"])
    writer.writerow(["Morocco","60", "MAR"])
    writer.writerow(["Mozambique","12", "MOZ"])
    writer.writerow(["Namibia","17"])
    writer.writerow(["Niger","19","NER"])
    writer.writerow(["Nigeria","49", "NGA"])
    writer.writerow(["Rwanda","6", "RWA"])
    writer.writerow(["Sao Tome and Principe","2"])
    writer.writerow(["Senegal","15", "SEN"])
    writer.writerow(["Seychelles","24"])
    writer.writerow(["Sierra Leone","21", "SLE"])
    writer.writerow(["Somalia","19", "SOM"])
    writer.writerow(["South Africa","60", "ZAF"])
    writer.writerow(["South Sudan","2", "SSD"])
    writer.writerow(["Sudan","25", "SDN"])
    writer.writerow(["Tanzania","0", "TAZ"])
    writer.writerow(["Togo","4", "TGO"])
    writer.writerow(["Tunisia","60", "TUN"])
    writer.writerow(["Uganda","6", "UGA"])
    writer.writerow(["Zambia","17", "ZMB"])
    writer.writerow(["Zimbabwe","10", "ZWE"])
file.close()