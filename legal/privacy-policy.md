---
layout: default
title: Privacy policy
description: Draft public-review privacy policy describing information NovaPulse may process and the safeguards still requiring owner review.
permalink: /legal/privacy-policy/
section: legal
status: Draft · owner/legal review required
status_style: warning
---

**Draft date:** July 22, 2026

This draft describes the confirmed behavior of the current NovaPulse private build. It is provided for public review and is not legal advice. The NovaPulse owner must review and approve operator identity, retention periods, deletion procedures, third-party terms, jurisdiction-specific notices, and launch readiness before treating it as a final policy.

## 1. Scope and operator

NovaPulse is operated within the Afterparty Bot Labs ecosystem. Questions and requests may be submitted through the [Afterparty Bot Labs support server]({{ site.links.support }}). Final operator identity and a dedicated privacy contact require owner review before public launch.

## 2. Information NovaPulse may process

Depending on features enabled by a server administrator, NovaPulse may process:

- Discord guild, channel, role, user, message, and invite identifiers.
- Usernames or display names needed for logs and staff review.
- Server configuration for roles, channels, verification, moderation, and security features.
- Invite codes, usage information, inviter identifiers, and member join timestamps.
- Per-guild or per-user message-count aggregates in the current private build.
- Introduction information submitted through a Discord modal, including configured profile or age fields.
- Verification request status, Discord user ID, and request timestamp.
- Message content, links, and attachment URLs when processed for configured NovaTrap or spam detection and staff evidence.
- Moderation action outcomes, deletion results, recovery-message status, and security counters.
- Minimal redacted operational information such as service activity, uptime or shard status, error class, safe reference ID, and limited security-event metadata.

NovaPulse should not receive passwords, Discord tokens, webhook credentials from end users, identity documents in Discord, private database files, or complete environment files.

## 3. Purposes

Information may be processed to provide server configuration, member onboarding, role assignment, staff-reviewed verification, invite attribution, customer-server logging, moderation or security features selected by administrators, support, abuse prevention, and minimal service reliability monitoring.

Server administrators are responsible for selecting appropriate features, permissions, notices, staff access, and lawful purposes for their community.

## 4. Verification and third parties

The optional <code>/idverify</code> workflow can create a session with **Stripe Identity** and associate the relevant Discord user ID in session metadata. Stripe processes the verification session outside Discord. Authorized staff access, review criteria, Stripe retention, deletion, international transfer disclosures, and contractual terms require owner/legal confirmation.

NovaPulse does not instruct members to upload an ID or selfie directly into Discord. This does not mean authorized provider-dashboard users can never access verification information; staff permissions must be documented and restricted.

NovaPulse also relies on **Discord** for account, server, command, message, role, moderation, and gateway services. Customer servers may configure Discord channels or supported webhook destinations for their own logs. No other processor is named here without confirmed production use.

## 5. Customer-server logs and internal monitoring

Customer-server logs are delivered to channels or supported destinations selected by the server administrator. Those logs may contain moderation, verification, invite, role, or security information and are controlled by the server's permissions and retention practices.

Internal NovaPulse monitoring is separate and is designed to contain minimal redacted service metadata. It should not include private message content, complete moderation records, raw guild configuration, webhook credentials, full invite history, or cross-server private records.

## 6. Retention

The current private build stores some guild configuration, invite/member records, message-count aggregates, and active verification metadata in local runtime files. Fixed retention periods, automatic expiry, guild-removal cleanup, and complete user/guild deletion or export procedures are not yet implemented for every category.

Some records may therefore persist until they are manually removed or the runtime data is replaced. Public rollout should not proceed until the owner approves documented retention periods and automated cleanup appropriate to each category.

Customer-server Discord logs remain subject to the server administrator's channel retention and access decisions. Stripe-held information is subject to confirmed operator settings and Stripe's applicable terms.

## 7. Data minimization and security

NovaPulse is designed to limit processing to enabled features, redact sensitive error data, hide webhook values from configuration displays, and keep operational monitoring minimal. Phase 1A added centralized redaction, restricted operational summaries, release-artifact checks, and safer error references.

No service can promise absolute security. Remaining public-release work includes protected persistence, fixed retention and deletion workflows, webhook destination restrictions, permission hardening, moderation-case review, and controlled beta testing.

## 8. Administrator responsibilities

Server administrators should:

- Grant least-privilege permissions and restrict command access.
- Tell members which features and logs are enabled.
- Limit staff access to verification and moderation information.
- Choose and enforce an appropriate log-retention period.
- Respond to member questions, corrections, and appeals.
- Disable a feature when its processing is unnecessary or unsafe.
- Never submit credentials or private production files to support.

## 9. Requests, deletion, and correction

To request access, correction, deletion, or review, contact the server administrator first. For NovaPulse operator escalation, use the [support server]({{ site.links.support }}). Provide the Discord user ID, relevant server ID, request type, and approximate date range. Do not send identity documents, passwords, tokens, or unrelated private messages.

Requests are subject to identity and authority verification appropriate to the request. Because automated export and deletion are incomplete in the current build, the operator must review the available runtime and provider locations manually. Final response time, verification method, exceptions, and jurisdictional rights require legal review.

## 10. Automated moderation and appeals

NovaTrap, anti-nuke, and age-policy workflows may produce automated or semi-automated moderation outcomes in controlled deployments. The current public release gate requires stronger false-positive, human-review, case, reversal, and appeal safeguards. Members should appeal first to their server's staff, then contact NovaPulse support if an operator-level issue is suspected.

## 11. Changes

This policy may be updated as NovaPulse behavior, providers, retention, or legal requirements change. Material changes should receive a new effective date and, where appropriate, notice through the documentation or support server.

## 12. Items requiring final review

- Legal operator name, address, and privacy contact.
- Applicable legal bases and jurisdiction-specific rights.
- Exact retention periods and deletion/export service levels.
- Stripe Identity dashboard access, provider settings, and processor terms.
- Hosting provider and international-transfer disclosures.
- Minors, age-policy, consent, and verification language.
- Security-incident notification procedure.
- Final policy effective date and acceptance process.
