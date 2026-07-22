---
layout: default
title: Roles and permissions
description: Choose manageable Discord roles and keep NovaPulse within a least-privilege hierarchy.
permalink: /configuration/roles-and-permissions/
section: configuration
section_title: Configuration
section_url: /configuration/
---

NovaPulse can use verified, non-verified, automatic join, gender, pronoun, exemption, and other workflow roles. Every configured role must be appropriate for automation.

## Role checklist

- The role is below NovaPulse in **Server Settings → Roles**.
- The role is not managed by another bot, booster integration, or connected service.
- Assigning the role does not grant Administrator or another broad privilege.
- Removing the role will not lock staff out of the server.
- The role name clearly explains its purpose to staff.
- Staff have documented who may change the configuration.

## Recommended hierarchy

```text
Server Owner
Senior Staff
NovaPulse
Moderator or workflow roles NovaPulse must manage
Verified / Member / Pending roles
@everyone
```

This is a conceptual order. Your server may differ, but NovaPulse cannot manage a role equal to or above its highest role.

## Configure roles

Use the configuration commands for the selected workflow, then run <code>/view-config</code>. Test with a disposable role before using a real member cohort.

## Avoid privilege escalation

Do not configure NovaPulse to assign a role that grants Administrator, Manage Server, Manage Roles above trusted boundaries, or access to secret staff channels. Automated roles should be narrower than the staff permissions used to configure them.
