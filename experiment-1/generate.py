from math import sqrt

phi = 1.61803398875
ratios = [
    {
        'id': 'square',
        'title': 'Square (1:1 or 1:√1)',
        'ratio': 1,
    },
    {
        'id': 'diagon',
        'title': 'Diagon (1:√2)',
        'ratio': sqrt(2),
    },
    {
        'id': 'hecton',
        'title': 'Hecton or sixton (1:√3)',
        'ratio': sqrt(3),
    },
    {
        'id': 'doppelquadrat',
        'title': 'Doppelquadrat (1:2 or 1:√4)',
        'ratio': 2,
    },
    {
        'id': 'hemiolion',
        'title': 'Hemiolion (2:3)',
        'ratio': 3.0/2.0,
    },
    {
        'id': 'auron',
        'title': 'Auron (the golden rectangle, 1:φ)',
        'ratio': phi,
    },
    {
        'id': 'hemidiagon',
        'title': 'Hemidiagon (1:½√5)',
        'ratio': 1.0/2.0*sqrt(5),
    },
    {
        'id': 'penton',
        'title': 'Penton (1:√φ)',
        'ratio': sqrt(phi),
    },
    {
        'id': 'trion',
        'title': 'Trion (1:⅔√3)',
        'ratio': 2.0/3.0*sqrt(3),
    },
    {
        'id': 'quadriagon',
        'title': 'Quadriagon (1:(1+√2)/2)',
        'ratio': (1.0 + sqrt(2))/2.0,
    },
    {
        'id': 'biauron',
        'title': 'Biauron (1:2φ)',
        'ratio': 2*phi,
    },
    {
        'id': 'bipenton',
        'title': 'Bipenton (1:2√(5-2√5))',
        'ratio': 2*sqrt(5 - 2*sqrt(5)),
    },
]

num_columns = 4

for ratio in ratios:
    j = 1
    grid_columns = []
    for i in range(num_columns):
        grid_columns.append(j)
        j = j*ratio['ratio']
    css = """
.wrapper-{id} {{
    display: grid;
    grid-template-columns: {columns};
    grid-column-gap: 1em;
}}
    """.format(**ratio, columns=" ".join(['{grid_column}fr'.format(grid_column=grid_column) for grid_column in grid_columns]))

    html = """
    <h2>{title}</h2>
    <div class="wrapper-{id}">
{columns}
    </div>
    """.format(**ratio, columns=" \n".join(['      <div class="fraction">{grid_column:.3f}</div>'.format(grid_column=grid_column) for grid_column in grid_columns]))

#    print(css, end='')
    print(html, end="")
