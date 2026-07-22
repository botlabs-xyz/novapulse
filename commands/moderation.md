---
layout: default
title: Moderation commands
description: Review the current bulk kick and unban commands, required Discord permissions, and controlled-release restrictions.
permalink: /commands/moderation/
section: commands
section_title: Commands
section_url: /commands/
status: Public rollout deferred
status_style: danger
---

The current moderation commands act on groups of members or the complete ban list. They do not yet provide the confirmation and target-preview safeguards required for unrestricted public use.

<div class="notice danger">
  Do not run these commands in a production community unless the deployment owner has approved a controlled procedure, a recent backup or recovery plan exists, and the operator has reviewed the exact target set.
</div>

<article class="command-card" id="kick">
  <h2><code>/kick</code></h2>
  <div class="command-meta"><span>Kick Members</span><span>Channel-visible result</span><span>Bulk destructive action</span></div>
  <p>Kicks non-bot members who have any of up to five selected roles. The bot checks its own Kick Members permission and skips members above its role.</p>
  <pre><code>/kick role1:@Compromised role2:@Quarantine</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role1</code> required; <code>role2</code> through <code>role5</code> optional.</p><p><strong>NovaPulse authorization</strong>Access is currently governed by Discord command permissions; restrict the command to trusted staff.</p><p><strong>Expected result</strong>A visible summary of successfully kicked, skipped, and failed targets.</p><p><strong>Common errors</strong>Bot lacks Kick Members, no matching members, target outranks the bot, or a Discord action fails.</p><p><strong>Response visibility</strong>Visible in the channel.</p><p><strong>Related</strong><a href="{{ '/features/moderation/' | relative_url }}">Moderation safety</a>, <a href="{{ '/getting-started/permissions/' | relative_url }}">Role hierarchy</a></p></div>
</article>

<article class="command-card" id="unban-all">
  <h2><code>/unban-all</code></h2>
  <div class="command-meta"><span>Ban Members</span><span>Channel-visible result</span><span>Bulk destructive action</span></div>
  <p>Fetches the server's ban list and attempts to unban every banned user.</p>
  <pre><code>/unban-all</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>NovaPulse authorization</strong>Access is currently governed by Discord command permissions; restrict the command to senior trusted staff.</p><p><strong>Expected result</strong>A visible summary of successful and failed unbans.</p><p><strong>Common errors</strong>Bot lacks Ban Members, no users are banned, fetch fails, or individual unban actions fail.</p><p><strong>Response visibility</strong>Visible in the channel.</p><p><strong>Related</strong><a href="{{ '/features/moderation/' | relative_url }}">Moderation safety</a></p></div>
</article>

## Why these commands are deferred

The current validated source does not require an explicit confirmation step or show a dry-run target preview before either bulk action. <code>/kick</code> also needs an invoker hierarchy preflight and a safe target cap. These are release requirements, not optional polish.
