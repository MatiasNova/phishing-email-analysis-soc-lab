# Phishing Email Investigation Report

## 1. Incident Overview

**Incident type:** Suspected phishing and malware distribution  
**Investigation:** CyberDefenders PhishStrike  
**Email subject:** COMMERCIAL PURCHASE RECEIPT ONLINE 27 NOV  
**Email date:** 9 December 2022  
**Severity:** High — preliminary assessment  
**Status:** Investigation documented; recipient impact not established

## 2. Executive Summary

A suspicious email claiming to concern a commercial purchase was investigated. The message included a link to an executable file hosted at an IP address rather than a conventional invoice document.

Email authentication results included SPF SoftFail, DKIM failure and no DMARC policy result. The extracted URL was subsequently correlated with historical threat-intelligence records on URLhaus. VirusTotal relations also identified suspicious URLs associated with the investigated sample.

These findings support treating the email and its associated infrastructure as potentially malicious. However, the available evidence does not establish that a recipient clicked the link, executed a file or suffered a compromise.

## 3. Email Header Analysis

The following observations were recorded:

- **Sender:** erikajohana.lopez@uptc.edu.co
- **Recipient:** Undisclosed recipients
- **Reply-To:** Not present
- **SPF:** SoftFail
- **DKIM:** Fail; the receiving system reported no key for the signature
- **DMARC:** None reported in the authentication results
- **Message-ID:** Present
- **Email routing:** The headers show mail passing through Google infrastructure, Trend Micro email security and Microsoft Exchange-related infrastructure.

The authentication failures and undisclosed-recipient format are suspicious in context, but neither observation alone proves that an email is malicious. The routing information must also be interpreted carefully because security gateways can appear in the delivery path.

## 4. Indicators of Compromise

The following indicators were identified during the investigation.

| Indicator | Type | Assessment |
|---|---|---|
| `107.175.247.199` | IP address | Associated with historical malware-distribution URLs in URLhaus |
| `hxxp://107[.]175[.]247[.]199/loader/install[.]exe` | URL | Suspicious executable link extracted from the email |
| `hxxp://107[.]175[.]247[.]199/loader/server[.]exe` | URL | Additional suspicious executable URL found in VirusTotal relations |
| `hxxp://ripley[.]studio/loader/uploads/Qanjttrbv[.]jpeg` | URL | Suspicious URL associated with the investigated sample |

The URLs are defanged to reduce the risk of accidental access.

## 5. Threat Intelligence Findings

### URLhaus

The URLhaus host record associated the IP address with historical malware-distribution activity. The exact `install.exe` URL was listed with the tags CoinMiner, BitRAT and AsyncRAT.

This indicates that the URL has been associated with multiple malware classifications in threat-intelligence reporting. The tags do not prove that all three malware families were delivered to the recipient through this email.

### VirusTotal

VirusTotal showed two contacted URLs, each with 13 detections out of 95 security vendors. One URL referenced `Qanjttrbv.jpeg`, while the other referenced `server.exe` on the same IP address identified in the email.

These relationships and detection ratios provide additional suspicion indicators. They do not independently establish that the email recipient contacted these URLs or executed malware.

## 6. Risk Assessment

**Preliminary severity: High**

The assessment is based on the combination of a purchase-themed email, a direct-IP link to an executable, failed email authentication checks and supporting threat-intelligence records.

The severity is preliminary because the investigation has not established whether the message reached an end user's inbox, whether the link was clicked, or whether a payload executed.

## 7. Recommended Response

1. Quarantine the email and search for other copies across the organization's mail systems.
2. Block confirmed malicious URLs and infrastructure using approved security controls and current threat intelligence.
3. Review email gateway, DNS, proxy and endpoint logs for evidence of access or download activity.
4. Identify recipients and contact them through an appropriate security-awareness process.
5. If execution is suspected, isolate the affected endpoint and conduct an approved incident-response investigation.
6. Preserve the original email, headers, relevant logs and investigation screenshots.
7. Review email authentication configuration and investigate the sender through trusted channels.

## 8. Investigation Limitations

This investigation used the provided email sample and public threat-intelligence results. No evidence currently establishes successful malware execution, data exfiltration, financial loss or attacker identity.

The available evidence supports a suspicious-email classification, but additional recipient, network and endpoint evidence would be required to confirm a compromise.

## 9. Conclusion

The email exhibits multiple phishing and potential malware-distribution indicators. The executable link, authentication concerns and external threat-intelligence associations justify defensive action and further investigation.

The case demonstrates a structured email-analysis workflow involving header inspection, URL extraction, IOC documentation and threat-intelligence correlation.

## 10. Evidence

- Email header extraction: `Headers/email_1_headers.txt`
- URL extraction script: `Scripts/extract_urls.py`
- Header analysis script: `Scripts/analyze_email.py`
- IOC register: `IOCs/Investigation-01-IOCs.md`
- VirusTotal contacted-URLs screenshot: `Screenshots/virustotal-contacted-urls.png`

Additional evidence screenshots and tool records should be added as they are collected.