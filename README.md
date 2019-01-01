# Plausible web analytics source snapshot

Plausible collects website pageviews and events and presents aggregate analytics in
an Elixir/Phoenix dashboard. This imported tree includes the application in `lib/`,
PostgreSQL migrations in `priv/`, ClickHouse event-storage configuration, dashboard
assets in `assets/`, and the browser tracker and its compiler in `tracker/`.
It also includes integrations for OAuth, S3 exports, billing, and SSO.

## Source and distribution status

Source: [plausible/analytics](https://github.com/plausible/analytics).
The upstream repository was created on 2018-12-04 (GitHub repository metadata);
the existing local `2019/` directory is retained. This is a 2026 source import,
not a record of original development. The imported revision is unknown.

**Publication is withheld:** `extra/COPYING.txt` explicitly grants no distribution
rights for the `extra/` subtree. The root AGPL license does not override that notice.
`LICENSE.md` was restored verbatim from the official upstream license blob
`0ad25db4bd1d86c452db3f9602ccdbe172438f52`; that restoration does not establish
permission to redistribute restricted files. Resolve the source provenance and
restricted-subtree licensing before publishing this complete snapshot.

## Requirements and development

`mix.exs` requires Elixir `~> 1.18`; `.tool-versions` pins the imported environment.
Use compatible Erlang/OTP, Node/npm, PostgreSQL and ClickHouse. The development
Makefile also offers Docker targets for these services; inspect versions and
networking before running them. No production deployment is implied by these
local commands.

From the repository root, with runtimes and databases available:

```sh
make postgres
make clickhouse
make install
make server
```

`make install` fetches Mix dependencies, creates and migrates the SQL database,
downloads country data, installs both JavaScript dependency trees and compiles
the tracker. `make server` invokes `mix phx.server`. The local base URL is
`http://localhost:8000`. Review `config/runtime.exs` and the `config/.env.*` profiles
for environment-specific database URLs and settings. Local development secrets
are public fixtures and must never be reused in production.

## Credentials

Google OAuth client ID/secret and Paddle authorization values have been cleared
from development/test/load profiles. Supply real values through a private runtime
configuration; never commit them. Potentially real removed credentials must be
revoked or rotated by their owner. Removing Git values does not revoke credentials.

Run the credential regression check without application dependencies:

```sh
python3 scripts/check_fixture_credentials.py
```

## Tests and deployment

With Mix dependencies, PostgreSQL and ClickHouse configured:

```sh
mix test
npm test --prefix tracker
```

Consult the scripts in `tracker/package.json` and `assets/package.json` for focused
JavaScript checks. `Dockerfile` and `rel/` define release packaging; production
configuration is read in `config/runtime.exs`. Obtain a properly licensed Community
Edition source/release before attempting production distribution. Full application
build/tests have not run in this environment because Elixir/Mix is unavailable.
