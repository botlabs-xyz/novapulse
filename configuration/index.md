---
layout: default
title: Configuration overview
description: Plan NovaPulse roles, channels, logging, verification, and security settings before changing the server.
permalink: /configuration/
section: configuration
status: Administrator guide
status_style: info
---

A safe NovaPulse configuration is guild-specific, least-privileged, and easy for staff to review. The current build stores settings per server and <code>/view-config</code> returns only the current server's redacted summary.

## Recommended order

1. [Roles and permissions]({{ '/configuration/roles-and-permissions/' | relative_url }})
2. [Log channels]({{ '/configuration/log-channels/' | relative_url }})
3. [Verification settings]({{ '/configuration/verification-settings/' | relative_url }})
4. [Security settings]({{ '/configuration/security-settings/' | relative_url }}) when your server uses an advanced security feature

## Configuration principles

- Grant only the permissions needed by enabled features.
- Prefer server-owned channels over manually pasted webhook credentials.
- Keep log channels private to relevant staff.
- Choose roles below the NovaPulse role.
- Review settings with <code>/view-config</code> after each change.
- Clear unused settings with <code>/clear-config</code> rather than leaving stale channels or roles.
- Never paste bot tokens, secret keys, complete environment files, or database files into commands or support tickets.

## Deleted resources

If a configured role or channel is deleted, <code>/view-config</code> may show it as unavailable. Reconfigure or clear that item. Do not create a replacement with the same name and assume NovaPulse will automatically use it; Discord identifies resources by ID.
