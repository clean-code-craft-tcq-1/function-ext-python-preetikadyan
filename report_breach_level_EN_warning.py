

def report_breach_level_EN_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    for parameter_value in range(parameter_min,parameter_min + tolerance + 1.00):
        parameters_limit[parameter_name] = '_LOW_WARNING'
    #elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
    for parameter_value in range(parameter_min,parameter_max - tolerance + 1.00):
        parameters_limit[parameter_name] = 'HIGH_WARNING' 
    parameters_limit[parameter_name] = 'NORMAL'
