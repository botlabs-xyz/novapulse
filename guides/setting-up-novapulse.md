---
layout: default
title: Set up NovaPulse safely
description: Complete an end-to-end least-privilege NovaPulse setup and verify the result.
permalink: /guides/setting-up-novapulse/
section: guides
section_title: Guides
section_url: /guides/
---

## Step 1: Install

Use the [official invite link]({{ site.links.invite }}) with Guild Install. The required scopes are <code>bot</code> and <code>applications.commands</code>. Do not grant Administrator as a shortcut.

## Step 2: Position NovaPulse

Move the NovaPulse role above every verified, pending, automatic, or workflow role it needs to manage. Keep senior staff above it.

## Step 3: Grant basic access

Give NovaPulse View Channels, Send Messages, Embed Links, and Read Message History in its command and log channels. Add Manage Roles only if you will test role automation.

## Step 4: Configure one role flow

```text
/set-verified-role role:@Verified-Test
/set-non-verified-role role1:@Pending-Test
```

Use disposable roles that grant no extra server permissions.

## Step 5: Configure one log

```text
/set role-log channel:#novapulse-test-log
```

Confirm only authorized staff can view the log channel.

## Step 6: Review configuration

```text
/view-config
```

Check that every displayed channel and role is correct. Sensitive webhook values should appear only as configured or not configured.

## Step 7: Run a safe test

Use a test member to add and remove the disposable role. Confirm the action and log outcome. Do not enable NovaTrap, anti-nuke lockdown, bulk moderation, age-policy bans, or ID verification as part of a basic setup test.

## Step 8: Record the setup

Document the enabled features, required permissions, staff roles with command access, log retention owner, and rollback steps. Review the record after any role or channel change.
