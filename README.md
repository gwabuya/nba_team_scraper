
# NBA Moneyline Odds Scraper

NBA Moneyline Odds Scraper
Scrapes NBA team betting odds (moneyline) from VegasInsider using Selenium and pandas. Saves output to timestamped CSV and JSON files.

# 🏀 NBA Moneyline Odds Scraper

This project scrapes NBA team moneyline odds from [VegasInsider](https://www.vegasinsider.com/nba/odds/money-line/) using Python, Selenium, and pandas.

It saves the results in both **CSV** and **JSON** formats, with **timestamped filenames** for easy recordkeeping.

---

## 📦 Features

- ✅ Scrapes team matchups and their corresponding moneyline odds
- ✅ Automatically saves results to `output/` folder
- ✅ Saves in `.csv` and `.json` formats with timestamps
- ✅ Lightweight, headless browser automation using Selenium

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone git@github.com:gwabuya/nba_team_scraper.git
cd nba_team_scraper
