---
layout: default
title: Log channels
description: Select private server-owned channels for NovaPulse events and protect sensitive moderation records.
permalink: /configuration/log-channels/
section: configuration
section_title: Configuration
section_url: /configuration/
---

NovaPulse can route several event categories independently. Use separate destinations when different staff teams need different access.

<div class="table-wrap" markdown="1">

| Log category | Typical audience | Example command |
| --- | --- | --- |
| Invite and member joins | Community administrators | <code>/set invite-log channel:#member-log</code> |
| Introductions | Verification staff | <code>/set intro-log channel:#verification-log</code> |
| Role changes | Senior moderators | <code>/set role-log channel:#role-log</code> |
| Kicks and bans | Moderation leads | <code>/set kick-log channel:#mod-log</code> |
| Bulk unban | Server owners | <code>/set unban-all-log channel:#admin-audit</code> |
| ID verification approval | Approved verification staff | <code>/set-verify-log-channel channel:#id-review-log</code> |
| NovaTrap or anti-nuke | Security staff | Controlled deployment only |

</div>

## Channel permissions

Give NovaPulse View Channel, Send Messages, and Embed Links in the destination. Restrict members from viewing staff logs. If the channel contains moderation evidence or identity-workflow status, limit access to the smallest authorized staff group.

## Webhook safety

The current build accepts optional webhook destinations in several commands. Public-release review requires tighter Discord-host validation and outbound-request controls. Prefer selecting a channel in the command. Never share a webhook URL; it contains a credential.

## Test the destination

1. Configure one category.
2. Run <code>/view-config</code> and confirm the displayed channel.
3. Trigger a harmless test event.
4. Confirm the event appears once and contains only expected information.
5. Confirm unauthorized roles cannot view the log.
