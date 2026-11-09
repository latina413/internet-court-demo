import requests
import json

API_URL = "https://api.argue.fun/v1/debates"

def fetch_dispute_data():
    print("[*] Menghubungkan ke API Argue.fun (Internet Court Partner)...")
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("[+] Berhasil mengambil data sengketa!")
            return data
        else:
            print(f"[-] Status code: {response.status_code}. Menggunakan data simulasi fallback.")
            return {
                "status": "success",
                "sample_case": "AI Consensus Validation on GenLayer Testnet",
                "dispute_id": "COURT-2026-001",
                "status_verdict": "Validated by GenLayer AI"
            }
    except Exception as e:
        print(f"[-] Catatan koneksi: {e}. Menggunakan data simulasi.")
        return {
            "status": "success",
            "sample_case": "AI Consensus Validation on GenLayer Testnet",
            "dispute_id": "COURT-2026-001",
            "status_verdict": "Validated by GenLayer AI"
        }

def simulate_genlayer_consensus(case_data):
    print("\n[*] Menjalankan GenLayer Intelligent Consensus...")
    print(f"    - Memproses Kasus: {case_data.get('sample_case', 'Unknown Case')}")
    print(f"    - ID Sengketa: {case_data.get('dispute_id', 'N/A')}")
    print("    - Status Verifikasi: [ OK ] Konsensus AI Tercapai (Valid)")
    print("[+] Keputusan Internet Court Berhasil Dikeluarkan secara Terdesentralisasi!\n")

if __name__ == "__main__":
    print("=== INTERNET COURT: PARTNER DEMO LAB (GenLayer x Argue.fun) ===")
    case = fetch_dispute_data()
    if case:
        simulate_genlayer_consensus(case)
