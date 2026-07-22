---
layout: default
title: Troubleshoot permissions
description: Diagnose missing commands, failed sends, role assignment, moderation actions, and channel access.
permalink: /guides/troubleshooting-permissions/
section: guides
section_title: Guides
section_url: /guides/
---

## Start with the exact failure

Identify whether the command is missing, the command starts but fails, a message cannot be sent, or a role/moderation action is rejected. Each points to a different permission layer.

## Command is missing

- Confirm the app was installed with <code>applications.commands</code>.
- Confirm you are testing in a server, not a direct message.
- Check the command's default member permission.
- Check **Server Settings → Integrations → NovaPulse** for command overrides.
- Wait briefly for global command registration if the application was recently updated.

## Bot cannot send or embed

Open the channel's permission settings and check NovaPulse for View Channel, Send Messages, Embed Links, and Read Message History. A channel deny can override a server-level allow.

## Bot cannot assign a role

1. Confirm NovaPulse has Manage Roles.
2. Move NovaPulse above the target role.
3. Confirm the role is not managed by an integration.
4. Confirm the target member is not above NovaPulse.
5. Re-select the role if the old configured role was deleted.

## Bot cannot kick, ban, or timeout

Confirm the matching permission, then compare the NovaPulse role to the target member's highest role. Discord never allows a bot to moderate the server owner or a member whose highest role is equal to or above the bot.

## Anti-nuke cannot attribute an action

The bot needs View Audit Log. Audit entries can be delayed; keep emergency lockdown disabled while diagnosing.

## Verification logging cannot create a webhook

NovaPulse needs Manage Webhooks in the selected channel. Remove stale duplicate bot-created webhooks if instructed by the command, then retry. Never share webhook URLs while troubleshooting.

## Still stuck?

Capture the command name, safe error text or reference ID, time, server ID, channel ID, and relevant role names. Then follow [Report a bug]({{ '/support/reporting-bugs/' | relative_url }}).
