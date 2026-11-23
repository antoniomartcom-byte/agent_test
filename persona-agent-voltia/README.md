# Persona agent · Voltia challenge

An agent that turns field research into an insights table and a user persona, and checks its own work until a deterministic checker passes.

Built for Creativity and Innovation (EDEM), Assessment 2, Level 3 (the agent).

**Challenge:** How might we help Voltia clients who have an Iberdrola (i-DE) file or an electrical certificate in progress to know what is happening with it?

## How the agent works

1. **Goal and rules:** `AGENT.md` (role, challenge, users, rules, output format, tools, when to stop).
2. **Data:** `data/field_research_anonymised.txt`. No personal names. It is the only source.
3. **Tools:** the agent can read files in this folder and write one file, `output/persona.md`. No web access.
4. **Loop:** the agent writes the persona, `check_persona.py` checks it, and the agent fixes exactly what failed. Maximum 3 rounds (`run_agent.py`).
5. **Record:** every round is written in `output/steps.log`.

## The checker (no model inside)

`check_persona.py` passes only if:
- Parts A, B and C are present, in order;
- Part B has the six headings and every line ends with a source in square brackets, or says NOT IN OUR DATA;
- every Spanish verbatim «...» appears in the data, word for word;
- there are no percentages, no "most clients" and no links;
- Part A has 3 to 5 rows and Part B has at most 600 words.

## How the teacher can test it

**Option 1, no install (30 seconds).** Check the result that is already here:

```bash
python check_persona.py output/persona.md
```
Expected: `PASS`. Then change one verbatim in `output/persona.md` and run it again: it prints `FAIL` and says which one is not in the data.

**Option 2, run the agent.** Needs Python 3.9+ and [Claude Code](https://code.claude.com) logged in once with `claude`:

```bash
python run_agent.py
```
The agent rewrites `output/persona.md`, the checker runs after each round, and the steps go to `output/steps.log`.

**Option 3, any other agent tool.** Give it `AGENT.md` and the data file, allow it to read files and write one file, and forbid web access.

## Limits

- One internal interview and one review: the persona is a set of hypotheses, not a finding.
- Forum posts and expert interviews are context, not Voltia clients. The persona marks them as "outside Voltia".
- The checker proves that quotes and sources are consistent with the data. It does not prove that an insight is right.
