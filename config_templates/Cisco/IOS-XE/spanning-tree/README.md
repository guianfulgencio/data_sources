# Spanning-Tree

## Protocol Notes

Chevron uses Cisco's per-vlan rapid spanning tree protocol.

## Setup and Instructions

1. Apply [spanning-tree.j2](spanning-tree.j2) to all layer 2 switches in a given local area network  

1. Apply [spanning-tree-root.j2](spanning-tree-root.j2) only on layer 3 core switch(es) in a given local area network

## Troubleshooting and Verification

### Spanning Tree Status

Displays the following information for a given vlan

1. Who is the root
1. Global timers
1. Which links are members of the vlan
1. Which links are fordwarding and blocking

```
#show spanning-tree vlan 192

VLAN0192
  Spanning tree enabled protocol ieee
  Root ID    Priority    32960
             Address     0008.e3ff.fc28
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32960  (priority 32768 sys-id-ext 192)
             Address     0008.e3ff.fc28
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Te1/1/19            Desg FWD 4         128.19   P2p 
Te1/1/20            Desg FWD 4         128.20   P2p 
Te2/1/19            Desg FWD 4         128.1299 P2p 
Te2/1/20            Desg FWD 4         128.1300 P2p 
Po22                Desg FWD 3         128.2582 P2p 
Po23                Desg FWD 3         128.2583 P2p 
Po33                Desg FWD 3         128.2593 P2p 
```   
