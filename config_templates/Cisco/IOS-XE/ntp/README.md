# NTP

## Setup and Instructions

1. Apply [ntp.j2](ntp.j2)  
   **IMPORTANT**: Use three NTP servers for accurate time sync

> Do not set a timezone or daylight savings time. All systems should default to UTC.

## Troubleshooting and Verification

### Check NTP associations

```
show ntp associations

    address         ref clock       st   when   poll reach  delay  offset   disp
*~146.38.37.9     .GPS.            1    914   1024   377  0.089  -0.583  1.098
+~146.22.70.251   .CDMA.           1    148   1024   377 112.88  -1.522  1.128
    ~146.38.105.70   .STEP.          16      -   1024     0  0.000   0.000 15937.
    * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
```   
St 16 (stratum 16) shows the system is not getting a sync from this NTP server. The IP address of the NTP server is probably incorrect.
    
### Check NTP sync status

```
WFCRM1V#show ntp status 
Clock is synchronized, stratum 2, reference is 146.38.37.9    
nominal freq is 250.0000 Hz, actual freq is 249.9968 Hz, precision is 2**10
ntp uptime is 2700793704 (1/100 of seconds), resolution is 4016
reference time is E5AE320A.67EF9ED0 (12:28:58.406 UTC Wed Feb 9 2022)
clock offset is -0.5839 msec, root delay is 0.84 msec
root dispersion is 33.85 msec, peer dispersion is 1.09 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000012749 s/s
system poll interval is 1024, last update was 2068 sec ago.
```

Clock is synchronized stratum 2 shows the system has successfully synchronized its internal clock to the NTP server
