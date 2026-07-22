---
layout: default
title: Configure logs
description: Create a private logging channel, point one NovaPulse category to it, and verify safe output.
permalink: /guides/configuring-logs/
section: guides
section_title: Guides
section_url: /guides/
---

## 1. Create a destination

Create a text channel such as <code>#novapulse-member-log</code>. Deny View Channel to <code>@everyone</code>, then grant access to the smallest appropriate staff role and NovaPulse.

## 2. Verify NovaPulse access

NovaPulse needs View Channel, Send Messages, and Embed Links. Verification webhook setup additionally needs Manage Webhooks in that channel.

## 3. Configure one category

```text
/set invite-log channel:#novapulse-member-log
```

Use the matching subcommand for ban, introduction, role, kick, or bulk-unban logs. Configure categories separately so staff access can remain narrow.

## 4. Review the saved destination

Run <code>/view-config</code>. The selected channel should appear by name. If it appears unavailable, check deletion, visibility, and permission overwrites.

## 5. Trigger a harmless test

Use a synthetic role change or approved test-member event. Confirm the log arrives once, contains expected fields, and does not expose a webhook URL, secret, raw configuration object, or unrelated member data.

## 6. Define retention

Choose who can view, export, and delete records; how long they are needed; and how a member can request review. NovaPulse does not currently enforce a universal retention period for customer-server channels.

<div class="notice warning">Never post a webhook URL in a screenshot or support ticket. If one is exposed, treat it as a credential and replace it.</div>
