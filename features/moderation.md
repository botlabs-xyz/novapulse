---
layout: default
title: Moderation
description: Understand NovaPulse moderation actions, Discord hierarchy, and the safeguards still required for public use.
permalink: /features/moderation/
section: features
section_title: Features
section_url: /features/
status: Controlled actions
status_style: danger
---

NovaPulse can kick members by role, unban a complete ban list, time out or remove accounts through NovaTrap, and ban through a configured introduction age policy.

## Administrator responsibility

Server administrators remain responsible for configuring commands, limiting staff access, choosing server policies, reviewing predicted targets, handling appeals, and complying with Discord's rules and applicable law. NovaPulse does not replace staff judgment.

## Current safeguards

- Discord default command permissions limit which commands are normally visible.
- Some commands check the invoking member's permission again at runtime.
- NovaTrap dry-run tools default to preview mode.
- The bot checks some of its own required action permissions.
- Discord role hierarchy prevents action against equal or higher roles.

## Release gaps

- Bulk kick and bulk unban lack confirmation flows.
- Bulk actions need target caps, invoker hierarchy checks, immutable action records, and rollback procedures.
- Automated age-policy bans need human review, typo protection, and appeal.
- NovaTrap needs a durable case model, safer default gates, and measured false-positive testing.
- Anti-nuke lockdown needs stronger staff exemptions and complete preflight checks.

## Safe operating rule

Do not grant a staff role access to a NovaPulse command merely because that role can see the command. Limit destructive commands through Discord's command settings, use a staff-only channel, and keep the NovaPulse role below trusted senior staff.

See [Moderation commands]({{ '/commands/moderation/' | relative_url }}) and [Permissions]({{ '/getting-started/permissions/' | relative_url }}).
