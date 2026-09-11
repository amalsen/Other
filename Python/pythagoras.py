import math

while True:
    utregning = str(input("Skal du finne hypotenus (h) eller en katet (k)? ")).lower()
    
    if utregning == str("h"):
        while True:
            try:
                kat1 = float(input("Lengde på katet 1: "))
                kat2 = float(input("Lengde på katet 2: "))
            except ValueError:
                print("Vennligst skriv inn tall.")
            except:
                print("Uventet feil oppsto.")
            else:
                hyp = math.sqrt((kat1 ** 2) + (kat2 ** 2))
                print(f"Lengde på hypotenusen: {hyp}")
                break
    elif utregning == str("k"):
        while True:
            try:
                hyp = float(input("Lengde på hypotenusen: "))
                kat1 = float(input("Lengde på katet 1: "))
            except ValueError:
                print("Vennligst skriv inn tall.")
            except:
                print("Uventet feil oppsto.")
            else:
                kat2 = math.sqrt((hyp ** 2) - (kat1 ** 2))
                print(f"Lengde på katet 2: {kat2}")
                break
    else:
        print("Vennligst velg et gyldig alternativ. (h/k)")
        continue
    break
