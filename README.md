# AbuseIPDB IP Reputation Checker for SOC Analysts

An automated Python script designed to assist SOC analysts in triaging large batches of IP addresses using the AbuseIPDB API v2. It parses addresses, queries AbuseIPDB without per-minute speed limits, handles API errors cleanly, and exports the ISP, full country name, and total reports directly to a CSV spreadsheet.

---

## ⚠️ IMPORTANT: API Quota & Usage

* **Get Your API Key:** You must create a free account on [AbuseIPDB](https://www.abuseipdb.com/) to obtain an API key. Once signed up, find your personal API key under the API tab in your profile settings.
* **Daily Limit:** A free AbuseIPDB account is restricted to **1,000 requests per day**.
* **No Per-Minute Delay:** Unlike VirusTotal, AbuseIPDB does not require a per-minute speed limit. The script will process your list continuously until the daily limit is reached.

---

## Prerequisites

* Python 3.8+ installed on your computer.
* A registered AbuseIPDB account (to get your free API key).
* Python `requests` and `pycountry` libraries installed:

```cmd
pip install requests pycountry


```

---

## Step-by-Step Instructions

1. **Get Your API Key:** Create a free account on [AbuseIPDB](https://www.abuseipdb.com/). Go to your profile menu, click on the **API** tab, and copy your key.
2. **Create a Folder:** Create a new folder on your system (e.g., on your Desktop) to hold your project files.
3. **Paste the `.py` File:** Move or download the `abuseipdb_ip_checker.py` file into this folder.
4. **Add Your API Key Inside `""`:** Open `abuseipdb_ip_checker.py` in a text editor and locate line 55:

```python
API_KEY = "YOUR_ACTUAL_API_KEY"


```

Paste your AbuseIPDB API key inside the double quotation marks (`""`). **Do not delete the quotation marks**, or the script will fail to run.

5. **Create the `ips.txt` File:** In the exact same folder as the script, create a new text file and name it strictly **`ips.txt`**.

* *Note:* You must use the exact name **`ips.txt`** because the script only accepts and looks for this specific file name as input.

6. **Paste IPs in the File:** Open `ips.txt` and paste only your IP addresses—one IP per line. Do not include extra text, commas, or descriptions.

```text
192.168.21.134
8.8.8.8
185.220.101.1


```

7. **Open CMD and Run the Script:**

* Open Command Prompt (`cmd`).
* Navigate to the folder where your files are saved:

```cmd
cd path\to\your\folder


```

* Run the script:

```cmd
python abuseipdb_ip_checker.py


```

---

## Output

* Results are written line-by-line directly into `abuseipdb_results.csv` after every query.
* Invalid IP formats (422 errors) are automatically caught and marked as "Invalid IP" directly in the CSV so the script can continue running without interruption.
* If stopped or interrupted, re-running the script will automatically pick up where it left off and skip already completed IPs.
