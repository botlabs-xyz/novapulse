# NovaPulse

Advanced moderation, automation, verification, logging, and server security for Discord communities.

[![Documentation](https://img.shields.io/badge/Documentation-9933FF?style=for-the-badge&logo=readthedocs&logoColor=white)](https://botlabs-xyz.github.io/novapulse/)
[![Invite](https://img.shields.io/badge/Invite_NovaPulse-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1354663481021829150)
[![Support](https://img.shields.io/badge/Support-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/BusuZp2G8w)
[![Website](https://img.shields.io/badge/Afterparty_Bot_Labs-9933FF?style=for-the-badge)](https://afterpartylabs.xyz)

## About NovaPulse

NovaPulse helps Discord communities organize moderation, server configuration, onboarding, verification, logging, and security workflows. The documentation explains how to install the app, configure only the features your server needs, and keep permissions and role hierarchy in good order.

## Documentation

- [Documentation](https://botlabs-xyz.github.io/novapulse/)
- [Invite NovaPulse](https://discord.com/oauth2/authorize?client_id=1354663481021829150)
- [Support server](https://discord.gg/BusuZp2G8w)
- [Afterparty Bot Labs](https://afterpartylabs.xyz)
- [botlabs-xyz on GitHub](https://github.com/botlabs-xyz)

## Core features

- Server roles, channels, logs, and configuration review
- Moderation and staff administration tools
- Introductory role workflows and optional verification features
- Server-owned activity and moderation logging
- Configurable automation, NovaTrap, and server-security tooling
- Guides for permissions, role hierarchy, setup, and troubleshooting

## Local documentation development

Requirements: Ruby, Bundler, and Jekyll.

```powershell
bundle install
bundle exec jekyll serve --baseurl /novapulse
```

Build without serving:

```powershell
bundle exec jekyll build
```

GitHub Pages publishes the site from `main` at the repository root with the `/novapulse` base URL.

## Repository purpose

This repository contains the public NovaPulse documentation website. It does **not** contain the private NovaPulse bot source code.

Maintainer-only notes live in `docs-development/` and are excluded from the published Jekyll site.

## Content safety

Never commit credentials, runtime data, `.env` files, logs, databases, private configuration, webhook URLs, identity documents, or production exports. If sensitive data is exposed, remove it from the pending change, rotate or revoke the affected credential, and review repository history before publishing.

## Afterparty Bot Labs

NovaPulse is part of [Afterparty Bot Labs](https://afterpartylabs.xyz).
