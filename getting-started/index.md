---
layout: default
title: Getting started
description: Install NovaPulse with least privilege, place its role correctly, and verify a safe initial configuration.
permalink: /getting-started/
section: getting-started
---

NovaPulse is designed to help server administrators configure moderation, logging, onboarding, and community-management workflows with clear permissions and role hierarchy.

<div class="doc-grid">
  <article class="doc-card"><h3>1. Invite</h3><p>Use a Guild Install with the <code>bot</code> and <code>applications.commands</code> scopes.</p><p><a href="{{ '/getting-started/inviting-novapulse/' | relative_url }}">Review the install guide</a></p></article>
  <article class="doc-card"><h3>2. Position the role</h3><p>Place NovaPulse above roles it needs to assign and members it may moderate.</p><p><a href="{{ '/getting-started/permissions/' | relative_url }}">Review permissions</a></p></article>
  <article class="doc-card"><h3>3. Configure basics</h3><p>Select server-owned roles and channels, then review the result with <code>/view-config</code>.</p><p><a href="{{ '/getting-started/initial-setup/' | relative_url }}">Follow initial setup</a></p></article>
  <article class="doc-card"><h3>4. Test safely</h3><p>Use a private test channel and non-privileged test account before enabling a new workflow.</p><p><a href="{{ '/guides/setting-up-novapulse/' | relative_url }}">Open the setup checklist</a></p></article>
</div>

## Before you begin

- You must be able to manage the Discord server and its roles.
- Decide which NovaPulse features your server actually needs.
- Create staff-only log channels before configuring logging.
- Identify a test member and test roles that cannot affect real staff or members.
- Confirm that NovaPulse's role can access the channel where you run commands.

<div class="notice warning">
  <strong>Availability:</strong> NovaPulse is currently being prepared for broader public availability. Some advanced security and bulk-administration features remain limited while final safety and reliability work is completed.
</div>

## A successful basic setup looks like this

1. NovaPulse appears online in your member list.
2. Slash commands appear after typing <code>/</code> in a channel the bot can access.
3. The bot role is below staff roles but above every role NovaPulse must manage.
4. <code>/view-config</code> returns only your server's redacted configuration summary.
5. A test logging action arrives in the intended staff-only channel.
6. No automatic moderation feature is enabled unintentionally.

## Next step

Open [Invite NovaPulse]({{ '/getting-started/inviting-novapulse/' | relative_url }}) for the current scopes and permission profiles.
