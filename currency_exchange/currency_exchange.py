import requests

def main():
    cache = {}

    currency = input("Введіть код вашої валюти (наприклад, USD):").strip().lower()
    url = f"http://www.floatrates.com/daily/{currency}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json()
    except Exception as e:
        print(f"Не вдалось отримати данні: {e}")
        return

    for code in ['usd', 'eur']:
        if code != currency and code in rates:
            cache[code] = rates[code]

    while True:
        target_currency = input("\nВведіть валюту, яку хочете отримати (або Enter для завершення): ").strip().lower()
        if not target_currency:
            break

        try:
            amount = float(input("Введіть суму для обміну: ").strip())
        except ValueError:
            print("Неправильне значення суми.")
            continue

        print("Checking the cache...")

        if target_currency in cache:
            print("It is in the cache!")
            rate = cache[target_currency]['rate']
        else:
            print("Sorry, but it is not in the cache!")
            if target_currency in rates:
                cache[target_currency] = rates[target_currency]
                rate = rates[target_currency]['rate']
            else:
                print(f"Валюта {target_currency.upper()} не знайдена.")
                continue

        received = amount * rate
        print(f"You received {round(received, 2)} {target_currency.upper()}.")

if __name__ == "__main__":
        main()
