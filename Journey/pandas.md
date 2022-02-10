# Pandas

## Use Cases

### Create a dummy dataframe for practice 
```df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})```

### Create new column based on other column

Create one clolumn:
```
df["new_col"] = df.apply(lambda row: func(row["col"]), axis=1)

def func(number):
  return new_number or np.nan
```

Create multiple clolumns:
```df[["new_col1", "new_col2"]] = df.apply(lambda row: [1, 2], result_type='expand', axis=1)```


