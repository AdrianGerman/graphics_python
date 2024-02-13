import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Mexico',
        'Population': 500
    },
    {
        'Country': 'Paraguay',
        'Population': 300
    }
]

country = input('Escribe el país => ')

result = utils.population_by_country(data, country)
print(result)