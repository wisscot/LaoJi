# Pandas

## Use Cases

### Create a new column based on another column

```
df["new_col"] = df.apply(lambda row: func(row["col"]), axis=1)

def func(number):
  return new_number or np.nan
```

