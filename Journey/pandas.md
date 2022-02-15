# Pandas

## Use Cases

### Create a dummy dataframe for practice 
```
import pandas as pd
df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
```

### Create new column based on other column

Create one clolumn:
```
df["new_col"] = df.apply(lambda row: func(row["col"]), axis=1)

def func(number):
  return new_number or np.nan
```

Create multiple clolumns:
```df[["new_col1", "new_col2"]] = df.apply(lambda row: [1, 2], result_type='expand', axis=1)```


### Sync 

Align df's index to original_df's
```
clock = origin_df.timestamp.unique()
df = df.reindex(clock, method="nearest")
```

### Interpolation on timestamp index
```
df.reindex(new_index).interpolate(method="index")
```

### Join two dataframes
```
df_1 = df_1.merge(df_1.reset_index(), how="inner", on="col1")
```
```
df = pd.merge(df_1, df_2, how="inner", left_on=['timestamp','objectName'])
```
