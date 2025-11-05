"""
Tiny arty Python math script,
which asks for insertion of a given value for either radius, area or perimeter of a circle.
Calculating the not-given values from the given one 
Printing out all values.

A dictionary with nested dictionaries gets iterated by List-Comprehension algorithms and calculated by the built-in eval function.
"""

import math
## Constants
PI = math.pi
## The dictionary 'job' contains the user input() dialog string as well as nested formula strings
job = {'input' : "First insert 'radius', 'area' oder 'perimeter' as given value-type and confirm by pressing Enter..."
                 +"Second insert the associated numbers. Floating point or integer are allowed:",
       'formula': {
                                           # Nested values will later be used as math formula in eval()
                                           # Each key represents the source variable which is given by the user input
                                           # Each value contains the needed formulas for deriving the two unknowns
                    'radius':   {'radius' :"zahl",
                                'perimeter' : "2* PI * zahl",
                                'area': "PI * zahl**2"
                                },
                    'perimeter':{'perimeter' : "zahl",
                                'radius' : "zahl / PI / 2",
                                'area': "PI * zahl**2"
                                },
                    'area':     {'area': "zahl",
                                'radius' : "math.sqrt(zahl/PI)",
                                'perimeter' : "2* PI * zahl"
                                }                        },
                    'circle' :  {'radius':   0.0,
                                'perimeter':   0.0,
                                'area':  0.0
                                }
       }

## Function
def circleberechnung(
                    variante:str="radius",  # bei ausbleibender Eingabe variante = 'radius'
                    zahl:float=0.0, 
                    formula:dict={}
                    )->dict:
    formula = formula[variante]

    return  { attribut : eval(  #return LC { KEY  : Value} <- LC Syntax für Dictionaries
                                formel,                 # Rechen-Formel
                                {'math':math,'PI':PI},  # globale Variablen für eval()
                                {'zahl':zahl}           # lokale Variablen        "
                            )   for attribut,formel     # key,value Paare zB:'perimeter',"2*PI*zahl"
                                in formula.items()      # Quelle aus der alle key,value Paare exportiert werden
            } 
## Execution
job['circle']= circleberechnung(  input(job['input']),
                                float(input()),
                                job['formula']
                             )

## Printing results
print(''.join(  # join(), damit print() eine LC ausgibt.
                # LC, die f-strings generiert
                f"{ergebnistyp}  ->  {str(wert):<12.6}\n" 
                for ergebnistyp,wert in job['circle'].items()
            )
    )