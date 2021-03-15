

def report_breach_level_DE_warning(parameters_action,parameters_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang): 
    tolerance = parameter_max * 0.05
    #if parameter_value >= parameter_min and parameter_value <= parameter_min + tolerance :
    for parameter_value in range(parameter_min,int(parameter_min + tolerance + 1.00)):
        parameters_limit[parameter_name] = 'NIEDRIGE WARNUNG'
        parameters_action[parameter_name] = 'Erhöhen Sie den angegebenen Parameter, um eine Verletzung der unteren Grenze zu vermeiden'
    #elif parameter_value <= parameter_max and parameter_value >= parameter_max - tolerance :
    for parameter_value in range(parameter_min,int(parameter_max - tolerance + 1.00)):
        parameters_limit[parameter_name] = 'HOHE WARNUNG' 
        parameters_action[parameter_name] = 'Schalten Sie den Lüfter ein, um eine Überschreitung der Obergrenze zu vermeiden'
    parameters_limit[parameter_name] = 'NORMAL'
    parameters_action[parameter_name] = 'Alles ist in Ordnung, nichts muss getan werden'
