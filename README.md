# 510 Python Apartment finder project

Apartment Finder<br>
A tool that scrapes Craigslist apartment listings across 5 Los Angeles neighborhoods, adds  commute times and walk scores, and visualizes the results for analysis. 

Installation<br>
Clone the repository and install the required packages:<br>
requirements.txt: This file lists all the external libraries you have used in your project.<br>
You can create this file manually or use the following commands in your virtual env:<br>
To create this file you can run:<br>
  pip freeze >> requirements.txt<br>
  To install all the required libraries, you can run:<br>
  pip install -r requirements.txt<br>

How to Get the Data<br>
The scraper pulls apartment listings from Craigslist. Run it with the number of bedrooms you want as the argument:<br>
python src/get_data.py 2<br>
This will scrape listings for 2-bedroom apartments across Downtown Long Beach, Cerritos, Redondo Beach, Corona, and Malibu.<br>
<br>
How to Clean the Data<br>
Once the data is scraped, run the integration and cleaning scripts to enrich listings with commute times and walk scores:<br>
python src/integrate_data.py<br>
python src/clean_data.py<br>
This will produce a cleaned CSV file at data/processed/apartments.csv.<br>
<br>
How to Run the Analysis and Visualizations<br>
Run the visualization script to produce the plots:<br>
python src/analyze_visualize.py<br>
This produces a 2x2 chart saved to results/overview.png with:<br>
<br>
Average rent by city<br>
Average price per square foot by city<br>
Commute times to USC and work by city<br>
Walk score and bike score by city<br>
<br>
API Keys are hard coded for ease of use 
<br>

Project Structure<br>
```text
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
```
