from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class CheckResult:
    name: str
    path: str
    present: bool
    recommendation: str

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


CHECKS = (
    ("README", ("README.md", "README.rst", "README"), "Add a README explaining the project."),
    ("License", ("LICENSE", "LICENSE.md", "LICENSE.txt"), "Add an OSI-approved license."),
    ("Contributing guide", ("CONTRIBUTING.md",), "Add contribution instructions."),
    ("Code of conduct", ("CODE_OF_CONDUCT.md",), "Add community behavior guidelines."),
    ("CI workflow", (".github/workflows",), "Add automated checks with GitHub Actions."),
)


def run_checks(root: Path) -> list[CheckResult]:
    """Return deterministic readiness checks for *root*."""
    if not root.is_dir():
        raise ValueError(f"Repository path is not a directory: {root}")

    results = []
    for name, candidates, recommendation in CHECKS:
        present = any((root / candidate).exists() for candidate in candidates)
        results.append(
            CheckResult(
                name=name,
                path=candidates[0],
                present=present,
                recommendation=recommendation,
            )
        )
    return results
