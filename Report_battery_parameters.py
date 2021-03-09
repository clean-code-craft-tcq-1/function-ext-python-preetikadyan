

def report_battery_parameters(Battery_Life_Parameters,lang):
     parameters_alert_dict = {}
     for battery_parameter in Battery_Life_Parameters:
          collect_battery_parameters(parameters_alert_dict,battery_parameter,Battery_Life_Parameters[battery_parameter],limit[battery_parameter],lang)
     return parameters_alert_dict