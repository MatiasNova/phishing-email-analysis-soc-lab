# Phishing Email Analysis & Threat Intelligence Investigation

## Project Overview

This project demonstrates a defensive cybersecurity investigation of a suspicious email using email-header analysis, automated URL extraction and public threat-intelligence resources.

The investigation is based on the PhishStrike challenge from CyberDefenders. The email claims to concern a commercial purchase and contains a link to an executable file hosted on an IP address.

The objective was to identify suspicious indicators, assess available threat intelligence, document the findings and recommend defensive actions.

## Objectives

- Inspect email headers and authentication results.
- Extract URLs from an email using Python.
- Identify suspicious URLs and infrastructure.
- Correlate indicators with public threat-intelligence sources.
- Document findings in an IOC register and incident report.
- Recommend practical incident-response actions.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Automating email-header and URL extraction |
| VirusTotal | Reviewing URL detections and sample relationships |
| URLhaus | Checking historical malware-distribution records |
| Windows PowerShell | Running analysis scripts and managing project files |
| Markdown | Documenting indicators, evidence and findings |

## Investigation Workflow

1. **Email acquisition:** Obtained the provided email sample from the CyberDefenders challenge.
2. **Header analysis:** Extracted sender details, routing information and authentication results.
3. **URL extraction:** Used Python to identify URLs embedded in the email.
4. **Threat intelligence:** Checked the suspicious IP address and related URLs against URLhaus and VirusTotal.
5. **IOC documentation:** Recorded suspicious infrastructure and supporting observations.
6. **Incident reporting:** Documented the findings, limitations, preliminary severity and recommended defensive actions.

## Key Findings

- The email's authentication results showed SPF SoftFail, DKIM failure and no DMARC policy result reported in the authentication headers.
- The email contained a suspicious direct-IP link to an executable named `install.exe`.
- URLhaus associated the IP address with historical malware-distribution activity.
- VirusTotal showed suspicious related URLs, each with 13 detections out of 95 security vendors.
- The investigation did not establish whether a recipient clicked the link or whether malware executed.

## Indicators of Compromise

The investigation recorded the following indicators:

| Indicator | Type | Assessment |
|---|---|---|
| `107.175.247.199` | IP address | Associated with historical malware-distribution records |
| `hxxp://107[.]175[.]247[.]199/loader/install[.]exe` | URL | Extracted from the suspicious email |
| `hxxp://107[.]175[.]247[.]199/loader/server[.]exe` | URL | Related suspicious executable URL |
| `hxxp://ripley[.]studio/loader/uploads/Qanjttrbv[.]jpeg` | URL | Suspicious URL associated with the investigated sample |

URLs are intentionally defanged to reduce the risk of accidental access. These indicators should be revalidated against current threat intelligence before being used in production security controls.

## Repository Structure

```text
Phishing-Email-Analysis/
├── Samples/
│   ├── Original/
│   └── Working/
├── Headers/
├── IOCs/
├── Screenshots/
├── Reports/
├── Scripts/
│   ├── analyze_headers.py
│   └── extract_urls.py
└── README.md
```

## Project Deliverables

- Python script for extracting email headers.
- Python script for extracting URLs.
- IOC register containing suspicious indicators and threat-intelligence findings.
- Incident report documenting the investigation and recommended response.
- Screenshots supporting the investigation.

## Security and Ethical Considerations

This project was conducted for defensive cybersecurity learning. Analysis focused on static inspection and public threat-intelligence sources.

Suspicious URLs and executable files were not intentionally opened or executed. Findings are limited to the evidence available from the supplied sample and external intelligence records.

## Lessons Learned

This investigation provided practical experience in:

- Interpreting SPF, DKIM and DMARC results.
- Identifying suspicious URLs in email messages.
- Correlating indicators across threat-intelligence sources.
- Distinguishing suspicious evidence from confirmed compromise.
- Producing structured incident documentation.

## Reference

CyberDefenders — PhishStrike

https://cyberdefenders.org/blueteam-ctf-challenges/phishstrike/

URLhaus host record:

https://urlhaus.abuse.ch/host/107.175.247.199/

VirusTotal:

https://www.virustotal.com/

## Disclaimer

This project is intended for education and defensive security research. The findings are based on the available investigation evidence and do not independently establish successful compromise or attribution to a specific threat actor.