goals = {}

while True:
    player_id = input('Skriv in spelarens nummer: ')
    players_points = input('Skriv in poäng att lägga till: ')

    if player_id.isdigit() and players_points.isdigit():
        player_id = int(player_id)  
        players_points = int(players_points)

        # Hur kan man göra det här med en if endast???
        if player_id in goals:
            goals[player_id] = goals[player_id] + players_points
        else:
            goals[player_id] = 0
            goals[player_id] = goals[player_id] + players_points

    else:
        print('Måste vara heltal dummer! Annars kraschar programmet!!')

    if input('Vill du fortsätta (y/n): ') == 'n':
        break

print(goals)

    