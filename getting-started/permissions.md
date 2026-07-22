---
layout: default
title: Permissions and role hierarchy
description: Grant NovaPulse only the Discord permissions needed for the features your server enables.
permalink: /getting-started/permissions/
section: getting-started
section_title: Getting started
section_url: /getting-started/
---

NovaPulse does not require **Administrator**. A least-privilege setup begins with basic channel access and adds permissions only for selected features.

## Basic operation

<div class="table-wrap" markdown="1">

| Permission | Used for | If missing |
| --- | --- | --- |
| View Channels | Access configured channels and command surfaces | The bot cannot see or use the channel |
| Send Messages | Panels, logs, and normal messages | Sends and logs may fail |
| Embed Links | Help, setup panels, and logs | Rich responses fail |
| Read Message History | Reuse panels and perform approved scans | Fetch, edit, and history-dependent actions fail |

</div>

## Feature permissions

<div class="table-wrap" markdown="1">

| Permission | Feature |
| --- | --- |
| Manage Roles | Auto roles, verification roles, and role removal |
| Manage Server | Invite metadata and several configuration command gates |
| Manage Messages | Remove NovaTrap or spam messages |
| Moderate Members | Timeout actions |
| Kick Members | <code>/kick</code> and some fallback removals |
| Ban Members | Softban behavior and <code>/unban-all</code> |
| View Audit Log | Attribute destructive actions for anti-nuke monitoring |
| Manage Channels | Create a NovaTrap warning channel during setup |
| Manage Webhooks | Create or reuse a server-owned verification log webhook |

</div>

## Role hierarchy is separate from permissions

Even with **Manage Roles**, **Kick Members**, **Ban Members**, or **Moderate Members**, Discord blocks actions against equal or higher roles.

1. Open **Server Settings → Roles**.
2. Place NovaPulse above every role it must assign or remove.
3. Place NovaPulse above members it may moderate.
4. Keep staff and owner roles above NovaPulse unless a controlled security design explicitly requires otherwise.
5. Do not configure managed integration roles; bots cannot assign them.

## Channel overwrites

A server-level permission can still be denied in a specific channel. For each configured channel, confirm that NovaPulse can view the channel, send messages, and embed links. Approved message cleanup also needs **Manage Messages** in every affected channel.

## Permission troubleshooting

If an action partly succeeds or fails:

- Check both server permissions and the channel's permission overwrites.
- Compare the NovaPulse role to the target role or member.
- Confirm the target is not the server owner or a managed integration role.
- Re-run the command only after correcting access; do not grant Administrator as a shortcut.

See [Troubleshoot permissions]({{ '/guides/troubleshooting-permissions/' | relative_url }}) for a focused checklist.
