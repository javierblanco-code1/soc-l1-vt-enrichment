import os
import requests

IP_LIST = [
    "8.8.8.8",
    "185.220.101.5",
    "203.0.113.45"
]

def check_ip_reputation(ip: str, api_key: str) -> dict:
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        stats = response.json()["data"]["attributes"]["last_analysis_stats"]
        return {
            "ip": ip,
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0)
        }
    return {"ip": ip, "error": f"HTTP {response.status_code}"}

def main():
    api_key = os.getenv("VT_API_KEY")
    if not api_key:
        print("[!] Error: La variable de entorno VT_API_KEY no está configurada.")
        return

    print("[-] Iniciando consulta de IoCs en VirusTotal...\n")
    for ip in IP_LIST:
        res = check_ip_reputation(ip, api_key)
        if "error" in res:
            print(f"[!] IP: {res['ip']} | Estado: {res['error']}")
        else:
            status = "⚠️ SOSPECHOSA/MALICIOSA" if (res['malicious'] > 0 or res['suspicious'] > 0) else "✅ LIMPIA"
            print(f"IP: {res['ip']:<15} | Estado: {status:<25} | Motores que la detectan: {res['malicious']}")

if __name__ == "__main__":
    main()
