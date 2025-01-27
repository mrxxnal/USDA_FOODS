# USDA Food Analysis Project

This project investigates the relationship between ultra-processed food consumption and public health, with a focus on obesity and chronic illnesses. Leveraging data from the USDA FoodData Central API, the project explores nutritional trends, applies machine learning techniques, and creates actionable insights. The findings are showcased on a custom-built website using HTML, CSS, and JavaScript.

---

## Project Question

**Does the consumption of ultra-processed foods directly correlate with increased obesity and chronic illness prevalence worldwide, and how can data-driven recommendations help mitigate these health risks?**

---

## Project Goals

- Analyze the nutritional content of ultra-processed foods.
- Identify patterns and trends in the consumption of these foods.
- Explore correlations between food composition and public health outcomes, such as obesity and chronic illnesses.
- Develop machine learning models to predict health risks based on food consumption data.
- Communicate findings through an interactive and visually engaging website.

---

## Structure

```plaintext
USDA_FOOD/
├── data/
│   ├── raw_data.csv       # Raw dataset fetched from the USDA API
│   ├── cleaned_data.csv   # Cleaned and preprocessed dataset
├── visuals/               # Stores generated visualizations
│   ├── bar_chart.png      # Visualization: Bar chart of key findings
│   ├── scatter_plot.png   # Visualization: Scatter plot of correlations
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
│   ├── introduction.html  # Introduction page for the website
│   ├── about_me.html      # About Me page with personal details and GitHub link
├── README.md              # Project documentation (this file)
├── requirements.txt       # Python dependencies