## Regex Steps
# Lovecraft

1. Added `<xml>` over entire document.
2. Found `^\n*(.+\n(?:.+\n)*)` and replaced it with `<para>$1</para>` to divide work into paragraphs
3. Found Gutenberg headings, titles, and beginning quotes from other authors and wrapped them in a `<meta>` tag. Changed `<para>` tags to `<info>` tags within these for clarity.
4. Found `(?<=<para>)([^<]+?)([.!?])` and wrapped in `<s>` tag for first sentence. Oxygen didn't play nice with the para tags at the beginning, so this was necessary.
5. Marked the rest of the `<s>` tags by using `(?<=</s>)([^<]+?)([.!?])`. Had to continually find and replace in order to get everything in a paragraph, as this simply targeted the next sentence.
6. Found `"(.*?)"` to find items in quotes and wrap them in a `quote` tag.

** Note: most paragraphs that consist *entirely* of quotes do not have `<s>` tags. I figured it could be valuable to have paragraphs with only quotations as a datapoint, so I didn't remedy this.**