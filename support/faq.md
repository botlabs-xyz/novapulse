---
layout: default
title: Frequently asked questions
description: Answers about NovaPulse availability, permissions, verification, logging, privacy, and support.
permalink: /support/faq/
section: support
---

## Is NovaPulse available for every server?

NovaPulse is being prepared for broader availability. Standard setup, configuration, and documentation are available, while some advanced security and bulk-administration features remain limited.

## Does NovaPulse require Administrator?

No. Basic operation uses View Channels, Send Messages, Embed Links, and Read Message History. Add feature-specific permissions only when needed.

## Why can NovaPulse not assign a role?

The bot needs Manage Roles and its highest role must be above the target role. Managed integration roles cannot be assigned by another bot.

## Why is a command missing?

NovaPulse may not have finished installing, your account may not have the command's required permission, the server may override command access, or Discord may still be updating the command list. Reopen the official invite link if the installation was interrupted.

## Does NovaPulse store identity documents?

NovaPulse does not ask members to upload documents into Discord. Where enabled for a server, the optional ID workflow creates a Stripe Identity session and can associate a Discord user ID with that session. Server administrators should limit staff access and clearly explain their server's handling of verification information.

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
