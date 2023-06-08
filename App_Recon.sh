#!/bin/bash

# Replace with your target domain or IP address
target="example.com"

# Run Subfinder to discover subdomains
echo "Running Subfinder..."
subfinder -d $target -o subdomains.txt

# Run HTTPX to get alive subdomains
echo "Running HTTPX..."
httpx -l subdomains.txt -o alive_subdomains.txt

# Run Naabu to perform port scanning
echo "Running Naabu..."
naabu -iL alive_subdomains.txt -p default -o naabu_results.txt

# Run Nuclei for vulnerability scanning
echo "Running Nuclei..."
nuclei -l alive_subdomains.txt -t <path-to-nuclei-templates> -o nuclei_results.txt

# Run Katana to perform directory and file enumeration
echo "Running Katana..."
katana -d alive_subdomains.txt -o katana_results.txt

# Run GoWitness to capture website screenshots
echo "Running GoWitness..."
gowitness file --source alive_subdomains.txt --log gowitness.log

# Run ASNMap for ASN enumeration
echo "Running ASNMap..."
asnmap -i alive_subdomains.txt -o asnmap_results.txt

# Run Uncover for IP reconnaissance
echo "Running Uncover..."
uncover -i alive_subdomains.txt -o uncover_results.txt

# Run Shodan CLI for Shodan search
echo "Running Shodan CLI..."
shodan search --limit 100 --fields ip_str,port,org,hostnames $target > shodan_results.txt

# Run WappalyzerGo for technology stack identification
echo "Running WappalyzerGo..."
wappalyzergo -input alive_subdomains.txt -output wappalyzer_results.json

# Run MapCIDR for IP range calculations
echo "Running MapCIDR..."
mapcidr -cidrFile uncover_results.txt -o mapcidr_results.txt

# Run ShuffleDNS for fast DNS enumeration
echo "Running ShuffleDNS..."
shuffledns -d $target -list alive_subdomains.txt -r resolvers.txt -o shuffledns_results.txt

echo "Scanning and reconnaissance completed."
