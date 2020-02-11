# Sub-Domains Enumeration Tools

### This repo has two parts:
1. The BruteForce Techniques.
2. The Reverse Lookup Techniques.

## BruteForce Techniques.

There was a lot of tools that do the brute-force techniques, but a few of them that were producing high performance with this techniques like massDNS but the rate of the false positive was very high in my experience, so i decided to build my own tool, after a lot of research i found a library called adns that was capable of sending a lot of dns queries asynchronously.

The tool is capable of performing brute force of 30,000 subdomains in one minute with a very high success rate.

I used the 2 best wordlists jhaddix and commonspeak and combine them in one big wordlist called jhaddix_commonspeak.txt .

```
pip install adns-python
python MassForce.py company_profile.txt
```

## Reverse Lookup Techniques.

With the same previous situation and mindset, i tried to build a reverse lookup dns asynchronous tool.

The tool is also capable of performing brute force of 30,000 IPs in one minute with a very high success rate.

```
pip install adns-python
python MassForceRev.py 8.8.0.0 8.8.64.255
```

#### If you find me wrong in something or you can make this repo better please let me know.
- [Facebook Profile](https://facebook.com/HassanSaad00)
- [Linkedin Profile](https://www.linkedin.com/in/HassanSaad00)
- [Facebook Page](https://www.facebook.com/NineHackers)
- [Facebook Group](https://www.facebook.com/groups/NineHackers)
