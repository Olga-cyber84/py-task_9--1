import requests


def get_most_intelligence(superheroes, superheroes_for_testing):
    counter = 0
    most_intelligence_superhero = ''
    for superhero in superheroes:
        for hero in superheroes_for_testing:
            if superhero["name"] == hero and superhero["powerstats"]["intelligence"] > counter:
                counter = superhero["powerstats"]["intelligence"]
                most_intelligence_superhero = superhero["name"]
    print(f"The most intelligence superhero is {most_intelligence_superhero}")
    return most_intelligence_superhero


if __name__ == '__main__':
    superheroes_for_testing = ["Hulk", "Captain America", "Thanos"]
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(url+'/all.json')
    get_most_intelligence(response.json(), superheroes_for_testing)
