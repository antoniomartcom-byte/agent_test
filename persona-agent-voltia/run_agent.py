#!/usr/bin/env python3
"""Runs the persona agent with Claude Code in headless mode.
The agent reads AGENT.md and the data, writes output/persona.md, and this script
runs check_persona.py. If it fails, the agent gets the list of problems and tries
again. Maximum 3 rounds. No web access: only Read and Write tools are allowed.
Requires: python 3.9+ and Claude Code (`claude`) logged in once."""
import subprocess, sys, datetime, pathlib
from check_persona import check

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "output" / "persona.md"
DATA = ROOT / "data" / "field_research_anonymised.txt"
LOG = ROOT / "output" / "steps.log"
MAX_ROUNDS = 3

def log(msg):
    line = f"{datetime.datetime.now():%H:%M:%S} {msg}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f: f.write(line + "\n")

def ask(prompt):
    r = subprocess.run(
        ["claude", "-p", prompt, "--allowedTools", "Read,Write", "--output-format", "text"],
        cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip()

def main():
    LOG.write_text("")
    prompt = ("Read AGENT.md and follow it exactly. Read data/field_research_anonymised.txt. "
              "Write the result to output/persona.md. Do not use any other file or the web.")
    for n in range(1, MAX_ROUNDS + 1):
        log(f"round {n}: asking the agent")
        reply = ask(prompt)
        log(f"round {n}: agent says: {reply[:200]!r}")
        if not OUT.exists():
            prompt = "output/persona.md does not exist. Write it as AGENT.md says."
            log(f"round {n}: no output file"); continue
        problems = check(str(OUT), str(DATA))
        if not problems:
            log(f"round {n}: checker PASS. Stopped."); print("RESULT: PASS"); return 0
        log(f"round {n}: checker FAIL, {len(problems)} problems")
        prompt = ("The checker found these problems in output/persona.md. Fix exactly these, "
                  "change nothing else, and rewrite the file:\n- " + "\n- ".join(problems))
    log("maximum rounds reached. Stopped."); print("RESULT: FAIL"); return 1

if __name__ == "__main__":
    sys.exit(main())
