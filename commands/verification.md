---
layout: default
title: Verification commands
description: Configure the NovaPulse introduction workflow and role-validation options.
permalink: /commands/verification/
section: commands
section_title: Commands
section_url: /commands/
---

Use the introduction workflow to welcome members and apply roles that your server has configured. Test the flow with dedicated roles and a non-staff account before announcing it to members.

<article class="command-card" id="set-intro-channel">
  <h2><code>/set-intro-channel</code></h2>
  <div class="command-meta"><span>Administrator</span><span>Ephemeral confirmation</span><span>Posts a public panel</span></div>
  <p>Selects the introduction channel, stores an optional role-validation requirement, and posts a button that opens the member introduction form.</p>
  <pre><code>/set-intro-channel channel:#introductions require:Either gender or pronoun role</code></pre>
  <div class="command-details"><p><strong>Options</strong><code>channel</code> required; <code>require</code> may be None, Gender role, Pronoun role, or Either.</p><p><strong>NovaPulse authorization</strong>Discord command access defaults to Administrator.</p><p><strong>Expected result</strong>A public introduction panel and private setup confirmation.</p><p><strong>Common errors</strong>Invalid text channel, bot cannot send, or configured validation roles are unavailable.</p><p><strong>Response visibility</strong>Setup result is ephemeral; the created panel is visible in the selected channel.</p><p><strong>Related</strong><a href="{{ '/commands/configuration/' | relative_url }}#set-gender-roles"><code>/set-gender-roles</code></a>, <a href="{{ '/commands/configuration/' | relative_url }}#set-pronoun-roles"><code>/set-pronoun-roles</code></a></p></div>
</article>

## Advanced verification features

Automated age actions, the free-verification panel, and third-party identity verification are not currently part of the standard NovaPulse workflow. They are available only where NovaPulse has authorized the deployment and the server has completed the required privacy and staff-review preparation.
