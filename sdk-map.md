<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Square (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Square |
| Root package | `square` |
| Distribution name | `square` |
| Requires | Python 3.10 or later |
| API spec version | `2.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from square import SquareClient
from square.auth import Oauth2Scope
from square.core import AuthorizationCodeCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = SquareClient(
    oauth2=AuthorizationCodeCredentials[Oauth2Scope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    oauth2_client_secret="YOUR_API_KEY",
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SquareClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from square import AsyncSquareClient
from square.auth import Oauth2Scope
from square.core import AsyncAuthorizationCodeCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncSquareClient(
        oauth2=AsyncAuthorizationCodeCredentials[Oauth2Scope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        oauth2_client_secret="YOUR_API_KEY",
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSquareClient(...) as client:` closes the pool on exit.

`AsyncClient` (`square/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `SquareClient` and `AsyncSquareClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.apple_pay`). Every constructor argument is optional and keyword-only. Sources: `square/client.py`, `square/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `oauth2` | `AuthorizationCodeCredentialsOrDict[Oauth2Scope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[Oauth2Scope] \| None` | `None` |
| `oauth2_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[Oauth2Scope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth2Scope]] \| None` | `None` |
| `oauth2_client_secret` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `square.server` | `Literal` of the Environments table's names |
| `HttpClient` | `square.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AuthorizationCodeCredentialsOrDict` | `square.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `Oauth2Scope` | `square.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `square.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `square.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `AsyncHttpClient` | `square.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |
| `AsyncAuthorizationCodeCredentialsOrDict` | `square.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `square.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `square.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `square/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`square/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`square/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is always `RawError` (no Case A alias in this SDK) | `error: E` · `status_code: int` · `response: HttpResponse` | `square/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `square/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `square/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from square.core import ApiError, RawError

try:
    response = client.apple_pay.register_domain(body)
except ApiError as e:
    # Case B — raw error: e.error is RawError
    print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **334 operations**, **0 are Case A (typed)** and **334 are Case B (raw)**.

---

## Operations — by controller (43 pages, 334 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`square/core/request_options.py`) |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.apple_pay` | 1 | [map/operations/apple_pay.md](map/operations/apple_pay.md) |
| `client.bank_accounts` | 5 | [map/operations/bank_accounts.md](map/operations/bank_accounts.md) |
| `client.booking_custom_attributes` | 11 | [map/operations/booking_custom_attributes.md](map/operations/booking_custom_attributes.md) |
| `client.bookings` | 13 | [map/operations/bookings.md](map/operations/bookings.md) |
| `client.cards` | 4 | [map/operations/cards.md](map/operations/cards.md) |
| `client.cash_drawers` | 3 | [map/operations/cash_drawers.md](map/operations/cash_drawers.md) |
| `client.catalog` | 14 | [map/operations/catalog.md](map/operations/catalog.md) |
| `client.channels` | 3 | [map/operations/channels.md](map/operations/channels.md) |
| `client.checkout_api` | 10 | [map/operations/checkout_api.md](map/operations/checkout_api.md) |
| `client.customer_custom_attributes` | 10 | [map/operations/customer_custom_attributes.md](map/operations/customer_custom_attributes.md) |
| `client.customer_groups` | 5 | [map/operations/customer_groups.md](map/operations/customer_groups.md) |
| `client.customer_segments` | 2 | [map/operations/customer_segments.md](map/operations/customer_segments.md) |
| `client.customers` | 14 | [map/operations/customers.md](map/operations/customers.md) |
| `client.devices` | 5 | [map/operations/devices.md](map/operations/devices.md) |
| `client.disputes` | 9 | [map/operations/disputes.md](map/operations/disputes.md) |
| `client.employees` | 2 | [map/operations/employees.md](map/operations/employees.md) |
| `client.events` | 4 | [map/operations/events.md](map/operations/events.md) |
| `client.gift_card_activities` | 2 | [map/operations/gift_card_activities.md](map/operations/gift_card_activities.md) |
| `client.gift_cards` | 7 | [map/operations/gift_cards.md](map/operations/gift_cards.md) |
| `client.inventory` | 19 | [map/operations/inventory.md](map/operations/inventory.md) |
| `client.invoices` | 10 | [map/operations/invoices.md](map/operations/invoices.md) |
| `client.labor` | 27 | [map/operations/labor.md](map/operations/labor.md) |
| `client.location_custom_attributes` | 11 | [map/operations/location_custom_attributes.md](map/operations/location_custom_attributes.md) |
| `client.locations` | 4 | [map/operations/locations.md](map/operations/locations.md) |
| `client.loyalty` | 18 | [map/operations/loyalty.md](map/operations/loyalty.md) |
| `client.merchant_custom_attributes` | 11 | [map/operations/merchant_custom_attributes.md](map/operations/merchant_custom_attributes.md) |
| `client.merchants` | 2 | [map/operations/merchants.md](map/operations/merchants.md) |
| `client.oauth` | 3 | [map/operations/oauth.md](map/operations/oauth.md) |
| `client.order_custom_attributes` | 11 | [map/operations/order_custom_attributes.md](map/operations/order_custom_attributes.md) |
| `client.orders` | 8 | [map/operations/orders.md](map/operations/orders.md) |
| `client.payments` | 7 | [map/operations/payments.md](map/operations/payments.md) |
| `client.payouts` | 3 | [map/operations/payouts.md](map/operations/payouts.md) |
| `client.refunds` | 3 | [map/operations/refunds.md](map/operations/refunds.md) |
| `client.sites` | 1 | [map/operations/sites.md](map/operations/sites.md) |
| `client.snippets` | 3 | [map/operations/snippets.md](map/operations/snippets.md) |
| `client.subscriptions` | 12 | [map/operations/subscriptions.md](map/operations/subscriptions.md) |
| `client.team` | 12 | [map/operations/team.md](map/operations/team.md) |
| `client.terminal` | 15 | [map/operations/terminal.md](map/operations/terminal.md) |
| `client.transactions` | 4 | [map/operations/transactions.md](map/operations/transactions.md) |
| `client.transfer_order_api` | 8 | [map/operations/transfer_order_api.md](map/operations/transfer_order_api.md) |
| `client.v1_transactions` | 3 | [map/operations/v1_transactions.md](map/operations/v1_transactions.md) |
| `client.vendors` | 7 | [map/operations/vendors.md](map/operations/vendors.md) |
| `client.webhook_subscriptions` | 8 | [map/operations/webhook_subscriptions.md](map/operations/webhook_subscriptions.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `square/models/` declares one type plus its input companion, and every module under `square/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`Achdetails` ↔ `achdetails.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 1271 | `square/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 203 | `square/models/enums/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`Achdetails` ↔ `AchdetailsDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`ActionCancelReason` ↔ `ActionCancelReasonOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `square` |
| Operation controllers | `square.apis` |
| Models | `square.models` |
| Enums | `square.models.enums` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `square.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `oauth2` your client id, redirect URI and authorization code; authorization is at `/oauth2/authorize` and tokens come from `/oauth2/token`, both on the base URL — so `base_url="https://…"` moves token traffic too. Scopes are the `Oauth2Scope` alias.

**API key (header `Authorization`).** Pass `oauth2_client_secret="<api_key>"`; sent as the `Authorization` request header.

**Environments.** `environment=` selects the target environment (`square/server/environment.py`); this SDK's one server (`square/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://connect.squareup.com` | — | `base_url="https://…"` |
| `"sandbox"` | `https://connect.squareupsandbox.com` | — | `base_url="https://…"` |
| `"custom"` | `{custom_url}` | — | `base_url="https://…"` |

`"custom"` template variables: `{custom_url}` defaults to `"https://connect.squareup.com"` — override the whole URL with `base_url="https://…"`.

Pick a row with `environment=`.

