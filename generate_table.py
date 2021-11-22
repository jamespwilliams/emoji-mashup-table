#!/usr/bin/env python3

emoji_codes = []
with open('emojis.txt', 'r') as f:
    emoji_codes = f.readlines()
    emoji_codes = [emoji_code.rstrip() for emoji_code in emoji_codes]

table = [[None for _ in range(len(emoji_codes) + 1)] for _ in range(len(emoji_codes) + 1)]

def noto_link_image(code):
    return f"<img src='noto-emoji/png/72/emoji_{code}.png'>"

def google_link_image(code1, code2):
    link = f"Google-Sticker-Mashup-Research/stickers/{code1}_{code2}.png"
    return f"<a href='{link}'><img style='width: 72px' src='{link}' onerror='this.parentNode.removeChild(this)'></a>"

def render_css():
    return '''
        <style>
            #container {
                overflow: scroll;
                max-width: 90vw;
                max-height: 90vh;
            }

            table {
                border-collapse: collapse;
            }

            table, th, td {
                border: 1px solid black;
                background-color: #fff;
            }
            
            thead th {
                background-color: black;
            }

            tbody th {
                background-color: black;
            }

            thead th {
                position: sticky;
                top: 0;
            }

            thead th:first-child {
                left: 0;
                z-index: 2;
            }

            tbody th {
                position: sticky;
                left: 0;
            }
        </style>
    '''

def render_table(table):
    result = '<div id="container">\n<table>\n'

    for row_index, row in enumerate(table):
        if row_index == 0:
            result += '<thead>'

        result += '<tr>\n'

        for elem_index, elem in enumerate(row):
            elem_tag = 'th' if row_index == 0 or elem_index == 0 else 'td'
            result += '<' + elem_tag + ' style="width: 72px">' + (elem if elem else '') + '</' + elem_tag + '>\n'

        if row_index == 0:
            result += '</thead>\n<tbody>'
        result += '</tr>\n'

    result += '</tbody></table>\n</div>'
    return result

# Add table header:
for index, code in enumerate(emoji_codes):
    table[0][index + 1] = noto_link_image(code)

# Add table row labels:
for index, code in enumerate(emoji_codes):
    table[index + 1][0] = noto_link_image(code)

for y, ycode in enumerate(emoji_codes):
    for x, xcode in enumerate(emoji_codes):
        table[y + 1][x + 1] = google_link_image(xcode, ycode)

print(render_css() + render_table(table))
