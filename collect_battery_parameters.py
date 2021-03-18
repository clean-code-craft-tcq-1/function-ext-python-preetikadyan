from collect_out_of_range_parameters import *
from collect_out_of_range_parameters import *
from check_limits import *

def collect_battery_parameters(parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit,lang):
   if lang == 'DE':
     collect_out_of_range_parameters(alert_logs['DE'],collector_logs['DE'],parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],'DE')
   else:
     collect_out_of_range_parameters(alert_logs['EN'],collector_logs['EN'],parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],'EN')  
