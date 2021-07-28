from covid import Covid

# Por defecto la base de datos es "john_hopkins"
covid = Covid()

# Para obtener los datos de worldometers.info
#covid = Covid(source="worldometers")

# Todos los países
countries = covid.list_countries()
for country in countries:
    print(country)

# Datos de un país por ID
spain_cases = covid.get_status_by_country_id(165)
print("\nSpain Data: ", spain_cases)
# {'id': '165', 'country': 'Spain', 'confirmed': 4342054, 'active': 4110410, 'deaths': 81268, 'recovered': 150376, 'latitude': 40.463667, 'longitude': -3.74922, 'last_update': 1627395686000}

# Datos de un país por nombre del país
italy_cases = covid.get_status_by_country_name("italy")
print("\nItaly Data: ", italy_cases)
# {'id': '86', 'country': 'Italy', 'confirmed': 4320530, 'active': 68236, 'deaths': 127971, 'recovered': 4124323, 'latitude': 41.8719, 'longitude': 12.5674, 'last_update': 1627395686000}

#---------------------------------------------------
# Total de casos activos
active = covid.get_total_active_cases()

# Total de casos confirmados
confirmed = covid.get_total_confirmed_cases()

# Total de casos recuperados
recovered = covid.get_total_recovered()

# Total de muertes
deaths = covid.get_total_deaths()

print(f"\n\
Total active cases: {active};\n\
Total confirmed cases: {confirmed};\n\
Total recovered cases: {recovered};\n\
Total deaths cases: {deaths};\n\
")
