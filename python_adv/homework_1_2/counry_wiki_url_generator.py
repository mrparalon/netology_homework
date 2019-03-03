import json
import os


class CountryIterator():
    URL = "https://en.wikipedia.org/wiki/"
    def __init__(self, filename):
        with open(filename , encoding='utf8') as countries:
            countries_json = json.load(countries)
        self.countries_json = countries_json
        self.country_iter = iter(self.countries_json)

    def __iter__(self):
        self.result_file = open(os.path.join('files','result.txt'), 'a', encoding='utf8')
        return self

    def __next__(self):
        try:
            country = next(self.country_iter)
            country_name = country['name']['common']
            country_name = country_name.replace(' ', '_')
            wiki_url = self.URL + country_name
            result = f"{country_name} - {wiki_url}"
            self.result_file.writelines(result+'\n')
            return result
        except StopIteration:
            self.result_file.close()
            raise StopIteration


if __name__ == "__main__":
    country_iterator = CountryIterator(os.path.join('files', 'countries.json'))
    for url in country_iterator:
        print(url)

