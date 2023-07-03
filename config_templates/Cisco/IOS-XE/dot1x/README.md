# Dot1x

## IOS Dependencies

There are two standard dot1x configurations deployed depending on the version of IOS on the switches

- Current : IOS Denali, Fuji and later
- Legacy : IOS versions prior to Denali (IOS XE 16.3.1)

## RADIUS Servers

1. Apply [dot1x-radius.j2](dot1x-radius.j2) to configure the RADIUS servers to use

## Current Configuration

1. Apply [dot1x-global.j2](dot1x-global.j2) to configure the system level dot1x commands
1. Apply [dot1x-interface.j2](dot1x-interface.j2) to configure dot1x on any downlink interfaces

## Legacy Configuration

1. Apply [dot1x-global-legacy.j2](dot1x-global-legacy.j2) to configure the system level dot1x commands
1. Apply [dot1x-interface-legacy.j2](dot1x-interface-legacy.j2) to configure dot1x on any downlink interfaces

## Troubleshooting and Verification

To be completed