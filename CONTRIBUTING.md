# 👥 Contributing

Want to add a contribution to **doty**? Feel free to send a [pull request](https://github.com/leahevy/doty/compare).

---

## 💿 Setup development environment

Setup a virtualenv with `make virtualenv-create` and `source ./.venv/bin/activate` or `source ./.venv/bin/activate.fish`.

After that you can install the development dependencies with `make install-dev`.

---

## ⌨️ Development commands

To see the development commands, run `make help`.

---

## ☁️ How to Create Releases on GitHub

1. In a clean work directory, create a release with one of:
    - `make release-major`
    - `make release-major`
    - `make release-patch`
2. Push the new release commit with `git push --follow-tags`

---

## 🏷 How to publish releases on Pypi

Create an account on <https://pypi.org/account/register/>

Releases will be automatically released on **Pypi** using the configured release workflow.
