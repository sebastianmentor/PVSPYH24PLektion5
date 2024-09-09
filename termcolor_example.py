# Kom ihåg att köra i terminalen: pip install termcolor 

from termcolor import colored

# Enkel text i olika färger
print(colored("Detta är en text i rött", "red"))
print(colored("Detta är en text i grönt", "green"))
print(colored("Detta är en text i blått", "blue"))

# Text med färgad bakgrund
print(colored("Text med gul bakgrund", "white", "on_yellow"))
print(colored("Text med röd bakgrund", "white", "on_red"))

# Text med attribut (fetstil och understruken)
print(colored("Detta är en fetstilad text", "cyan", attrs=["bold"]))
print(colored("Detta är en understruken text", "magenta", attrs=["underline"]))

# Kombinera flera attribut och färger
print(colored("Flera attribut: fet och understruken", "yellow", "on_blue", attrs=["bold", "underline"]))
"""
Förklaring:
1. colored(): 
    Huvudfunktionen i termcolor. Den tar argument för:
        text: Strängen du vill färga.
        färg: Färgen på texten (t.ex. "red", "green", "blue", etc.).
        bakgrundsfärg (valfritt): Färgen på bakgrunden (börjar med "on_", t.ex. "on_yellow", "on_red").
        attrs (valfritt): Attribut som "bold", "underline", "blink" m.m.
        
    Tillgängliga färger:
    Textfärger: grey, red, green, yellow, blue, magenta, cyan, white
    Bakgrundsfärger: Samma färger, men med prefix "on_" (t.ex. on_red, on_green)
"""