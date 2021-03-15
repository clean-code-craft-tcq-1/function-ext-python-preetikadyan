def collect_out_of_range_parameters_EN(parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'LOW_BREACH'
         parameters_action[parameter_name] = 'Parameter needs to be increased for the given parameter to cross lower limit'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HIGH_BREACH'
         parameters_action[parameter_name] = 'Switch on fan to bring the given parameter below max limit'
    else:    
        report_breach_level_EN_warning(parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
