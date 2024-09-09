name_age_dict = {} # dict()

run_program = True
while run_program == True:
    name = input('Vänligen skriv in ett namn: ')
    age = input(f'Vänligen skriv in {name}s ålder:')

    name_age_dict[name] = age

    if input('Vill du fortsätta (y/n): ') == 'n':
        print(name_age_dict)
        run_program = False
        continue

    print('Då kör vi igen!')


for key, value in name_age_dict.items():
    print(f'{key} är {value} gammal!!')