---
layout: default
title: Configuration commands
description: Configure server-owned roles and log destinations, review redacted settings, and reset selected modules.
permalink: /commands/configuration/
section: commands
section_title: Commands
section_url: /commands/
---

Configuration commands change settings for the current Discord server. Run them in a staff-only channel and verify every selected role or channel before saving.

<article class="command-card" id="set">
  <h2><code>/set</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral</span><span>Runtime check: Administrator</span></div>
  <p>Sets channel and optional webhook destinations for invite, ban, introduction, role, kick, and bulk-unban logs.</p>
  <pre><code>/set invite-log channel:#member-log
/set role-log channel:#role-log</code></pre>
  <div class="command-details"><p><strong>Options</strong>Subcommand plus optional <code>channel</code> and <code>webhook</code>.</p><p><strong>Expected result</strong>A private summary of the updated destination.</p><p><strong>Common errors</strong>Not in a server, missing Administrator, no destination supplied, invalid webhook URL.</p><p><strong>Related</strong><a href="#view-config"><code>/view-config</code></a>, <a href="#clear-config"><code>/clear-config</code></a></p></div>
</article>

<article class="command-card" id="view-config">
  <h2><code>/view-config</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral</span><span>Runtime check: Administrator</span></div>
  <p>Shows the current server's configuration with sensitive webhook values hidden and unavailable resources clearly identified.</p>
  <pre><code>/view-config</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>Expected result</strong>Private redacted configuration embeds.</p><p><strong>Common errors</strong>No configuration exists, unavailable channel or role, or insufficient access.</p><p><strong>Related</strong><a href="#set"><code>/set</code></a>, <a href="#clear-config"><code>/clear-config</code></a></p></div>
</article>

<article class="command-card" id="clear-config">
  <h2><code>/clear-config</code></h2>
  <div class="command-meta"><span>Manage Server or Administrator at runtime</span><span>Ephemeral</span><span>Confirmation required</span></div>
  <p>Resets one selected configuration item, a category, or all saved server configuration.</p>
  <pre><code>/clear-config module:Intro Channel confirm:true</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>module</code> (required choice), <code>confirm</code> (must be true).</p><p><strong>Expected result</strong>A private list of cleared settings.</p><p><strong>Common errors</strong>Confirmation is false, permission is missing, module is unknown, or nothing is configured.</p><p><strong>Related</strong><a href="#view-config"><code>/view-config</code></a></p></div>
  <p class="notice warning">The current Discord command metadata combines Manage Server and Administrator more strictly than the runtime check intends. Administrators normally satisfy the combined bitfield; non-administrator managers may not see the command until metadata remediation is complete.</p>
</article>

<article class="command-card" id="set-auto-roles">
  <h2><code>/set-auto-roles</code></h2>
  <div class="command-meta"><span>Manage Roles</span><span>Channel-visible result</span><span>Controlled administration</span></div>
  <p>Stores up to two roles to add when a member joins.</p>
  <pre><code>/set-auto-roles role1:@Member role2:@Announcements</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role1</code> required; <code>role2</code> optional.</p><p><strong>Expected result</strong>A list of saved auto roles.</p><p><strong>Common errors</strong>No role selected, role deleted, role is managed, or bot role is too low.</p><p><strong>Related</strong><a href="{{ '/commands/utility/' | relative_url }}#list-auto-roles"><code>/list-auto-roles</code></a></p></div>
</article>

<article class="command-card" id="set-gender-roles">
  <h2><code>/set-gender-roles</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Channel-visible result</span><span>Introduction workflow</span></div>
  <p>Stores up to six roles accepted by optional introduction validation.</p>
  <pre><code>/set-gender-roles role1:@Woman role2:@Man role3:@Nonbinary</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role1</code> required; <code>role2</code> through <code>role6</code> optional.</p><p><strong>Expected result</strong>A list of saved role names.</p><p><strong>Common errors</strong>No role selected, deleted role, or hierarchy prevents management.</p><p><strong>Related</strong><a href="{{ '/commands/verification/' | relative_url }}#set-intro-channel"><code>/set-intro-channel</code></a>, <a href="#set-pronoun-roles"><code>/set-pronoun-roles</code></a></p></div>
</article>

<article class="command-card" id="set-non-verified-role">
  <h2><code>/set-non-verified-role</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Channel-visible result</span><span>Role hierarchy required</span></div>
  <p>Stores up to two roles used for members who have not completed verification.</p>
  <pre><code>/set-non-verified-role role1:@Pending</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role1</code> required; <code>role2</code> optional.</p><p><strong>Expected result</strong>A list of saved non-verified roles.</p><p><strong>Common errors</strong>No role selected, role unavailable, or bot role is below the target.</p><p><strong>Related</strong><a href="#set-verified-role"><code>/set-verified-role</code></a>, <a href="{{ '/commands/utility/' | relative_url }}#assign-no-roles"><code>/assign-no-roles</code></a></p></div>
</article>

<article class="command-card" id="set-pronoun-roles">
  <h2><code>/set-pronoun-roles</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Channel-visible result</span><span>Introduction workflow</span></div>
  <p>Stores up to five roles accepted by optional introduction validation.</p>
  <pre><code>/set-pronoun-roles role1:@She-Her role2:@He-Him role3:@They-Them</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role1</code> required; <code>role2</code> through <code>role5</code> optional.</p><p><strong>Expected result</strong>A list of saved role names.</p><p><strong>Common errors</strong>No role selected, unavailable role, or hierarchy issue.</p><p><strong>Related</strong><a href="{{ '/commands/verification/' | relative_url }}#set-intro-channel"><code>/set-intro-channel</code></a></p></div>
</article>

<article class="command-card" id="set-verified-role">
  <h2><code>/set-verified-role</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Channel-visible result</span><span>Role hierarchy required</span></div>
  <p>Stores the role assigned after an approved verification or completed introduction flow.</p>
  <pre><code>/set-verified-role role:@Verified</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>role</code> required; the current schema also exposes an unused optional <code>role2</code>.</p><p><strong>Expected result</strong>Confirmation mentioning the saved role.</p><p><strong>Common errors</strong>Role unavailable, managed role, or bot role too low.</p><p><strong>Related</strong><a href="{{ '/commands/verification/' | relative_url }}#idverify"><code>/idverify</code></a>, <a href="{{ '/commands/verification/' | relative_url }}#set-intro-channel"><code>/set-intro-channel</code></a></p></div>
</article>

<article class="command-card" id="set-verify-log-channel">
  <h2><code>/set-verify-log-channel</code></h2>
  <div class="command-meta"><span>Manage Server or Administrator at runtime</span><span>Ephemeral</span><span>Manage Webhooks required</span></div>
  <p>Selects the age-verification approval log channel and creates or reuses a server-owned <strong>NovaPulse Logs</strong> webhook.</p>
  <pre><code>/set-verify-log-channel channel:#verification-log</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>channel</code> (required text channel).</p><p><strong>Expected result</strong>Private confirmation of the channel and logging method.</p><p><strong>Common errors</strong>Invalid channel, missing Manage Webhooks, duplicate webhook issue, or inaccessible destination.</p><p><strong>Related</strong><a href="{{ '/commands/verification/' | relative_url }}#idverify"><code>/idverify</code></a>, <a href="#view-config"><code>/view-config</code></a></p></div>
  <p class="notice warning">This command's combined default permission metadata is stricter than its runtime OR check. The behavior remains under permission remediation.</p>
</article>
