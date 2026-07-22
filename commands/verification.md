---
layout: default
title: Verification commands
description: Configure introductions, age policy, free verification, and staff-reviewed third-party ID verification.
permalink: /commands/verification/
section: commands
section_title: Commands
section_url: /commands/
status: Controlled workflows
status_style: warning
---

Verification features can assign roles or trigger moderation outcomes. Test them with dedicated test roles and obtain the required server policy and privacy review before using age or identity workflows.

<article class="command-card" id="set-intro-channel">
  <h2><code>/set-intro-channel</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral confirmation</span><span>Posts a public panel</span></div>
  <p>Selects the introduction channel, stores an optional role-validation requirement, and posts a button that opens the member introduction form.</p>
  <pre><code>/set-intro-channel channel:#introductions require:Either gender or pronoun role</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>channel</code> required; <code>require</code> may be None, Gender role, Pronoun role, or Either.</p><p><strong>NovaPulse authorization</strong>Discord command access defaults to Administrator.</p><p><strong>Expected result</strong>A public introduction panel and private setup confirmation.</p><p><strong>Common errors</strong>Invalid text channel, bot cannot send, or configured validation roles are unavailable.</p><p><strong>Response visibility</strong>Setup result is ephemeral; the created panel is visible in the selected channel.</p><p><strong>Related</strong><a href="{{ '/commands/configuration/' | relative_url }}#set-gender-roles"><code>/set-gender-roles</code></a>, <a href="{{ '/commands/configuration/' | relative_url }}#set-pronoun-roles"><code>/set-pronoun-roles</code></a></p></div>
</article>

<article class="command-card" id="set-underage-ban-policy">
  <h2><code>/set-underage-ban-policy</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral</span><span>Automated action deferred</span></div>
  <p>Chooses how a self-entered age in the introduction workflow is evaluated: Off, Discord ToS only, server policy, or both.</p>
  <pre><code>/set-underage-ban-policy policy:Off</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>policy</code> required.</p><p><strong>NovaPulse authorization</strong>Discord command access defaults to Administrator.</p><p><strong>Expected result</strong>Private confirmation of the selected policy.</p><p><strong>Common errors</strong>Invalid policy or configuration write failure.</p><p><strong>Response visibility</strong>Ephemeral.</p><p><strong>Related</strong><a href="#set-intro-channel"><code>/set-intro-channel</code></a>, <a href="{{ '/features/verification/' | relative_url }}">Verification feature</a></p></div>
  <p class="notice danger">Automatic bans based on a single self-entered age are not approved for public rollout. Keep this policy off until typo protection, human review, appeal, and policy-owner approval are complete.</p>
</article>

<article class="command-card" id="setup-verify">
  <h2><code>/setup-verify</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Public panel</span><span>Currently incomplete</span></div>
  <p>Posts a free-verification prompt with a button intended to begin verification.</p>
  <pre><code>/setup-verify</code></pre>
  <div class="command-details"><p><strong>Options</strong>None.</p><p><strong>NovaPulse authorization</strong>Administrator is checked at runtime.</p><p><strong>Expected result</strong>A public verification panel.</p><p><strong>Common errors</strong>Missing Administrator or inability to post in the channel.</p><p><strong>Response visibility</strong>The created panel is public.</p><p><strong>Related</strong><a href="#idverify"><code>/idverify</code></a></p></div>
  <p class="notice warning">The current panel button has no confirmed interaction handler. Do not publish this panel to members until the workflow is repaired and tested.</p>
</article>

<article class="command-card" id="idverify">
  <h2><code>/idverify</code></h2>
  <div class="command-meta"><span>Manage Roles or Administrator at runtime</span><span>Public prompt</span><span>Stripe Identity</span></div>
  <p>Creates an optional Stripe Identity session for the selected Discord member, posts a link prompt, and includes a separate staff approval action.</p>
  <pre><code>/idverify user:@Member</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>user</code> optional, but staff should provide the ticket member.</p><p><strong>NovaPulse authorization</strong>Manage Roles or Administrator is checked at runtime; command metadata is currently stricter.</p><p><strong>Expected result</strong>A public verification prompt and an ephemeral staff confirmation. Approval assigns the configured verified role after staff review.</p><p><strong>Common errors</strong>No user, no verified role, third-party service unavailable, session creation failure, or hierarchy prevents role assignment.</p><p><strong>Response visibility</strong>Prompt is public; staff status and errors are ephemeral.</p><p><strong>Related</strong><a href="{{ '/commands/configuration/' | relative_url }}#set-verified-role"><code>/set-verified-role</code></a>, <a href="{{ '/commands/configuration/' | relative_url }}#set-verify-log-channel"><code>/set-verify-log-channel</code></a></p></div>
  <p class="notice warning">NovaPulse does not ask users to upload identity documents into Discord. Stripe handles the verification session. Staff access, retention, deletion, review criteria, and appeal procedures require owner/legal approval before public use.</p>
</article>
