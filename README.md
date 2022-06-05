# Inversion CloudIPs

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

[![GitHub license](https://img.shields.io/badge/LICENSE-BSD--3--CLAUSE-GREEN?style=for-the-badge)](LICENSE)
[![update](https://img.shields.io/github/workflow/status/elliotwutingfeng/Inversion-CloudIPs/update?label=UPDATE&style=for-the-badge)](https://github.com/elliotwutingfeng/Inversion-CloudIPs/actions/workflows/update.yml)
<img src="https://img.shields.io/tokei/lines/github/elliotwutingfeng/Inversion-CloudIPs?label=Total%20Blocklist%20IPs&style=for-the-badge" alt="Total Blocklist IPs"/>

Machine-readable `.txt` blocklist of IP addresses derived via lexical analysis of [cloud](https://en.wikipedia.org/wiki/Cloud_computing) [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) hostnames listed in the [Inversion DNSBL Blocklists](https://github.com/elliotwutingfeng/Inversion-DNSBL-Blocklists), updated every hour.

**Disclaimer:** _This project is not sponsored, endorsed, or otherwise affiliated with Google._

## Blocklist download

You may download the blocklist [here](ips.txt?raw=1)

## Requirements

-   Python >= 3.9.13

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
