# Logic :
## I used [color.csv](https://raw.githubusercontent.com/imvickykumar999/Supernova-Colors/master/colors.csv) file to get rgb tuple using pandas and then used pygame's screen.fill(rgb) function to fill respective color on screen.

[![](https://raw.githubusercontent.com/imvickykumar999/Supernova-Colors/master/color.png)](https://github.com/imvickykumar999/Supernova-Colors/blob/master/Supernova.py)

### Color Names
===========

#### CSV
---

Comma separated values for example to import into a spreadsheet utility.
Looks like:

```csv
...
red,"Red",#f00,255,0,0
...
```

#### JSON
----

JavaScript Object Notation, looks like a JS or Python data structure, for
example:

```js
{
  ...
  "red": {
    "name": "Red",
    "hex": "#f00",
    "rgb": [255, 0, 0]
  }
  ...
}
```
