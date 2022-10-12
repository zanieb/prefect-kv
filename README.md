# prefect-kv

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-kv/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-kv?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/madkinsz/prefect-kv/" alt="Stars">
        <img src="https://img.shields.io/github/stars/madkinsz/prefect-kv?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-kv/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-kv?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/madkinsz/prefect-kv/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/madkinsz/prefect-kv?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

A simple key-value store for use with Prefect.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-kv` with `pip`:

```bash
pip install prefect-kv
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_kv.credentials
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### Write and run a flow

```python
from prefect import flow
from prefect_kv.tasks import (
    goodbye_prefect_kv,
    hello_prefect_kv,
)


@flow
def example_flow():
    hello_prefect_kv
    goodbye_prefect_kv

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-kv`, feel free to open an issue in the [prefect-kv](https://github.com/madkinsz/prefect-kv) repository.

If you have any questions or issues while using `prefect-kv`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-kv`](https://github.com/madkinsz/prefect-kv) for updates too!

## Development

If you'd like to install a version of `prefect-kv` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/madkinsz/prefect-kv.git

cd prefect-kv/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
