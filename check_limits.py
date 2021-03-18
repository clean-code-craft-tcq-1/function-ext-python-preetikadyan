from raise_alert_for_battery_parameters import *

limit = {
     'temperature': {'min': 0, 'max': 45},
     'state_of_charge': {'min': 20, 'max': 80},
     'charge_rate': {'min' : 0, 'max': 0.8}
        }  

alert_logs = {
                'EN':['LOW_BREACH','HIGH_BREACH','LOW_WARNING','HIGH_WARNING','NORMAL'],
                'DE':['NIEDRIGER VERLETZUNG','HOHE VERLETZUNG','NIEDRIGE WARNUNG','HOHE WARNUNG','NORMAL']
            }

collector_logs = {
                    'EN' : ['Parameter needs to be increased for the given parameter to cross lower limit',
                            'Switch on fan to bring the given parameter below max limit',
                            'Increase the given parameter to avoid lower limit breach',
                            'Switch on fan to avoid higher limit breach',
                            'Everything is fine, nothing needs to be done'],
                    'DE' : ['Der Parameter muss erhöht werden, damit der angegebene Parameter die Untergrenze überschreitet',
                            'Schalten Sie den Lüfter ein, um den angegebenen Parameter unter die maximale Grenze zu bringen',
                            'Erhöhen Sie den angegebenen Parameter, um eine Verletzung der unteren Grenze zu vermeiden',
                            'Schalten Sie den Lüfter ein, um eine Überschreitung der Obergrenze zu vermeiden',
                            'Alles ist in Ordnung, nichts muss getan werden']
        
              }
    
if __name__ == '__main__':
     raise_alert_for_battery_parameters({'temperature' : 25, 'state_of_charge' : 70, 'charge_rate' : 0.7},'DE')
     raise_alert_for_battery_parameters({'temperature' : 50, 'state_of_charge' : 85, 'charge_rate' : 0},'EN')
