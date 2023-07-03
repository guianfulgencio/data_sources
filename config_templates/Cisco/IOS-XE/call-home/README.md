# Call Home

Cisco's Call Home service is used for smart license verification and reporting system status to Cisco Smart Software Manager (CSSM).

## CSSM configuration

There are two options to connect to Cisco's systems

1. Direct to Cisco (preferred)
1. Via the on-prem CSSM server in Houston

### Direct to the Cloud service

> This option is preferred

Use this option for systems that have Internet access via the default route firewall. All devices with management interfaces connected to the corporate network should be able to reach Cisco's cloud service.

Apply [call-home-cisco.j2](call-home-cisco.j2)

### Via the CSSM server

Only use this option when the device does not have Internet access via the default route firewalls but can reach the Houston server

Apply [call-home-onprem.j2](call-home-onprem.j2)

## License Registration

When the system has registered with the CSSM service, obtain a token ID for the license to be activated

Apply [call-home-enrollment.j2](call-home-enrollment.j2)
