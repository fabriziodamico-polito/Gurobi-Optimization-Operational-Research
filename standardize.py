import json
import re

files_titles = {
    'coffe_transport.ipynb': '## Coffee Transport Optimization\n\n',
    'netflix.ipynb': '## TV Series Scheduling\n\n',
    'orange_distribution.ipynb': '## Orange Distribution Logistics\n\n',
    'pens.ipynb': '## Pen Manufacturing Product Mix\n\n',
    'supplychain.ipynb': '## Warehouse Location and Supply Chain\n\n',
    'farm_optimization.ipynb': '## Farm Production Planning\n\n',
    'vaccination_campaign_optimization.ipynb': '## Vaccination Campaign Logistics\n\n'
}

for nb_file, title in files_titles.items():
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    first_markdown_cell = True
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = "".join(cell['source'])
            
            # Replace 'Exercise X (Y points).'
            source = re.sub(r'\*\*(?:Exercise|Task)\s*\d*\s*\(?[^\)]*\)?\.\*\*', '', source, flags=re.IGNORECASE)
            source = re.sub(r'Exercise\s*\d*\s*\(?[^\)]*\)?\.', '', source, flags=re.IGNORECASE)
            
            # Prepend title to the first markdown cell
            if first_markdown_cell:
                source = title + source.lstrip()
                first_markdown_cell = False

            # Standardize section headers
            source = re.sub(r'\*\*Indexes\*\*\s*:?', '**INDEXES**:', source, flags=re.IGNORECASE)
            source = re.sub(r'\*\*Parameters\*\*\s*:?', '**PARAMETERS**:', source, flags=re.IGNORECASE)
            source = re.sub(r'\*\*Variables\*\*\s*:?', '**VARIABLES**:', source, flags=re.IGNORECASE)

            # Fix LaTeX in farm_optimization and other missing $ (e.g. "- L : ")
            source = re.sub(r'-\s+([a-zA-Z])\s+:', r'- $\1$ :', source)
            source = re.sub(r'-\s+([a-zA-Z_]+)\s+:', r'- $\1$ :', source)

            # Fix symbols (replace unicode replacement char with Euro)
            source = source.replace('\ufffd', '€')
            
            # Restore to lines for jupyter
            cell['source'] = [line + '\n' for line in source.split('\n')]
            # Remove trailing newline in the last element to avoid extra spacing
            if cell['source']:
                cell['source'][-1] = cell['source'][-1].rstrip('\n')
                
    with open(nb_file, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

print("Standardization applied successfully!")
