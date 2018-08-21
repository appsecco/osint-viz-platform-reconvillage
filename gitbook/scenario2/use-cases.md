# Use cases and ideas

- FDNS dataset is a contains a large amount of historical DNS information which makes it an valuable dataset when understanding an organisation's external posture
- Rapid7 Labs Open Data project maintains periodical snapshots of the FDNS dataset. All the snapshots contain historical DNS information. By carefully examining all the A or AAAA records that are associated with a domain over a period of time, we will be able to find origin servers of websites that are protected by services like CloudFlare
- Find subdomains that may have been moved between companies during acquisition etc.
- Find TXT records that may reveal SPF related information. This could lead to the discovery of additional domains/IP addresses
