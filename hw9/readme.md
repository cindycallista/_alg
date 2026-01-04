# Minimum Edit Distance Example

Minimum edit distance measures the minimum number of operations needed to convert one string into another.  
Operations allowed: **insert**, **delete**, **replace**.

## Example: "kitten" → "sitting"

### DP Table

|   |   | s | i | t | t | i | n | g |
|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| k | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| i | 2 | 2 | 1 | 2 | 3 | 4 | 5 | 6 |
| t | 3 | 3 | 2 | 1 | 2 | 3 | 4 | 5 |
| t | 4 | 4 | 3 | 2 | 1 | 2 | 3 | 4 |
| e | 5 | 5 | 4 | 3 | 2 | 2 | 3 | 4 |
| n | 6 | 6 | 5 | 4 | 3 | 3 | 2 | 3 |

### Minimum Edit Distance

**3**

### Step-by-Step Changes

1. `kitten` → `sitten` (replace 'k' with 's')  
2. `sitten` → `sittin` (replace 'e' with 'i')  
3. `sittin` → `sitting` (insert 'g')  
