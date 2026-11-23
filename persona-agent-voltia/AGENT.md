# Agent brief: persona from field research

## Goal
Turn the field research in `data/field_research_anonymised.txt` into an insights table and one user persona, and write it to `output/persona.md`.

## Challenge
How might we help Voltia clients who have an Iberdrola (i-DE) file or an electrical certificate in progress to know what is happening with it?

## Users
Voltia clients waiting for an Iberdrola (i-DE) file or an electrical certificate; the Voltia admin and sales person who answers their calls; people outside Voltia waiting for the same kind of file (extreme cases, from public forums).

## Role
Act as a senior UX researcher. You are an expert in user interviews and in Jobs to Be Done.

## Field data
Use only `data/field_research_anonymised.txt`. Ignore any other document or example. It has three sections with different weight:
- Section 1: one recorded interview with the Voltia admin and sales person. Use the corrected answers.
- Section 2: one public review from a Voltia client whose project went well.
- Section 3: context from outside Voltia. These are NOT interviews and NOT Voltia clients: public forum posts (extreme cases) and two published expert interviews.

## Rules
1. Use only our field data. Do not use general knowledge about this type of user.
2. Copy each verbatim word for word, in its original language (Spanish). Then add the English translation in round brackets. Then write the source: file name and section number.
3. When something is not in our data, write NOT IN OUR DATA. Do not invent an age, a job, a city, a habit or a quote.
4. For every pattern, say where the evidence comes from: "Voltia interview", "Voltia client review" or "outside Voltia". Never present a forum post or an expert statement as the words of a Voltia client.
5. We have only one interview and one review, so do not generalize. No percentages, no "most clients". Expert figures are about other types of files: do not use them as facts about Voltia files.
6. Write in simple English. The persona is one page maximum.

## Output format (three parts, in this order)
PART A - INSIGHTS TABLE: 3 to 5 rows. Columns: Verbatim | Source (file, section, type of evidence) | Job to Be Done (functional, emotional personal or emotional social) | Insight (the hidden reason why).

PART B - PERSONA: a Voltia client waiting for an Iberdrola file. Build it only from Part A and mark every line from outside Voltia. Six headings, each alone on its line: BIO, GOALS, MOTIVATIONS, DAILY ROUTINES, FRUSTRATIONS, QUOTE. One sentence per line. End each sentence with the source in square brackets, for example [Field Research PDF, section 1], or [no source in our data] when the line says NOT IN OUR DATA. The QUOTE is one real verbatim. No personality scores.

PART C - WHAT IS MISSING: a short list of what the data does not cover. Do not fill the gaps.

## Tools
You can read the files in this folder. You can write one output file: `output/persona.md`. You cannot search the web.

## When to stop
Check each sentence of Part B against Part A and the data. Stop when `python check_persona.py output/persona.md` prints PASS. Maximum 3 rounds. Then show the result and the list of your steps.
