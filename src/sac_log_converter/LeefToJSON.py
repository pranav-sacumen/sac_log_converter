import json
import re
import yaml

def leef_to_json(is_config=True):
   if is_config==True:
        with open("/home/dell/sac_log_converter/config/config.yaml", "r") as yamlfile:
               data = yaml.load(yamlfile, Loader=yaml.FullLoader)
               print("Read successful")
        print(data)
   else:
       pass 
   print(data['present'])
   while is_config==False:
       with open("config.json", "r") as jsonfile:
             data = json.load(jsonfile) 
             print("Read successful")
             jsonfile.close()