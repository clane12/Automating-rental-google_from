🏠 Zillow Rental Scraper & Auto-Form Filler
A Python automation tool that scrapes rental listing data (price, address, and URL) from a sample Zillow website and automatically submits the details to a Google Form using Selenium.

✨ Features
🔍 Scrapes rental listings (price, address, link) from Zillow Clone site
📬 Automatically fills and submits a Google Form with the listing data
⚙️ Built using BeautifulSoup, Selenium, and dotenv
💨 Configurable via .env for form link and other secure data
📦 Supports multiple listings in one run

📦 Requirements
Python 3.x

Google Chrome

ChromeDriver (same version as your Chrome)

Environment variables:

FORM_LINK="your_google_form_url"

Install dependencies:

pip install selenium requests beautifulsoup4 python-dotenv

🚀 How to Run
Clone this repository or download the code files.

Set your Google Form link in a .env file:

FORM_LINK=https://your-form-link

Install all required dependencies:

pip install selenium requests beautifulsoup4 python-dotenv
Make sure your ChromeDriver is downloaded and added to system PATH:

Download ChromeDriver

Run the script:

python main.py
🎮 How It Works
🔗 Scrapes the Zillow Clone website using requests and BeautifulSoup.

🏘 Collects:

Property addresses

Rental prices

Listing URLs

📝 Uses Selenium to:

Open your Google Form

Autofill the form fields for each listing

Click submit and loop to "Submit another response"

🧩 Future Enhancements
🧠 Add support for real Zillow listings with dynamic content

🖼 Capture property images and store links

📊 Export scraped data to a CSV or Google Sheet

✅ Add validation for skipped or broken listings

⚠️ Disclaimer
This tool is for educational purposes only and works with the App Brewery’s sample Zillow clone. Scraping real websites may violate their terms of service — use responsibly and respectfully.
