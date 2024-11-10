import requests

def check_server(url):
    try:
        response = requests.get(url)
        print(f"Server {url} responded with status: {response.status_code}")
        print(f"Response content: {response.text}")
    except Exception as e:
        print(f"Could not connect to {url}. Error: {e}")

# URLs for both servers
check_server("http://nginx:8080")
check_server("http://nginx:8081")
