---
layout: default
title: Security settings
description: Review NovaTrap and anti-nuke settings before enabling an authorized advanced security feature.
permalink: /configuration/security-settings/
section: configuration
section_title: Configuration
section_url: /configuration/
status: Advanced feature
status_style: warning
---

NovaTrap and anti-nuke settings are available only for authorized advanced deployments. Start with observation or dry-run behavior, and make sure your staff understand the feature before enabling it.

## NovaTrap baseline

- Use a dedicated test channel.
- Configure a private staff log destination.
- Keep dry-run enabled for scans and manual cleanup.
- Review user and role exemptions.
- Do not configure an unreviewed recovery URL or expose a webhook URL.
- Confirm the bot can delete messages before assuming spam will be removed.

Use <code>/honeypot stats</code> to review the current configuration.

## Anti-nuke baseline

- Keep emergency lockdown disabled until a safe test is approved.
- Give View Audit Log only if audit attribution is required.
- Configure a server-owned alert channel.
- Exempt trusted response roles explicitly.
- Test alert-only behavior with synthetic events.
- Do not test role stripping or timeouts on staff accounts.

## Change review

Record who approved the setting, when it was changed, which test was run, and how the feature can be disabled. Keep this record in your server's staff process.
