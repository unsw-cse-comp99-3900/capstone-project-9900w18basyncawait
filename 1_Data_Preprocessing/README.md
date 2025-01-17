# Data Preprocessing

## Data
The dataset used is the 10X PBMC ATAC dataset from 10X Genomics. You can access it [here](https://support.10xgenomics.com/single-cell-atac/datasets/1.2.0/atac_pbmc_10k_nextgem).

## Methodology
The process involves two key steps:

## Binning:
- The binning process is included in the Binning folder.
- Description: Binning involves segmenting the genome into equal-sized bins to facilitate analysis of chromatin accessibility.
- Utilizes the [ArchR](https://github.com/GreenleafLab/ArchR) project for binning.
- Binning size: 0.5 million.
- For detail of the theory, ArchR has the [publication in Nature](https://www.nature.com/articles/s41588-021-00790-6).

## Metacell Construction:
- The metacell process is included in the Metacell folder
- Description: In scATAC-seq data, the sparsity means not all cell fragments are present in every region, resulting in many zeros in the matrix. This can lower correlation coefficients between regions. To mitigate this, we use metacells. A metacell aggregates similar cells, increasing data density and improving analysis.
- Employs the [SEACells](https://github.com/dpeerlab/SEACells) project.
- For detail of the theory, SEACells has the [publication in Nature](https://www.nature.com/articles/s41587-023-01716-9).

