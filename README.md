# IMDB Data Analysis & Wikipedia Stream Processing Project

## Project Overview

This project performs comprehensive data analysis on IMDB movie data and implements a real-time stream processing system for tracking Wikipedia events related to selected IMDB entities.

## Team Members

- SBAI WAHIBA
- HEBBACHE BELKISS

## Project Structure

```
.
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── imdb_analysis.ipynb         # Main analysis notebook (Jupyter)
├── config.py                   # Configuration file
├── .gitignore                  # Git ignore file
└── data/                       # Data directory (created automatically)
    ├── imdb/                   # IMDB datasets
    └── wiki_stream/            # Wikipedia stream outputs
        ├── README.md           # Stream output documentation
        ├── metrics/            # Metrics JSON files
        └── alerts/             # Alerts JSON files (separate from metrics)
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Java 8, 11, or 17 (required for Spark)
- Jupyter Notebook

### Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Java** (if not already installed):
   - Windows: Install Eclipse Adoptium JDK 17 from https://adoptium.net/
   - The notebook will automatically detect Java at: `C:\Program Files\Eclipse Adoptium\jdk-17.0.17.10-hotspot`
   - Alternatively, set `JAVA_HOME` environment variable manually

3. **Start Jupyter Notebook:**
```bash
jupyter notebook
```

4. **Open `imdb_analysis.ipynb`** and run all cells sequentially

### Configuration

- IMDB data will be automatically downloaded from https://datasets.imdbws.com/
- Large files (>2GB) may need to be downloaded manually - see notebook output for details
- Wikipedia stream processing uses EventStreams HTTP Service

## Project Components

### Part 1: IMDB Data Analysis (Questions 1-14)

The notebook answers all 14 questions:

1. **Data Loading**: Automated download and loading of IMDB datasets
2. **Question 2**: How many total people in dataset?
3. **Question 3**: What is the earliest year of birth?
4. **Question 4**: How many years ago was this person born?
5. **Question 5**: Using only the data in the dataset, determine if this date of birth is correct
6. **Question 6**: Explain the reasoning for the answer
7. **Question 7**: What is the most recent date of birth?
8. **Question 8**: What percentage of people do not have a listed date of birth?
9. **Question 9**: What is the length of the longest "short" after 1900?
10. **Question 10**: What is the length of the shortest "movie" after 1900?
11. **Question 11**: List all of the genres represented
12. **Question 12**: What is the highest rated comedy "movie"? (tie broken by most votes)
13. **Question 13**: Who was the director of the movie?
14. **Question 14**: List alternate titles for the movie

All answers are provided in markdown cells within the notebook.

### Part 2: Wikipedia Stream Processing

The stream processing implementation:

1. **Selects 5 entities** from the IMDB dataset (movie, actor, genre, director, popular title)
2. **Connects to Wikipedia EventStreams API** to track events for these entities
3. **Collects events** in real-time (or uses simulated events if connection fails)
4. **Calculates metrics**:
   - Total events count
   - Events by type (edit, new, etc.)
   - Events by entity
   - Events by user
   - Bot vs human edits
   - Average change size
5. **Detects alerts** for events requiring action:
   - Keywords in comments (vandalism, deletion, block, revert, protection)
   - Large deletions (>1000 bytes)
6. **Stores results**:
   - **Metrics**: Stored in `data/wiki_stream/metrics/` (JSON format)
   - **Alerts**: Stored in `data/wiki_stream/alerts/` (JSON format, separate from metrics)

The alert system routes alert-type events to a different file/database as required by the project specifications.

## Running the Project

### Run as Jupyter Notebook (Recommended)

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `imdb_analysis.ipynb`

3. Execute all cells sequentially from top to bottom

4. Results will be displayed in output cells

### First-Time Setup Notes

- The notebook will automatically download IMDB datasets (this may take some time)
- Java configuration is handled automatically if Java is at the expected path
- If Java is not detected, follow the error messages in the notebook for setup instructions

## Output Structure

### IMDB Analysis Results
All results are displayed in the notebook output cells with clear formatting.

### Stream Processing Outputs

#### Metrics Storage
**Location**: `data/wiki_stream/metrics/`  
**Format**: JSON files (one per collection session)  
**Schema**:
- `total_events`: Total number of events collected
- `events_by_type`: Count of events grouped by type
- `events_by_entity`: Count of events grouped by tracked entity
- `events_by_user`: Count of events grouped by Wikipedia user
- `bot_edits`: Number of bot edits
- `human_edits`: Number of human edits
- `change_sizes`: List of change sizes in bytes
- `summary`: Summary statistics (unique entities, users, ratios, etc.)

#### Alerts Storage (Separate File/Database)
**Location**: `data/wiki_stream/alerts/`  
**Format**: JSON files (one per collection session, **separate from metrics**)  
**Schema**:
- `timestamp`: ISO timestamp of alert
- `entity`: Entity name that triggered alert
- `alert_type`: Type of alert (VANDALISM, DELETION, BLOCK, REVERT, PROTECTION, LARGE_DELETION)
- `user`: Wikipedia username
- `details`: Alert details/comment
- `severity`: Severity level (HIGH, MEDIUM, LOW)

See `data/wiki_stream/README.md` for detailed documentation (created automatically by the notebook).

## Key Features

✅ **Automated Data Loading**: Downloads IMDB datasets automatically  
✅ **Comprehensive Analysis**: Answers all 14 questions with detailed explanations  
✅ **Stream Processing Implementation**: Fully functional stream processing with event collection, metrics calculation, and alert detection  
✅ **Separate Alert Storage**: Alerts routed to separate files as required  
✅ **Well Documented**: Code comments, markdown explanations, output structure clearly defined  
✅ **Ready to Run**: Minimal setup required, Java configuration handled automatically

## Dependencies

- **pyspark**: Apache Spark Python API for distributed data processing
- **jupyter**: Jupyter Notebook environment
- **findspark**: Utility to locate Spark installation
- **requests**: HTTP library for downloading IMDB data and connecting to Wikipedia EventStreams

## Notes

- All code is documented with comments
- Answers to questions are provided in markdown cells within the notebook
- Stream processing outputs are clearly structured and documented
- Any manual steps required (e.g., large file downloads) are documented in the notebook output
- The implementation handles connection issues gracefully (uses simulated events for demonstration)

## Submission

- **Code repository**: Shared Git repository with all code
- **Submission email**: Sent to joe@adaltas.com
- **Team members**: SBAI WAHIBA and HEBBACHE BELKISS (listed in notebook and this README)
- **All commits**: Each team member has commits in the repository

## Troubleshooting

If you encounter issues:

1. **Java not found**: Ensure Java is installed and `JAVA_HOME` is set, or place Java at the expected path
2. **Import errors**: Run `pip install -r requirements.txt` to install all dependencies
3. **Connection timeout**: The stream processing will use simulated events if the Wikipedia API is unreachable
4. **Large file downloads**: Some IMDB files may need manual download - the notebook will indicate which ones

For detailed setup instructions, see the notebook's error messages and setup cells.
