from report_battery_parameters import *

def raise_alert_for_battery_parameters(Battery_Life_Parameters,lang):
     battery_parameters = report_battery_parameters(Battery_Life_Parameters,lang)
     
     print("---------Battery Parameters Alert--------\n")
     print("Language selected:",lang,"\n")
     for param_name in battery_parameters  :
         print(param_name +'  ->  '+battery_parameters[param_name],"\n")
