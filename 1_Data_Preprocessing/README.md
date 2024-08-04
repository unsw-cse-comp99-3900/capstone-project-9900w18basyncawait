# Project Overview
This project explores the scENCORE method and single-cell epigenetic data to predict chromatin conformation using graph embedding techniques. For detailed insights, refer to the [scENCORE publication](https://doi.org/10.1093/bib/bbae096).

# Data
The dataset used is the 10X PBMC ATAC dataset from 10X Genomics. You can access it [here](https://support.10xgenomics.com/single-cell-atac/datasets/1.2.0/atac_pbmc_10k_nextgem).

# Methodology
The process involves several key steps:

## Binning:
- Description: Binning involves segmenting the genome into equal-sized bins to facilitate analysis of chromatin accessibility.
- Utilizes the [ArchR](https://github.com/GreenleafLab/ArchR) project for binning.
- Binning size: 0.5 million.
- For detail of the theory, ArchR has the [publication in Nature](https://www.nature.com/articles/s41588-021-00790-6).

## Metacell Construction:
- Description: In scATAC-seq data, the sparsity means not all cell fragments are present in every region, resulting in many zeros in the matrix. This can lower correlation coefficients between regions. To mitigate this, we use metacells. A metacell aggregates similar cells, increasing data density and improving analysis.
- Employs the [SEACells](https://github.com/dpeerlab/SEACells) project.
- For detail of the theory, SEACells has the [publication in Nature](https://www.nature.com/articles/s41587-023-01716-9).

## Meta-cell Feature Matrix, normalization, and correlation Calculation: 
- Description: This step involves calculating the feature matrix, normalizing data, and computing correlations to prepare for graph analysis.
- Uses custom code

## Graph Construction, Graph Embedding, and Unsupervised Clustering: 
- Description: This involves constructing a graph from the data, learning its embedded representation, and applying unsupervised clustering to uncover patterns.
- Methods adapted from the [scENCORE project](https://github.com/aicb-ZhangLabs/scENCORE) and are intergrated into this project.

