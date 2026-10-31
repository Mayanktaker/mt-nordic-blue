# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Regression tests for recolor_accent.py: the glacier base/strong collision, literal forms, identity.

import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "dev" / "recolor_accent.py"

failures = []


def run(css: str, *args: str) -> tuple:
    # Run the tool over a temp file and return (exit_code, result_css, output).
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "t.css"
        path.write_text(css)
        proc = subprocess.run([sys.executable, str(TOOL), *args, str(path)],
                              capture_output=True, text=True)
        return proc.returncode, path.read_text(), proc.stdout + proc.stderr


def check(name: str, ok: bool, detail: str = "") -> None:
    # Record and print one test result.
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'' if ok else f' — {detail}'}")
    if not ok:
        failures.append(name)


# The light glacier base equals frost's strong source; a naive two-step pass would chain and corrupt it.
code, out, log = run('a{color:#4C719C}b{color:#5E81AC}', "--variant", "light", "--flavor", "glacier")
check("glacier light: base -> #5E81AC", "color:#5E81AC" in out, out)
check("glacier light: strong -> #7091BC", "color:#7091BC" in out, out)
check("glacier light: no frost base left", "#4C719C" not in out, out)

# Every literal form of the accent must be rewritten, in one pass.
code, out, log = run(
    'a{color:#88C0D0}b{background:rgb(136, 192, 208)}c{border:rgba(136, 192, 208, 0.4)}',
    "--variant", "dark", "--flavor", "cyber")
check("hex rewritten", "#00D2FF" in out, out)
check("rgb() rewritten", "rgb(0, 210, 255)" in out, out)
check("rgba() rewritten with space", "rgba(0, 210, 255, 0.4)" in out, out)

# Default flavour is an identity mapping; nothing may change.
src = 'a{color:#88C0D0}b{color:#5E81AC}'
code, out, log = run(src, "--variant", "dark", "--flavor", "frost")
check("frost is a no-op", out == src, out)

# Unknown flavour must fail loudly rather than write a partial file.
code, out, log = run('a{color:#88C0D0}', "--variant", "dark", "--flavor", "nope")
check("unknown flavour exits 2", code == 2, f"exit={code}")

# --base-only must leave the strong family untouched.
code, out, log = run('a{color:#4C719C}b{color:#5E81AC}', "--variant", "light", "--flavor", "glacier", "--base-only")
check("base-only keeps strong", "color:#5E81AC}" in out and "#7091BC" not in out, out)

if failures:
    print(f"\n{len(failures)} failing test(s): {failures}", file=sys.stderr)
    sys.exit(1)
print("\nAll recolor_accent tests pass.")
