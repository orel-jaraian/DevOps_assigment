# check_servers.py
import requests

def check_server(url):
    try:
        response = requests.get(url)
        print(f"{url} responded with {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error connecting to {url}: {e}")
        return False

if __name__ == "__main__":
    server_1 = check_server("http://nginx:8080")
    server_2 = check_server("http://nginx:8081")
    if server_1 and not server_2:
        with open("/result/succeeded", "w") as f:
            f.write("All tests passed")
    else:
        with open("/result/fail", "w") as f:
            f.write("Some tests failed")
