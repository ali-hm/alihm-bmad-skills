# Maintaining and publishing the bundle

## Version policy

The root plugin.json version is the bundle's release identity. Keep metadata.version in all four SKILL.md files and the README bundle version identical to it. Keep skill names stable across versions.

Use major.minor.patch versions. Before 1.0, use a minor bump for breaking workflow changes and describe the break clearly. After 1.0, use a major bump for incompatible invocation, approval, workflow, or installation changes; a minor bump for compatible capabilities; and a patch for corrections that preserve workflow behavior.

Version labels do not implement automatic updates. GitHub-backed Skills CLI installations track source content; Git tags identify snapshots. Keep unreleased experiments off the public default branch when default-branch consumers could receive them through an update.

## Before the first publication

1. Confirm that the GitHub identity in README.md and plugin.json matches your intended publishing repository, currently https://github.com/ali-hm/alihm-bmad-skills. Keep repository and homepage accurate if it moves.
2. Review the four skills, their supporting files, dependency documentation, and MIT license. Keep machine-specific paths, private project data, credentials, and upstream vendored code out of the package.
3. Install validation dependencies, then run python scripts/validate.py --release from the repository root. This extra release check rejects the GitHub-owner placeholder and requires an HTTPS GitHub repository URL.
4. List the local package through npx skills add . --list. Confirm exactly four skills are discovered without installing them over working copies.
5. Exercise representative routes in an isolated sample project. Cover an idea, an approved spec, a defect, a consequential change, read-only review, guided Interactive, explicit Auto, missing wrapper, and CRITICAL approval. Record which checks are live versus dry runs.
6. Create the public GitHub repository and connect this checkout to it. Review the pending files before committing and pushing. Publish only when you intend to make them public.
7. Tag the validated commit v0.1.0 and create a GitHub Release with matching changelog notes. Do not claim a release exists merely because the changelog has an entry.

These are maintainer actions. The validation script and CI never commit, tag, push, create releases, or publish on your behalf.

## Each subsequent release

1. Make scoped changes to the authoritative skills/ copies in this repository. Installed copies are consumers; avoid maintaining divergent originals.
2. Update plugin.json, all four metadata.version values, the README version, and CHANGELOG.md together. Use the actual release date. Identify compatibility or approval changes clearly.
3. Recheck BMad interfaces if the upstream installation changed. Update docs/compatibility.md with the exact evidence and verification limits.
4. Run package validation and affected behavioral scenarios. Resolve introduced failures and review the final diff.
5. Commit and push the intended release when authorized, then create a new immutable vX.Y.Z tag and GitHub Release. Do not move an already published tag to different content.
6. Tell users to update the four skills together using the command in README.md. Upstream BMad upgrades remain a separate operation.

## Optional plugin-directory publication

The root plugin.json uses the portable Agent Plugins format and the root skills/ directory. It needs no bundled MCP server for these four local workflows. This manifest alone does not create a public listing or prove eligibility on every host.

For submission, make a ZIP with plugin.json, LICENSE, README.md, and the complete skills/ directory at the archive root. Include the linked docs/ and CHANGELOG.md if retaining the README in the archive. Exclude .git, validation caches, local environments, and private files.

Use a verified developer identity in the OpenAI Plugins portal, upload the ZIP, resolve checks, and follow the portal's review/publication steps. Confirm the target surface can supply BMad and the local execution capabilities these skills require. A ChatGPT listing does not guarantee that every ChatGPT surface can execute a repository build.

Skill/metadata changes require a new ZIP upload to the existing plugin entry. Updating GitHub does not automatically replace the directory package. See the [packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).
