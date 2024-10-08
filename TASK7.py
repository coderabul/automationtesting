#1) 
import requests

class Country:
    def __init__(self, name, capital, population, area, languages):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        self.languages = languages

    def display_info(self):
        print(f"Country: {self.name}")
        print(f"Capital: {self.capital}")
        print(f"Population: {self.population}")
        print(f"Area: {self.area} square kilometers")
        print("Languages:")
        for lang in self.languages:
            print(f"- {lang}")
        print()


class CountryInfoFetcher:
    def fetch_countries_info(self):
        try:
            response = requests.get("https://restcountries.com/v3.1/all")
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return []

    def display_countries_info(self, countries):
        for country_data in countries:
            country = self.create_country_object(country_data)
            country.display_info()

    def create_country_object(self, country_data):
        name = country_data.get("name", "N/A")
        capital = country_data.get("capital", "N/A")
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        languages = country_data.get("languages", [])
        return Country(name, capital, population, area, languages)


if __name__ == "__main__":
    info_fetcher = CountryInfoFetcher()
    countries_info = info_fetcher.fetch_countries_info()
    info_fetcher.display_countries_info(countries_info)
#2)
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_countries_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return []

    def display_countries_info(self, countries):
        for country_data in countries:
            self.display_country_info(country_data)

    def display_country_info(self, country_data):
        name = country_data.get("name", "N/A")
        capital = country_data.get("capital", "N/A")
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        languages = country_data.get("languages", [])
        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        print(f"Area: {area} square kilometers")
        print("Languages:")
        for lang in languages:
            print(f"- {lang}")
        print()


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    countries_info = info_fetcher.fetch_countries_info()
    info_fetcher.display_countries_info(countries_info)
#3)
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_json_data(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching JSON data:", e)
            return None


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    json_data = info_fetcher.fetch_json_data()
    if json_data:
        print(json_data)
#4)
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_countries_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return None

    def display_country_info(self, countries):
        for country_data in countries:
            name = country_data.get("name", "N/A")
            currencies = country_data.get("currencies", [])
            currency_symbols = [currency.get("symbol", "N/A") for currency in currencies]
            print(f"Country: {name}")
            print("Currency Symbols:", ", ".join(currency_symbols))
            print()


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    countries_info = info_fetcher.fetch_countries_info()
    if countries_info:
        info_fetcher.display_country_info(countries_info)
#5)
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_countries_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return None

    def display_countries_with_dollar_currency(self, countries):
        dollar_countries = []
        for country_data in countries:
            name = country_data.get("name", "N/A")
            currencies = country_data.get("currencies", [])
            currency_names = [currency.get("name", "") for currency in currencies]
            if "DOLLAR" in currency_names:
                dollar_countries.append(name)
        if dollar_countries:
            print("Countries with DOLLAR as currency:")
            for country in dollar_countries:
                print(country)
        else:
            print("No countries found with DOLLAR as currency.")


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    countries_info = info_fetcher.fetch_countries_info()
    if countries_info:
        info_fetcher.display_countries_with_dollar_currency(countries_info)
#6) 
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_countries_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return None

    def display_countries_with_euro_currency(self, countries):
        euro_countries = []
        for country_data in countries:
            name = country_data.get("name", "N/A")
            currencies = country_data.get("currencies", [])
            for currency in currencies:
                if "code" in currency and currency["code"] == "EUR":
                    euro_countries.append(name)
                    break
        if euro_countries:
            print("Countries with EURO as currency:")
            for country in euro_countries:
                print(country)
        else:
            print("No countries found with EURO as currency.")


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    countries_info = info_fetcher.fetch_countries_info()
    if countries_info:
        info_fetcher.display_countries_with_euro_currency(countries_info)
#B) 
#1)
import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_countries_info(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            return data
        except requests.RequestException as e:
            print("Error fetching country information:", e)
            return None

    def display_countries_with_euro_currency(self, countries):
        euro_countries = []
        for country_data in countries:
            name = country_data.get("name", "N/A")
            currencies = country_data.get("currencies", [])
            for currency in currencies:
                if "code" in currency and currency["code"] == "EUR":
                    euro_countries.append(name)
                    break
        if euro_countries:
            print("Countries with EURO as currency:")
            for country in euro_countries:
                print(country)
        else:
            print("No countries found with EURO as currency.")


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    info_fetcher = CountryInfoFetcher(url)
    countries_info = info_fetcher.fetch_countries_info()
    if countries_info:
        info_fetcher.display_countries_with_euro_currency(countries_info)
#2)
import requests

def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch breweries for {state}.")
        return []

def count_breweries_in_states(states):
    for state in states:
        breweries = fetch_breweries_by_state(state)
        brewery_count = len(breweries)
        print(f"Number of breweries in {state}: {brewery_count}")

if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    count_breweries_in_states(states)
#3) 
import requests

def fetch_breweries_by_state_and_city(state, city):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&by_city={city}&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch breweries for {city}, {state}.")
        return []

def count_brewery_types_in_cities(states):
    for state in states:
        print(f"State: {state}")
        cities = set()
        breweries_count = 0
        breweries_by_city = {}

        # Fetch breweries for the state
        breweries = fetch_breweries_by_state_and_city(state, "")

        # Count the number of types of breweries in each city
        for brewery in breweries:
            city = brewery.get('city', 'Unknown')
            if city not in cities:
                cities.add(city)
                breweries_by_city[city] = set()
            brewery_type = brewery.get('brewery_type', 'Unknown')
            breweries_by_city[city].add(brewery_type)
            breweries_count += 1

        # Print the count of types of breweries in each city
        for city, types in breweries_by_city.items():
            print(f"City: {city}, Number of Brewery Types: {len(types)}")
        print(f"Total Breweries in {state}: {breweries_count}")
        print()

if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    count_brewery_types_in_cities(states)
#4)
import requests

def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&per_page=50"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch breweries for {state}.")
        return []

def count_and_list_breweries_with_websites_in_states(states):
    for state in states:
        print(f"State: {state}")
        breweries = fetch_breweries_by_state(state)
        breweries_with_websites = [brewery for brewery in breweries if brewery.get('website_url')]
        brewery_count_with_websites = len(breweries_with_websites)
        print(f"Number of Breweries with Websites in {state}: {brewery_count_with_websites}")
        if breweries_with_websites:
            print("Breweries with Websites:")
            for brewery in breweries_with_websites:
                print("-", brewery['name'])
        print()

if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    count_and_list_breweries_with_websites_in_states(states)
