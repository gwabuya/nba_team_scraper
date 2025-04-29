"""
NBA Moneyline Scraper
---------------------
Scrapes NBA game odds (moneyline) from the target website
and saves results into timestamped CSV and JSON files.

Usage:
    python scraper_main.py
"""

import time
import datetime
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# helper function to validate odds
def is_moneyline(s):
    return s.startswith('+') or s.startswith('-')

def main():
    # initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run Chrome in headless mode (no window)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # target site
        url = "https://www.vegasinsider.com/nba/odds/money-line/"
        driver.get(url)
        time.sleep(5)  # wait for page to fully load

        # find game blocks
        blocks = driver.find_elements(By.CSS_SELECTOR, "div.duration-200ms")
        print(f"[DEBUG] Found {len(blocks)} game blocks")

        records = []
        for idx, blk in enumerate(blocks, 1):
            text_lines = blk.text.splitlines()
            if idx == 1:
                print("[DEBUG] First block preview:", text_lines[:6])

            if len(text_lines) >= 6:
                team1 = text_lines[1].strip()
                team2 = text_lines[2].strip()
                odds1 = text_lines[4].strip()
                odds2 = text_lines[5].strip()

                if is_moneyline(odds1) and is_moneyline(odds2):
                    records.append({
                        "Team1": team1,
                        "Team2": team2,
                        "Odds1": odds1,
                        "Odds2": odds2
                    })
                else:
                    print(f"[DEBUG] Skipped block #{idx}, invalid odds:", odds1, odds2)
            else:
                print(f"[DEBUG] Skipped block #{idx}, not enough lines")

        print(f"[INFO] Scraped {len(records)} games.")

        # save results
        if records:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            df = pd.DataFrame(records)
            csv_filename = f"output/nba_team_odds_{timestamp}.csv"
            json_filename = f"output/nba_team_odds_{timestamp}.json"

            df.to_csv(csv_filename, index=False)
            with open(json_filename, "w") as f:
                json.dump(records, f, indent=2)

            print("✅ CSV + JSON saved to output folder.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()