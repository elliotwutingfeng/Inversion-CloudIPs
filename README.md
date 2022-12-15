<div align="center">

  <h3 align="center">Inversion CloudIPs</h3>
  <img src="images/inversion_logo.svg" alt="Logo" width="200" height="200">

  <p align="center">
    Malicious IP blocklists derived via lexical analysis of <a href="https://en.wikipedia.org/wiki/Cloud_computing">cloud</a> <a href="https://en.wikipedia.org/wiki/Virtual_machine">virtual machine</a> hostnames listed in the <a href="https://github.com/elliotwutingfeng/Inversion-DNSBL-Blocklists">Inversion DNSBL Blocklists</a>, updated every hour.
  </p>

  <p align="center">
  <a href="https://docs.netgate.com/pfsense/en/latest/packages/pfblocker.html"><img src="https://img.shields.io/badge/pfBlockerNG-212121?style=for-the-badge&logo=pfsense&logoColor=white" alt="pfBlockerNG"/></a>
  </p>

  <p align="center">
  <img src="https://tokei-rs.onrender.com/b1/github/elliotwutingfeng/Inversion-CloudIPs?label=Total%20Blocklist%20IPs&style=for-the-badge" alt="Total Blocklist IPs"/>
  <a href="https://github.com/elliotwutingfeng/Inversion-CloudIPs/commits"><img src="https://img.shields.io/github/last-commit/elliotwutingfeng/Inversion-CloudIPs?label=Last%20Updated&style=for-the-badge" alt="Last Updated"/></a>
  <a href="https://github.com/elliotwutingfeng/Inversion-CloudIPs/actions/workflows/update.yml"><img src="https://img.shields.io/github/actions/workflow/status/elliotwutingfeng/Inversion-CloudIPs/update.yml?branch=main&label=UPDATE&style=for-the-badge" alt="Update"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/LICENSE-BSD--3--CLAUSE-GREEN?style=for-the-badge" alt="GitHub license"/></a>
  </p>

</div>

**Disclaimer:** _This project is not sponsored, endorsed, or otherwise affiliated with Google._

## Blocklist download

| File | Download |
|:-:|:-:|
| ips.txt | [:floppy_disk:](ips.txt?raw=1) |

## Requirements

-   Python >= 3.11

## Setup instructions

`git clone` and `cd` into the project directory, then run the following

```bash
pip3 install tldextract
```

## Usage

```bash
python3 update.py
```

## Libraries/Frameworks used

-   [tldextract](https://github.com/john-kurkowski/tldextract)

&nbsp;

<sup>These files are provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, arising from, out of or in connection with the files or the use of the files.</sup>

<sub>Any and all trademarks are the property of their respective owners.</sub>
