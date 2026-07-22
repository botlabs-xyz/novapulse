---
layout: default
title: Security commands
description: Configure anti-nuke monitoring and NovaTrap only within an approved controlled deployment.
permalink: /commands/security/
section: commands
section_title: Commands
section_url: /commands/
status: Automatic enforcement deferred
status_style: danger
---

Security automation can remove members, strip roles, delete messages, or lock down an account. The current release audit requires additional opt-in, authorization, false-positive, logging, retention, and appeal controls before public use.

<article class="command-card" id="antinuke">
  <h2><code>/antinuke</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral</span><span>Controlled feature</span></div>
  <p>Views or configures destructive-action thresholds, optional emergency lockdown, alert destinations, and user or role exemptions.</p>
  <pre><code>/antinuke status
/antinuke configure enabled:false
/antinuke alerts channel:#security-log
/antinuke allow-role role:@Security Team</code></pre>
  <div class="command-details"><p><strong>Subcommands</strong><code>status</code>, <code>configure</code>, <code>alerts</code>, <code>allow-user</code>, <code>remove-user</code>, <code>allow-role</code>, <code>remove-role</code>.</p><p><strong>NovaPulse authorization</strong>Discord command access defaults to Administrator; public runtime hardening remains pending.</p><p><strong>Expected result</strong>Private status or update confirmation.</p><p><strong>Common errors</strong>Invalid alert destination, missing audit-log access, bot cannot manage the suspected member, or threshold action fails.</p><p><strong>Response visibility</strong>Ephemeral.</p><p><strong>Related</strong><a href="{{ '/features/server-security/' | relative_url }}">Server security</a></p></div>
  <p class="notice danger">Keep emergency lockdown disabled outside an approved controlled test. The current design still needs administrator/moderator false-positive protections and complete permission preflights.</p>
</article>

<article class="command-card" id="honeypot">
  <h2><code>/honeypot</code></h2>
  <div class="command-meta"><span>Manage Server or Administrator at runtime</span><span>Ephemeral</span><span>NovaTrap</span></div>
  <p>Configures the NovaTrap warning channel, log destination, recovery invite, enforcement mode, exclusions, statistics, dry-run cleanup, and historical spam scans.</p>
  <pre><code>/honeypot stats
/honeypot scan-spam messages:100 max-age-days:7 dryrun:true
/honeypot cleanup-users users:@Member dryrun:true</code></pre>
  <div class="command-details"><p><strong>Subcommands</strong><code>setup</code>, <code>enable</code>, <code>disable</code>, <code>stats</code>, <code>sync</code>, <code>resetstats</code>, <code>setchannel</code>, <code>setlogchannel</code>, <code>setinvite</code>, <code>setaction</code>, <code>settimeout</code>, <code>togglemultichannel</code>, threshold/exclusion controls, <code>cleanup-users</code>, and <code>scan-spam</code>.</p><p><strong>NovaPulse authorization</strong>Manage Server or Administrator at runtime; <code>scan-spam</code> additionally requires Administrator.</p><p><strong>Expected result</strong>Private configuration, status, or dry-run summary. Setup may create or update a public warning panel.</p><p><strong>Common errors</strong>No valid channel, missing channel permissions, invalid URL, no valid users, or action permissions unavailable.</p><p><strong>Response visibility</strong>Administrative replies are ephemeral; the warning panel is public.</p><p><strong>Related</strong><a href="{{ '/features/novatrap/' | relative_url }}">NovaTrap safety guide</a>, <a href="{{ '/configuration/security-settings/' | relative_url }}">Security settings</a></p></div>
  <p class="notice danger">Do not enable live enforcement for public servers. Dry-run scanning is the only recommended testing mode until the master disable behavior, repeat-content false positives, message-history deletion, recovery destination validation, durable cases, retention, and appeal process are remediated.</p>
</article>

## Developer commands

NovaPulse also contains internal commands for diagnostics and process maintenance. They are intentionally omitted from the public reference and are not supported for server administrators.
