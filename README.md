# Sub-Domains Enumeration Research

## Research Information

The best tools and techniques to perform sub-domains enumeration and get the best result with high performance.

## Table of Contents

1. Web Scraping Techniques.
2. BruteForce Techniques.
3. Reverse Lookup Techniques.

######################################################

1. Web Scraping Techniques

### AMASS

Project: https://github.com/OWASP/Amass <br>
Download: https://github.com/OWASP/Amass/releases

```
unzip amass_v3.1.9_linux_amd64.zip
cd amass_v3.1.9_linux_amd64
./amass enum --passive -d alexu.edu.eg -o result1.txt
```

######################################################

### SUBFINDER

Project: https://github.com/subfinder/subfinder

```
apt-get install golang
git clone https://github.com/subfinder/subfinder.git
cd subfinder
go build
./subfinder -d alexu.edu.eg -o result2.txt
```

######################################################

### SUBLIST3R

Project: https://github.com/aboul3la/Sublist3r

```
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt
./sublist3r.py -d alexu.edu.eg -o result3.txt
```

Combine all the previous tools' results into one file.

```
cat result1 result2 result3 > results.txt
cat results.txt | tr "[A-Z]" "[a-z]" | sort -u > FinalResult.txt
```

######################################################

### BRUTEFORCE

jhaddix: https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056 <br>
commonspeak: https://github.com/assetnote/commonspeak2-wordlists/tree/master/subdomains <br>
MixWordFile: jhaddix_commonspeak.txt

```
sed -e 's/$/.alexu.edu.eg/' jhaddix_commonspeak.txt > company_profile.txt
pip install adns-python
python resolve.py company_profile.txt
```

######################################################
