

def report_breach_level_DE_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
        parameters_limit[parameter_name] = 'NIEDRIGE WARNUNG'
    elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
        parameters_limit[parameter_name] = 'HOHE WARNUNG' 
    else:
        parameters_limit[parameter_name] = 'NORMAL'
