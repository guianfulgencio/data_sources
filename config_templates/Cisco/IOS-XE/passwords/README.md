# Passwords

Network devices would normally use TACACS authentication but there are local passwords of last resort configured on each device

- password applied to the vty and console lines
- admin account with password for ssh access
- enable password to access privileged mode

## Configuration

- Apply [line-passwords](line-passwords.j2)
- Apply [secrets](secrets.j2)