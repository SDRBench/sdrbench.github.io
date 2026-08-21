---
layout: default
title: Home
---

<div class="hero">
  <h1>Scientific Data Reduction Benchmarks</h1>
  <p>Reference scientific datasets, data reduction techniques, error metrics, error controls, and error assessment tools for users and developers of scientific data reduction techniques.</p>
</div>

<div class="content" markdown="1">

This site has been established as part of the [ECP](https://www.exascaleproject.org/) [CODAR](https://www.exascaleproject.org/project/codar-co-design-center-online-data-analysis-reduction-exascale/) project. It provides reference scientific datasets, data reduction techniques, error metrics, error controls, and error assessment tools for users and developers of scientific data reduction techniques.

<div class="alert" markdown="1">

### Important: When publishing results from one or more datasets presented in this website, please:

- **Cite**: SDRBench -- *https://sdrbench.github.io*
- **Please also cite**: K. Zhao, S. Di, X. Liang, S. Li, D. Tao, J. Bessac, Z. Chen, and F. Cappello, "SDRBench: Scientific Data Reduction Benchmark for Lossy Compressors", International Workshop on Big Data Reduction (IWBDR2020), in conjunction with IEEE Bigdata20.
- **Acknowledge**: the source of the dataset you used, the DOE NNSA ECP project, and the ECP CODAR project.
- **Check**: the condition of publications (some dataset sources request prior check).
- **Contact**: the compressor authors to get the correct compressor configuration according to each dataset and each comparison metrics.

</div>

<div class="info-box" markdown="1">

**Dimension ordering note:** The order of the dimensions shown in the "Format" column of the dataset table is in row-major order (C order), consistent with well-known I/O libraries such as HDF5. For example, for the CESM-ATM dataset (1800 x 3600), 1800 is the higher dimension (changing slower) and 3600 is the lower dimension (changing faster). For most compressors (such as SZ, ZFP, and FPZIP), the dimensions should be given in the reverse order (such as `-2 3600 1800`) for their executables. If you are not sure about the order of dimensions, one simple method is trying different dimension orders and selecting the results with highest compression ratios.

</div>

## File Extension Conventions

| Extension | Description |
|-----------|-------------|
| `.f32` | Single-precision floating point data, little-endian |
| `.F32` | Single-precision floating point data, big-endian |
| `.f64` | Double-precision floating point data, little-endian |
| `.F64` | Double-precision floating point data, big-endian |

## Submit a Dataset

Please submit your proposal of datasets to **codar-reduction (at) cels.anl.gov**.

**Requirements:**
- Datasets must be open to public access
- Dataset should be linked to a simulation application or a scientific instrument
- Metadata should explain the source origin of the dataset and how it has been produced (what simulation, what instrument, what settings)
- Upon review by the SDRBenchmarks committee, the dataset will (or will not) be added to the SDRBenchmarks repository

</div>
