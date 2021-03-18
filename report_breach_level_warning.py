

def report_breach_level_warning(alert,collector,parameters_action,parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    for parameter_value in range(parameter_min,int(parameter_min + tolerance + 1.00)):
        parameters_limit[parameter_name] = alert[2]
        parameters_action[parameter_name] = collector[2]
    #elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
    for parameter_value in range(parameter_min,int(parameter_max - tolerance + 1.00)):
        parameters_limit[parameter_name] = alert[3]
        parameters_action[parameter_name] = collector[3]
    parameters_limit[parameter_name] = alert[4]
    parameters_action[parameter_name] = collector[4]
