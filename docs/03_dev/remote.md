---
icon: material/remote-desktop
---

# :material-remote-desktop: Remote Development
Start by generating SSH keys.

```bash
ssh-keygen                          # Generate SSH key
```

Copy your SSH keys to the host.
```bash
ssh-copy-id <user_id>@<host_ip>     # Copy the SSH keys to the host
```

Log into the host.
```bash
ssh <user_id>@<host_ip>             # Log into the host
```