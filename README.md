# covid19-module-py
Project that uses the Covid-19 module in python to obtain information on current covid cases around the world.

![cover](https://user-images.githubusercontent.com/76132256/127327672-52a24802-901a-4f01-911f-347f1f79f10d.png)

<br /><br /><br /><br />

## Requirements
Python version must be 3.6 or higher  <br /><br />

## How to install the module
1. Open CMD
2. Type `pip install covid`  <br /><br />

## Importing the module
The instruction is:<br />
`from covid import Covid`<br />
(IMPORTANT: The second 'C' is MAYUS)  <br />

First of all, it is necessary to call to the method `Covid` and save it into a variable (I called it "covid")  <br />
`covid = Covid()` 
###### NOTE: The default database is Johns Hopkins university; If you want to change it, the instruction is:  
`covid = Covid(source="worldometers")`  
###### Replace "worldometers" by the name of another covid database  <br /><br />

## How covid module works
### Get the 'id' and 'name' of all the countries (--> dictionary)
`countries = covid.list_countries()`
##### Printing it
```
for country in countries:
    print(country)
```
##### Output
![list-countries](https://user-images.githubusercontent.com/76132256/127326537-02a5dabd-560b-4c65-90af-fa4f2fd53a40.png)
<br /><br />

### Get all the data by a country's ID (--> dictionary)
`spain_cases = covid.get_status_by_country_id(165)`
##### Printing it
`print("\nSpain Data: ", spain_cases)`
##### Output
![spain-data](https://user-images.githubusercontent.com/76132256/127326593-4a5b03dd-3e20-45ea-bd34-f67693b0e4fc.png)
<br /><br /><br />

### Get all the data by a country's name (--> dictionary)
`italy_cases = covid.get_status_by_country_name("italy")`
##### Printing it
`print("\nItaly Data: ", italy_cases)`
##### Output
![italy-data](https://user-images.githubusercontent.com/76132256/127326628-deacdc16-a6cd-46d0-a0dc-23c83c144c8c.png)
<br /><br /><br />

### Get the global cases (--> int)
#### Active
`active = covid.get_total_active_cases()`
<br />

#### Confirmed
`confirmed = covid.get_total_confirmed_cases()`
<br />

#### Recovered
`recovered = covid.get_total_recovered()`
<br />

#### Deaths
`deaths = covid.get_total_deaths()`
<br />

##### Printing it
```
print(f"\n\
Total active cases: {active};\n\
Total confirmed cases: {confirmed};\n\
Total recovered cases: {recovered};\n\
Total deaths cases: {deaths};\n\
")
```
##### Output
![global-data](https://user-images.githubusercontent.com/76132256/127326717-506d477e-677e-48a1-bf57-dd7e629811cd.png)
<br /><br /><br />

You can find all the documentation [here](https://ahmednafies.github.io/covid/)
