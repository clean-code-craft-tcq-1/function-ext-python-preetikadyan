from report_breach_level_warning import *

def collect_out_of_range_parameters(alert,collector,parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = alert[0]
         parameters_action[parameter_name] = collector[0]
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = alert[1]
         parameters_action[parameter_name] = collector[1]
    else:    
        report_breach_level_warning(alert,collector,parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
