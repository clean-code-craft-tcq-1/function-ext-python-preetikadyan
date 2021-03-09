from report_breach_level_DE_warning import *

def collect_out_of_range_parameters_DE(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'NIEDRIGER VERLETZUNG'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HOHE VERLETZUNG'
    else:    
        report_breach_level_DE_warning(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
