from report_breach_level_EN_warning import *

def collect_out_of_range_parameters_EN(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'LOW_BREACH'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HIGH_BREACH'
    else:    
        report_breach_level_EN_warning(parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
