import requests
import os

def check_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success: {url} returned status {response.status_code}")
            return "succeeded"
        else:
            print(f"Failure: {url} returned status {response.status_code}")
            return "fail"
    except requests.RequestException as e:
        print(f"Error: Could not connect to {url} - {e}")
        return "fail"

if __name__ == "__main__":
    # Ensure /test_result directory exists
    os.makedirs("/test_result", exist_ok=True)
    
    results = [
        check_server("http://nginx:8080"),
        check_server("http://nginx:8081")
    ]

    if "fail" in results:
        with open("/test_result/fail", "w") as f:
            f.write("Test failed.")
    else:
        with open("/test_result/succeeded", "w") as f:
            f.write("All tests passed.")

