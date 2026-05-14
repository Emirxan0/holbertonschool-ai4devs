# Data Model - Smart Task Manager

## Entity 1: Task

The core entity representing a work item managed by the user.

| Field       | Type     | Constraints                        | Description                          |
|-------------|----------|------------------------------------|--------------------------------------|
| id          | INTEGER  | PRIMARY KEY, AUTOINCREMENT         | Unique task identifier               |
| title       | VARCHAR  | NOT NULL, MAX 200 chars            | Short task title                     |
| description | TEXT     | NULLABLE                           | Detailed task description            |
| status      | VARCHAR  | NOT NULL, DEFAULT 'todo'           | One of: todo, in_progress, done      |
| priority    | VARCHAR  | NOT NULL, DEFAULT 'medium'         | One of: high, medium, low            |
| due_date    | DATE     | NULLABLE                           | Task deadline                        |
| created_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP| Timestamp when task was created      |
| updated_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP| Timestamp of last update             |
| category_id | INTEGER  | FOREIGN KEY → Category.id          | Optional category assignment         |
| tag_id      | INTEGER  | FOREIGN KEY → Tag.id (via join)    | Optional tag assignment              |

---

## Entity 2: Category

Groups tasks into named collections for better organization.

| Field       | Type     | Constraints                        | Description                          |
|-------------|----------|------------------------------------|--------------------------------------|
| id          | INTEGER  | PRIMARY KEY, AUTOINCREMENT         | Unique category identifier           |
| name        | VARCHAR  | NOT NULL, UNIQUE, MAX 100 chars    | Category name (e.g. "Work", "Study") |
| color       | VARCHAR  | NOT NULL, DEFAULT '#6366f1'        | Hex color code for UI display        |
| created_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP| Timestamp when category was created  |

---

## Entity 3: Tag

Flexible labels that can be attached to tasks for cross-category filtering.

| Field       | Type     | Constraints                        | Description                          |
|-------------|----------|------------------------------------|--------------------------------------|
| id          | INTEGER  | PRIMARY KEY, AUTOINCREMENT         | Unique tag identifier                |
| name        | VARCHAR  | NOT NULL, UNIQUE, MAX 50 chars     | Tag label (e.g. "urgent", "client-a")|
| created_at  | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP| Timestamp when tag was created       |

---

## Entity 4: TaskTag (Join Table)

Many-to-many relationship between Tasks and Tags.

| Field   | Type    | Constraints                    | Description         |
|---------|---------|--------------------------------|---------------------|
| task_id | INTEGER | PRIMARY KEY, FK → Task.id      | Reference to task   |
| tag_id  | INTEGER | PRIMARY KEY, FK → Tag.id       | Reference to tag    |

---

## Entity Relationships
