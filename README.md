# Logic :
## I used [color.csv](https://github.com/imvickykumar999/Super-Nova/blob/master/output/colors.csv) file to get rgb tuple using pandas and then used pygame's screen.fill(rgb) function to fill respective color on screen.

[![screenshot]('./color.png')](https://github.com/imvickykumar999/Super-Nova/blob/master/Pygame%20Display%20RGB%20Tuple%20Color.py)

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
