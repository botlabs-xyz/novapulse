---
layout: default
title: NovaTrap
description: Draft safety documentation for NovaPulse's controlled warning-channel and anti-spam system.
permalink: /features/novatrap/
section: features
section_title: Features
section_url: /features/
status: Draft · enforcement deferred
status_style: danger
---

NovaTrap is the public name for the feature called **Honeypot** in the current commands. It combines a configured do-not-message channel with optional spam detection, recovery messaging, message cleanup, moderation action, and staff logging.

<div class="notice danger">
  This page is a controlled-release draft. Do not enable automatic NovaTrap enforcement in an unrestricted public server. The current safety review identifies false-positive, disable-gate, message-history deletion, recovery-link validation, retention, case-review, and appeal work that must be completed first.
</div>

## Purpose

NovaTrap is intended to identify a likely compromised account that posts in a clearly marked warning channel or repeats high-confidence spam across public channels. The intended response is to remove harmful messages, warn the account owner through a recovery DM, apply the configured moderation action, and notify server staff.

It is not a general anti-raid, mention-spam, invite-filter, or account-risk system.

## What members should avoid

- Do not post, reply, or attach files in the configured NovaTrap channel.
- Do not test the panel with a real account.
- Do not repeat suspicious promotional or account-compromise content across channels.
- If you believe an action was incorrect, contact server staff or the [NovaPulse support server]({{ site.links.support }}).

Reactions, direct messages to the bot, message edits, and thread messages are not confirmed trigger surfaces in the current implementation. Any normal member message posted directly in the configured trap channel can trigger, including an attachment-only message.

## Confirmed exemptions

The current implementation skips bots and protects the server owner, NovaPulse owner/developer identities, configured exempt users and roles, administrators, and members with common moderation permissions by default. Staff-safety settings require further hardening so they cannot be weakened accidentally.

## Possible moderation actions

- **Timeout** for the configured duration, capped by Discord's maximum.
- **Softban**, implemented as a ban followed by an unban, with a kick fallback if the ban path is unavailable.
- **Message deletion** when NovaPulse has Manage Messages in each source channel.
- **Recovery DM** before removal, using a configured rejoin destination or support fallback.

<div class="notice warning">
  The current softban path may request deletion of recent message history beyond the triggering spam. Public use is deferred until that behavior is reduced and documented.
</div>

## Administrator configuration

Review settings with <code>/honeypot stats</code>. Use dry-run tools only in the current documentation phase:

```text
/honeypot scan-spam messages:100 max-age-days:7 dryrun:true
/honeypot cleanup-users users:@TestMember dryrun:true
```

The available configuration includes the trap channel, staff log destination, recovery invite, timeout or softban action, timeout duration, cross-channel behavior, exclusions, statistics, and warning-message synchronization. Do not paste webhook credentials into a public channel or support ticket.

## Role and channel requirements

NovaPulse needs View Channel, Send Messages, Embed Links, and Manage Messages in the trap channel for setup. Live actions may additionally require Moderate Members, Kick Members, or Ban Members. The bot role must be above every target it may time out, kick, or ban.

If message deletion is unavailable, the current implementation may still continue with member enforcement. This behavior is part of the release review; staff must not assume that removing a member also removed the spam.

## Logging

A configured customer-server log may include the affected user and channel identifiers, triggering message details, attachment links, matched indicators, deletion outcomes, recovery-DM outcome, moderation action, and counters. Those records remain under the server's access and retention controls.

NovaPulse does not currently maintain a durable moderation-case database with a case owner, appeal state, reversal, policy version, and retention deadline.

## Safe testing

1. Keep live enforcement disabled.
2. Use a private test server or dedicated test channels.
3. Use a non-staff test account and synthetic, non-harmful text.
4. Run <code>scan-spam</code> or <code>cleanup-users</code> with <code>dryrun:true</code> only.
5. Confirm excluded channels, staff roles, and logging access.
6. Review the predicted targets manually.
7. Do not enable live action until the NovaPulse owner approves the release gate.

## Appeals and recovery

The current bot has no built-in appeal form. Affected members should contact their server's moderators first. Server staff can escalate a suspected false positive through the [Afterparty Bot Labs support server]({{ site.links.support }}). Do not send identity documents, account passwords, tokens, or private server exports.
