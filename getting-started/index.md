---
layout: default
title: Getting started
description: Install NovaPulse with least privilege, place its role correctly, and verify a safe initial configuration.
permalink: /getting-started/
section: getting-started
status: Controlled deployment
status_style: warning
---

NovaPulse is currently used in controlled environments while public-release hardening continues. Server owners can review this documentation and prepare a configuration, but should not treat every feature as ready for unrestricted production use.

<div class="doc-grid">
  <article class="doc-card"><h3>1. Invite</h3><p>Use a Guild Install with the <code>bot</code> and <code>applications.commands</code> scopes.</p><p><a href="{{ '/getting-started/inviting-novapulse/' | relative_url }}">Review the install guide</a></p></article>
  <article class="doc-card"><h3>2. Position the role</h3><p>Place NovaPulse above roles it needs to assign and members it may moderate.</p><p><a href="{{ '/getting-started/permissions/' | relative_url }}">Review permissions</a></p></article>
  <article class="doc-card"><h3>3. Configure basics</h3><p>Select server-owned roles and channels, then review the result with <code>/view-config</code>.</p><p><a href="{{ '/getting-started/initial-setup/' | relative_url }}">Follow initial setup</a></p></article>
  <article class="doc-card"><h3>4. Test safely</h3><p>Use a private test channel and non-privileged test account. Keep automated enforcement disabled unless your deployment is approved for it.</p><p><a href="{{ '/guides/setting-up-novapulse/' | relative_url }}">Open the setup checklist</a></p></article>
</div>

## Before you begin

- You must be able to manage the Discord server and its roles.
- Decide which NovaPulse features your server actually needs.
- Create staff-only log channels before configuring logging.
- Identify a test member and test roles that cannot affect real staff or members.
- Confirm that NovaPulse's role can access the channel where you run commands.

<div class="notice warning">
  <strong>Release status:</strong> NovaTrap automatic enforcement, anti-nuke lockdown, bulk kick, bulk unban, automated age-policy actions, and third-party ID verification require additional review before a public rollout. Use only in an approved controlled deployment.
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
