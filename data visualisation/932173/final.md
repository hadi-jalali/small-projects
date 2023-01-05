---
follows: followup1
---

# First feature type in each location

{(aim|}With this presentation, it is possible to check the first type of civilization that was found in each of the named locations. This helps us understand when each locatins was civilized and what type of civilization it was . Using selection on the second chart we can also compare two or more location to see which one was civilized before. further information on the number of feature types in each locations is also available to observe from the second chart.
{|aim)}

```python{l}
new_locations = locations_[['id','featureType','minDate']]
new_names = names[['nameTransliterated','id','minDate']]
new = pd.merge(locations_,names,on = ['id'], how='inner')

data_vis4 = new.loc[new.groupby('nameTransliterated', sort=True)['minDate_x'].idxmin()]
multi = alt.selection_multi(fields=['nameTransliterated'])


dates = alt.Chart(data_vis4).mark_circle(size = 100).encode(
    y='nameTransliterated',
    x='minDate_x',
    color='featureType',
    tooltip = 'featureType'
).transform_filter(multi
).interactive()

counts = alt.Chart(new).mark_bar().encode(
    y='nameTransliterated',
    x='count()',
    color = alt.condition(multi, 'featureType' , alt.value('lightgrey')),
    tooltip = 'featureType'
).properties(
    selection=multi
)
dates & counts
```

