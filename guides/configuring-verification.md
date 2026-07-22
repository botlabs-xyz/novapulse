---
layout: default
title: Configure verification
description: Set up test roles and an introduction channel while keeping age and identity features controlled.
permalink: /guides/configuring-verification/
section: guides
section_title: Guides
section_url: /guides/
status: Controlled workflow
status_style: warning
---

## 1. Create safe test roles

Create <code>@Verified-Test</code> and <code>@Pending-Test</code>. Give them no staff or administrative permissions, and place them below NovaPulse.

## 2. Save the roles

```text
/set-verified-role role:@Verified-Test
/set-non-verified-role role1:@Pending-Test
```

## 3. Optional introduction role validation

Configure only the role lists your server actually uses. Then choose the validation requirement when setting the introduction channel.

```text
/set-pronoun-roles role1:@She-Her role2:@He-Him role3:@They-Them
/set-intro-channel channel:#introductions-test require:Pronoun role only
```

## 4. Keep automated age action off

```text
/set-underage-ban-policy policy:Off
```

Public use is deferred until human review, typo handling, appeal, and reversal safeguards exist.

## 5. Test the introduction

Use a non-staff test account. Confirm the panel opens, the form submits, selected roles are recognized, the verified role can be assigned, and the pending role can be removed.

## 6. Treat ID verification separately

Do not enable <code>/idverify</code> as part of the basic introduction test. It requires a configured third-party service, a private staff procedure, a verification log, a reviewed privacy notice, retention and deletion rules, and an appeal/manual-correction path.

## 7. Do not use the incomplete free-verification panel

The current <code>/setup-verify</code> button does not have a confirmed handler in the validated source state. Wait for remediation and testing.
