import requests
import json
import pprint

kills_on_episode_count = dict()
max_deaths, top_episode = 0, 0

result = requests.get('https://breakingbadapi.com/api/deaths')
print(result.status_code)

death_list = json.loads(result.text)

for death in death_list:
    if not death['episode'] in kills_on_episode_count.keys():
        kills_on_episode_count[death['episode']] = {"season": death['season'],
                                                    "episode": death['episode'],
                                                    "number_of_deaths": death['number_of_deaths'],
                                                    "death_list": [death['death']]
                                                    }
    else:
        kills_on_episode_count[death['episode']]['number_of_deaths'] += death['number_of_deaths']
        kills_on_episode_count[death['episode']]['death_list'].append(death['death'])
    if kills_on_episode_count[death['episode']]['number_of_deaths'] > max_deaths:
        max_deaths = kills_on_episode_count[death['episode']]['number_of_deaths']
        top_episode = death['episode']

pprint.pprint(kills_on_episode_count[top_episode])

with open('result.json', 'w') as results_file:
    json.dump(kills_on_episode_count[top_episode], results_file, indent=4)





