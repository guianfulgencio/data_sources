# Readme

The samplicator network management solution uses two software elements installed on a Red Hat Linux (RHEL) server

1. Samplicator running to perform the packet replication function (three instances running as three separate services)
1. Gocast as a BGP daemon running on the Linux server checking whether samplicator is running and advertising the appropriate loopback addresses to the network

| Function | Virtual IP    | Port | Service name |
|----------|---------------|------|--------------|
| Netflow  | 139.65.245.55 | 2055 | samplicator-netflow  |
| Syslog   | 139.65.245.14 | 514  | samplicator-syslog   |
| SNMPrap  | 139.65.245.62 | 162  | samplicator-snmptrap |

## Automated Installation

Need a Linux admin to write a shell script which does a curl to the git repo and copies the files to the right places

## Manual Installation

Clone or pull down the repo files from https://chevron@dev.azure.com/chevron/TPS-ITC-AnsibleNetwork/_git/Golden_templates/Samplicator then sftp all the files to ``/var/tmp`` on the host.

An example set of sftp commands is listed below
```
sftp> cd /var/tmp
sftp> mkdir samplicator
sftp> cd samplicator
sftp> lcd C:\Users\hosg\repos\Golden_templates-1\Samplicator    
sftp> put -r *
```

Copy files to the appropriate place on the host
```
cd /var/tmp/samplicator
sudo cp etc/* /usr/local/etc
sudo cp bin/* /usr/local/bin
sudo cp services/* /usr/lib/systemd/system
```

Make the binaries executable
```
sudo chmod +x /usr/local/bin/gocast
sudo chmod +x /usr/local/bin/samplicate
```

## Samplicator services

Enable the services

```bash
sudo systemctl enable samplicator-syslog
sudo systemctl enable samplicator-snmptrap
sudo systemctl enable samplicator-netflow
```

Start services and verify they are running

```
sudo systemctl start samplicator-syslog
sudo systemctl start samplicator-snmptrap
sudo systemctl start samplicator-netflow

sudo systemctl status samplicator-syslog
sudo systemctl status samplicator-snmptrap
sudo systemctl status samplicator-netflow
```

Use netstat to verify the processes are running on the ports you expect bound to the appropriate loopback

```
[ec2-user@ip-172-31-14-246 system]$ sudo netstat -pln | grep samplicate
udp        0      0 0.0.0.0:514             0.0.0.0:*                           2814/samplicate     
udp        0      0 0.0.0.0:2055            0.0.0.0:*                           2812/samplicate     
udp        0      0 0.0.0.0:162             0.0.0.0:*                           2816/samplicate     
raw        0      0 0.0.0.0:255             0.0.0.0:*               7           2816/samplicate     
raw        0      0 0.0.0.0:255             0.0.0.0:*               7           2814/samplicate     
raw        0      0 0.0.0.0:255             0.0.0.0:*               7           2812/samplicate    
```

## Gocast

Gocast is a wrapper around the popular GoBGP library that provides built in process monitoring and configuration of virtual IP addresses. It is much easier to configure than having separate healthcheck scripts and BGP configuration, but you do lose the ability to do complex BGP troubleshooting (this will need to be done on the peer).

The ``/usr/local/etc/config.yaml`` file just needs editing with the variables replaced.

``sudo vi /usr/local/etc/config.yaml`` and replace

- {{remote-as}} with the BGP AS number of the peer
- {{remote-ip}} with the IP address of the peer *if it is not the default gateway*
  If you are peering with the default gateway (usual topology) then leave it commented out

Then just start and verify the gocast service

```bash
sudo systemctl enable gocast
sudo systemctl start gocast
sudo systemctl status gocast
```

### Gocast verification

Use ``ifconfig`` to show the virtual ip addresses bound to the loopback address. If you stop a samplicator service you should see the vip disappear in 10 seconds (``sudo systemctl stop sampplicator-netflow``)

```
[ec2-user@ip-172-31-16-246 system]$ sudo systemctl status gocast
â— gocast.service - GoCast
   Loaded: loaded (/usr/lib/systemd/system/gocast.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2021-10-27 11:28:36 UTC; 2s ago
 Main PID: 32467 (gocast)
   CGroup: /system.slice/gocast.service
           â””â”€32467 /usr/local/bin/gocast -logtostderr -v=2 -config /usr/local/etc/gocast.yaml

Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal systemd[1]: Started GoCast.
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.963202   32467 monitor.go:174] Registered a new app: Name: anycast-netflow, Vip: 139....e: config
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.963248   32467 monitor.go:174] Registered a new app: Name: anycast-syslog, Vip: 139.6...e: config
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.963265   32467 monitor.go:174] Registered a new app: Name: anycast-snmptrap, Vip: 139...e: config
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.964144   32467 monitor.go:234] All Monitors for app: anycast-netflow succeeded
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.966766   32467 server.go:29] Starting http server on 127.0.0.1:8080
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: time="2021-10-27T11:28:36Z" level=info msg="Add a peer configuration for:172.31.1.251" Topic=Peer
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.969835   32467 monitor.go:234] All Monitors for app: anycast-syslog succeeded
Oct 27 11:28:36 ip-172-31-16-246.eu-west-1.compute.internal gocast[32467]: I1027 11:28:36.977557   32467 monitor.go:234] All Monitors for app: anycast-snmptrap succeeded
```

Upstream BGP neighbour should show the VIPs being advertised.

### Example Gocast config file

```yml
agent:
  # http server listen addr
  # listen_addr: :8080
  # Interval for health check
  monitor_interval: 10s
  # Time to flush out inactive apps
  cleanup_timer: 15m
  # Consul api addr for dynamic discovery
  # consul_addr: https://consul
  # interval to query consul for app discovery
  # consul_query_interval: 5m

bgp:
  local_as: 65453
  remote_as: 65000
  # override the peer IP to use instead of assuming the default gateway
  # peer_ip: 172.31.1.251
  origin: igp

# optional list of apps to register on startup
apps:
  - name: netflow
    vip: 139.65.245.55/32
    vip_config:
      # additional per VIP BGP communities
      bgp_communities: [ 65453:2055 ]
    monitors: [ port:udp:2055 ]
  - name: syslog
    vip: 139.65.245.14/32
    vip_config:
      # additional per VIP BGP communities
      bgp_communities: [ 65453:514 ]
    monitors: [ port:udp:514 ]
  - name: snmptrap
    vip: 139.65.245.62/32
    vip_config:
      # additional per VIP BGP communities
      bgp_communities: [ 65453:162 ]
    monitors: [ port:udp:162 ]
```
