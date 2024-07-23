# Project Overview
This project explores the scENCORE method and single-cell epigenetic data to predict chromatin conformation using graph embedding techniques. For detailed insights, refer to the publication.

### Data
The dataset used is the 10X PBMC ATAC dataset from 10X Genomics. You can access it here.

# Methodology
The process involves several key steps:

### Binning:
Utilizes the ArchR project, with a binning size of 0.5 million.

### Metacell Construction:
Employs the SEACells project.

### Meta-cell Feature Matrix, normalization, and correlation Calculation: 
Uses custom code

### Graph Construction and Embedding: 
Methods are adapted from the scENCORE project.

### Unsupervised Clustering: 
Derived from scENCORE adaptations.

