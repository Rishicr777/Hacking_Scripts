import requests

def main():
    target_url = "http://www.example.com"  # Replace with your target URL

    # Send a GET request to the target URL and retrieve the server headers
    response = requests.get(target_url)
    server_headers = response.headers

    # Print server headers
    print("Server Headers:\n")
    for header, value in server_headers.items():
        print(f"{header}: {value}")
    print("\n")

    # Print response code
    print(f"Response Code: {response.status_code}\n")

    # Find available endpoints
    print("Available Endpoints:\n")
    for endpoint in find_endpoints(target_url):
        print(endpoint)
    print("\n")

def find_endpoints(target_url):
    # Common list of endpoints to check
    common_endpoints = [
        "/",
        "/login",
        "/admin",
        "/robots.txt",
        "/sitemap.xml",
        "/wp-admin",
        "/phpinfo.php"
        # Add more endpoints to check as needed
    ]

    endpoints = []
    for endpoint in common_endpoints:
        url = target_url + endpoint
        response = requests.get(url, allow_redirects=False)
        if response.status_code < 400:
            endpoints.append(url)

    return endpoints

if __name__ == "__main__":
    main()
