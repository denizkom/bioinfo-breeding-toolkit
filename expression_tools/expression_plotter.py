#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizes expression levels of a specific gene from a GEO matrix file.
Draws a barplot with per-sample values, includes a red dashed mean line,
and adds a summary table below the chart.

@author: denizkom and used ChatGPT for correction and providing definations. 
"""
import pandas as pd
import matplotlib.pyplot as plt

# === Step 1: Load and clean the data ===
# Read the expression matrix, skipping metadata lines (commented with '!')
df = pd.read_csv("GSE70509_series_matrix.txt", sep="\t", comment="!")

# Strip whitespace from column headers to prevent access errors
df.columns = df.columns.str.strip()

# === Step 2: Select a gene by ID_REF ===
# Change this ID to visualize another gene
gene_id = "171723_x_at"

# Find the row corresponding to the gene
gen_row = df[df["ID_REF"] == gene_id]

# If the gene is not found, exit with a message
if gen_row.empty:
    print(f"❌ Gene {gene_id} not found in the dataset.")
    exit()

# === Step 3: Extract expression values ===
# Take numeric expression values across all samples for this gene
expression_values = gen_row.iloc[0, 1:].astype(float)
samples = expression_values.index

# Calculate the mean expression value
mean_expression = expression_values.mean()

# === Step 4: Plot bar plot with values ===
fig, ax = plt.subplots(figsize=(14, 6))

# Create bar plot
bars = ax.bar(samples, expression_values, color="skyblue")

# Add text label on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 2,
            f"{height:.1f}", ha="center", va="bottom", fontsize=8)

# Draw mean line (dashed red) and annotate
ax.axhline(mean_expression, color='red', linestyle='--', linewidth=1)
ax.text(len(samples) - 0.5, mean_expression + 1,
        f"Mean: {mean_expression:.2f}", color='red', fontsize=9, ha='right')

# Set labels and title
ax.set_title(f"Expression of {gene_id} across samples", fontsize=14)
ax.set_ylabel("Expression Level")
ax.set_xticks(range(len(samples)))
ax.set_xticklabels(samples, rotation=45, ha='right')

# === Step 5: Add table underneath ===
# Create one-row table containing expression values
table_data = [["{:.1f}".format(val) for val in expression_values]]
table = ax.table(cellText=table_data,
                 colLabels=samples,
                 loc='bottom',
                 cellLoc='center',
                 bbox=[0.0, -0.49, 1.0, 0.25])  # Push table lower to avoid overlap

# Format table font
table.auto_set_font_size(False)
table.set_fontsize(8)

# === Step 6: Adjust layout ===
# Increase bottom margin to fit table
plt.subplots_adjust(bottom=0.52)
plt.tight_layout()

# === Step 7: Show plot ===
plt.show()
