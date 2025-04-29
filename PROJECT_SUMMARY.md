
# 🏁 NBA Moneyline Scraper – Final Summary

### 📌 Project Overview

This project is a Python-based web scraper that extracts **NBA team moneyline odds** from [VegasInsider](https://www.vegasinsider.com/nba/odds/money-line/), using a **headless browser automation approach**. The output is saved in **timestamped CSV and JSON files**.

---

### 🔧 Key Processes & Technologies Used

| Step | Description |
|------|-------------|
| ✅ Web Automation | Used **Selenium WebDriver** to control a Chrome browser in headless mode |
| ✅ Driver Management | Used `webdriver-manager` to auto-download and manage the right ChromeDriver version |
| ✅ Data Extraction | Parsed structured text blocks from the page to extract team names and moneyline odds |
| ✅ Output Formats | Saved scraped data as both `.csv` and `.json` using **pandas** and Python’s built-in `json` |
| ✅ Timestamping | Automatically names output files using a timestamp format (`nba_team_odds_YYYYMMDD_HHMMSS`) |
| ✅ Cross-platform | Developed in a Windows environment, with compatibility for future Linux/cloud deployment |
| ✅ Git + GitHub | Full version control and public repo hosting with SSH authentication for secure pushes |

---

### 📚 Libraries Used

| Library             | Purpose                                    |
|---------------------|--------------------------------------------|
| `selenium`          | Browser control and scraping automation    |
| `webdriver-manager` | Auto-handling of ChromeDriver              |
| `pandas`            | Data manipulation and CSV export           |
| `json` (built-in)   | Exporting results to `.json` format        |
| `datetime`          | File naming with run timestamps            |

---

### ✨ Key Features

- 📦 **Headless scraping**: Efficient, non-visual browser session for clean runs
- 📈 **Structured output**: Easy-to-read JSON and spreadsheet-compatible CSV
- 📅 **Auto-timestamping**: Each run saves separate output files with precise time tracking
- 🔄 **Resilient logic**: Skips unexpected formats and logs warnings without crashing
- 🔐 **Secure GitHub push**: Configured SSH access for long-term, token-free repo management

---

### ⚠️ Challenges to Watch Out For

| Issue                         | Notes / Mitigation |
|------------------------------|---------------------|
| ❗ Page structure changes     | Site structure may change — scraper relies on consistent text block layout |
| ❗ Timing issues (loading)    | Some pages load data dynamically — use `time.sleep()` or explicit waits |
| ❗ Chrome updates             | Keep Chrome and ChromeDriver synced — `webdriver-manager` helps here |
| ❗ GitHub authentication      | PAT errors led to switch from HTTPS to SSH (recommended for all future work) |
| ❗ Large browser memory use   | Keep background apps minimal when scraping many blocks in headless mode |

---

### 💼 Use Cases & Portfolio Value

This project demonstrates your ability to:
- Build reliable, repeatable scraping pipelines
- Cleanly extract structured data for sports analytics or betting markets
- Package and publish professional Python repos to GitHub
- Solve real-world Git/GitHub challenges with SSH

You can now reuse this as a **portfolio project** or template for:
- Scraping other sports odds (tennis, football, etc.)
- Price tracking, betting intelligence, or B2B sports analytics
- Future Upwork or freelance data scraping contracts
