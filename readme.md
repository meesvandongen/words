# Words

A project to create a word list for usage in various applications, such as games, educational tools, and more.

- Words are extracted from sources such as news articles.
- The articles datasets are in the feather format.
- Words are processed using https://github.com/explosion/spaCy
- The project uses Python for data processing.
- The words are stored in a SQLite database.
- Words are categorized by their part of speech (POS).
- The word frequency is also recorded.
- The word frequency is per year.
- The program is created as Jupyter Notebooks.
- Python is installed using uv.

## Project Structure

This project contains two main Jupyter notebooks:

1. **`dataset_documentation.ipynb`** - Documents the structure, format, and contents of the NOS Dutch news articles dataset
2. **`word_extraction_strategy.ipynb`** - Implements the complete pipeline for extracting and processing words from the dataset

Each notebook is self-contained and can be run independently.

## Dataset Documentation: NOS_NL_articles_2015_mar_2025.feather

### Overview
The `NOS_NL_articles_2015_mar_2025.feather` file contains Dutch news articles from NOS (Nederlandse Omroep Stichting) spanning from January 1, 2015 to March 31, 2025. The dataset is stored in Apache Feather format for efficient data processing and analysis.

### File Statistics
- **Total Articles**: 295,259
- **File Size**: 503.98 MB (on disk)
- **Memory Usage**: ~1.36 GB (when loaded)
- **Format**: Apache Feather (.feather)
- **Language**: Dutch (Nederlandse)
- **Time Period**: 2015-01-01 to 2025-03-31
- **Source**: NOS (Nederlandse Omroep Stichting)

### Column Schema
The dataset contains 11 columns with the following structure:

| Column | Data Type | Description | Non-Null Count | Sample Values |
|--------|-----------|-------------|----------------|---------------|
| `channel` | object | Source channel identifier | 295,259 (100%) | "nos" |
| `url` | object | Article URL | 295,259 (100%) | "https://nos.nl/artikel/..." |
| `type` | object | Content type | 295,259 (100%) | "article" |
| `title` | object | Article headline | 295,259 (100%) | "Euro nu ook in Litouwen" |
| `keywords` | object | Article keywords/tags | 279,786 (94.8%) | "eurozone", "EU-voorzitter" |
| `section` | object | News section category | 289,735 (98.1%) | "Economie", "Binnenland", "Buitenland" |
| `description` | object | Article summary/excerpt | 295,259 (100%) | Short article summaries |
| `published_time` | datetime64[ns] | Publication timestamp | 295,259 (100%) | "2015-01-01 00:32:52" |
| `modified_time` | object | Last modification time | 295,259 (100%) | "2015-01-01 00:32:52" |
| `image` | object | Associated image URL | 295,158 (99.97%) | "https://cdn.nos.nl/image/..." |
| `content` | object | Full article content (HTML) | 295,259 (100%) | HTML formatted article text |

### Content Characteristics

#### Text Length Statistics
- **Title**: Average 58.6 characters (8.4 words), ranging 1-248 characters
- **Description**: Average 125.8 characters (20.0 words), ranging 1-356 characters  
- **Content**: Average 2,586.6 characters (380.4 words), ranging 29-153,229 characters
- **Keywords**: Average 27.2 characters when present, ranging 1-469 characters

#### Temporal Distribution
The dataset shows the following distribution of articles per year:
- **2015**: 42,667 articles
- **2016**: 41,781 articles  
- **2017**: 34,818 articles
- **2018**: 30,877 articles
- **2019**: 27,034 articles
- **2020**: 23,736 articles
- **2021**: 24,064 articles
- **2022**: 21,756 articles
- **2023**: 21,155 articles
- **2024**: 21,816 articles
- **2025**: 5,555 articles (through March)

#### Content Format
- **Content Field**: Contains HTML-formatted article text with tags like `<h1>`, `<p>`, etc.
- **URLs**: Follow the pattern `https://nos.nl/artikel/{article_id}-{title-slug}` or `https://nos.nl/l/{id}`
- **Images**: CDN-hosted images at `https://cdn.nos.nl/image/...` with standardized dimensions
- **Sections**: Include categories like "Economie", "Binnenland", "Buitenland", "Politiek", "Sport", etc.

### Data Quality
- **Completeness**: Very high data quality with minimal missing values
- **Duplicates**: No duplicate rows found
- **Consistency**: Standardized URL patterns, consistent datetime formatting
- **Coverage**: Comprehensive coverage of Dutch news topics over 10+ years

### Usage Notes
- Load using `pandas.read_feather()` with `pyarrow` backend for optimal performance
- Content contains HTML markup that may need parsing for text analysis
- Published and modified times are in UTC format
- Keywords field has ~5% missing values
- Image URLs are CDN-hosted and may require validation for availability

This dataset serves as an excellent source for Dutch language processing, news analysis, and word frequency studies spanning a decade of contemporary Dutch journalism.
