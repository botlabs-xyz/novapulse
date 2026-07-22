---
layout: default
title: Command reference
description: Browse NovaPulse commands for server setup, roles, verification, and everyday administration.
permalink: /commands/
section: commands
---

NovaPulse uses slash commands for server configuration, roles, onboarding, verification, and day-to-day administration. Internal diagnostic and maintenance commands are available only to NovaPulse developers and are intentionally not documented here.

## Administrator commands

<div class="table-wrap" markdown="1">

| Command | Category | Required Discord permission |
| --- | --- | --- |
| <code>/set</code> | Configuration | Administrator |
| <code>/view-config</code> | Configuration | Administrator |
| <code>/clear-config</code> | Configuration | Manage Server or Administrator |
| <code>/set-auto-roles</code> | Configuration | Manage Roles |
| <code>/set-gender-roles</code> | Configuration | Administrator |
| <code>/set-intro-channel</code> | Verification | Administrator |
| <code>/set-non-verified-role</code> | Configuration | Administrator |
| <code>/set-pronoun-roles</code> | Configuration | Administrator |
| <code>/set-verified-role</code> | Configuration | Administrator |
| <code>/set-verify-log-channel</code> | Configuration | Manage Server or Administrator |
| <code>/list-auto-roles</code> | Utility | Manage Roles |
| <code>/assign-no-roles</code> | Utility | Manage Roles |

</div>

<div class="notice info">
  Required permissions may vary by enabled feature. Run administration commands in a staff-only channel, review selected roles and channels before saving, and keep the NovaPulse role above every role it must manage.
</div>

## Everyday help

<div class="table-wrap" markdown="1">

| Command | What it does |
| --- | --- |
| <code>/help</code> | Opens an interactive menu with command categories and useful links. |

</div>

## Advanced features

NovaTrap, anti-nuke response, bulk moderation, automated age actions, and third-party identity verification are currently limited to authorized deployments. They are not part of the standard server setup flow. If your server has access to one of these features, follow the related feature guidance and contact support before enabling it.

## Choose a category

<div class="doc-grid">
  <article class="doc-card"><h3>Configuration</h3><p>Roles, logging destinations, configuration review, and reset tools.</p><p><a href="{{ '/commands/configuration/' | relative_url }}">View configuration commands</a></p></article>
  <article class="doc-card"><h3>Verification</h3><p>Introductions, roles, and feature-specific verification settings.</p><p><a href="{{ '/commands/verification/' | relative_url }}">View verification commands</a></p></article>
  <article class="doc-card"><h3>Utility</h3><p>Help and role-management utilities.</p><p><a href="{{ '/commands/utility/' | relative_url }}">View utility commands</a></p></article>
  <article class="doc-card"><h3>Advanced features</h3><p>Learn about NovaTrap, moderation, and server-security boundaries.</p><p><a href="{{ '/features/' | relative_url }}">Explore features</a></p></article>
</div>

## Response visibility

Several configuration and security responses are ephemeral, meaning only the invoking user sees them. Some role-management commands post visible results in the channel. Review each command’s documented visibility before using it.
