---
layout: default
title: Moderation commands
description: Learn why NovaPulse bulk moderation commands are limited to authorized deployments.
permalink: /commands/moderation/
section: commands
section_title: Commands
section_url: /commands/
status: Not currently available for standard deployments
status_style: danger
---

Bulk moderation commands are currently limited to authorized deployments and are not part of standard NovaPulse setup.

<div class="notice danger">
  Do not use these commands in a production community unless NovaPulse has explicitly authorized the deployment and your staff have reviewed the target set and recovery plan.
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

## Availability

These tools need additional confirmation, preview, and hierarchy safeguards before they can be offered as standard features. Contact support if your authorized deployment needs help with them.
