# Simple_Python_recon_script
Learning_to_script_in_python


To use this script, replace the target_url variable with the URL of the web application you want to test. The script starts by sending a GET request to the target URL and retrieving the server headers. It then prints the server headers and the response code.

Next, the script uses a list of common endpoints to check for their availability. It sends GET requests to each endpoint by appending it to the target_url and checks if the response status code is less than 400 (indicating a successful request). If an endpoint is available, it is added to the endpoints list.

Finally, the script prints the available endpoints.

You can customize the list of common endpoints (common_endpoints) to include additional endpoints you want to check during the reconnaissance phase. Remember to use this script responsibly and with proper authorization for any security testing activities.
