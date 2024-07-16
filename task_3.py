world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция'
    }

world_champions[2022] = 'Аргентина'     # Добавляю 2022 год и чемпиона
def run3():
    for year, country in world_champions.items():
        print(year, '-', country)
        # Проверяю, выигрывала ли Италия
        country = 'Италия'
        if country in world_champions.values():
            var ='Италия становилась чемпионом мира по футболу в 21 веке!'
        else:
            var = 'Италия не выигрывала чемпионат мира по футболу в 21 веке.'
    return print(var)
