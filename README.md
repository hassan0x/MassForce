# Sub-Domains Enumeration Research

## Research Information

The best tools and techniques to perform sub-domains enumeration and get the best result with high performance.

## Table of Contents

1. Web Scraping Techniques.
2. BruteForce Techniques.
3. Reverse Lookup Techniques.

## Web Scraping Techniques

With the scraping techniques it was there a lot of tools that do a great job like Theharverster, Recon-ng and others, but the best tools that were producing the best result are the three following tools.

### AMASS

[Project Link](https://github.com/OWASP/Amass) <br>
[Download Link](https://github.com/OWASP/Amass/releases)

```
unzip amass_v3.1.9_linux_amd64.zip
cd amass_v3.1.9_linux_amd64
./amass enum --passive -d example.com -o result1.txt
```

### SUBFINDER

[Project Link](https://github.com/subfinder/subfinder)

```
apt-get install golang
git clone https://github.com/subfinder/subfinder.git
cd subfinder
go build
./subfinder -d example.com -o result2.txt
```

### SUBLIST3R

[Project Link](https://github.com/aboul3la/Sublist3r)

```
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt
./sublist3r.py -d example.com -o result3.txt
```

Combine all the previous tools' results into one file.

```
cat result1 result2 result3 > results.txt
cat results.txt | tr "[A-Z]" "[a-z]" | sort -u > FinalResult.txt
```

## BruteForce Techniques.

With the brute-force techniques also there were a lot of tools that do a great job, but a few of tools that was producing high performace with this techniques like massDNS but the rate of the false positive was very high in my experience, so i decided to build my own tool, after a lot of research i found a library called adns that was capable of sending a lot of dns queries asynchronously.

The tool is capable of performing brute force of 30,000 subdomains in one minute with a very high success rate.

### The Wordlist

I used the 2 best wordlists jhaddix and commonspeak and combine them in one big wordlist called jhaddix_commonspeak.txt .

[jhaddix Wordlist](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056) <br>
[commonspeak Wordlist](https://github.com/assetnote/commonspeak2-wordlists/tree/master/subdomains)

```
sed -e 's/$/.example.com/' jhaddix_commonspeak.txt > company_profile.txt
pip install adns-python
python massForce.py company_profile.txt
```

## Reverse Lookup Techniques.

With the same previous situation and mindset, i tried to build a reverse lookup dns asynchronous tool.

The tool is also capable of performing brute force of 30,000 IPs in one minute with a very high success rate.

```
pip install adns-python
python massForceRev.py 8.8.0.0 8.8.64.255
```

#### The tool is based on the [catonmat research](https://catonmat.net/asynchronous-dns-resolution).