```vega-lite {v interactive}
{
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "background": "white",
  "padding": 5,
  "data": [
    {"name": "selector126_store"},
    {"name": "selector125_store"},
    {
      "name": "data-fba704c7e3536bb2384fd11946f2779a",
      "values": [
        {
          "id": "acropolis",
          "featureType": "unknown",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "agora",
          "featureType": "sanctuary",
          "minDate_x": -750,
          "nameTransliterated": "Agora",
          "minDate_y": -550
        },
        {
          "id": "akropolis",
          "featureType": "fort",
          "minDate_x": -550,
          "nameTransliterated": "Akropolis",
          "minDate_y": -750
        },
        {
          "id": "asteria",
          "featureType": "settlement",
          "minDate_x": -330,
          "nameTransliterated": "Asteria",
          "minDate_y": 300
        },
        {
          "id": "athena-t",
          "featureType": "temple",
          "minDate_x": -750,
          "nameTransliterated": "Athena, T",
          "minDate_y": -550
        },
        {
          "id": "castellum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Castellum",
          "minDate_y": -30
        },
        {
          "id": "castellum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Castellum (...)",
          "minDate_y": -30
        },
        {
          "id": "forum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Forum",
          "minDate_y": 1700
        },
        {
          "id": "izmir",
          "featureType": "settlement-modern",
          "minDate_x": 1700,
          "nameTransliterated": "Izmir",
          "minDate_y": null
        },
        {
          "id": "kahramanmaras",
          "featureType": "province-2",
          "minDate_x": -720,
          "nameTransliterated": "Kahramanmaraş, Kahramanmarash, K. Maraş",
          "minDate_y": 1918
        },
        {
          "id": "kalekoy",
          "featureType": "settlement-modern",
          "minDate_x": 2000,
          "nameTransliterated": "Kalekoy, Kaleköy",
          "minDate_y": 1700
        },
        {
          "id": "karpathos",
          "featureType": "settlement",
          "minDate_x": 1700,
          "nameTransliterated": "Karpathos",
          "minDate_y": -30
        },
        {
          "id": "kayseri",
          "featureType": "settlement",
          "minDate_x": -1000,
          "nameTransliterated": "Kayseri",
          "minDate_y": -1200
        },
        {
          "id": "maltepe",
          "featureType": "settlement",
          "minDate_x": -3000,
          "nameTransliterated": "Maltepe",
          "minDate_y": -1750
        },
        {
          "id": "odeon",
          "featureType": "theatre",
          "minDate_x": -30,
          "nameTransliterated": "Odeon",
          "minDate_y": 1700
        },
        {
          "id": "old-palace",
          "featureType": "architecturalcomplex",
          "minDate_x": -2000,
          "nameTransliterated": "Old Palace",
          "minDate_y": 1900
        },
        {
          "id": "rhodos-1",
          "featureType": "unknown",
          "minDate_x": -750,
          "nameTransliterated": "Rhodos",
          "minDate_y": -1200
        },
        {
          "id": "roman-amphitheatre",
          "featureType": "theatre",
          "minDate_x": -30,
          "nameTransliterated": "Roman Amphitheatre",
          "minDate_y": 1700
        },
        {
          "id": "tempio-di-afrodite",
          "featureType": "temple",
          "minDate_x": -550,
          "nameTransliterated": "Tempio di Afrodite",
          "minDate_y": 1700
        },
        {
          "id": "temple-of-apollo",
          "featureType": "temple",
          "minDate_x": -750,
          "nameTransliterated": "Temple of Apollo",
          "minDate_y": 1700
        },
        {
          "id": "tindari",
          "featureType": "settlement-modern",
          "minDate_x": 1700,
          "nameTransliterated": "Tindari",
          "minDate_y": -30
        },
        {
          "id": "toprakkale",
          "featureType": "fort",
          "minDate_x": -900,
          "nameTransliterated": "Toprakkale",
          "minDate_y": -540
        }
      ]
    },
    {
      "name": "data-1e53e7f45e9225bf13b1edf9957bb01d",
      "values": [
        {
          "id": "kahramanmaras",
          "featureType": "province-2",
          "minDate_x": -720,
          "nameTransliterated": "Kahramanmaraş, Kahramanmarash, K. Maraş",
          "minDate_y": 1918
        },
        {
          "id": "kayseri",
          "featureType": "settlement",
          "minDate_x": -1000,
          "nameTransliterated": "Kayseri",
          "minDate_y": -1200
        },
        {
          "id": "izmir",
          "featureType": "settlement-modern",
          "minDate_x": 1700,
          "nameTransliterated": "Izmir",
          "minDate_y": null
        },
        {
          "id": "agora",
          "featureType": "sanctuary",
          "minDate_x": -750,
          "nameTransliterated": "Agora",
          "minDate_y": -550
        },
        {
          "id": "agora",
          "featureType": "sanctuary",
          "minDate_x": -750,
          "nameTransliterated": "Agora",
          "minDate_y": 1700
        },
        {
          "id": "forum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Forum",
          "minDate_y": 1700
        },
        {
          "id": "forum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Forum",
          "minDate_y": 1700
        },
        {
          "id": "forum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Forum",
          "minDate_y": 1700
        },
        {
          "id": "karpathos",
          "featureType": "settlement",
          "minDate_x": 1700,
          "nameTransliterated": "Karpathos",
          "minDate_y": -30
        },
        {
          "id": "rhodos-1",
          "featureType": "unknown",
          "minDate_x": -750,
          "nameTransliterated": "Rhodos",
          "minDate_y": -1200
        },
        {
          "id": "maltepe",
          "featureType": "settlement",
          "minDate_x": -3000,
          "nameTransliterated": "Maltepe",
          "minDate_y": -1750
        },
        {
          "id": "acropolis",
          "featureType": "unknown",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "acropolis",
          "featureType": "unknown",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "acropolis",
          "featureType": "unknown",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "acropolis",
          "featureType": "unknown",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "acropolis",
          "featureType": "fort",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "acropolis",
          "featureType": "acropolis",
          "minDate_x": -330,
          "nameTransliterated": "Acropolis",
          "minDate_y": 1700
        },
        {
          "id": "akropolis",
          "featureType": "fort",
          "minDate_x": -550,
          "nameTransliterated": "Akropolis",
          "minDate_y": -750
        },
        {
          "id": "asteria",
          "featureType": "settlement",
          "minDate_x": -330,
          "nameTransliterated": "Asteria",
          "minDate_y": 300
        },
        {
          "id": "asteria",
          "featureType": "settlement",
          "minDate_x": -330,
          "nameTransliterated": "Asteria",
          "minDate_y": -330
        },
        {
          "id": "tindari",
          "featureType": "settlement-modern",
          "minDate_x": 1700,
          "nameTransliterated": "Tindari",
          "minDate_y": -30
        },
        {
          "id": "temple-of-apollo",
          "featureType": "temple",
          "minDate_x": -750,
          "nameTransliterated": "Temple of Apollo",
          "minDate_y": 1700
        },
        {
          "id": "athena-t",
          "featureType": "temple",
          "minDate_x": -750,
          "nameTransliterated": "Athena, T",
          "minDate_y": -550
        },
        {
          "id": "odeon",
          "featureType": "unknown",
          "minDate_x": null,
          "nameTransliterated": "Odeon",
          "minDate_y": 1700
        },
        {
          "id": "odeon",
          "featureType": "theatre",
          "minDate_x": -30,
          "nameTransliterated": "Odeon",
          "minDate_y": 1700
        },
        {
          "id": "toprakkale",
          "featureType": "fort",
          "minDate_x": -900,
          "nameTransliterated": "Toprakkale",
          "minDate_y": -540
        },
        {
          "id": "old-palace",
          "featureType": "architecturalcomplex",
          "minDate_x": -2000,
          "nameTransliterated": "Old Palace",
          "minDate_y": 1900
        },
        {
          "id": "castellum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Castellum",
          "minDate_y": -30
        },
        {
          "id": "castellum",
          "featureType": "unknown",
          "minDate_x": -30,
          "nameTransliterated": "Castellum (...)",
          "minDate_y": -30
        },
        {
          "id": "kalekoy",
          "featureType": "settlement-modern",
          "minDate_x": 2000,
          "nameTransliterated": "Kalekoy, Kaleköy",
          "minDate_y": 1700
        },
        {
          "id": "tempio-di-afrodite",
          "featureType": "temple",
          "minDate_x": -550,
          "nameTransliterated": "Tempio di Afrodite",
          "minDate_y": 1700
        },
        {
          "id": "roman-amphitheatre",
          "featureType": "theatre",
          "minDate_x": -30,
          "nameTransliterated": "Roman Amphitheatre",
          "minDate_y": 1700
        }
      ]
    },
    {
      "name": "data_0",
      "source": "data-fba704c7e3536bb2384fd11946f2779a",
      "transform": [
        {
          "type": "filter",
          "expr": "!(length(data(\"selector125_store\"))) || (vlSelectionTest(\"selector125_store\", datum))"
        },
        {
          "type": "filter",
          "expr": "isValid(datum[\"minDate_x\"]) && isFinite(+datum[\"minDate_x\"])"
        }
      ]
    },
    {
      "name": "data_1",
      "source": "data-1e53e7f45e9225bf13b1edf9957bb01d",
      "transform": [
        {
          "type": "aggregate",
          "groupby": ["featureType", "nameTransliterated"],
          "ops": ["count"],
          "fields": [null],
          "as": ["__count"]
        },
        {
          "type": "stack",
          "groupby": ["nameTransliterated"],
          "field": "__count",
          "sort": {"field": ["featureType"], "order": ["descending"]},
          "as": ["__count_start", "__count_end"],
          "offset": "zero"
        }
      ]
    }
  ],
  "signals": [
    {"name": "childWidth", "value": 400},
    {"name": "concat_0_y_step", "value": 20},
    {
      "name": "concat_0_height",
      "update": "bandspace(domain('concat_0_y').length, 1, 0.5) * concat_0_y_step"
    },
    {"name": "concat_1_y_step", "value": 20},
    {
      "name": "concat_1_height",
      "update": "bandspace(domain('concat_1_y').length, 0.1, 0.05) * concat_1_y_step"
    },
    {
      "name": "unit",
      "value": {},
      "on": [
        {"events": "mousemove", "update": "isTuple(group()) ? group() : unit"}
      ]
    },
    {"name": "selector126", "update": "{\"minDate_x\": selector126_minDate_x}"},
    {"name": "selector126_minDate_x"},
    {
      "name": "selector125",
      "update": "vlSelectionResolve(\"selector125_store\", \"union\", true)"
    }
  ],
  "layout": {"padding": 20, "columns": 1, "bounds": "full", "align": "each"},
  "marks": [
    {
      "type": "group",
      "name": "concat_0_group",
      "style": "cell",
      "encode": {
        "update": {
          "width": {"signal": "childWidth"},
          "height": {"signal": "concat_0_height"}
        }
      },
      "signals": [
        {
          "name": "selector126_minDate_x",
          "on": [
            {
              "events": {"signal": "selector126_translate_delta"},
              "update": "panLinear(selector126_translate_anchor.extent_x, -selector126_translate_delta.x / childWidth)"
            },
            {
              "events": {"signal": "selector126_zoom_delta"},
              "update": "zoomLinear(domain(\"concat_0_x\"), selector126_zoom_anchor.x, selector126_zoom_delta)"
            },
            {
              "events": [{"source": "scope", "type": "dblclick"}],
              "update": "null"
            }
          ],
          "push": "outer"
        },
        {
          "name": "selector126_nameTransliterated",
          "on": [
            {
              "events": {"signal": "selector126_translate_delta"},
              "update": "panLinear(selector126_translate_anchor.extent_y, selector126_translate_delta.y / concat_0_height)"
            },
            {
              "events": {"signal": "selector126_zoom_delta"},
              "update": "zoomLinear(domain(\"concat_0_y\"), selector126_zoom_anchor.y, selector126_zoom_delta)"
            },
            {
              "events": [{"source": "scope", "type": "dblclick"}],
              "update": "null"
            }
          ]
        },
        {
          "name": "selector126_tuple",
          "on": [
            {
              "events": [
                {
                  "signal": "selector126_minDate_x || selector126_nameTransliterated"
                }
              ],
              "update": "selector126_minDate_x && selector126_nameTransliterated ? {unit: \"concat_0\", fields: selector126_tuple_fields, values: [selector126_minDate_x,selector126_nameTransliterated]} : null"
            }
          ]
        },
        {
          "name": "selector126_tuple_fields",
          "value": [
            {"field": "minDate_x", "channel": "x", "type": "R"},
            {"field": "nameTransliterated", "channel": "y", "type": "E"}
          ]
        },
        {
          "name": "selector126_translate_anchor",
          "value": {},
          "on": [
            {
              "events": [{"source": "scope", "type": "mousedown"}],
              "update": "{x: x(unit), y: y(unit), extent_x: domain(\"concat_0_x\"), extent_y: domain(\"concat_0_y\")}"
            }
          ]
        },
        {
          "name": "selector126_translate_delta",
          "value": {},
          "on": [
            {
              "events": [
                {
                  "source": "window",
                  "type": "mousemove",
                  "consume": true,
                  "between": [
                    {"source": "scope", "type": "mousedown"},
                    {"source": "window", "type": "mouseup"}
                  ]
                }
              ],
              "update": "{x: selector126_translate_anchor.x - x(unit), y: selector126_translate_anchor.y - y(unit)}"
            }
          ]
        },
        {
          "name": "selector126_zoom_anchor",
          "on": [
            {
              "events": [{"source": "scope", "type": "wheel", "consume": true}],
              "update": "{x: invert(\"concat_0_x\", x(unit)), y: invert(\"concat_0_y\", y(unit))}"
            }
          ]
        },
        {
          "name": "selector126_zoom_delta",
          "on": [
            {
              "events": [{"source": "scope", "type": "wheel", "consume": true}],
              "force": true,
              "update": "pow(1.001, event.deltaY * pow(16, event.deltaMode))"
            }
          ]
        },
        {
          "name": "selector126_modify",
          "on": [
            {
              "events": {"signal": "selector126_tuple"},
              "update": "modify(\"selector126_store\", selector126_tuple, true)"
            }
          ]
        }
      ],
      "marks": [
        {
          "name": "concat_0_marks",
          "type": "symbol",
          "clip": true,
          "style": ["circle"],
          "interactive": true,
          "from": {"data": "data_0"},
          "encode": {
            "update": {
              "opacity": {"value": 0.7},
              "size": {"value": 100},
              "fill": {"scale": "color", "field": "featureType"},
              "tooltip": {"signal": "''+datum[\"featureType\"]"},
              "x": {"scale": "concat_0_x", "field": "minDate_x"},
              "y": {"scale": "concat_0_y", "field": "nameTransliterated"},
              "shape": {"value": "circle"}
            }
          }
        }
      ],
      "axes": [
        {
          "scale": "concat_0_x",
          "orient": "bottom",
          "gridScale": "concat_0_y",
          "grid": true,
          "tickCount": {"signal": "ceil(childWidth/40)"},
          "domain": false,
          "labels": false,
          "maxExtent": 0,
          "minExtent": 0,
          "ticks": false,
          "zindex": 0
        },
        {
          "scale": "concat_0_x",
          "orient": "bottom",
          "grid": false,
          "title": "minDate_x",
          "labelFlush": true,
          "labelOverlap": true,
          "tickCount": {"signal": "ceil(childWidth/40)"},
          "zindex": 0
        },
        {
          "scale": "concat_0_y",
          "orient": "left",
          "grid": false,
          "title": "nameTransliterated",
          "zindex": 0
        }
      ]
    },
    {
      "type": "group",
      "name": "concat_1_group",
      "style": "cell",
      "encode": {
        "update": {
          "width": {"signal": "childWidth"},
          "height": {"signal": "concat_1_height"}
        }
      },
      "signals": [
        {
          "name": "selector125_tuple",
          "on": [
            {
              "events": [{"source": "scope", "type": "click"}],
              "update": "datum && item().mark.marktype !== 'group' ? {unit: \"concat_1\", fields: selector125_tuple_fields, values: [(item().isVoronoi ? datum.datum : datum)[\"nameTransliterated\"]]} : null",
              "force": true
            },
            {
              "events": [{"source": "scope", "type": "dblclick"}],
              "update": "null"
            }
          ]
        },
        {
          "name": "selector125_tuple_fields",
          "value": [{"type": "E", "field": "nameTransliterated"}]
        },
        {
          "name": "selector125_toggle",
          "value": false,
          "on": [
            {
              "events": [{"source": "scope", "type": "click"}],
              "update": "event.shiftKey"
            },
            {
              "events": [{"source": "scope", "type": "dblclick"}],
              "update": "false"
            }
          ]
        },
        {
          "name": "selector125_modify",
          "on": [
            {
              "events": {"signal": "selector125_tuple"},
              "update": "modify(\"selector125_store\", selector125_toggle ? null : selector125_tuple, selector125_toggle ? null : true, selector125_toggle ? selector125_tuple : null)"
            }
          ]
        }
      ],
      "marks": [
        {
          "name": "concat_1_marks",
          "type": "rect",
          "style": ["bar"],
          "interactive": true,
          "from": {"data": "data_1"},
          "encode": {
            "update": {
              "fill": [
                {
                  "test": "!(length(data(\"selector125_store\"))) || (vlSelectionTest(\"selector125_store\", datum))",
                  "scale": "color",
                  "field": "featureType"
                },
                {"value": "lightgrey"}
              ],
              "tooltip": {"signal": "''+datum[\"featureType\"]"},
              "x": {"scale": "concat_1_x", "field": "__count_end"},
              "x2": {"scale": "concat_1_x", "field": "__count_start"},
              "y": {"scale": "concat_1_y", "field": "nameTransliterated"},
              "height": {"scale": "concat_1_y", "band": true}
            }
          }
        }
      ],
      "axes": [
        {
          "scale": "concat_1_x",
          "orient": "bottom",
          "gridScale": "concat_1_y",
          "grid": true,
          "tickCount": {"signal": "ceil(childWidth/40)"},
          "domain": false,
          "labels": false,
          "maxExtent": 0,
          "minExtent": 0,
          "ticks": false,
          "zindex": 0
        },
        {
          "scale": "concat_1_x",
          "orient": "bottom",
          "grid": false,
          "title": "Count of Records",
          "labelFlush": true,
          "labelOverlap": true,
          "tickCount": {"signal": "ceil(childWidth/40)"},
          "zindex": 0
        },
        {
          "scale": "concat_1_y",
          "orient": "left",
          "grid": false,
          "title": "nameTransliterated",
          "zindex": 0
        }
      ]
    }
  ],
  "scales": [
    {
      "name": "color",
      "type": "ordinal",
      "domain": {
        "fields": [
          {"data": "data_0", "field": "featureType"},
          {"data": "data_1", "field": "featureType"}
        ],
        "sort": true
      },
      "range": "category"
    },
    {
      "name": "concat_0_x",
      "type": "linear",
      "domain": {"data": "data_0", "field": "minDate_x"},
      "domainRaw": {"signal": "selector126[\"minDate_x\"]"},
      "range": [0, {"signal": "childWidth"}],
      "nice": true,
      "zero": true
    },
    {
      "name": "concat_0_y",
      "type": "point",
      "domain": {"data": "data_0", "field": "nameTransliterated", "sort": true},
      "range": {"step": {"signal": "concat_0_y_step"}},
      "padding": 0.5
    },
    {
      "name": "concat_1_x",
      "type": "linear",
      "domain": {"data": "data_1", "fields": ["__count_start", "__count_end"]},
      "range": [0, {"signal": "childWidth"}],
      "nice": true,
      "zero": true
    },
    {
      "name": "concat_1_y",
      "type": "band",
      "domain": {"data": "data_1", "field": "nameTransliterated", "sort": true},
      "range": {"step": {"signal": "concat_1_y_step"}},
      "paddingInner": 0.1,
      "paddingOuter": 0.05
    }
  ],
  "legends": [
    {
      "fill": "color",
      "symbolType": "circle",
      "title": "featureType",
      "encode": {"symbols": {"update": {"opacity": {"value": 0.7}}}}
    }
  ]
}
```

{(vistype|}Interactive scatter plot and bar chart with multi selection avbility
{|vistype)}

{(vismapping|}

#### Scatter Plot:

x positions
: name of the location

y positions
: date of the first found civilization

colour
: featureType category

tooltip
: featureType category

#### Bar Chart:

x positions
: name of the location

length
: number of records found in this location

colour
: featureType category

tooltip
: featureType category

{|vismapping)}

{(dataprep|}• locations and names datasets were combined on column 'id'
• Data were aggregated by category to generate minimum date
{|dataprep)}

{(limitations|} This visualization takes a big hit from the lack of connection between the two databases . only a handdful of rows in locations and names dataset can be merged and these locations dobn't have many records. howeever this visualization is still a very informative on these specific locations.
{|limitations)}
