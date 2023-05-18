import ipaddress
import re
from urllib.request import urlopen

import tldextract

with urlopen(
    "https://raw.githubusercontent.com/elliotwutingfeng/"
    "Inversion-DNSBL-Blocklists/main/Google_hostnames.txt"
) as response:
    urls: list[str] = response.read().decode().splitlines()

rows: list[tuple[str, str]] = []
for url in urls:
    # IP addresses in cloud virtual machine hostnames tend to exist
    # in the form of {number}-{number}-{number}-{number}
    # or the form of {number}.{number}.{number}.{number}

    # Only extract IP addresses from subdomain
    r = tldextract.extract(url)
    # Reverse subdomain before regex search
    # to prevent mixed alphanumeric leading segments from being included (e.g. "ec2-")
    match_dashes = re.search(
        "([0-9]{1,3}[-][0-9]{1,3}[-][0-9]{1,3}[-][0-9]{1,3})", r.subdomain[::-1]
    )
    match_dots = re.search(
        "([0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3})", r.subdomain[::-1]
    )
    match = match_dashes if match_dashes else match_dots
    # Ensure extracted IP address is valid
    if match is not None:
        maybe_IP = match.group(1).strip().replace("-", ".")[::-1]
        if "googleusercontent.com" == r.registered_domain:
            # Special case for googleusercontent; IP already reversed in hostname
            maybe_IP = ".".join(maybe_IP.split(".")[::-1])
        ip = None
        try:
            ip = ipaddress.ip_address(maybe_IP)
        except ValueError:
            continue
        if ip is None or type(maybe_IP) is not str:
            continue
        if any(
            (octet.startswith("0") and len(octet) > 1) for octet in maybe_IP.split(".")
        ):
            # zero-padded octets in hostname are unlikely to represent IP addresses
            continue
        if ip.is_private or ip.is_multicast or ip.is_reserved:
            # Reject bogons
            continue
        rows.append((maybe_IP, url))

if rows:
    with open("ips.txt", "w") as f:
        f.writelines("\n".join(" # ".join(e) for e in rows))
