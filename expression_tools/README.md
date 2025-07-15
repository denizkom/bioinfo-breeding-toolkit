# Expression Analysis Tools

This module contains scripts for visualizing gene expression data, particularly from GEO Series Matrix files. It is designed for plant-focused transcriptomic studies.

⚠️ **Note:** This toolset is under continuous development. New features and analysis functions will be added over time.

## Contents

- `expression_plotter.py`: A script to visualize the expression level of a specific gene across multiple samples using bar plots. It also includes a data table below the chart.

## Usage

1. Place your `GSE_series_matrix.txt` file in the same directory or modify the script path.
2. Open and edit the `gene_id` variable inside the script to match your gene of interest.
3. Run the script to generate:
   - The average expression value of the gene
   - A bar chart showing gene expression levels
   - A table below the chart for data readability

## Notes
Make sure your matrix file includes an ID_REF column with gene identifiers.

The script is optimized for plant datasets, such as Arabidopsis thaliana.

## License
This project is licensed under the terms of the LICENSE file in the root directory.


