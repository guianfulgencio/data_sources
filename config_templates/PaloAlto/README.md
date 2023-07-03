# General Guidelines

Details on how to use the below templates to configure a piece of equipment running IOS-XE are displayed in the [README.md](README.md) file in each folder in this repo.

## Compatible Plaforms

| Platform   | Tested Version | Notes                              |
|------------|----------------|------------------------------------|
|            |                |                                    |

## Netflow

### Netflow Setup and Instructions

1. Apply [netflow-base.j2](netflow-base.j2)
1. Apply [netflow-servers.j2](netflow-servers.j2)  
   Servers in production are listed below. **RECOMMENDED : USE ANYCAST**

| System and Location | IP Address    | UDP Port       | Notes                      |
|---------------------|---------------|----------------|----------------------------|
| Anycast             | 139.65.245.55 | 2055           | Various - fan out system   |
| US Solarwinds       |               |                |                            |
|                     |               |                |                            |

1. Apply [netflow-interfaces.j2](netflow-interfaces.j2)

### Netflow Troubleshooting and Verification

1. Check Flow Exporter
``show flow exporter``  

1. Check Flow Exporter Statistics
``show flow exporter NETQOS-EXPORTER statistics``

1. Check Flow Enabled Interfaces
``show flow interface``

