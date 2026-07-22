---
layout: default
title: Initial setup
description: Configure NovaPulse channels, roles, logs, and verification in a safe order.
permalink: /getting-started/initial-setup/
section: getting-started
section_title: Getting started
section_url: /getting-started/
---

Configure NovaPulse in stages. Finish and test each stage before enabling the next one.

## 1. Check access and hierarchy

- Give NovaPulse access to the command and log channels it will use.
- Place the NovaPulse role above configured verified, non-verified, auto, gender, and pronoun roles.
- Keep the bot below server owners and trusted staff roles.
- Grant moderation permissions only when an approved feature requires them.

## 2. Configure roles

Choose only roles NovaPulse can manage:

```text
/set-verified-role role:@Verified
/set-non-verified-role role1:@Pending
/set-auto-roles role1:@Member
```

Gender and pronoun role lists are optional and are used only when the introduction workflow requires them.

## 3. Configure introductions or verification

```text
/set-intro-channel channel:#introductions require:Either gender or pronoun role
```

The command posts an introduction button and stores the selected channel. Test the form with a non-staff account before announcing it.

Keep advanced verification features separate from this initial setup. Contact support if your server has been authorized to use an advanced verification workflow.

## 4. Configure server-owned logs

Create private staff channels with appropriate channel overwrites, then configure only the destinations you need:

```text
/set invite-log channel:#member-log
/set role-log channel:#role-log
/set intro-log channel:#verification-log
```

Prefer channels selected inside Discord. Do not paste webhook URLs into screenshots, tickets, or public documentation.

## 5. Review the result

Run <code>/view-config</code>. The response is private to the invoking administrator and hides sensitive webhook values. Deleted or inaccessible roles and channels are shown as unavailable.

## 6. Test one workflow

Use a disposable test role and test member. Confirm:

- The bot can send embeds.
- The selected log channel receives the expected event.
- Role additions and removals obey hierarchy.
- Failure messages do not reveal internal details.
- No automated enforcement feature is enabled outside the approved scope.

<div class="notice danger">
  Do not test NovaTrap, bulk kick, bulk unban, anti-nuke lockdown, or age-policy bans on real members. Those workflows remain controlled until their confirmation, false-positive, and appeal safeguards are complete.
</div>
