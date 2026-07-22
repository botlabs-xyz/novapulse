---
layout: default
title: Report a bug
description: Submit a useful NovaPulse bug report without exposing credentials, production data, or private member information.
permalink: /support/reporting-bugs/
section: support
section_title: Support
section_url: /support/faq/
---

Report NovaPulse issues in the [Afterparty Bot Labs support server]({{ site.links.support }}).

## Include

- A short, specific summary.
- Command or feature name.
- Date, time, and timezone.
- Server and channel IDs when relevant.
- Safe NovaPulse error reference ID.
- Relevant role names and their order, without unrelated staff details.
- Expected result and actual result.
- Minimal reproduction steps using a test account where possible.
- A cropped screenshot only if it contains no credentials or unrelated member information.

## Do not include

- Bot tokens or client secrets.
- Webhook URLs or tokens.
- Stripe keys or dashboard screenshots containing personal information.
- Passwords, session cookies, authorization headers, or recovery codes.
- A complete <code>.env</code> file.
- Private databases, configuration files, runtime logs, or production archives.
- Identity documents, selfies, or private message exports.

## Template

```text
Summary:
Feature or command:
Time and timezone:
Server/channel IDs:
Safe error reference:
Expected result:
Actual result:
Steps to reproduce:
Permissions and role order checked:
```

If you accidentally expose a credential, delete the message where possible, rotate or revoke the credential immediately, and notify the relevant service owner.
