---
layout: default
title: Invite NovaPulse
description: Use the official NovaPulse invite link and approve only the permissions needed by your server's selected features.
permalink: /getting-started/inviting-novapulse/
section: getting-started
section_title: Getting started
section_url: /getting-started/
---

Use the official [NovaPulse invite link]({{ site.links.invite }}) and select a server where you have permission to install apps.

<div class="notice warning">
  <strong>Availability:</strong> NovaPulse access may be limited while the product is prepared for broader availability. Advanced security and bulk-administration features are not part of the standard installation flow.
</div>

## What the invite does

The official invite adds NovaPulse to your server and makes its slash commands available automatically.

NovaPulse does not ask for access to your Discord account information beyond the server installation approval.

## Permission profiles

Administrator is not required and should not be granted by default.

<div class="table-wrap" markdown="1">

| Profile | Permissions | When to use it |
| --- | --- | --- |
| Basic | View Channels, Send Messages, Embed Links, Read Message History | Commands, panels, and basic channel output |
| Onboarding and roles | Basic plus Manage Server and Manage Roles | Invite attribution, join roles, and verification roles |
| Moderation add-on | Kick Members, Ban Members, Manage Messages, Moderate Members, View Audit Log | Only when your server uses the related moderation or security features |
| Optional setup | Manage Channels or Manage Webhooks | Only when NovaPulse must create a NovaTrap channel or a server-owned verification webhook |

</div>

## Install steps

1. Open the official invite link.
2. Choose the intended server.
3. Review the displayed permissions rather than approving automatically.
4. Complete Discord's authorization prompt.
5. Move the NovaPulse role to the correct position in **Server Settings → Roles**.
6. Use a channel where NovaPulse can view and send messages, then type <code>/help</code>.

## If the server does not appear

You may not have **Manage Server**, the server may restrict app installation, or your Discord account may require an additional security step. Ask the server owner to perform the install; never ask them to share their password, token, or session.

## Related pages

- [Permissions and hierarchy]({{ '/getting-started/permissions/' | relative_url }})
- [Initial setup]({{ '/getting-started/initial-setup/' | relative_url }})
- [Troubleshoot missing commands]({{ '/support/troubleshooting/' | relative_url }})
