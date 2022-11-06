import requests
import json

# Зробити виклик через API та зберегти відповідь

for step in range(0, 250, 50):
    url = f'https://russianwarship.rip/api/v1/statistics?offset={step}&limit=50'
    r = requests.get(url)  # Робимо запит
    print(f"Status code: {r.status_code}")  # Атрибут status_code повідомляє нам, чи був запит успішним
    # Зберегти відповідь API у змінну
    response_dict = r.json()
    file_name = f'data/statistics_step_{step}.json'
    with open(file_name, 'w') as f:
        json.dump(response_dict, f, indent=4)
