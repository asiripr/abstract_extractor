# DOI Abstract Extractor

A simple Python tool that extracts abstracts from up to 10 DOI links using the Crossref REST API and exports the results to a CSV file.

---

## Features

- Accepts up to 10 DOI URLs or raw DOI strings  
- Fetches abstracts via the Crossref API  
- Cleans basic JATS tags in abstracts  
- Handles missing abstracts (marked as "N/A")  
- Saves output to `abstracts.csv`  
- Modular and easy to extend

pip install requests
python main.py
