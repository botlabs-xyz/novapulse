---
layout: default
title: Verification settings
description: Configure introduction roles and optional verification logging without exposing private documents or credentials.
permalink: /configuration/verification-settings/
section: configuration
section_title: Configuration
section_url: /configuration/
status: Policy review required
status_style: warning
---

## Core roles

```text
/set-verified-role role:@Verified
/set-non-verified-role role1:@Pending
```

The verified role is added after an approved flow. Configured non-verified roles may be removed. Both must be below NovaPulse.

## Introduction roles

If the introduction form should validate a configured role, save the allowed gender and/or pronoun roles first. Then choose the requirement when setting the introduction channel.

```text
/set-gender-roles role1:@Woman role2:@Man role3:@Nonbinary
/set-pronoun-roles role1:@She-Her role2:@He-Him role3:@They-Them
/set-intro-channel channel:#introductions require:Either gender or pronoun role
```

Make optional identity fields genuinely optional where possible. Explain why the server requests information and who can view related logs.

## ID verification

Configure the verified role and a staff-only approval log before testing <code>/idverify</code>. Members must never upload identity documents directly into Discord. The third-party provider, staff dashboard access, review criteria, retention, deletion, and appeal procedure require owner/legal approval.

## Age policy

Keep automatic underage action off for public or unreviewed deployments. A self-entered number can be mistyped, and the current workflow does not provide a complete review and appeal path.
