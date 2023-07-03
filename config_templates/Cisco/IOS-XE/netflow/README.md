# Netflow

## Setup Instructions

1. Apply [netflow-base.j2](netflow-base.j2)
1. Apply [netflow-servers.j2](netflow-servers.j2)  
   Servers in production are listed below. **RECOMMENDED : USE ANYCAST**
    | System and Location | IP Address    | UDP Port       | Notes                      |
    |---------------------|---------------|----------------|----------------------------|
    | Anycast             | 139.65.245.55 | 2055           | Various - fan out system   |
    | US Solarwinds       |               |                |                            |
    |                     |               |                |                            |

1. Apply [netflow-interfaces.j2](netflow-interfaces.j2)

## Troubleshooting and Verification

### Check Flow Exporter

``show flow exporter``  

### Check Flow Exporter Statistics

``show flow exporter NETQOS-EXPORTER statistics``

### Check Flow Enabled Interfaces

``show flow interface``
