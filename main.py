# import csv.read_csv as read_csv
import charts
from docs_csv import read_csv


def run():
    data = read_csv.read_csv('./docs_csv/world_population.csv')
    data = list(filter(lambda item : item['Continent'] == 'North America',data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
if __name__ == '__main__':
    run()
