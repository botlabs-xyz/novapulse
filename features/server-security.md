---
layout: default
title: Server security
description: Understand anti-nuke monitoring, audit-log requirements, response boundaries, and safe operating guidance.
permalink: /features/server-security/
section: features
section_title: Features
section_url: /features/
status: Advanced feature
status_style: danger
---

NovaPulse's anti-nuke feature observes selected destructive actions through Discord audit logs. The current implementation covers channel deletion, role deletion, and kicks within configurable windows and thresholds.

## What it can do

- Count selected destructive actions by the attributed executor.
- Send an alert to a configured Discord channel or webhook.
- Exempt configured users and roles.
- Optionally attempt an emergency lockdown by removing dangerous roles and timing out the suspected member.

## Requirements

NovaPulse needs View Audit Log to attribute actions. Emergency response may also need Manage Roles and Moderate Members, and Discord hierarchy must permit action against the suspected member and their roles.

## Boundaries

The feature is not a replacement for Discord's own security controls, staff account protection, least privilege, two-factor authentication, or change review. Audit-log attribution can arrive late or be unavailable. A missing permission should cause the feature to alert or skip rather than perform a partial response.

## Availability

Emergency lockdown is currently limited to authorized deployments. Use <code>/antinuke status</code> for review, and keep <code>emergency_lockdown</code> disabled unless NovaPulse has approved a safe test for your server.
