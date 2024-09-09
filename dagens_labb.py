LEDIG = True

idrottshall = {
    "bowling":{1:{}, 2:{}, 3:{}},
    "badminton":{1:{}, 2:{}, 3:{},4:{},5:{}},
    "tennis":{1:{}, 2:{}, 3:{}, 4:{}}
    } 

for sport in idrottshall.keys():
    
    for bana in idrottshall[sport]:

        for tid in range(9,22):
            
            idrottshall[sport][bana][tid] = LEDIG



print('Välkommen till Sunes Idrottspalats!')
while True:
    print('1. Boka')
    print('2. Avboka')
    print('3. Skriv ut bokningar')
    print('4. Avsluta')

    meny_val = input('Gör ett val: ')

    if meny_val == '1':
        while True:
            print('Välj önskad sport att boka')
            print('1. Bowling')
            print('2. Badminton')
            print('3. Tennis')
            sport_val = input('Sportid: ')
            valet_av_sport = ''

            if sport_val == '1':
                valet_av_sport = 'bowling'

            elif sport_val == '2':
                valet_av_sport = 'badminton'

            elif sport_val == '3':
                valet_av_sport = 'tennis'
            else:
                print('Ogiltligt val!')

            if valet_av_sport != '': break

        while True:
            ban_val = input('Ange bannummer: ')

            if ban_val.isdigit():
                ban_val = int(ban_val)

                if ban_val in idrottshall[valet_av_sport]:
                    break
                else:
                    print('Ogiltligt bannummer!')

            else:
                print('Ogiltligt bannummer!')

        while True:
            tidsbokning = input('Ange tid, 9-21 eller q för att avsluta: ')
            if tidsbokning == 'q': break

            if tidsbokning.isdigit() and 9 <= int(tidsbokning) <= 21:

                är_ledig = idrottshall[valet_av_sport][ban_val][int(tidsbokning)]

                if är_ledig:
                    idrottshall[valet_av_sport][ban_val][int(tidsbokning)] = not LEDIG
                    print(f'Bana {ban_val} för {valet_av_sport} är bokad kl {tidsbokning}!\nVälkommna då!!')
                else:
                    print('Tyvärr, tiden är redan bokad!')

            else:
                print('Ogiltligt val av tid!')



    elif meny_val == '2':
        pass

    elif meny_val == '3':
        # Skriver ut allt snyggt!
        for sport in idrottshall:
            print(f"Sport: {sport}")
            for bana in idrottshall[sport]:
                print(f'\tBanid {bana}')
                for tid, ledig in idrottshall[sport][bana].items():
                    print(f'\t\t{tid}:{ledig}')

    elif meny_val == '4':
        break
    else:
        print('Ogiltligt val!')