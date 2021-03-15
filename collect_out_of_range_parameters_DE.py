from report_breach_level_DE_warning import *

def collect_out_of_range_parameters_DE(parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang):
    if parameter_value < parameter_min:
         parameters_exceeded_limit[parameter_name] = 'NIEDRIGER VERLETZUNG'
         parameters_action[parameter_name] = 'Der Parameter muss erhöht werden, damit der angegebene Parameter die Untergrenze überschreitet'
    elif parameter_value > parameter_max:
         parameters_exceeded_limit[parameter_name] = 'HOHE VERLETZUNG'
         parameters_action[parameter_name] = 'Schalten Sie den Lüfter ein, um den angegebenen Parameter unter die maximale Grenze zu bringen'
    else:    
        report_breach_level_DE_warning(parameters_action,parameters_exceeded_limit,parameter_name,parameter_value,parameter_min,parameter_max,lang)
