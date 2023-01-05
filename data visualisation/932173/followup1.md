---
follows: coursework
---

# Distribution of Records in Different Time Periods

{(aim|} This combination of a map and a bar chart with an added selector, helps the user to get a better understanding of the distribution of the recorded civilizations(location wise and also feature type wise) in different time periods. The user can compare and see where most people were settled in any time period and what sort of locations were used and buildings were bulit in this specific time period. This is very helpful to see any type of immigration that's happened at any time. Users can go back and forth with the time periods using the drop down menu and observe different information. Tooltips are also used in the map to observe the feature type of any point on the map. It can be gathered from the map that the first civilizations were formed in Greece and Italy and spreaded to nearby locations quickly.
{|aim)}

###### Because of the big amount of data (even with filtering out unused columns), this visualization wouldn't load in visual studio where it only took couple of seconds in jupyter. So I decided to include pictures instead of vega-lite code.

```python {l}
map =  alt.topo_feature(data.world_110m.url, 'countries')
data_vis2 = locations_[['reprLong','reprLat','featureType','timePeriodsKeys']]
data_vis2_ = sub_locations[['featureType','timePeriodsKeys']]
input_dropdown = alt.binding_select(options=['classical,hellenistic-republican,roman','hellenistic-republican',
                                             'hellenistic-republican,roman',
                                             'hellenistic-republican,roman,late-antique',
                                             'roman','roman,late-antique','late-antique','modern'], name = 'Time Period')
selection = alt.selection_single(fields=['timePeriodsKeys'], bind=input_dropdown)
color1 = alt.Color('featureType',
            sort=alt.EncodingSortField('count', order='descending'))
main= alt.layer(
    alt.Chart(map).mark_geoshape(
        fill='lightgray',
        stroke='white',
        strokeWidth = 0.5
    ),
    alt.Chart(data_vis2).mark_circle().encode(
        longitude='reprLong:Q',
        latitude='reprLat:Q',
        size=alt.value(5),
        tooltip='featureType',
        color = alt.value('black')
    ).add_selection(
    selection
).transform_filter(
    selection)
).properties(
    width=400,
    height=220
).project(
    type = "mercator",
    scale = 600,
    translate = [10,650]
).properties(
    width=500,
    height=320
)
bar3 = alt.Chart(data_vis2_).mark_bar().encode(
    y='count()',
    x='featureType',
    color = color1
).transform_filter(
    selection
).interactive()

main & bar3
```

![](2021-03-29-21-14-54.png)

![](2021-03-29-21-16-37.png)

{(vistype|}Linked map and bar chart with a drop down selector menu
{|vistype)}

{(vismapping|}

#### Map:

latitude
: latitude of location

longitude
: longitude of location

colour
: black (to prevent confusion with bar chart colours)

tooltips
: featureType category

#### Bar Chart:

x positons
: featureType category

colour
: featureType category

length
: count of records with this specific feature type

{|vismapping)}

{(dataprep|}

• Data were aggregated by category to generate counts
• limited columns were selected to improve the efficiency
• 'unknown' and 'settlement' types were removed becase of being an being too big and also not adding anything valuable to visualizations
• less popular feature types were removed to make the visualization more clear
• less popular feature types were removed to make the visualization more clear

{|dataprep)}

{(limitations|} This map only focuses on the most important part of the maps and may be not ideal for user trying to evaluate the distruibution though the whole world. The user can't really see the specific feature on the map unless using the tooltip. an improvement can be making multiple maps of different areas and also including an option to colour the points based on their category. however I decided not to include this in my map because it would be dominated by unknwon category. Removing unknown category wasn't something I opted for neither because the puropose of the map should be the distribution opf all the points not specific ones
{|limitations)}
