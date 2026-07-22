---
layout: default
title: Security settings
description: Review NovaTrap and anti-nuke settings without enabling unsafe automatic enforcement.
permalink: /configuration/security-settings/
section: configuration
section_title: Configuration
section_url: /configuration/
status: Controlled deployment only
status_style: danger
---

Security features should begin in observation or dry-run mode. The current release audit does not approve automatic enforcement for unrestricted public servers.

## NovaTrap baseline

- Keep automatic enforcement disabled.
- Use a dedicated test channel.
- Configure a private staff log destination.
- Keep dry-run enabled for scans and manual cleanup.
- Review user and role exemptions.
- Do not configure an unreviewed recovery URL or expose a webhook URL.
- Confirm the bot can delete messages before assuming spam will be removed.

Use <code>/honeypot stats</code> to review the current configuration. Note that the validated audit found that disabling the main flag did not stop every related detector; the release remediation must establish one master gate before public use.

## Anti-nuke baseline

- Keep emergency lockdown disabled.
- Give View Audit Log only if audit attribution is required.
- Configure a server-owned alert channel.
- Exempt trusted response roles explicitly.
- Test alert-only behavior with synthetic events.
- Do not test role stripping or timeouts on staff accounts.

## Change review

Record who approved the setting, when it was changed, which test was run, and how the feature can be disabled. The current bot does not yet provide a durable policy-versioned case system, so this operational record belongs in the server's approved staff process.
