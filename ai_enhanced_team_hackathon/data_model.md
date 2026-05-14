# Data Model - AI Code Snippet Manager

## Entity 1: Snippet

The core entity representing a saved code snippet.

| Field       | Type     | Constraints                         | Description                              |
|-------------|----------|-------------------------------------|------------------------------------------|
| id          | INTEGER  | PRIMARY KEY, AUTOINCREMENT          | Unique snippet identifier                |
| title       | VARCHAR  | NOT NULL, MAX 200 chars             | Short descriptive title                  |
| code        | TEXT     | NOT NULL                            | The actual code content                  |
| language    | VARCHAR  | NOT NULL, MAX 50 chars              | Programming language (e.g. Python, JS)   |
| description | TEXT     | NULLABLE                            | User-written description                 |
| ai_explanation | TEXT  | NULLABLE                            | AI-generated explanation of the code     |
| access_count| INTEGER  | NOT NULL, DEFAULT 0                 | Number of times snippet was viewed       |
| created_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp when snippet was created       |
| updated_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp of last update                 |
| collection_id | INTEGER | FOREIGN KEY → Collection.id        | Optional collection assignment           |

---

## Entity 2: Tag

Flexible labels attached to snippets for cross-filtering.

| Field      | Type     | Constraints                         | Description                              |
|------------|----------|-------------------------------------|------------------------------------------|
| id         | INTEGER  | PRIMARY KEY, AUTOINCREMENT          | Unique tag identifier                    |
| name       | VARCHAR  | NOT NULL, UNIQUE, MAX 50 chars      | Tag label (e.g. "sorting", "auth")       |
| ai_suggested | BOOLEAN | NOT NULL, DEFAULT FALSE            | Whether tag was suggested by AI          |
| created_at | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp when tag was created           |

---

## Entity 3: Collection

Groups snippets into named project-based collections.

| Field      | Type     | Constraints                         | Description                              |
|------------|----------|-------------------------------------|------------------------------------------|
| id         | INTEGER  | PRIMARY KEY, AUTOINCREMENT          | Unique collection identifier             |
| name       | VARCHAR  | NOT NULL, MAX 100 chars             | Collection name (e.g. "React Hooks")     |
| description | TEXT    | NULLABLE                            | Optional collection description          |
| created_at | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp when collection was created    |

---

## Entity 4: SnippetTag (Join Table)

Many-to-many relationship between Snippets and Tags.

| Field      | Type     | Constraints                         | Description                              |
|------------|----------|-------------------------------------|------------------------------------------|
| snippet_id | INTEGER  | PRIMARY KEY, FK → Snippet.id        | Reference to snippet                     |
| tag_id     | INTEGER  | PRIMARY KEY, FK → Tag.id            | Reference to tag                         |

---

## Entity Relationships

    Collection (1) ──────< Snippet (many)
    Snippet (many) >──────< Tag (many)  [via SnippetTag join table]

## Sample Data

### Collections
| id | name          | description                  |
|----|---------------|------------------------------|
| 1  | React Hooks   | Reusable React hook patterns |
| 2  | API Utilities | HTTP and REST helper code    |

### Snippets
| id | title              | language   | collection_id |
|----|--------------------|------------|---------------|
| 1  | useFetch hook      | JavaScript | 1             |
| 2  | Debounce function  | TypeScript | 1             |
| 3  | Retry with backoff | Python     | 2             |
