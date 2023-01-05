---
elm:
  dependencies:
    gicentre/elm-vegalite: latest

narrative-schemas:
  - coursework
---

Author: Mohammad Hadi Jalali Lak (932173)

# Ancient civilizations

```python {l=hidden}
import pandas as pd
import altair as alt
import numpy as np
```

```python {l=hidden}
locations = pd.read_csv("pleiades-locations-latest.csv")
names = pd.read_csv("pleiades-names-latest.csv")
places = pd.read_csv("pleiades-places-latest.csv")
alt.data_transformers.disable_max_rows()
```

## Getting started

Looking at the CSV and [documentation](http://atlantides.org/downloads/pleiades/dumps/README.txt), we decide that maybe we'll start with a simple bar chart/histogram.

{(aim|}
This chart shows that certain categories occur much more frequently than others and that
some data processing is needed to split the `featureType` column up by the delimeter.
Many locations have multiple types.
{|aim)}

```elm {v}
histo : Spec
histo =
  let
    --trans = transform
    enc =
      encoding
        << position Y [ pName "featureType"]
        << position X [ pAggregate opCount ]
  in
  toVegaLite [ locs, enc [], bar [] ]
```

{(vistype|}
bar chart
{|vistype)}

{(vismapping|}

**Note**: this should be a list of some type (here I'm using a dictionary list)

y position
: featureType category

length
: count of location

{|vismapping)}

{(dataprep|}
Data were aggregated by category to generate counts
{|dataprep)}

{(limitations|}
This is a very simple visualization and it's not clear what it yields.
{|limitations)}
