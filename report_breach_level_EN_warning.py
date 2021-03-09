

def report_breach_level_EN_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
        parameters_limit[parameter_name] = 'LOW_WARNING'
    elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
        parameters_limit[parameter_name] = 'HIGH_WARNING' 
    else:
        parameters_limit[parameter_name] = 'NORMAL'