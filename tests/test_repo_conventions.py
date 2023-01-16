import re
from pathlib import Path
from typing import Iterable

import algokit_arc
import markdown
import pytest
from beaker.application import Application
from bs4 import BeautifulSoup


def _check_doc_conventions(name: str, path: Path) -> list[str]:
    failures = []
    try:
        # convert markdown to HTML and then parse
        html = markdown.markdown(path.read_text())
        soup = BeautifulSoup(html, "html.parser")

        if not soup.find("a", string=re.compile("ARC.*")):
            failures.append(f"{name} missing ARC reference")

        if not soup.find("a", string="Audit"):
            failures.append(f"{name} missing Audit reference")
    except IOError:
        failures.append(f"{name} missing documentation ({path})")
    return failures


def _get_arc_exports() -> Iterable[str]:
    exports = vars(algokit_arc)
    for name, value in exports.items():
        if not name.startswith("_") and issubclass(value, Application):
            yield name


def test_exported_classes_meet_conventions(request: pytest.FixtureRequest):
    root_dir = request.config.rootdir
    failures = []
    for name in _get_arc_exports():
        doc_name = name.lower()
        path = Path(root_dir, "docs", "arcs", f"{doc_name}.md")
        failures.extend(_check_doc_conventions(name, path))

    failures = "\n".join(failures)
    assert failures == ""
