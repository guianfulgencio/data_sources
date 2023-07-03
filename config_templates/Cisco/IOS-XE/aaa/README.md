# AAA Configuration

AAA can be tricky to deploy. Make sure you apply configuration in the right order

## Pre-Requisites

> Deploy passwords to the devices which includes username, secret and other passwords

## Setup

- Apply [aaa-servers](aaa-servers.j2) to define the TACACS servers and create a group
- Apply [aaa-authentication](aaa-authentication.j2) to define authentication commands
- Reauthenticate to the device
- Apply [aaa-authorization](aaa-authorization.j2)