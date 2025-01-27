import requests
import pandas as pd
import os
import time

# Your USDA API key
API_KEY = "*******"  # Replace with your actual API key

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Function to fetch data with pagination
def fetch_data(query, max_pages=50, page_size=50):
    """
    Fetch data for a given query using pagination.
    - max_pages: Maximum number of pages to fetch.
    - page_size: Number of results per page (maximum is 100 for USDA API).
    """
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    all_foods = []

    for page in range(1, max_pages + 1):
        params = {
            "query": query,
            "pageSize": page_size,
            "pageNumber": page,
            "api_key": API_KEY,
        }
        try:
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if "foods" in data and data["foods"]:
                    for food in data["foods"]:
                        # Safeguard against missing nutrient data
                        nutrients = {
                            nutrient.get('nutrientName', 'Unknown'): nutrient.get('value', None)
                            for nutrient in food.get("foodNutrients", [])
                        }
                        all_foods.append({
                            "Description": food.get("description"),
                            "Category": food.get("foodCategory"),
                            "Brand": food.get("brandOwner"),
                            "Calories": nutrients.get("Energy", None),
                            "Protein": nutrients.get("Protein", None),
                            "Fat": nutrients.get("Total lipid (fat)", None),
                            "Carbs": nutrients.get("Carbohydrate, by difference", None),
                        })
                else:
                    print(f"No more data on page {page} for query '{query}'.")
                    break
            else:
                print(f"Error {response.status_code} on page {page} for query '{query}': {response.text}")
                break

            # Pause between requests to avoid API rate limits
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for query '{query}' on page {page}: {e}")
            break

    return all_foods

# Reduced list of queries for slightly less data
queries = [
    "soda", "chips", "cookies", "candy", "snacks", "fast food",
    "pizza", "burger", "ice cream", "energy drinks", "bread",
    "sandwich", "fries", "milkshake", "chocolate"
]

all_foods = []

# Fetch data for each query and aggregate results
for query in queries:
    print(f"Fetching data for query: {query}")
    foods = fetch_data(query, max_pages=50, page_size=50)  # Limit to 50 pages and 50 items per page
    all_foods.extend(foods)

# Save data to a CSV file
df = pd.DataFrame(all_foods)
print(f"Total records fetched: {len(all_foods)}")  # Debugging statement
if not df.empty:
    df.to_csv("data/raw_data.csv", index=False)
    print(f"Raw data saved to data/raw_data.csv. Total records: {len(df)}")
else:
    print("No data fetched. Please check your API key or queries.")