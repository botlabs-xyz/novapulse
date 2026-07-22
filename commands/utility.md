---
layout: default
title: Utility commands
description: Use the interactive help menu and review role-assignment utilities in the current NovaPulse build.
permalink: /commands/utility/
section: commands
section_title: Commands
section_url: /commands/
---

<article class="command-card" id="help">
  <h2><code>/help</code></h2>
  <div class="command-meta"><span>Everyone</span><span>Interactive menu</span><span>Original invoker only</span></div>
  <p>Shows a category selector and links to the website and support server.</p>
  <pre><code>/help</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>NovaPulse authorization</strong>No staff role required; menu interactions are limited to the original invoker.</p><p><strong>Expected result</strong>An interactive command-category menu.</p><p><strong>Common errors</strong>Menu expired after 15 minutes or another user tries to use it.</p><p><strong>Response visibility</strong>Initial menu is visible; denial messages are ephemeral.</p><p><strong>Related</strong><a href="{{ '/commands/' | relative_url }}">Complete command reference</a></p></div>
  <p class="notice warning">The current in-Discord menu needs alignment with the public command list and must not expose private developer commands before release.</p>
</article>

<article class="command-card" id="assign-no-roles">
  <h2><code>/assign-no-roles</code></h2>
  <div class="command-meta"><span>Manage Roles</span><span>Channel-visible result</span><span>Bulk role action</span></div>
  <p>Assigns the first configured non-verified role to human members who currently have no server roles.</p>
  <pre><code>/assign-no-roles</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>NovaPulse authorization</strong>Access is currently governed by Discord command permissions; restrict to trusted role managers.</p><p><strong>Expected result</strong>Counts of assigned and failed members.</p><p><strong>Common errors</strong>No non-verified role configured, role deleted, no eligible members, or role hierarchy failure.</p><p><strong>Response visibility</strong>Visible in the channel.</p><p><strong>Related</strong><a href="{{ '/commands/configuration/' | relative_url }}#set-non-verified-role"><code>/set-non-verified-role</code></a></p></div>
  <p class="notice warning">This bulk action currently has no dry-run preview or target cap. Use only in a controlled maintenance window.</p>
</article>

<article class="command-card" id="list-auto-roles">
  <h2><code>/list-auto-roles</code></h2>
  <div class="command-meta"><span>Manage Roles</span><span>Channel-visible result</span><span>Read-only</span></div>
  <p>Lists the server's configured automatic join roles.</p>
  <pre><code>/list-auto-roles</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>NovaPulse authorization</strong>Access is governed by Discord command permissions.</p><p><strong>Expected result</strong>Configured roles or a message that none are configured.</p><p><strong>Common errors</strong>Configured role was deleted or is unavailable.</p><p><strong>Response visibility</strong>Visible in the channel.</p><p><strong>Related</strong><a href="{{ '/commands/configuration/' | relative_url }}#set-auto-roles"><code>/set-auto-roles</code></a></p></div>
</article>
