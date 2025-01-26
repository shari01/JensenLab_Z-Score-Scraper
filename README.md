# Automating Biomarker Z-Score Extraction with Python and Selenium

Are you working on biomarker discovery or disease association research? This Python script leverages **Selenium** to automate Z-score extraction from the [JensenLab Disease database](https://diseases.jensenlab.org/Search), providing insights into biomarker-disease associations like cervical cancer or general cancer.

## What This Script Does
- Extracts **Z-scores** for biomarkers to quantify their relevance to diseases.
- Automates the process of navigating through multiple pages and tables.
- Handles multiple retries, random delays, and CSV export for results.
- Flexible to work with **any disease**—just update the keyword (e.g., "cervical cancer" → "diabetes").

## Why Z-scores Matter
Z-scores from the JensenLab database measure the strength of association between biomarkers and diseases, helping prioritize candidates for research or therapeutic targets.

## 📂 Key Features
- **Efficient web scraping** for large biomarker lists.
- **Randomized delays** for anti-detection measures.
- Saves results to a CSV for further analysis.

## How to Use
1. Clone this repository and set up the environment by installing the required dependencies:
   ```bash
   git clone <your-repository-link>
   cd <repository-folder>
   pip install -r requirements.txt
