---
layout: default
title: Frequently asked questions
description: Answers about NovaPulse availability, permissions, verification, logging, privacy, and support.
permalink: /support/faq/
section: support
---

## Is NovaPulse publicly ready?

No public-readiness claim is made by this documentation. NovaPulse remains a controlled deployment while security, permissions, onboarding, retention, false-positive testing, and legal review continue.

## Does NovaPulse require Administrator?

No. Basic operation uses View Channels, Send Messages, Embed Links, and Read Message History. Add feature-specific permissions only when needed.

## Why can NovaPulse not assign a role?

The bot needs Manage Roles and its highest role must be above the target role. Managed integration roles cannot be assigned by another bot.

## Why is a command missing?

The app may lack the <code>applications.commands</code> scope, your account may not have the command's required permission, the server may override command access, or global command registration may still be updating.

## Does NovaPulse store identity documents?

NovaPulse does not ask members to upload documents into Discord. The optional ID workflow creates a Stripe Identity session and can associate a Discord user ID with that session. Authorized staff access and provider retention require owner/legal review.

## Where do moderation logs go?

Customer-server logs go to channels or supported destinations selected by the server administrator. Internal NovaPulse operational monitoring is separate and should contain only minimal redacted service metadata.

## Can members click the NovaTrap counter to moderate someone?

No. The confirmed counter button reads configuration and returns an ephemeral stats response. It does not delete, timeout, kick, ban, or change roles.

## Can I safely test NovaTrap?

Only in a controlled test server or private test channel, with live enforcement disabled and <code>dryrun:true</code>. Do not use real member accounts.

## How do I request deletion or report a false positive?

Contact the server's administrators first, then use the [Afterparty Bot Labs support server]({{ site.links.support }}) if escalation is needed. Provide IDs and timestamps, not secrets or identity documents.

## What should I never send to support?

Never send a bot token, client secret, webhook URL or token, Stripe secret, password, session cookie, private database, full environment file, raw production log archive, or identity document.
