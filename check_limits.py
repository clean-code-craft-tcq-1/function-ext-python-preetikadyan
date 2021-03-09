
limit = {
     'temperature': {'min': 0, 'max': 45},
     'state_of_charge': {'min': 20, 'max': 80},
     'charge_rate': {'min' : 0, 'max': 0.8}
        } 
 
def collect_battery_parameters(parameters_alert,parameter_name,parameter_value,parameter_limit,lang):
   if lang == 'DE':
     collect_out_of_range_parameters_DE(parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],'DE')
   else:
     collect_out_of_range_parameters_EN(parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],lang)       
 
def collect_out_of_range_parameters_DE(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'NIEDRIGER VERLETZUNG'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HOHE VERLETZUNG'
    else:    
        report_breach_level_DE_warning(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)

def collect_out_of_range_parameters_EN(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'LOW_BREACH'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HIGH_BREACH'
    else:    
        report_breach_level_EN_warning(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
                
def report_breach_level_EN_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
        parameters_limit[parameter_name] = 'LOW_WARNING'
    elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
        parameters_limit[parameter_name] = 'HIGH_WARNING' 
    else:
        parameters_limit[parameter_name] = 'NORMAL'
        
def report_breach_level_DE_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
        parameters_limit[parameter_name] = 'NIEDRIGE WARNUNG'
    elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
        parameters_limit[parameter_name] = 'HOHE WARNUNG' 
    else:
        parameters_limit[parameter_name] = 'NORMAL'
        
def report_battery_parameters(Battery_Life_Parameters,lang):
     parameters_alert_dict = {}
     for battery_parameter in Battery_Life_Parameters:
          collect_battery_parameters(parameters_alert_dict,battery_parameter,Battery_Life_Parameters[battery_parameter],limit[battery_parameter],lang)
     return parameters_alert_dict

def raise_alert_for_battery_parameters(Battery_Life_Parameters,lang):
     battery_parameters = report_battery_parameters(Battery_Life_Parameters,lang)
     
     print("---------Battery Parameters Alert--------\n")
     print("Language selected:",lang,"\n")
     for param_name in battery_parameters  :
         print(param_name +'  ->  '+battery_parameters[param_name],"\n")
          
    
if __name__ == '__main__':
     raise_alert_for_battery_parameters({'temperature' : 25, 'state_of_charge' : 70, 'charge_rate' : 0.7},'EN')
     raise_alert_for_battery_parameters({'temperature' : 50, 'state_of_charge' : 85, 'charge_rate' : 0},'DE')
