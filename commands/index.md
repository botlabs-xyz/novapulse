---
layout: default
title: Command reference
description: Browse the 20 non-developer slash commands confirmed in the current NovaPulse source state.
permalink: /commands/
section: commands
status: Current private build
status_style: info
---

This reference is generated from the current command modules. It excludes five developer commands from public documentation. Internal diagnostics, code execution, runtime logs, and process controls are restricted to NovaPulse developers.

<div class="notice warning">
  A command appearing here does not mean it is approved for unrestricted public use. Commands with destructive or automated outcomes are marked controlled until runtime authorization, confirmation, target limits, false-positive testing, or appeal safeguards are complete.
</div>

## Command inventory

<div class="table-wrap" markdown="1">

| Command | Category | Who can see/use it by default | Release status |
| --- | --- | --- | --- |
| <code>/help</code> | Utility | Everyone | Available in current build |
| <code>/set</code> | Configuration | Administrator | Controlled administration |
| <code>/view-config</code> | Configuration | Administrator | Controlled administration |
| <code>/clear-config</code> | Configuration | Manage Server + Administrator metadata | Permission metadata review pending |
| <code>/set-auto-roles</code> | Configuration | Manage Roles | Controlled administration |
| <code>/set-gender-roles</code> | Configuration | Administrator | Controlled administration |
| <code>/set-intro-channel</code> | Verification | Administrator | Controlled administration |
| <code>/set-non-verified-role</code> | Configuration | Administrator | Controlled administration |
| <code>/set-pronoun-roles</code> | Configuration | Administrator | Controlled administration |
| <code>/set-underage-ban-policy</code> | Verification | Administrator | Public rollout deferred |
| <code>/set-verified-role</code> | Configuration | Administrator | Controlled administration |
| <code>/set-verify-log-channel</code> | Configuration | Manage Server + Administrator metadata | Permission metadata review pending |
| <code>/setup-verify</code> | Verification | Administrator | Incomplete interaction; do not publish panel |
| <code>/idverify</code> | Verification | Manage Roles + Administrator metadata | Controlled; third-party review required |
| <code>/assign-no-roles</code> | Utility | Manage Roles | Bulk action; controlled |
| <code>/list-auto-roles</code> | Utility | Manage Roles | Available in current build |
| <code>/kick</code> | Moderation | Kick Members | Bulk action; public rollout deferred |
| <code>/unban-all</code> | Moderation | Ban Members | Bulk action; public rollout deferred |
| <code>/antinuke</code> | Security | Administrator | Controlled; false-positive review pending |
| <code>/honeypot</code> | Security | Manage Server + Administrator metadata | Controlled; automatic enforcement deferred |

</div>

## Choose a category

<div class="doc-grid">
  <article class="doc-card"><h3>Configuration</h3><p>Roles, logging destinations, configuration review, and reset tools.</p><p><a href="{{ '/commands/configuration/' | relative_url }}">View 9 commands</a></p></article>
  <article class="doc-card"><h3>Verification</h3><p>Introductions, age policy, free verification, and staff-reviewed ID verification.</p><p><a href="{{ '/commands/verification/' | relative_url }}">View 4 commands</a></p></article>
  <article class="doc-card"><h3>Utility</h3><p>Help and role-management utilities.</p><p><a href="{{ '/commands/utility/' | relative_url }}">View 3 commands</a></p></article>
  <article class="doc-card"><h3>Moderation</h3><p>Bulk kick and bulk unban tools with controlled-release warnings.</p><p><a href="{{ '/commands/moderation/' | relative_url }}">View 2 commands</a></p></article>
  <article class="doc-card"><h3>Security</h3><p>Anti-nuke and NovaTrap configuration.</p><p><a href="{{ '/commands/security/' | relative_url }}">View 2 commands</a></p></article>
</div>

## Response visibility

Several configuration and security responses are ephemeral, meaning only the invoking user sees them. Some role and moderation commands currently post visible results in the channel. Run sensitive administration commands in a staff-only channel and review the command's documented visibility before use.
