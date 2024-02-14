from utils import utils
from docs_csv import read_csv

import charts

data = read_csv.read_csv('./docs_csv/world_population.csv')
country = input('Type Country => ')

result = utils.population_by_country(data, country)

if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

