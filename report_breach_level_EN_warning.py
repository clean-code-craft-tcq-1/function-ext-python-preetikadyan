

def report_breach_level_EN_warning(parameters_action,parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    for parameter_value in range(parameter_min,int(parameter_min + tolerance + 1.00)):
        parameters_limit[parameter_name] = 'LOW_WARNING'
        parameters_action[parameter_name] = 'Increase the given parameter to avoid lower limit breach'
    #elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
    for parameter_value in range(parameter_min,int(parameter_max - tolerance + 1.00)):
        parameters_limit[parameter_name] = 'HIGH_WARNING' 
        parameters_action[parameter_name] = 'Switch on fan to avoid higher limit breach'
    parameters_limit[parameter_name] = 'NORMAL'
    parameters_action[parameter_name] = 'Everything is fine, nothing needs to be done'
