import requests


def get_weather(city):
    if not city.strip():
        return "Ошибка: название города не может быть пустым."
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе: {e}"


city = input("Введите название города: ")
weather = get_weather(city)
print(weather)
