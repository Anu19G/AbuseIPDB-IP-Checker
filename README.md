# AbuseIPDB IP Reputation Checker for SOC Analysts

An automated Python script designed to assist SOC analysts in triaging large batches of IP addresses using the AbuseIPDB API v2. It parses addresses, queries AbuseIPDB without per-minute speed limits, handles API errors cleanly, and exports the ISP, full country name, and total reports directly to a CSV spreadsheet.

## ⚠️ IMPORTANT: API Quota & Usage
* **Get Your API Key:** You must create a free account on AbuseIPDB to obtain an API key. Once signed up, find your personal API key under the API tab in your profile settings.
* **Daily Limit:** A free AbuseIPDB account is restricted to 1,000 requests per day. 
* **No Per-Minute Delay:** Unlike VirusTotal, AbuseIPDB does not require a per-minute speed limit. The script will process your list continuously until the daily limit is reached.

## Prerequisites
* Python 3.8+ installed on your computer.
* A registered AbuseIPDB account (to get your free API key).
* Required Python libraries (`requests` for the API connection and `pycountry` to translate 2-letter country codes into full names). 

Install the required dependencies by running this command in your terminal:
```bash
pip install requests pycountry
