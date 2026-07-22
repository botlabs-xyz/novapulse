---
layout: default
title: NovaTrap
description: Learn how NovaTrap warning-channel and anti-spam tooling works, including safe setup and testing.
permalink: /features/novatrap/
section: features
section_title: Features
section_url: /features/
status: Advanced feature
status_style: danger
---

NovaTrap is the public name for the feature called **Honeypot** in the current commands. It combines a configured do-not-message channel with optional spam detection, recovery messaging, message cleanup, moderation action, and staff logging.

<div class="notice danger">
  Automatic NovaTrap enforcement is currently limited to selected servers. Do not enable it for a standard server installation; use dry-run tools and contact support if you need access.
</div>

## Purpose

NovaTrap is intended to identify a likely compromised account that posts in a clearly marked warning channel or repeats high-confidence spam across public channels. The intended response is to remove harmful messages, warn the account owner through a recovery DM, apply the configured moderation action, and notify server staff.

It is not a general anti-raid, mention-spam, invite-filter, or account-risk system.

## What members should avoid

- Do not post, reply, or attach files in the configured NovaTrap channel.
- Do not test the panel with a real account.
- Do not repeat suspicious promotional or account-compromise content across channels.
- If you believe an action was incorrect, contact server staff or the [NovaPulse support server]({{ site.links.support }}).

Any normal member message posted directly in the configured trap channel can trigger, including an attachment-only message.

## Confirmed exemptions

NovaTrap skips bots and protects the server owner, NovaPulse team members, configured exempt users and roles, administrators, and members with common moderation permissions by default.

## Possible moderation actions

- **Timeout** for the configured duration, capped by Discord's maximum.
- **Softban**, implemented as a ban followed by an unban, with a kick fallback if the ban path is unavailable.
- **Message deletion** when NovaPulse has Manage Messages in each source channel.
- **Recovery DM** before removal, using a configured rejoin destination or support fallback.


## Administrator configuration

Review settings with <code>/honeypot stats</code>. Use dry-run tools while evaluating the feature:

```text
/honeypot scan-spam messages:100 max-age-days:7 dryrun:true
/honeypot cleanup-users users:@TestMember dryrun:true
```

The available configuration includes the trap channel, staff log destination, recovery invite, timeout or softban action, timeout duration, cross-channel behavior, exclusions, statistics, and warning-message synchronization. Do not paste webhook credentials into a public channel or support ticket.

## Role and channel requirements

NovaPulse needs View Channel, Send Messages, Embed Links, and Manage Messages in the trap channel for setup. Live actions may additionally require Moderate Members, Kick Members, or Ban Members. The bot role must be above every target it may time out, kick, or ban.

If message deletion is unavailable, do not assume that removing a member also removes the spam. Review the affected channels and messages directly.

## Logging

A configured customer-server log may include the affected user and channel identifiers, triggering message details, attachment links, matched indicators, deletion outcomes, recovery-DM outcome, moderation action, and counters. Those records remain under the server's access and retention controls.

Keep your server's own moderation notes and appeal process available for any action taken through NovaTrap.

## Safe testing

1. Keep live enforcement disabled.
2. Use a private test server or dedicated test channels.
3. Use a non-staff test account and synthetic, non-harmful text.
4. Run <code>scan-spam</code> or <code>cleanup-users</code> with <code>dryrun:true</code> only.
5. Confirm excluded channels, staff roles, and logging access.
6. Review the predicted targets manually.
7. Do not enable live action unless NovaPulse confirms that it is available for your server.

## Appeals and recovery

The current bot has no built-in appeal form. Affected members should contact their server's moderators first. Server staff can escalate a suspected false positive through the [Afterparty Bot Labs support server]({{ site.links.support }}). Do not send identity documents, account passwords, tokens, or private server exports.
