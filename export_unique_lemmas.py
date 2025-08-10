import os, sqlite3

# Use the high frequency export database instead of the full words database
SOURCE_DB = 'output/high_frequency_words.sqlite'
OUT_TXT = 'output/exports/unique_lemmas_by_frequency.txt'

os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)

if not os.path.exists(SOURCE_DB):
    raise SystemExit(f'Source DB not found: {SOURCE_DB} (run the high frequency export notebook first)')

with sqlite3.connect(SOURCE_DB) as conn:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT lemma, SUM(total_frequency) AS agg_freq
        FROM words
        GROUP BY lemma
        ORDER BY agg_freq DESC, lemma
        """
    )
    # Fetch all rows; could stream if needed
    rows = cur.fetchall()

lemmas = [r[0] for r in rows]

with open(OUT_TXT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lemmas))

print(f'Exported {len(lemmas)} lemmas to {OUT_TXT}')
