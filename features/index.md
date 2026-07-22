---
layout: default
title: Feature overview
description: Understand confirmed NovaPulse capabilities, their intended audience, and their current release status.
permalink: /features/
section: features
status: Documentation preview
status_style: info
---

NovaPulse is a multi-purpose Discord operations bot. The current source confirms the features below, but public availability is not uniform.

<div class="table-wrap" markdown="1">

| Feature | Confirmed behavior | Current status |
| --- | --- | --- |
| Server configuration | Guild-specific roles, channels, logging destinations, and redacted configuration review | Controlled administration |
| Introduction workflow | Button and modal flow with optional role validation | Controlled testing |
| Staff-reviewed ID verification | Stripe Identity session plus manual staff approval and role assignment | Controlled; legal/privacy review required |
| Join automation | Auto roles, non-verified roles, bot-role behavior, and invite attribution | Opt-in and retention work pending |
| Customer-server logging | Configured Discord channels and optional webhooks | Controlled; server access policy required |
| NovaTrap | Warning channel, spam detection, dry-run scans, message cleanup, recovery DM, timeout or softban | Automatic enforcement deferred |
| Anti-nuke | Audit-log detection for channel deletion, role deletion, and kicks | Emergency lockdown deferred |
| Bulk moderation | Role-wide kick and full unban | Public rollout deferred |

</div>

## What NovaPulse does not currently provide

The validated source does not contain general invite filtering, mention-spam detection, same-channel flood limits, warning/strike cases, native Discord AutoMod integration, an appeal form, a durable moderation-case database, or a public setup wizard.

## Explore a feature

<div class="doc-grid">
  <article class="doc-card"><h3>NovaTrap</h3><p>Purpose, triggers, exemptions, logs, safe testing, and deferred safeguards.</p><p><a href="{{ '/features/novatrap/' | relative_url }}">Read NovaTrap guide</a></p></article>
  <article class="doc-card"><h3>Verification</h3><p>Introductions, roles, third-party identity sessions, and staff review.</p><p><a href="{{ '/features/verification/' | relative_url }}">Read verification guide</a></p></article>
  <article class="doc-card"><h3>Logging</h3><p>Customer-server records versus minimal internal operational monitoring.</p><p><a href="{{ '/features/logging/' | relative_url }}">Read logging guide</a></p></article>
  <article class="doc-card"><h3>Server security</h3><p>Anti-nuke monitoring, audit-log access, exemptions, and limits.</p><p><a href="{{ '/features/server-security/' | relative_url }}">Read security guide</a></p></article>
</div>
