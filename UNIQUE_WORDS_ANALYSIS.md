# Unique Words Per Year Analysis

## Overview

The `unique_words_per_year.ipynb` notebook implements a statistical analysis to identify words that are used **relatively more** in specific years compared to their baseline usage across the entire corpus. This analysis is crucial for understanding temporal language patterns and identifying words that serve as markers for specific time periods.

## Methodology

### 1. Relative Frequency Analysis
- **Raw frequencies** are normalized by total word count per year to account for varying article volumes
- **Relative frequency** = Word frequency in year / Total words in year
- This removes bias from years with more or fewer articles

### 2. Statistical Significance Testing
- **Z-score calculation**: Measures how many standard deviations a word's yearly frequency is from its average
- **Threshold**: Words with Z-score ≥ 2.0 are considered statistically significant (2+ standard deviations above mean)
- **Lift calculation**: Ratio of observed frequency to expected frequency

### 3. Temporal Specificity Measurement
- **Concentration metric**: How focused a word's usage is in specific years
- **Temporal specificity** = 1 / Number of unique years with significant spikes
- Higher values indicate words that are more concentrated in specific time periods

## Key Features

### Bias Correction
- ✅ **Volume bias**: Accounts for different article counts per year
- ✅ **Baseline comparison**: Each word is compared to its own historical average
- ✅ **Statistical significance**: Only reports truly anomalous patterns

### Comprehensive Analysis
- **Word-level statistics**: Total usage, temporal patterns, POS categories
- **Year-level summaries**: Unique words count per year, average significance
- **Trend identification**: Growing, declining, or spike-based patterns

### Multiple Output Formats
- **CSV exports**: Complete datasets for further analysis
- **Text lists**: Simple word lists per year for quick reference
- **Visualizations**: Temporal patterns and trend charts
- **Summary reports**: Key findings and methodology documentation

## Expected Results

### Types of Unique Words Identified

1. **Event-driven words**: Related to specific news events (e.g., elections, disasters, policy changes)
2. **Seasonal terms**: Words with recurring yearly patterns
3. **Emerging vocabulary**: New terms entering common usage
4. **Historical markers**: Words that characterize specific time periods

### Sample Use Cases

- **Historical analysis**: Understanding how language reflects current events
- **Content categorization**: Automatically tagging content by time period
- **Trend detection**: Early identification of emerging terminology
- **Research applications**: Supporting linguistic and sociological studies

## Technical Requirements

### Dependencies
```python
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

### Prerequisites
1. **Database**: Must run `word_extraction_strategy.ipynb` first to generate the SQLite database
2. **Python packages**: pandas, numpy, matplotlib, seaborn, scipy
3. **Memory**: Moderate requirements for analysis (varies with database size)

### Database Schema Requirements
The notebook expects these tables in the SQLite database:

```sql
-- Core word information
words (
    id INTEGER PRIMARY KEY,
    word TEXT,
    lemma TEXT,
    pos_category TEXT,
    total_frequency INTEGER
)

-- Yearly frequency data
word_frequencies (
    word_id INTEGER,
    year INTEGER,
    frequency INTEGER
)
```

## Output Structure

### Generated Files
```
output/unique_words_analysis/
├── unique_words_complete.csv           # Full dataset
├── top_unique_words_per_year.csv      # Top words per year
├── word_temporal_statistics.csv       # Word-level statistics
├── yearly_summary.csv                 # Year-level summaries
├── analysis_summary.txt               # Key findings report
└── word_lists_by_year/                # Simple text lists
    ├── unique_words_2015.txt
    ├── unique_words_2016.txt
    └── ...

output/visualizations/
├── temporal_overview.png              # Overview charts
└── top_words_timeline.png             # Detailed timelines
```

### Key Metrics in Output

- **Z-score**: Statistical significance of the frequency spike
- **Relative frequency**: Normalized frequency accounting for yearly totals
- **Lift**: Ratio to expected frequency (observed/expected)
- **Temporal specificity**: How concentrated the word's usage is temporally

## Validation

The analysis includes built-in validation through:

1. **Test script** (`test_unique_words_analysis.py`): Demonstrates the methodology with synthetic data
2. **Statistical checks**: Ensures Z-score calculations are meaningful
3. **Data quality filters**: Minimum frequency thresholds to avoid noise
4. **Cross-validation**: Multiple metrics confirm temporal uniqueness

## Interpretation Guidelines

### Z-Score Interpretation
- **Z ≥ 2.0**: Statistically significant (95% confidence)
- **Z ≥ 3.0**: Highly significant (99.7% confidence)
- **Z ≥ 4.0**: Extremely significant (rare events)

### Temporal Specificity
- **High (> 0.5)**: Word usage concentrated in 1-2 years
- **Medium (0.2-0.5)**: Usage spread across 2-5 years  
- **Low (< 0.2)**: Usage spread across many years

## Limitations and Considerations

1. **Minimum frequency**: Analysis focuses on words with reasonable frequency to avoid statistical noise
2. **Corpus bias**: Results reflect the news corpus characteristics and editorial decisions
3. **Language evolution**: Natural language change may create apparent "unique" patterns
4. **Event correlation**: Temporal spikes often correlate with real-world events covered in news

## Future Enhancements

- **Semantic clustering**: Group related unique words by topic
- **Cross-correlation**: Identify words that spike together
- **Predictive modeling**: Forecast emerging word trends
- **Multi-language support**: Extend analysis to other language corpora

This analysis provides a robust foundation for understanding temporal language patterns in the Dutch news corpus and can be adapted for other text collections with temporal metadata.