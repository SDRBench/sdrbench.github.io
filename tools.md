---
layout: default
title: Tools
---

<div class="page-header">
  <div class="content">
    <h1>Tools & Compressors</h1>
    <p>Lossy and lossless compressors, assessment metrics, error controls, and evaluation tools.</p>
  </div>
</div>

<div class="content" markdown="1">

## Lossy Compressors

| Compressor | Link |
|------------|------|
| SZ | [https://github.com/szcompressor/SZ](https://github.com/szcompressor/SZ) |
| ZFP | [https://github.com/LLNL/zfp](https://github.com/LLNL/zfp) |
| TTHRESH | [https://github.com/rballester/tthresh](https://github.com/rballester/tthresh) |
| MGARD | [https://github.com/CODARcode/MGARD](https://github.com/CODARcode/MGARD) |
| SPERR | [https://github.com/NCAR/SPERR](https://github.com/NCAR/SPERR) |
| ISABELA | [http://freescience.org/cs/ISABELA/ISABELA.html](http://freescience.org/cs/ISABELA/ISABELA.html) |
| PFPL | [https://github.com/burtscher/PFPL](https://github.com/burtscher/PFPL) |
| DCTZ | [https://github.com/swson/DCTZ](https://github.com/swson/DCTZ) |
| Digit Rounding | [https://github.com/CNES/Digit_Rounding](https://github.com/CNES/Digit_Rounding) (standalone: [digitroundingZ](https://github.com/disheng222/digitroundingZ)) |
| Bit Grooming | [https://github.com/nco/nco](https://github.com/nco/nco) (standalone: [BitGroomingZ](https://github.com/disheng222/BitGroomingZ.git)) |

*Others: please submit your suggestion of lossy compressor, with GitHub link to **codar-reduction (at) cels.anl.gov**.*

## Lossless Compressors

| Compressor | Link |
|------------|------|
| FPZIP | [https://computation.llnl.gov/projects/floating-point-compression](https://computation.llnl.gov/projects/floating-point-compression) |
| ZFP | [https://github.com/LLNL/zfp](https://github.com/LLNL/zfp) |
| FPC | [http://cs.txstate.edu/~burtscher/research/FPC/](http://cs.txstate.edu/~burtscher/research/FPC/) |
| pFPC (parallel) | [http://cs.txstate.edu/~burtscher/research/pFPC/](http://cs.txstate.edu/~burtscher/research/pFPC/) |
| SPDP | [http://cs.txstate.edu/~burtscher/research/SPDP/](http://cs.txstate.edu/~burtscher/research/SPDP/) |
| GFC (GPUs) | [http://cs.txstate.edu/~burtscher/research/GFC/](http://cs.txstate.edu/~burtscher/research/GFC/) |
| MPC (GPUs) | [http://cs.txstate.edu/~burtscher/research/MPC/](http://cs.txstate.edu/~burtscher/research/MPC/) |
| BLOSC | [https://github.com/Blosc/c-blosc](https://github.com/Blosc/c-blosc) |
| FPcompress | [https://github.com/burtscher/FPcompress/](https://github.com/burtscher/FPcompress/) |

*Others: please submit your suggestion of lossless compressor, with GitHub link to **codar-reduction (at) cels.anl.gov**.*

## Unifying Generic Interface for Compression

- **LibPressio** (lossy and lossless): [https://robertu94.github.io/libpressio/](https://robertu94.github.io/libpressio/)

## Assessment Metrics

Commonly used metrics for reduction technique assessment:

- Reduction/reconstruction rate in \[G\|M\|K\]B/s
- Reduction ratio (initial size / compressed size)
- \[Lossy\] Rate distortion (PSNR at different bit rates)
- \[Lossy\] PSNR in dB, MSE, RMSE, and NRMSE
- \[Lossy\] SSIM (structural similarity index)
- \[Lossy\] Pearson correlation of the initial and reconstructed dataset
- \[Lossy\] Autocorrelation of the compression error (1D, ... nD)
- \[Lossy\] Spectral alteration (difference of power spectrum)
- \[Lossy\] Preservation of the n-order derivatives

*Others: please submit your suggestion of assessment metric to **codar-reduction (at) cels.anl.gov**.*

## Error Controls

- \[Common\] Point-wise absolute error bound
- \[Common\] Point-wise relative error bound
- \[Variation\] Value range point-wise relative error bound
- \[Other\] Fixed PSNR

## Assessment Tools

| Tool | Link |
|------|------|
| Z-checker | [https://github.com/CODARcode/Z-checker](https://github.com/CODARcode/Z-checker) |
| Foresight | [https://github.com/lanl/VizAly-Foresight](https://github.com/lanl/VizAly-Foresight) |
| ldcpy | [https://github.com/NCAR/ldcpy](https://github.com/NCAR/ldcpy) |
| SFS | [https://github.com/JulianKunkel/statistical-file-scanner](https://github.com/JulianKunkel/statistical-file-scanner) |

*Others: please submit your suggestion of assessment tools, with GitHub link to **codar-reduction (at) cels.anl.gov**.*

</div>
