---
title: 'Exercise sheet 1'
author:
- Matthias Müller
- Ruben Hutter
---

# Task 2

The output of `SELECT version();` is:

```
PostgreSQL 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu,
compiled by gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, 64-bit
```

# Task 3

The DB contains chess data.\

The query:

```sql
SELECT COUNT(*)
FROM games
WHERE result = '1-0'
```

returns the number of games (7'753'413) that ended with a white victory.

# Task 4

The query:

```sql
SELECT EXTRACT(MONTH FROM game_start), COUNT(*)
FROM games
GROUP BY EXTRACT(MONTH FROM game_start)
```

returns the number of games played in each month.

Output:

```
1	4770357
2	5015361
3	5801234
```

# Task 5

## Q:

What are the advantages and disadvantages of using databases to manage data
compared to file-based approaches? (2 advantages and 2 disadvantages as bullet
points)

## A: 

**Advantages**:

- Data consistency: Databases ensure that data is consistent and that it follows the defined constraints.
- Data integrity: Databases provide mechanisms to enforce data integrity, e.g., foreign key constraints.

**Disadvantages**:

- Complexity: Databases are more complex to set up and maintain compared to file-based approaches.
- Performance: Databases can be slower than file-based approaches for simple read/write operations.

## Q:

What is the link to the official documentation for the `version()` function used in
the first task and to which category of functions does it belong?

## A:

The link to the official documentation for the `version()` function is [here](https://www.postgresql.org/docs/16/functions-info.html#FUNCTIONS-INFO-SESSION). The `version()` function belongs to the category of Session Information Functions.
