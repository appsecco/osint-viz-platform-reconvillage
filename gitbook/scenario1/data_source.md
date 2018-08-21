# Data source 

## Certificate Transparency Logs

- Under Certificate Transparency(CT), a Certificate Authority(CA) will have to publish all SSL/TLS certificates they issue in a public log
Anyone can look through the CT logs and find certificates issued for a domain
- Details of known CT log files can be found at - https://www.certificate-transparency.org/known-logs
- CT logs by design contain all the certificates issued by a participating CA for any given domain. These logs are available publicly and anyone can look through these logs
- CT logs are append-only and the integrity of the data is cryptographically verified (sort of like block chain)
- Basically, if you have buy a new SSL/TLS certificate, it will end up on the CT Logs
- CT is to prevent malicious actors from getting away with the creation of rogue certificates 
- Attackers and bug bounty hunters often use this to identify sub-domains to increase the attack surface of their targets

- You can read more about Certificate Transparency on our technical blog https://blog.appsecco.com/certificate-transparency-the-bright-side-and-the-dark-side-8aa47d9a6616