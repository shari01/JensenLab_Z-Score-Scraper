<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automating Z-Score Extraction</title>
</head>
<body>
    <h1>Automating Biomarker Z-Score Extraction with Python and Selenium</h1>
    <p>
        Are you working on biomarker discovery or disease association research? This Python script leverages 
        <strong>Selenium</strong> to automate Z-score extraction from the 
        <a href="https://diseases.jensenlab.org/Search" target="_blank">JensenLab Disease database</a>, providing insights 
        into biomarker-disease associations like cervical cancer or general cancer.
    </p>

    <h2>What This Script Does</h2>
    <ul>
        <li>Extracts <strong>Z-scores</strong> for biomarkers to quantify their relevance to diseases.</li>
        <li>Automates the process of navigating through multiple pages and tables.</li>
        <li>Handles multiple retries, random delays, and CSV export for results.</li>
        <li>Flexible to work with <strong>any disease</strong>—just update the keyword (e.g., "cervical cancer" → "diabetes").</li>
    </ul>

    <h2>Why Z-scores Matter</h2>
    <p>
        Z-scores from the JensenLab database measure the strength of association between biomarkers and diseases, 
        helping prioritize candidates for research or therapeutic targets.
    </p>

    <h2>📂 Key Features</h2>
    <ul>
        <li>Efficient web scraping for large biomarker lists.</li>
        <li>Randomized delays for anti-detection measures.</li>
        <li>Saves results to a CSV for further analysis.</li>
    </ul>

    <h2>How to Use</h2>
    <p>
        Clone this repository and set up the environment by installing the required dependencies. Update the disease 
        keyword in the script to match your area of research. Run the script, and it will generate a CSV with Z-scores 
        for biomarkers.
    </p>

    <p>
        If you have any questions, suggestions, or contributions, feel free to open an issue or submit a pull request!
    </p>

    <h2>📥 Download and Installation</h2>
    <pre>
    git clone <your-repository-link>
    cd <repository-folder>
    pip install -r requirements.txt
    </pre>

    <h2>💻 Example Use Case</h2>
    <pre>
    python z_score_extractor.py
    </pre>

    <h2>🔗 Useful Links</h2>
    <ul>
        <li><a href="https://diseases.jensenlab.org/Search" target="_blank">JensenLab Disease Database</a></li>
        <li><a href="<your-repository-link>" target="_blank">GitHub Repository</a></li>
    </ul>
</body>
</html>
