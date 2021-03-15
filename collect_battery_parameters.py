from collect_out_of_range_parameters_DE import *
from collect_out_of_range_parameters_EN import *

def collect_battery_parameters(parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit,lang):
   if lang == 'DE':
     collect_out_of_range_parameters_DE(parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],'DE')
   else:
     collect_out_of_range_parameters_EN(parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],lang)       
