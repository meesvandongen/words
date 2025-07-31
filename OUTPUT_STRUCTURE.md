# Output Directory Structure

This project uses a git-ignored `output/` directory to store all generated files from the word extraction pipeline.

## Directory Structure

```
output/
├── words_database.sqlite          # Main production database
├── test_words.sqlite              # Test database for development
├── test_dutch_words.sqlite        # Test database with sample processing
├── exports/                       # Production word list exports
│   ├── all_words.txt             # Complete word list
│   ├── common_words.txt          # Common words (frequency >= 10)
│   ├── noun_words.txt            # Nouns only
│   ├── verb_words.txt            # Verbs only
│   ├── adjective_words.txt       # Adjectives only
│   ├── adverb_words.txt          # Adverbs only
│   ├── words_full_data.csv       # Complete dataset with metadata
│   └── game_words.txt            # Game-friendly words (4-8 letters)
└── test_exports/                  # Test exports for development
    └── (same structure as exports/)
```

## Benefits

1. **Git-ignored**: All generated files are ignored by git, keeping the repository clean
2. **Organized**: Clear separation between databases and exports
3. **Flexible**: Easy to delete and regenerate all outputs without affecting source code
4. **Portable**: Can be easily backed up or moved separately from the codebase

## Usage

All functions in the word extraction notebooks now default to using the `output/` directory. The directory is automatically created when needed.

To run the full processing pipeline:
1. Set `RUN_FULL_PROCESSING = True` in the notebook
2. Run the processing cell
3. All outputs will be saved to `output/`

## Cleaning Up

To clean all generated files:
```bash
rm -rf output/
```

The next run will recreate the directory structure automatically.
