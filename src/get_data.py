import sys, time, random, json, re
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}
base_url = "https://losangeles.craigslist.org/search/apa?"
cities = ["downtown+long+beach", "cerritos", "redondo+beach", "corona", "malibu"]

session = requests.Session()
session.headers.update(HEADERS)

num_rooms = sys.argv[1] if len(sys.argv) > 1 else "2"

def get_square_footage(listing_url, session):
    try:
        res = session.get(listing_url)
        if res.status_code != 200:
            return None
        soup = BeautifulSoup(res.text, 'html.parser')
        housing = soup.find("span", class_="housing")
        if housing:
            match = re.search(r'(\d+)\s*ft2', housing.get_text().lower())
            if match:
                return int(match.group(1))
    except Exception:
        pass
    return None

def scrape_for_rooms(num_rooms, session, cities, base_url):
    all_htmls = {}
    for city in cities:
        url = f"{base_url}query={city}&min_bedrooms={num_rooms}&max_bedrooms={num_rooms}"
        req = session.get(url)
        print(city, req.status_code)
        if req.status_code == 200:
            all_htmls[city] = req.text
        else:
            raise Exception("Failed to retrieve the page")
        time.sleep(random.uniform(2, 5))

    scraped_results = []
    apartment_counter = 1

    for city, html in all_htmls.items():
        soup = BeautifulSoup(html, 'html.parser')
        listings = soup.find_all("li", class_="cl-static-search-result")
        seen = set()
        unique_count = 0

        for listing in listings:
            title = listing.find("div", class_="title")
            price = listing.find("div", class_="price")
            link = listing.find("a")

            title_text = title.get_text(strip=True) if title else None
            price_text = price.get_text(strip=True) if price else None
            listing_url = link.get("href") if link else None
            parsed_price = int(price_text.replace("$", "").replace(",", "")) if price_text else None

            if not parsed_price or parsed_price == 0:
                continue

            square_footage = get_square_footage(listing_url, session) if listing_url else None

            key = (title_text.lower() if title_text else None, price_text)
            if key in seen:
                continue
            seen.add(key)

            scraped_results.append({
                "apartment_id": apartment_counter,
                "city": city.replace("+", " ").title(),
                "listing_title": title_text,
                "price": parsed_price,
                "beds": num_rooms,
                "square_footage": square_footage,
                "listing_url": listing_url
            })
            apartment_counter += 1
            unique_count += 1
            if unique_count == 50:
                break
    return scraped_results

all_results = scrape_for_rooms(num_rooms, session, cities, base_url)

with open("data/raw/listings.json", "w") as f:
    json.dump(all_results, f)
