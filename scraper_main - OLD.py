
from driver_setup import create_chrome_driver
import pandas as pd
import time

# 1) spin up Chrome
driver = create_chrome_driver(headless=False)

# 2) go to the NBA odds page
driver.get("https://oddsjam.com/nba/odds")
time.sleep(7)   # let all JS render

# 3) grab only the game blocks whose class starts with "duration-200ms"
blocks = driver.find_elements("css selector", "div.duration-200ms")

records = []
for blk in blocks:
    text = blk.text.splitlines()
    # we expect at least 4 lines: [datetime, teams, "MONEYLINE", odds]
    if len(text) >= 4:
        # line 1: two team codes separated by whitespace
        teams = text[1].split()
        # line 3: two moneyline odds
        odds  = text[3].split()
        if len(teams) == 2 and len(odds) == 2:
            records.append({
                "Team1": teams[0],
                "Team2": teams[1],
                "Odds1": odds[0],
                "Odds2": odds[1]
            })

# 4) save out
df = pd.DataFrame(records, columns=["Team1","Team2","Odds1","Odds2"])
df.to_csv("output/nba_team_odds.csv", index=False)
df.to_json("output/nba_team_odds.json", orient="records", indent=2)

print(f"[INFO] Scraped {len(records)} games.")
print("✅ CSV + JSON saved to output folder.")

driver.quit()