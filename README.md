# csvparser

This script parses a CSV or JSON file from an exported playlist into a m3u8, for use with iTunes, VLC, etc.


## Notes:

- The default format is "Artist - Title", but you can change it to "Title - Artist" by changing the `format` variable in the script.
- The CSV or JSON file must have the following columns: `Artist`, `Title` and `Duration`. Capitalisation doesn't matter, nor does the order of the columns or any spaces in the column names.