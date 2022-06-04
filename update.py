import re
import socket
from urllib.request import urlopen

import tldextract

response = urlopen(
    "https://raw.githubusercontent.com/elliotwutingfeng/"
    "Inversion-DNSBL-Blocklists/main/Google_hostnames.txt"
    )
urls: list[str] = [line for line in response.read().decode().splitlines()]

res: list[list[str]] = []
for url in urls:
    # IP addresses in cloud virtual machine hostnames tend to exist
    # in the form of {number}-{number}-{number}-{number}

    # Only extract IP addresses from subdomain
    r = tldextract.extract(url)
    # Reverse subdomain before regex search
    # to prevent mixed alphanumeric leading segments from being included (e.g. "ec2-")
    match = re.search('([0-9]{1,3}-[0-9]{1,3}-[0-9]{1,3}-[0-9]{1,3})', r.subdomain[::-1])
    # Ensure extracted IP address is valid
    if match is not None:
        maybe_IP = match.group(1).strip().replace('-', '.')[::-1]
        try:
            socket.inet_aton(maybe_IP)
        except socket.error:
            continue
        res.append([maybe_IP, url])

if res:
    with open('ips.txt', 'w') as f:
        f.writelines("\n".join(" # ".join(e) for e in res))
