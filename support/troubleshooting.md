---
layout: default
title: Troubleshooting
description: Resolve common NovaPulse availability, slash command, permission, role, channel, verification, and NovaTrap issues.
permalink: /support/troubleshooting/
section: support
---

## NovaPulse is offline

Check whether Discord is experiencing an incident, then check the support server for a service notice. Do not repeatedly remove and re-add the bot. If only your server is affected, confirm NovaPulse still appears in the member list and has not been manually disabled.

## Slash commands are missing

- Confirm NovaPulse was installed with <code>applications.commands</code>.
- Test in a server text channel the bot can view.
- Check your permission for the specific command.
- Check server integration command overrides.
- Allow time for a recent global command update.

## Missing permissions or role hierarchy

Review both the server role and the target channel's overwrites. For roles and moderation, place NovaPulse above the role or member it must manage. Do not grant Administrator as a troubleshooting shortcut.

## Log channel no longer exists

Run <code>/view-config</code>. Clear the unavailable item with <code>/clear-config</code>, create or choose the intended replacement, then configure it again. A same-named channel has a new Discord ID and is not an automatic replacement.

## Verification setup does not work

Confirm the verified and pending roles exist below NovaPulse. Check the introduction channel, the bot's send/embed access, and any configured role-validation list. Do not use <code>/setup-verify</code> until its button handler is confirmed repaired.

## ID verification session fails

Confirm a target user, verified role, provider configuration, and staff authorization are present. Use the safe error reference ID when contacting support. Never post identity documents or provider credentials.

## NovaTrap configuration problems

Use <code>/honeypot stats</code> to review the selected channel and settings. Keep enforcement disabled. Setup needs View Channel, Send Messages, Embed Links, and Manage Messages in the trap channel; automatic channel creation also needs Manage Channels.

## Bot cannot ban, kick, timeout, or manage roles

Check the matching bot permission and hierarchy. The server owner and members with equal or higher roles cannot be moderated. A managed integration role cannot be assigned or removed.

## Bot cannot send embeds

Grant Embed Links and Send Messages in the destination channel. Confirm no category or channel overwrite denies them.

## Bot cannot access a channel

Grant View Channel in both the category and channel. Check whether a role-specific deny applies to NovaPulse.

## Configuration appears outdated

Run <code>/view-config</code>, clear deleted resources, and re-run the relevant setup command. If configuration still appears stale, record the affected item and contact support before attempting a full reset.

## Before asking for help

Include the command, time and timezone, safe error text or reference ID, server ID, channel ID, relevant role names, expected behavior, actual behavior, and steps already tried. Redact unrelated member data.
