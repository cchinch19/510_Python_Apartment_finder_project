# 510_Python_Apartment_finder_project

Apartment Finder
A tool that scrapes Craigslist apartment listings across 5 Los Angeles neighborhoods, adds  commute times and walk scores, and visualizes the results for analysis. 

Installation
Clone the repository and install the required packages:
requirements.txt: This file lists all the external libraries you have used in your project.
You can create this file manually or use the following commands in your virtual env:
To create this file you can run:
  pip freeze >> requirements.txt
  To install all the required libraries, you can run:
  pip install -r requirements.txt

How to Get the Data
The scraper pulls apartment listings from Craigslist. Run it with the number of bedrooms you want as the argument:
python src/get_data.py 2
This will scrape listings for 2-bedroom apartments across Downtown Long Beach, Cerritos, Redondo Beach, Corona, and Malibu.

How to Clean the Data
Once the data is scraped, run the integration and cleaning scripts to enrich listings with commute times and walk scores:
python src/integrate_data.py
python src/clean_data.py
This will produce a cleaned CSV file at data/processed/apartments.csv.

How to Run the Analysis and Visualizations
Run the visualization script to produce the plots:
python src/analyze_visualize.py
This produces a 2x2 chart saved to results/overview.png with:

Average rent by city
Average price per square foot by city
Commute times to USC and work by city
Walk score and bike score by city

API Keys are hard coded for ease of use 


Project Structure
github_repository_structure/
├── README.md
├── requirements.txt
├── data/
│   ├── processed/
│   └── raw/
├── proposal.pdf
├── results/
│   └── final_report.pdf
└── src/
    ├── analyze_visualize.py
    ├── clean_data.py
    ├── get_data.py
    └── integrate_data.py
