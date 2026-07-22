---
layout: default
title: Logging
description: Distinguish customer-server logs from NovaPulse's minimal, redacted operational monitoring.
permalink: /features/logging/
section: features
section_title: Features
section_url: /features/
---

NovaPulse uses two separate logging concepts. Keeping them separate helps server owners understand where records go and who controls access.

## Customer-server logs

Server administrators choose Discord channels or supported webhook destinations for events such as invites, introductions, roles, kicks, bans, bulk unbans, verification approvals, NovaTrap detections, and anti-nuke alerts.

These records are delivered inside infrastructure chosen by the customer server. The server administrator controls channel permissions and should define retention, review access, and deletion rules.

NovaTrap evidence can include message content and attachment links when needed to explain a detection. Restrict these logs to authorized moderators and avoid copying them outside the server.

## Internal NovaPulse operational monitoring

The Phase 1A implementation added centralized redaction and optional internal channels for service activity, redacted errors, shard or uptime status, and minimal security summaries. Internal monitoring is designed to use an allowlist of minimal metadata.

It should not contain private message content, full moderation evidence, raw configuration, webhook credentials, complete member records, invite history, or cross-server private records.

## What users should expect

- User-facing errors may contain a safe NovaPulse reference ID for support.
- <code>/view-config</code> hides webhook URLs and tokens.
- The restricted internal operational-summary command does not return raw logs or guild data.
- Missing monitoring channels should not interrupt customer-server moderation or commands.

## Configure responsibly

Use [Log channels]({{ '/configuration/log-channels/' | relative_url }}) and [Configure logs]({{ '/guides/configuring-logs/' | relative_url }}) to select destinations and test access.
