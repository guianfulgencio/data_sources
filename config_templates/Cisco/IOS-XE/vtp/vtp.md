# VTP

VLAN Trunking Protocol (VTP) is a legacy protocol to advertise created vlans to other switches in the same LAN.

Chevron's standard is to turn it off on supported switches and set to transparent on legacy switches.

## Setup

- Apply [vtp](vtp.j2) to modern switches
- Apply [vtp-legacy](vtp-legacy.j2) to ancient switches
