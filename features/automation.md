---
layout: default
title: Automation and member events
description: Review confirmed join roles, introduction flows, invite attribution, and member-event behavior.
permalink: /features/automation/
section: features
section_title: Features
section_url: /features/
status: Opt-in design pending
status_style: warning
---

The current private build handles several member and server events automatically.

## Confirmed automation

- Assign up to two configured auto roles when a member joins.
- Apply configured non-verified roles for onboarding.
- Process introduction forms and assign a verified role when conditions are met.
- Remove configured non-verified roles after approval.
- Fetch invite information and attribute member joins where Discord permissions allow.
- Track server member events and respond to deleted configured channels or roles.
- Create or use a dedicated bot role in parts of the current member-join flow.

## Current limitations

Public onboarding is incomplete. New servers do not have a complete feature opt-in wizard, permission-check command, retention selection, or idempotent disable/remove workflow. Invite and message-count records in the current private build also need final retention and deletion procedures.

## Recommended approach

1. Configure roles before enabling any member automation.
2. Confirm every role is below NovaPulse and is not managed by an integration.
3. Limit features to the smallest approved set.
4. Use a test account to verify join and verification behavior.
5. Review logs for one complete test cycle.
6. Contact support before enabling behavior not covered by the controlled deployment plan.
