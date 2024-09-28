# Exercise 1

## Task 2

The output of `SELECT version();` is:

```
PostgreSQL 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu,
compiled by gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, 64-bit
```

## Task 3

The DB contains chess data.\

The query:

```sql
SELECT COUNT(*)
FROM games
WHERE result = '1-0'
```

returns the number of games (7'753'413) that ended with a white victory.

## Task 4

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

