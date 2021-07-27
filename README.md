# Bux

Python SDK for BUX Zero ([getbux.com](https://getbux.com/)).

Features:

+ 100% type safe.
+ Multiple network libraries supported.
+ Both sync and async APIs.
+ [Open-world assumption](https://en.wikipedia.org/wiki/Open-world_assumption), changes in API won't break the library.

Supported networking libraries:

+ [requests](https://docs.python-requests.org/en/master/)
+ [httpx](https://www.python-httpx.org/)
+ [aiohttp](https://docs.aiohttp.org/en/stable/)

## Disclaimer

+ This is an unofficial library! I'm not affiliated with BUX B.V., don't work there, don't know anyone who works there. BUX B.V. is not responsible for any bugs in this library and does not provide technical support for the library usage or development.
+ This is an OSS distributed under MIT License. I don't provide warranty nor technical support for the project. I'm not responsible for any bugs or issues you may encounter. See [LICENSE](./LICENSE).
+ The library uses public API, in a sense that it is publicly available and all you need to get access to it is an account (which you own, thanks to GDPR). However, this API is not documented and can be broken by BUX B.V. at any moment.
+ Keep in mind that [BUX Client Agreement](https://getbux.com/documents/20210705-BUX-Zero-Client-Agreement-EN.pdf) forbids placing orders in other way than the official mobile app: "You can only provide Orders to BUX through a mobile application". However, it doesn't say anything about other API endpoints, like getting historical data. Hence all endpoints, except those that place orders, are legal.
+ So, use it at your own risk! If you found a bug, you're the only one who can fix it. Please, when you fix something, contribute it back, the project is open for contributions.

## Getting started

### Installation

Install bux and the networking library you want to use. If you don't know which one you need, just use requests.

```bash
python3 -m pip install bux requests
```

### Getting token

To make requests to the API, you need to get token. The library provides a CLI command specifically for this:

```bash
python3 -m bux get-token
```

Keep this token in secret! This is all you need to get full access to the API.

## Usage

```python
import bux

api = bux.UserAPI(token=your_token)

me = api.me().requests()
```

Every API endpoint is represented as a method of `UserAPI`. Every such method returns a `bux.Request` method which provides a method for every supported networking library (`requests`, `httpx`, and so on). Just call this method and you get the result. The result is represented as `bux.Response` object which is just a `dict` with some additional type-safe properties.
