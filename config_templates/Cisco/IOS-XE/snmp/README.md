# SNMP

SNMP v3 is our standard configuration. SNMP v2c is deprecated due to its insecure nature (though some network management systems still "like" v2C)

## Configuration

Follow these steps

1. Base configuration [snmp.j2](./snmp.j2)
1. Access-list to secure the device
1. SNMPv3 groups and associated configuration
1. SNMPv3 usernames
1. SNMPv3 trap destinations and config