personer_dict = {}

# person? 
# -> namn, personnummer, ålder, kön, längd, vikt, favoritsaker
personer_dict.update(
    {'199901015555': 
        {'namn': 'Lina',
        'ålder': '22',
        'vikt': '55',
        'kön': 'Kvinna',
        'längd': '179',
        'favoritsaker': []
        },

     '188501047777': 
        {'namn': 'Kalle',
         'ålder': '23', 
         'vikt': '77', 
         'kön': 'Anka', 
         'längd': '150', 
         'favoritsaker': ['Brorsöner', 'Mat', 'Pengar']
        }
        }
    )

while True:
    personnummer = input('Ange personnummer: ')
    # ------------------- Uppdaterar en person ---------------------
    if personnummer in personer_dict.keys():
        # print('Personen med det personnummret finns redan!!')
        hämtad_person = personer_dict[personnummer]
        print('---- Person -----')
        for key, val in hämtad_person.items():
            print(f"{key} -> {val}")

        uppdatera = input('Vill du uppdatera uppgifterna? (y/n):')

        if uppdatera == 'y':
            while True:
                print('1. Uppdatera namn')
                print('2. Uppdatera kön')
                print('3. Uppdatera vikt')
                print('4. Uppdatera ålder')
                print('5. Uppdatera längd')
                print('6. Lägg till favoritsak')
                print('7. Ta bort favoritsak')
                print('8. Ta bort personen')
                print('9. Avsluta')
                menyval = input('Ange ett val:')

                if menyval == '1':
                    nytt_namn = input('Ange nytt namn!')
                    hämtad_person['namn'] = nytt_namn
                    #personer[personnummer][namn] = nytt_namn

                elif menyval == '2':
                    pass
                elif menyval == '3':
                    pass
                elif menyval == '4':
                    pass
                elif menyval == '5':
                    pass
                elif menyval == '6':
                    ny_favoritsak = input('Skriv in en ny favoritsak: ')

                    hämtad_person['favoritsaker'].append(ny_favoritsak)
                    # hämtad_person['favoritsaker'] += [ny_favoritsak] 
                    # hämtad_person['favoritsaker'] -> []

                elif menyval == '7':
                    sak_att_ta_bort = input('Skriv in sak att ta bort: ')
                    if sak_att_ta_bort in hämtad_person['favoritsaker']:
                        hämtad_person['favoritsaker'].remove(sak_att_ta_bort)
                    else:
                        print('Saken fanns inte bland favoritsaker!!!')

                elif menyval == '8':
                    if input('Är du säker på att du vill ta bort personen? (yes/no)') == 'yes':
                        print(personer_dict.pop(personnummer))
                        break

                elif menyval == '9':
                    break
                else:
                    print('Ogiltligt val!')

    # ------------------- Skapar en ny person ---------------------
    else:
        print('--------- Skapa en person ---------')
        namn = input('Ange namn: ')
        ålder = input('Ange ålder:')
        vikt = input('Ange vikt: ')
        kön = input('Ange kön: ')
        längd = input('Ange längd')

        favoritsaker = []

        while True:
            if input('Vill du ange en favoritsak? (y/n): ') == 'y':
                favosak = input('Ange en favoritsak: ')
                favoritsaker.append(favosak)
            else:
                break
        
        personer_dict[personnummer] = {
            "namn":namn,
            "ålder":ålder,
            "vikt":vikt,
            "kön":kön,
            "längd":längd,
            "favoritsaker":favoritsaker
            }
        
        if input('Vill du fortsätta? (y/n): ') == "n":
            break
    
print(personer_dict)
    
