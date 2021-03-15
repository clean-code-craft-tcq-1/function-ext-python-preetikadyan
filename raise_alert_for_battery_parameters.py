from report_battery_parameters import *

def raise_alert_for_battery_parameters(Battery_Life_Parameters,lang):
     battery_parameters_collect,battery_parameters_action = report_battery_parameters(Battery_Life_Parameters,lang)
     
     print("---------Battery Parameters Alert--------\n")
     print("Language selected:",lang,"\n")
     
     for param_name in battery_parameters_collect  :
         print(param_name +'  ->  '+battery_parameters_collect[param_name],"\n")
     
     print("---------Battery Parameters Action--------\n")
     
     for param_name in battery_parameters_action  :
         print(param_name +'  ->  '+battery_parameters_action[param_name],"\n")
