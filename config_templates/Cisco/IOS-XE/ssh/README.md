# SSH

SSH is mandatory on all network equipment with telnet as a banned protocol due to its insecure, plain text protocol.

## Pre-requisites

A valid hostname and domain-name must be set. Changing either of these after the ssh keys are generated will result in invalid keys.

## Configuration

Apply the [ssh](ssh.j2) configuration.

## Generate the SSH keys

Run the exec command ``crypto key generate rsa modulus 2048``
