import matplotlib.pyplot as plt

from docs_csv import read_csv

def run():
    data = read_csv.read_csv('./docs_csv/world_population.csv')
    data = list(filter(lambda item: item['Continent'] == 'North America', data))

    # Ordena los datos por población en orden descendente
    data.sort(key=lambda x: float(x['World Population Percentage']), reverse=True)

    # Toma solo los primeros 10 países más poblados
    top_countries = data[:10]

    # Suma los porcentajes de población de los países restantes para "otros"
    other_percentage = sum(float(item['World Population Percentage']) for item in data[10:])

    # Crea listas para los nombres de los países y sus respectivos porcentajes de población
    countries = [item['Country/Territory'] for item in top_countries]
    percentages = [float(item['World Population Percentage']) for item in top_countries]

    # Agrega "otros" a las listas
    countries.append('Otros')
    percentages.append(other_percentage)

    # Configura el gráfico de pastel con etiquetas y porcentajes
    plt.pie(percentages, labels=countries, autopct='%1.1f%%', startangle=180)

    # Añade título
    plt.title('Distribución de población en América del Norte')

    # Muestra el gráfico
    plt.show()

if __name__ == '__main__':
    run()
