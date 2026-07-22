# NovaPulse Documentation

Official public-review documentation for NovaPulse, an advanced Discord moderation, automation, verification, logging, and community-management bot built by Afterparty Bot Labs.

Live documentation: <https://botlabs-xyz.github.io/novapulse>

> The documentation can be published while NovaPulse remains in controlled deployment. Do not interpret the site as a public-readiness declaration for the bot or for features marked draft, controlled, incomplete, or deferred.

## Framework

The site uses GitHub Pages-compatible Jekyll with custom layouts, responsive CSS, and lightweight vanilla JavaScript. It does not depend on an external theme or unsupported plugin.

## Local development

Requirements: Ruby, Bundler, and Jekyll.

```powershell
bundle install
bundle exec jekyll serve --baseurl /novapulse
```

Open the local URL printed by Jekyll. Build without serving:

```powershell
bundle exec jekyll build
```

## Project structure

```text
_data/             Navigation data
_includes/         Shared head, header, sidebar, and footer
_layouts/          Jekyll page layout
assets/            CSS, JavaScript, and optimized NovaPulse images
commands/          Slash-command reference
configuration/     Administrator configuration guidance
features/          Confirmed feature behavior and release status
getting-started/   Installation, setup, and permissions
guides/            Task-focused administrator guides
legal/             Draft privacy policy and terms
support/           FAQ, troubleshooting, bug reports, and support
docs-development/  Implementation report, excluded from the public build
scripts/            Reproducible development helpers, excluded from the public build
```

## Contribution expectations

- Verify behavior against the current NovaPulse source before documenting it.
- Clearly distinguish available, controlled, incomplete, and deferred behavior.
- Do not advertise a feature as public-ready until its release gate is approved.
- Use `relative_url` or `absolute_url` filters for paths under the `/novapulse` base path.
- Keep navigation, metadata, accessibility, mobile behavior, and cross-links current.
- Mark Privacy Policy and Terms changes for owner/legal review.

## Content safety

Never add:

- Bot tokens, client secrets, Stripe keys, passwords, authorization headers, or recovery codes.
- Discord webhook URLs or tokens.
- Complete `.env` files or live configuration.
- Production guild, channel, role, or member data except intentionally public application links.
- Databases, runtime logs, invite records, audit reports, backups, archives, or source-project files.
- Identity documents, private messages, or personal member information.

If a credential is exposed, stop, remove it from the pending change, rotate or revoke it through the owning service, and review repository history before publishing.

## Deployment

The repository is configured for GitHub Pages at `/novapulse`. Publish from the `main` branch and repository root. GitHub's supported Jekyll build will generate the site; `_site` should remain uncommitted.

If Pages is not enabled, open **Repository Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.

## Branding

NovaPulse uses `#9933FF` as its primary accent. Optimized website derivatives are generated from the official source image with:

```powershell
python scripts/generate_brand_assets.py
```

The original source image remains unchanged and is excluded from version control.

## Attribution

NovaPulse and this documentation are part of [Afterparty Bot Labs](https://afterpartylabs.xyz).
