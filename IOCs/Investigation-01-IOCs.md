# Investigation 01 — IOC Register

## Suspicious Email

Subject: COMMERCIAL PURCHASE RECEIPT ONLINE 27 NOV

### Indicators

| Type | Value | Assessment |
|---|---|---|
| Malware delivery IP | 107.175.247.199 | High priority |
| Suspicious URL | hxxp://107[.]175[.]247[.]199/loader/install[.]exe | Malware delivery indicator |
| Filename | install.exe | Suspicious executable |
| SPF | SoftFail | Authentication concern |
| DKIM | Fail | Authentication concern |
| DMARC | None | No applicable enforcement result reported |

### Supporting Observations

- The executable URL appears twice in the email.
- The message uses a commercial invoice theme.
- The email includes a university logo image.
- The purported invoice link points to a Windows executable rather than an ordinary invoice document.

### Preliminary Conclusion

The email contains a suspicious executable download URL associated with malware distribution in the PhishStrike investigation.

Further threat intelligence analysis is required to establish the associated malware families and additional indicators.

## Threat Intelligence Correlation

### Source

URLhaus — Host record for 107.175.247.199

Reference: https://urlhaus.abuse.ch/host/107.175.247.199/

### Findings

The URLhaus record associates the host with multiple historical malware-distribution URLs.

The exact URL found in the email is tagged with:

- CoinMiner
- BitRAT
- AsyncRAT

The corresponding URL was listed as offline in the retrieved threat intelligence record.

### Confidence Assessment

- Suspicious URL identified in email: High confidence.
- Historical malware association: High confidence based on the URLhaus record.
- Actual execution on a recipient's computer: Not established.
- Attribution to a specific attacker: Not established.

### Recommended Response

1. Block the malicious URL and associated IP where appropriate, after validating the organization's current threat intelligence.
2. Search email gateway and proxy logs for the URL and IP.
3. Identify recipients who received the email and determine whether anyone clicked the link.
4. If execution is suspected, isolate the affected endpoint and investigate it using approved incident response procedures.
5. Preserve relevant email, endpoint and network evidence.

## Additional Threat Intelligence: VirusTotal Relations

### Source
VirusTotal — Contacted URLs associated with the investigated sample.

### Findings

Two suspicious URLs were identified in the VirusTotal relations:

1. `hxxp://ripley[.]studio/loader/uploads/Qanjttrbv[.]jpeg`
   - Detection ratio: 13/95
   - The `.jpeg` extension does not independently establish that the resource is a legitimate image.
   - The URL is considered suspicious based on its association with the investigated sample and its security-vendor detections.

2. `hxxp://107[.]175[.]247[.]199/loader/server[.]exe`
   - Detection ratio: 13/95
   - The URL points to an executable hosted at the same IP address found in the email investigation.
   - This provides additional evidence of potentially malicious activity associated with the host.

### Assessment

The VirusTotal results strengthen the suspicion that the host was associated with malware distribution. However, the contacted-URL relationships do not independently prove that either URL was accessed by the email recipient or that malware executed on a victim's device.

### Recommended Actions

- Block confirmed malicious URLs and infrastructure according to the organization's security procedures.
- Search email gateway, DNS, proxy and endpoint logs for these indicators.
- Determine whether any recipients clicked the email link or downloaded a file.
- Preserve the original email and relevant logs for further investigation.

### Evidence Limitations

The detection ratios and URL relationships are threat-intelligence indicators, not proof of a successful compromise. The investigation has not established victim execution, data theft or attribution to a specific attacker.