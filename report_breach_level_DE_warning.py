

def report_breach_level_DE_warning(parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    min_tolerance = parameter_min + tolerance + 1
    max_tolerance = parameter_max - tolerance + 1
    #if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
    for parameter_value in range(parameter_min,min_tolerance):
        parameters_limit[parameter_name] = 'NIEDRIGE WARNUNG'
    #elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
    for parameter_value in range(parameter_min,max_tolerance):
        parameters_limit[parameter_name] = 'HOHE WARNUNG' 
    parameters_limit[parameter_name] = 'NORMAL'
