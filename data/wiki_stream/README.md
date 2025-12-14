
# Wikipedia Stream Processing Output Structure

## Selected Entities
- MOVIE: O La La (ID: tt8458418)
- ACTOR: Kenjirô Ishimaru (ID: nm0411100)
- GENRE: Comedy (ID: genre_comedy)
- DIRECTOR: Sripad Pai (ID: director_Sripad_Pai)
- MOVIE: The Shawshank Redemption (ID: tt0111161)

## Metrics Storage
**Location**: `data/wiki_stream/metrics/`

**Format**: JSON files (one file per collection session)

**Schema**:
- total_events: Integer - Total number of events collected
- events_by_type: Dict - Count of events grouped by type
- events_by_entity: Dict - Count of events grouped by tracked entity
- events_by_user: Dict - Count of events grouped by Wikipedia user
- bot_edits: Integer - Number of bot edits
- human_edits: Integer - Number of human edits
- change_sizes: List[Integer] - List of change sizes in bytes
- summary: Dict - Summary statistics (unique entities, users, ratios, etc.)

## Alerts Storage (Separate File/Database)
**Location**: `data/wiki_stream/alerts/`

**Format**: JSON files (one file per collection session, separate from metrics)

**Schema**:
- timestamp: String - ISO timestamp of alert
- entity: String - Entity name that triggered alert
- alert_type: String - Type of alert (VANDALISM, DELETION, BLOCK, REVERT, PROTECTION, LARGE_DELETION)
- user: String - Wikipedia username
- details: String - Alert details/comment
- severity: String - Severity level (HIGH, MEDIUM, LOW)

## Metrics Calculated
1. **Edit count per entity**: How many edits per tracked entity
2. **Edit frequency over time**: Timestamps of events
3. **Most active editors**: Users grouped by edit count
4. **Change size distribution**: Distribution of page size changes
5. **Bot vs human edit ratio**: Ratio of automated vs manual edits

## Alert Conditions
1. Edit comments containing alert keywords: vandalism, deletion, block, revert, protection
2. Large deletions: More than 1000 bytes removed in a single edit
3. Anonymous users making significant changes: (future enhancement)

## Implementation Notes
- Uses Wikipedia EventStreams API: https://stream.wikimedia.org/v2/stream/recentchange
- Events are filtered to match tracked entities by title matching
- Metrics and alerts are stored in separate files as per requirements
- In production, this would run continuously as a streaming job
