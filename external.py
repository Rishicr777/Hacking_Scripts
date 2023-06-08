import socket
import whois
import dns.resolver

def main():
    target_domain = "example.com"  # Replace with your target domain

    # Perform domain reconnaissance
    print(f"Domain Reconnaissance for {target_domain}:\n")
    resolve_domain(target_domain)
    whois_lookup(target_domain)
    dns_lookup(target_domain)

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print("Failed to resolve domain.")

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print("\nWHOIS Information:")
        print(f"Registrar: {w.registrar}")
        print(f"Registered on: {w.creation_date}")
        print(f"Expiration date: {w.expiration_date}")
        print(f"Name servers: {w.name_servers}")
        # Additional WHOIS data can be extracted based on the specific library used
    except Exception as e:
        print(f"Failed to perform WHOIS lookup. Error: {e}")

def dns_lookup(domain):
    try:
        print("\nDNS Records:")
        records = dns.resolver.query(domain, 'A')
        for record in records:
            print(f"A Record: {record}")
        # Additional DNS record types (MX, CNAME, etc.) can be queried as needed
    except dns.resolver.NoAnswer:
        print("No DNS records found.")
    except Exception as e:
        print(f"Failed to perform DNS lookup. Error: {e}")

if __name__ == "__main__":
    main()
