---
layout: default
title: NovaPulse
description: Advanced moderation, automation, verification, and server security for Discord communities.
permalink: /
home: true
---

<section class="home-hero">
  <div class="hero-copy">
    <p class="eyebrow">Afterparty Bot Labs · Discord server operations</p>
    <h1><span>NovaPulse</span></h1>
    <p class="hero-lead">Advanced moderation, automation, verification, and server security for Discord communities.</p>
    <div class="hero-actions">
      <a class="button primary" href="{{ site.links.invite }}" target="_blank" rel="noopener noreferrer">Invite NovaPulse</a>
      <a class="button" href="{{ '/getting-started/' | relative_url }}">Get started</a>
      <a class="button ghost" href="{{ site.links.support }}" target="_blank" rel="noopener noreferrer">Join support</a>
    </div>
    <p class="hero-note">NovaPulse is currently a controlled deployment. The documentation is public for review, but an invite link does not indicate that every feature is ready for unrestricted public use.</p>
  </div>
  <div class="hero-art">
    <img src="{{ '/assets/images/novapulse-logo.webp' | relative_url }}" alt="NovaPulse neon pulse logo" width="512" height="512">
  </div>
</section>

<section class="home-section" aria-labelledby="capabilities-heading">
  <p class="section-kicker">Confirmed capabilities</p>
  <h2 id="capabilities-heading">A focused control layer for safer Discord communities.</h2>
  <p class="section-intro">NovaPulse combines server configuration, member onboarding, staff-reviewed verification, logging, and security tooling. Availability varies while safety work continues.</p>
  <div class="feature-grid">
    <article class="feature-card">
      <span class="card-label">Controlled release</span>
      <h3>NovaTrap</h3>
      <p>A configurable warning-channel and spam-response system with staff exemptions, recovery messaging, dry-run scans, and server-owned logging. Automatic enforcement remains restricted pending false-positive and appeal safeguards.</p>
    </article>
    <article class="feature-card">
      <span class="card-label">Staff workflow</span>
      <h3>Verification</h3>
      <p>Introduction prompts, configurable verified and non-verified roles, and optional third-party identity sessions with a manual staff approval step.</p>
    </article>
    <article class="feature-card">
      <span class="card-label">Server-owned</span>
      <h3>Logging</h3>
      <p>Route moderation, invite, introduction, role, and verification events to channels selected by the server. Internal service monitoring is separate and uses minimal redacted metadata.</p>
    </article>
    <article class="feature-card">
      <span class="card-label">Administration</span>
      <h3>Automation &amp; security</h3>
      <p>Configure join roles, introduction validation, invite tracking, and destructive-action monitoring with clear permission and role-hierarchy requirements.</p>
    </article>
  </div>
</section>

<section class="home-section" aria-labelledby="quick-start-heading">
  <p class="section-kicker">Quick start</p>
  <h2 id="quick-start-heading">Start small, verify access, then enable only what you need.</h2>
  <div class="quick-grid">
    <article class="quick-card"><h3>Install the app</h3><p>Use the Guild Install flow with the <code>bot</code> and <code>applications.commands</code> scopes.</p></article>
    <article class="quick-card"><h3>Place the bot role</h3><p>Move NovaPulse above every role it must assign, remove, or moderate. Discord hierarchy always applies.</p></article>
    <article class="quick-card"><h3>Configure in stages</h3><p>Start with channels and roles, review <code>/view-config</code>, then test one workflow in a controlled channel.</p></article>
  </div>
</section>

<section class="home-section" aria-labelledby="explore-heading">
  <p class="section-kicker">Documentation</p>
  <h2 id="explore-heading">Find the right path for your server.</h2>
  <div class="link-grid">
    <a class="link-card" href="{{ '/getting-started/' | relative_url }}"><h3>Getting started</h3><p>Install scopes, initial setup, permissions, and hierarchy.</p><span>Open guide →</span></a>
    <a class="link-card" href="{{ '/commands/' | relative_url }}"><h3>Commands</h3><p>Browse syntax, options, access, results, and common errors.</p><span>View commands →</span></a>
    <a class="link-card" href="{{ '/features/' | relative_url }}"><h3>Features</h3><p>Understand verification, logging, automation, and security status.</p><span>Explore features →</span></a>
    <a class="link-card" href="{{ '/support/troubleshooting/' | relative_url }}"><h3>Troubleshooting</h3><p>Resolve missing commands, access, channel, and hierarchy issues.</p><span>Fix a problem →</span></a>
  </div>
</section>

<section class="home-section">
  <div class="home-callout">
    <div>
      <p class="section-kicker">Need a hand?</p>
      <h2>Bring the symptoms. Keep credentials private.</h2>
      <p class="section-intro">The support team can help with commands, permissions, role hierarchy, and configuration. Never share bot tokens, webhook tokens, secret keys, database files, or a complete environment file.</p>
    </div>
    <a class="button primary" href="{{ site.links.support }}" target="_blank" rel="noopener noreferrer">Join support server</a>
  </div>
</section>
