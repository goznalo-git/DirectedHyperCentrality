# Spectral centrality of directed hypergraphs

This repository contains the scripts, data and (pre-processed) figures/tables from the "Beyond directed hypergraphs: heterogeneous hypergraphs and spectral centralities" paper by G. Contreras-Aso, R. Criado, M. Romance, published in [Journal of Complex Networks](https://doi.org/10.1093/comnet/cnae037)), and available as a preprint at [arXiv:2403.11825](https://arxiv.org/abs/2403.11825).

## Structure of the repository

The following files and directories are briefly summarized.
- `tensor_functions.py, useful_functions.py`: Tensor construction functions and centrality computations (power-like method based on the code from [1], as well as other utilities.
- `0-*.ipynb, 1-*.ipynb, ...`: Jupyter notebooks with the data pipeline (`Data/` -> `ParsedHyperedges/` -> `ProcesseHypergraphs/` -> `CentralityData/` -> `Figures/`), from the raw data downloaded/scraped from each data source (cited in the paper), to the construction and analysis of adjacency tensors and their centralities.
- `kstepHypergraphs.ipynb`: Jupyter notebook with the construction and analysis of k-step centralities of standard networks located at `DirectedNets/`.


[1] "Uplifting edges in higher order networks: spectral centralities for non-uniform hypergraphs". G. Contreras-Aso, C. Pérez-Corral and M. Romance. arXiv:2310.20335 (2023). [GitHub repository](https://github.com/LaComarca-Lab/non-uniform-hypergraphs).

Bibtex citation:
```
@article{contrerasaso2024beyond,
    author = {Contreras-Aso, Gonzalo and Criado, Regino and Romance, Miguel},
    title = {Beyond directed hypergraphs: heterogeneous hypergraphs and spectral centralities},
    journal = {Journal of Complex Networks},
    volume = {12},
    number = {5},
    pages = {cnae037},
    year = {2024},
    month = {09},
    issn = {2051-1329},
    doi = {10.1093/comnet/cnae037},
    url = {https://doi.org/10.1093/comnet/cnae037},
    eprint = {https://academic.oup.com/comnet/article-pdf/12/5/cnae037/59074198/cnae037.pdf},
}

```
