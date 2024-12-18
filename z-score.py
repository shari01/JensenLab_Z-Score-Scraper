import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import randint  # For introducing random delays

# Function to extract Z-score from the web
def extract_z_score(driver, biomarker_name):
    url = f"https://diseases.jensenlab.org/Search?query={biomarker_name}"
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'body'))
        )
        time.sleep(randint(10, 20))  # Extended random delay before proceeding
        
        # Look for the first table
        table = driver.find_element(By.TAG_NAME, 'table')
        first_row = table.find_element(By.TAG_NAME, 'tbody').find_element(By.TAG_NAME, 'tr')
        link = first_row.find_element(By.TAG_NAME, 'a').get_attribute('href')  # Get the href from the first row's anchor tag
        driver.get(link)
        
        time.sleep(randint(10, 20))  # Extended random delay after loading the link
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='table_title' and text()='Text mining']"))
        )

        # Loop through multiple pages and tables to find Z-scores
        z_score_cervical = None
        z_score_cancer = None
        category = "Not found"
        
        # Set a limit for the number of pages to search through
        page_count = 1
        
        while page_count <= 5:  # Limit to 5 pages
            # Search for tables containing relevant terms
            tables = driver.find_elements(By.TAG_NAME, 'table')  # All tables on the page
            
            for table in tables:
                rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
                for row in rows:
                    columns = row.find_elements(By.TAG_NAME, 'td')
                    if len(columns) > 1:
                        # Look for Cervical Cancer first
                        if "Cervical cancer" in columns[0].text.strip() and not z_score_cervical:
                            z_score_cervical = columns[1].text.strip()
                            category = "Cervical Cancer"
                        # Look for general Cancer if Cervical Cancer wasn't found
                        elif "Cancer" in columns[0].text.strip() and not z_score_cancer:
                            z_score_cancer = columns[1].text.strip()
                            category = "Cancer"

            # Check if a "Next" button exists to navigate to the next page
            try:
                next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
                next_button.click()  # Click to go to the next page
                time.sleep(randint(15, 30))  # Longer random delay between 15-30 seconds before navigating
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='table_title' and text()='Text mining']"))
                )
                page_count += 1
            except Exception:
                break  # No more pages to navigate or no "Next" button

            # If Cancer was found, no need to continue checking for Cervical Cancer on further pages
            if z_score_cancer:
                break

        # Determine the correct category based on what was found
        if z_score_cancer and z_score_cervical:
            category = "Both Cancer and Cervical Cancer"
        elif z_score_cancer:
            category = "Cancer"
        elif z_score_cervical:
            category = "Cervical Cancer"
        
        # If no z-score is found, the result is None
        if not z_score_cancer and not z_score_cervical:
            z_score_cervical = z_score_cancer = None

    except Exception as e:
        print(f"Error encountered for biomarker {biomarker_name}: {e}")
        z_score_cervical = z_score_cancer = None
        category = "Error"
    
    return z_score_cervical, z_score_cancer, category

# Main function
def main():
    start_time = time.time()
    
    # Get biomarker list input from the user
    biomarker_list = input("Enter biomarkers separated by commas: ").split(',')

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        results = []
        for biomarker_name in biomarker_list:
            biomarker_name = biomarker_name.strip()  # Clean up extra spaces
            z_score_cervical, z_score_cancer, category = None, None, "Not found"
            retries = 3  # Number of retries

            for attempt in range(retries):
                z_score_cervical, z_score_cancer, category = extract_z_score(driver, biomarker_name)

                if z_score_cervical is not None or z_score_cancer is not None:
                    results.append({
                        "Biomarker": biomarker_name,
                        "Cervical Z-Score": z_score_cervical,
                        "Cancer Z-Score": z_score_cancer,
                        "Category": category
                    })
                    print(f"Biomarker: {biomarker_name}, Cervical Z-Score: {z_score_cervical}, Cancer Z-Score: {z_score_cancer}, Category: {category}")
                    break
                else:
                    print(f"Attempt {attempt + 1}: Z-score could not be retrieved for {biomarker_name}. Retrying...")
                    time.sleep(randint(10, 20))  # Longer delay before retrying

            if z_score_cervical is None and z_score_cancer is None:
                print(f"Failed to retrieve Z-scores for {biomarker_name} after {retries} attempts.")

        # Save the results to a CSV file
        results_df = pd.DataFrame(results)
        results_df.to_csv("C:/Users/Sheryar Malik/Downloads/cgc/updated-biomarker_z_scores.csv", index=False)
        print(f"Results saved to 'biomarker_z_scores.csv'.")
        
        # Print summary
        total_biomarkers = len(biomarker_list)
        total_time = time.time() - start_time
        print(f"Total biomarkers processed: {total_biomarkers}")
        print(f"Total time taken: {total_time:.2f} seconds")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
