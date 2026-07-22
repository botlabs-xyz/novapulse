---
layout: default
title: Verification
description: Understand NovaPulse introductions, role assignment, optional identity sessions, and staff responsibilities.
permalink: /features/verification/
section: features
section_title: Features
section_url: /features/
status: Controlled workflow
status_style: warning
---

NovaPulse contains two distinct verification paths: a Discord introduction workflow and an optional staff-reviewed third-party identity workflow.

## Introduction verification

Administrators select an introduction channel and may require a configured gender role, pronoun role, either, or neither. A member opens a modal from the posted panel. When the workflow succeeds, NovaPulse can assign the verified role and remove configured non-verified roles.

The form can process self-entered profile information and age. Configure only fields your community genuinely needs, tell members how the information is used, and restrict staff access to related logs.

## Age-policy automation

The current build can apply a configured age policy to self-entered information. Automatic bans based on a single text entry are deferred from public release because typo handling, review, appeal, and reversal safeguards are not complete.

Keep the policy set to **Off** unless the controlled deployment owner has approved a reviewed procedure.

## Third-party identity verification

<code>/idverify user:@Member</code> can create a Stripe Identity session and place the Discord user ID in the session metadata. The verification link opens outside Discord. NovaPulse stores a Discord ID and request timestamp for the active request; it does not ask members to upload documents in a Discord channel.

Staff approval is manual. The current approval button assigns the configured verified role; it does not independently prove that a Stripe session reached a particular state.

<div class="notice warning">
  Before use, the owner must approve staff access, review criteria, retention, deletion, incident handling, age-verification policy, and an appeal/manual-correction procedure. Depending on provider permissions, authorized staff may be able to access verification information in the provider dashboard.
</div>

## Required setup

- A verified role below the NovaPulse role.
- Optional non-verified roles below the NovaPulse role.
- A private staff log channel if verification approvals are logged.
- Manage Roles for NovaPulse and the reviewing staff workflow.
- A published privacy notice accepted by the server administrator.

## Related documentation

- [Configure verification]({{ '/guides/configuring-verification/' | relative_url }})
- [Verification commands]({{ '/commands/verification/' | relative_url }})
- [Privacy policy draft]({{ '/legal/privacy-policy/' | relative_url }})
