import requests
from bs4 import BeautifulSoup as bs


class DataContainer:
    def __init__(self):
        self.countries = []
        self.no_countries_infected = 0
        self.total_cases = 0
        self.total_recoverd = 0
        self.total_deaths = 0
        self.table = []


class DataPipe:
    def __init__(self, container):
        URL = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory'

        try:
            RESPONSE = requests.get(URL, verify=False)
        except:
            exit('Make sure requests has access to internet')

        assert RESPONSE.ok, f'Response from requests is not ok {RESPONSE.STATUS_CODE}'

        self.container = container

        self.soup = bs(RESPONSE.content, 'html5lib')
        self.data_table = self.soup.find('div', {'id': 'covid19-container'})

        self.table_data = []

        self._update()

    def _update(self):
        total_cases = self.data_table.tbody.find_all('tr')[1]
        total_cases = total_cases.text.strip().split('\n\n')

        self.container.total_deaths = total_cases[2]
        self.container.total_cases = total_cases[1]
        self.container.total_recoverd = total_cases[3]

        first_row = self.data_table.tbody.find_all('tr')[2:]

        for row in first_row:
            if len(row.text.split()) <=6:
                row = row.text.split('\n')
                data_row = []
                [data_row.append(element) for element in row if element != '']
                self.table_data.append(data_row[:-1])

                country = data_row[0].strip()
                country = country.replace(' ', '_')
                country = country.replace('-', '_')
                cases = data_row[1]
                dead = data_row[2]

                if data_row[3] == '–':
                    recover = '0'
                else:
                    recover = data_row[3]

                clean_row = []

                if '(' in country:
                    self.container.countries.append(country[: country.find('(')].strip())
                    clean_row.append(country[: country.find('(')])
                    clean_row.append(cases.replace(',', '.'))
                    clean_row.append(dead.replace(',', '.'))
                    clean_row.append(recover.replace(',', '.'))
                    self.container.table.append(clean_row)

                elif '[' in country:
                    self.container.countries.append(country[: country.find('[')].strip())
                    clean_row.append(country[: country.find('[')].strip())
                    clean_row.append(cases.replace(',', '.'))
                    clean_row.append(dead.replace(',', '.'))
                    clean_row.append(recover.replace(',', '.'))
                    self.container.table.append(clean_row)

                else:
                    self.container.countries.append(country.strip())
                    clean_row.append(country.strip())
                    clean_row.append(cases.replace(',', '.'))
                    clean_row.append(dead.replace(',', '.'))
                    clean_row.append(recover.replace(',', '.'))
                    self.container.table.append(clean_row)

if __name__ == '__main__':
    coronavirus_data = DataContainer()

    data = DataPipe(coronavirus_data)

    print()
    print('Total global cases : ', coronavirus_data.total_cases)
    print('Total global deatsh : ', coronavirus_data.total_deaths)
    print('Total global revoverd : ', coronavirus_data.total_recoverd)
    print()

    for country in coronavirus_data.table:
        print(country)
