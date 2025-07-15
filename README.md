# 🌿 Bioinfo Breeding Toolkit

**A curated collection of Python-based tools and workflows for genomic data analysis, SNP discovery, QTL matching, and GWAS in plant breeding.**

---

## 📦 Repository Structure

- `sequence_tools/` — Functions for basic sequence quality control and content analysis (GC, AT, base validation)
- `expression_tools/` — Visualize gene expression values from GEO Series Matrix files

*Modules such as SNP panel generation, QTL matching, and GWAS will be added as development progresses.*

---

## 🧪 Functional Modules

### ✅ Available


#### `sequence_qc.py`  
- Read sequences from TXT and FASTA  
- Identify invalid bases (non-ATGC)  
- Calculate GC and AT content  
- Summarize clean and dirty sequences  

#### `expression_plotter.py`  
- Extract a specific gene’s expression values across multiple samples  
- Calculate and display average expression  
- Generate bar plots with inline data labels  
- Include a table of expression values below the plot  

---
🎯 Planned Modules
- `snp_panel_generation/` — Scripts for filtering VCFs and extracting flanking regions  
- `qtl_matching/` — Match SNP positions to annotated gene/QTL regions  
- `gwas_analysis/` — Perform GWAS using PLINK or pandas-based pipelines  
- `data_visualization/` — Plot distributions, Manhattan plots, summary charts  
---

🧬 Goals
- Analyze real genomic data (FASTA, GFF3, VCF, RNA-seq counts)  
- Generate publication-ready summaries and plots  
- Demonstrate strong coding skills and biological insight for plant genomics  

---

## 👩‍💻 Author

- Deniz Kom — Biotech researcher & aspiring computational plant breeder  
- This repository supports my portfolio for roles in plant genomics and data-driven breeding.

---

## 📜 License

[MIT License](LICENSE)
