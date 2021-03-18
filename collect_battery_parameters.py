from collect_out_of_range_parameters import *
from collect_out_of_range_parameters import *
from check_limits import *

def collect_battery_parameters(parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit,lang):
     collect_out_of_range_parameters(alert_logs[lang],collector_logs[lang],parameters_action,parameters_alert,parameter_name,parameter_value,parameter_limit['min'],parameter_limit['max'],lang)
   
