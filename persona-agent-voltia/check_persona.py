#!/usr/bin/env python3
"""Deterministic checker for the persona agent. No model inside.
Usage: python check_persona.py output/persona.md [data/field_research_anonymised.txt]
Exit code 0 = PASS, 1 = FAIL."""
import re, sys

HEADINGS = ["BIO", "GOALS", "MOTIVATIONS", "DAILY ROUTINES", "FRUSTRATIONS", "QUOTE"]

def norm(s):
    s = s.replace(" ", " ").lower()
    return re.sub(r"\s+", " ", s).strip()

def check(out_path, data_path):
    out = open(out_path, encoding="utf-8").read()
    data = norm(open(data_path, encoding="utf-8").read())
    problems = []

    # 1. structure
    ia, ib, ic = (out.find(k) for k in ("PART A", "PART B", "PART C"))
    if min(ia, ib, ic) < 0 or not ia < ib < ic:
        problems.append("Parts A, B and C must be present, in this order.")
        return problems
    part_a, part_b, part_c = out[ia:ib], out[ib:ic], out[ic:]

    # 2. Part B headings, in order, each alone on a line
    lines = [l.strip() for l in part_b.splitlines()]
    pos = -1
    for h in HEADINGS:
        if h not in lines:
            problems.append(f"Part B: heading {h} is missing.")
        else:
            i = lines.index(h)
            if i < pos:
                problems.append(f"Part B: heading {h} is out of order.")
            pos = i

    # 3. every sentence line of Part B ends with a source in square brackets
    for l in lines[1:]:
        if not l or l in HEADINGS or l.startswith("PART B"):
            continue
        if not re.search(r"\[[^\[\]]+\]\s*$", l):
            problems.append(f"Part B: line without a source in brackets: {l[:70]}")
        if "NOT IN OUR DATA" in l and "no source in our data" not in l.lower():
            problems.append(f"Part B: a NOT IN OUR DATA line should end with [no source in our data]: {l[:70]}")

    # 4. every Spanish verbatim «...» must be in the data, word for word
    for v in re.findall(r"«([^»]+)»", out):
        for frag in re.split(r"\[\.\.\.\]", v):
            frag = norm(frag)
            if len(frag) > 3 and frag not in data:
                problems.append(f"Verbatim not found in the data: «{frag[:70]}»")

    # 5. no percentages, no generalizations, no web
    if re.search(r"\d+\s?%", out):
        problems.append("A percentage appears. Do not use percentages.")
    for bad in ("most clients", "all clients", "http://", "https://"):
        if bad in out.lower():
            problems.append(f"Forbidden text: {bad}")

    # 6. Part A has 3 to 5 numbered rows
    rows = re.findall(r"^\s*\d+\.\s", part_a, flags=re.M)
    if not 3 <= len(rows) <= 5:
        problems.append(f"Part A must have 3 to 5 rows, it has {len(rows)}.")

    # 7. persona is one page: 600 words or fewer in Part B
    words = len(part_b.split())
    if words > 600:
        problems.append(f"Part B has {words} words. Maximum 600.")

    # 8. Part C is not empty
    if len(part_c.split()) < 8:
        problems.append("Part C (what is missing) is empty.")
    return problems

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "output/persona.md"
    data = sys.argv[2] if len(sys.argv) > 2 else "data/field_research_anonymised.txt"
    p = check(out, data)
    if p:
        print("FAIL")
        for x in p: print(" -", x)
        sys.exit(1)
    print("PASS")
