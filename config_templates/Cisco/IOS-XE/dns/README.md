# DNS

## Implementation Notes

Chevron uses a set of Anycast servers for consistent configuration globally (146.23.1.1 and 146.23.2.2)

## Setup and Instructions

!!! warning
    Changing the domain name invalidates the SSH keys on the device
    Apply [SSH](ssh.md) before applying the DNS configuration

1. Apply [dns.j2](dns.j2)

## Troubleshooting and Verification

### Ping

Ping a given domain name (e.g. ``ping resolver1.chevron.com``)
