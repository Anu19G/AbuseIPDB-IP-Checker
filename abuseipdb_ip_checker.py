import requests
import csv
import os
import pycountry

def get_full_country_name(country_code):
    if not country_code or country_code == 'N/A':
        return 'N/A'
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name if country else country_code
    except Exception:
        return country_code

def check_ip_abuseipdb(ip_address, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        
        # Handle Rate Limit
        if response.status_code == 429:
            print("[!] API rate limit exceeded. You hit your 1,000/day limit.")
            return "RATE_LIMIT"
            
        # Handle Invalid IPs (422 Unprocessable Entity)
        if response.status_code == 422:
            print(f"[-] Invalid IP format rejected by API: {ip_address}")
            return "INVALID"

        response.raise_for_status()
        
        data = response.json()['data']
        total_reports = data.get('totalReports', 0)
        distinct_users = data.get('numDistinctUsers', 0)
        report_string = f"{total_reports} from {distinct_users} distinct reporters"
        
        raw_country_code = data.get('countryCode', 'N/A')
        full_country_name = get_full_country_name(raw_country_code)
        
        return {
            "IP": ip_address,
            "ISP": data.get('isp', 'N/A'),
            "Country": full_country_name,
            "Total Reports": report_string
        }
        
    except requests.exceptions.RequestException as e:
        print(f"[-] Connection error checking IP {ip_address}: {e}")
        return "ERROR"

def main():
    # --- ADD YOUR API KEY HERE ---
    API_KEY = "YOUR_ACTUAL_API_KEY"
    
    input_file = "ips.txt"
    output_file = "abuseipdb_results.csv"

    if not os.path.exists(input_file):
        print(f"[!] Error: '{input_file}' not found. Please create it and add IPs.")
        return

    with open(input_file, 'r') as f:
        all_ips = [line.strip() for line in f if line.strip()]

    completed_ips = set()
    file_exists = os.path.isfile(output_file)

    if file_exists:
        with open(output_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if row:
                    completed_ips.add(row[0])

    ips_to_check = [ip for ip in all_ips if ip not in completed_ips]

    if not ips_to_check:
        print("[+] All IPs in ips.txt have already been processed.")
        return

    print(f"[*] Found {len(all_ips)} total IPs. {len(completed_ips)} already checked. {len(ips_to_check)} remaining.")

    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists or os.stat(output_file).st_size == 0:
            writer.writerow(["IP", "ISP", "Country", "Total Reports"])

        for ip in ips_to_check:
            print(f"[*] Checking {ip}...")
            result = check_ip_abuseipdb(ip, API_KEY)
            
            if result == "RATE_LIMIT":
                print("[-] Stopping execution due to rate limit.")
                break
            elif result == "INVALID" or result == "ERROR":
                # Write placeholder for invalid IPs and move to the next
                writer.writerow([ip, "Invalid IP", "N/A", "N/A"])
                f.flush()
                continue
                
            writer.writerow([result["IP"], result["ISP"], result["Country"], result["Total Reports"]])
            f.flush()

    print("[+] Script execution finished.")

if __name__ == "__main__":
    main()