"""A very small mutation testing tool for this lab. No extra packages needed.

    python mutation_run.py

This command makes all mutants of juicebar.py and tests them with test_juicebar.py.
You can choose other files with --source and --tests (for example: --tests test_llm.py).

What it does:
  1. It runs your tests on the original code. They must all pass.
  2. It makes mutants: copies of the code with ONE small change each
     (for example  >=  becomes  >,  or  -  becomes  +).
  3. It runs your tests on every mutant.
     At least one test fails  ->  the mutant is KILLED (good).
     All tests pass           ->  the mutant SURVIVED (your tests did not notice the change).
  4. Mutation score = killed mutants / all mutants.

Your own files are never changed: every mutant lives in a temporary folder.
"""
import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile
import time
import tokenize

# One small change per mutant: the token on the left becomes the token on the right.
SWAPS = {
    ">=": ">", ">": ">=", "<=": "<", "<": "<=",
    "==": "!=", "!=": "==",
    "+": "-", "-": "+", "*": "/", "/": "*", "//": "*",
    "or": "and", "and": "or",
}


def find_mutants(source):
    """Return a list of (line number, column, old token, new token)."""
    found = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type in (tokenize.OP, tokenize.NAME) and tok.string in SWAPS:
            found.append((tok.start[0], tok.start[1], tok.string, SWAPS[tok.string]))
    return found


def apply_mutant(source, mutant):
    """Return (mutated source, original line, mutated line)."""
    line_no, col, old, new = mutant
    lines = source.splitlines(keepends=True)
    line = lines[line_no - 1]
    changed = line[:col] + new + line[col + len(old):]
    lines[line_no - 1] = changed
    return "".join(lines), line.strip(), changed.strip()


def run_tests(folder, test_file):
    """Run pytest in `folder`. Return (all tests passed?, last line of the output)."""
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    cmd = [sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", test_file]
    try:
        done = subprocess.run(cmd, cwd=folder, env=env, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    out = (done.stdout or "").strip().splitlines()
    return done.returncode == 0, (out[-1] if out else "no output")


def main():
    parser = argparse.ArgumentParser(description="Small mutation testing tool for SENG 403 Lab 5")
    parser.add_argument("--source", default="juicebar.py", help="the code to mutate (default: juicebar.py)")
    parser.add_argument("--tests", default="test_juicebar.py", help="the test file (default: test_juicebar.py)")
    args = parser.parse_args()

    for path in (args.source, args.tests):
        if not os.path.isfile(path):
            print("File not found:", path)
            print("Run this command in the folder that has juicebar.py and test_juicebar.py.")
            return 2

    with open(args.source, encoding="utf-8") as f:
        source = f.read()
    module_name = os.path.basename(args.source)
    test_name = os.path.basename(args.tests)
    started = time.time()

    with tempfile.TemporaryDirectory() as tmp:
        shutil.copyfile(args.tests, os.path.join(tmp, test_name))
        target = os.path.join(tmp, module_name)

        print("Step 1: your tests on the original code ...")
        shutil.copyfile(args.source, target)
        ok, summary = run_tests(tmp, test_name)
        print("        " + summary)
        if not ok:
            print()
            print("STOP. Your tests must all pass on the original code first.")
            print("A mutant is killed when a test fails. If a test already fails,")
            print("the result would mean nothing. Make the tests green, then run again.")
            return 1

        mutants = find_mutants(source)
        print("Step 2: your tests on %d mutants ..." % len(mutants))
        print()
        print("%-4s %-5s %-11s %-9s %s" % ("ID", "Line", "Change", "Result", "Mutated line"))
        print("-" * 78)
        killed = 0
        survivors = []
        for number, mutant in enumerate(mutants, start=1):
            mutated, _, new_line = apply_mutant(source, mutant)
            with open(target, "w", encoding="utf-8") as f:
                f.write(mutated)
            ok, _ = run_tests(tmp, test_name)
            name = "M%02d" % number
            change = "%s -> %s" % (mutant[2], mutant[3])
            if ok:
                survivors.append("%s (line %d)" % (name, mutant[0]))
                result = "SURVIVED"
            else:
                killed += 1
                result = "killed"
            print("%-4s %-5d %-11s %-9s %s" % (name, mutant[0], change, result, new_line))

    total = len(mutants)
    score = 100.0 * killed / total if total else 0.0
    print("-" * 78)
    print("Killed %d of %d mutants.  Mutation score = %d / %d = %.0f %%" % (killed, total, killed, total, score))
    print("Survivors: " + (", ".join(survivors) if survivors else "none"))
    print("Time: %.1f s" % (time.time() - started))
    return 0


if __name__ == "__main__":
    sys.exit(main())
