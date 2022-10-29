# Brooser
`brooser` is a small-ish script to automatically open URLs in different browsers or browser profiles. For example, you might want to contain everything related to work in one browser, so you [configure](#configuration) `brooser` to send all work-URLs to that one.
(Yes, the name needs work.)

## Configuration
`brooser` reads from a configuration file located at `${XDG_CONFIG_HOME}/brooser.conf` (usually `.config/brooser.conf`).

In the file, you can define as many profiles as you want, each consisting of one `command` and a list of URLs - written as Python regular expressions, so remember to escape `.`.
For example:
```toml
[work]
command = "firefox -P work %url"
urls = [
  "https://.*\\.work\\.com.*"
]

[default]
command = "firefox %url"
```
You also need to define the fallback command, called `default`.

## Installation
1. Somehow install it on your system.
2. Add `brooser.desktop` to your system.
3. Set `brooser.desktop` as your default handler for HTTP, HTTPS etc.