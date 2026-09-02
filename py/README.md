# Python solutions

### Running tests

Create venv

```bash
python -m venv venv
```

Activate venv

```bash
source venv/bin/activate
```

Pip install from requirements.txt

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```

Run linter/formatter

```bash
ruff check .
ruff format .
```

### Setting up a shortcut in Mac using iCanHazShortcut

Install `iCanHazShortcut`

```bash
brew install --cask icanhazshortcut
```

Set up the script:
* Open iCanHazShortcut from your menu bar or applications.
* Navigate to the Shortcuts tab, then click the plus (+) button to add a new entry.
* Enter an Action name to label your shortcut (e.g. "Clipboard strip links").
* In the Command field, enter `python3 path/to/clipboard_link_stripper/strip_links.py`
