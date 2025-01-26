# USDA Food Analysis Project

This project analyzes nutritional data for ultra-processed foods and their potential impact on public health. The project uses the USDA FoodData Central API to fetch data and applies machine learning techniques to analyze trends and relationships. The entire project will be presented on a website built from scratch using HTML, CSS, and JavaScript.

---

## Structure
```plaintext
USDA_FOOD/
├── data/
│   ├── raw_data.csv       # Raw dataset fetched from the USDA API
│   ├── cleaned_data.csv   # Cleaned and preprocessed dataset
├── visuals/               # Stores generated visualizations
│   ├── bar_chart.png
│   ├── scatter_plot.png
├── src/
│   ├── fetch_data.py      # Script for fetching data from USDA API
│   ├── clean_data.py      # Script for cleaning and preprocessing data
│   ├── visualize_data.py  # Script for creating visualizations
├── website/
│   ├── index.html         # Main HTML file for the website
│   ├── style.css          # CSS file for styling the website
│   ├── script.js          # JavaScript for interactivity
│   ├── images/            # Folder to store images and visualizations
│   ├── data/              # Downloadable raw and cleaned datasets
├── README.md              # Detailed project documentation
├── requirements.txt       # Python dependencies