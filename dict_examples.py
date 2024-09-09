my_dict = {'hälsning':'Tjabba tjena hallå!!'}

# print(my_dict)
# print(type(my_dict))

# print(my_dict['hälsning'])
# print(type(my_dict['hälsning']))

my_dict['hälsning'] = my_dict['hälsning'] + 'Hur mår du?'
# my_dict['hälsning'] += 'Hur mår du?'

# print(my_dict['hälsning'])
# print(type(my_dict['hälsning']))

my_dict.update({'avskedshälsning':'Hej då, tack för idag!'})
my_dict.update([(1,2),(3,4)])

# my_dict['avskedshälsning'] = 'Hej då, tack för idag!'

print(my_dict)

