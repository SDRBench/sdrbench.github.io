---
layout: default
title: Datasets
---

<div class="page-header">
  <div class="content">
    <h1>Datasets</h1>
    <p>Reference scientific datasets for benchmarking data reduction techniques. Click on command examples to expand.</p>
  </div>
</div>

<div class="content">

<div class="card" id="python-access">
  <div class="card-body" markdown="1">

**Python and Hugging Face.** All datasets below except NSTX GPI are also mirrored, byte for byte, on [Hugging Face](https://huggingface.co/sdrbench), and can be loaded as numpy arrays with the [`sdrbench`](https://pypi.org/project/sdrbench/) package. It downloads single files from Hugging Face, checks them against their sha256, and falls back to the archives listed here:

```python
# pip install sdrbench
import sdrbench
x = sdrbench.dataset("cesm-atm")["CLDHGH"]     # numpy array, shape (1800, 3600)
```

Every field comes with its dtype and C-order shape; see [szcompressor/sdrbench](https://github.com/szcompressor/sdrbench) for the dataset, variant and field names.

  </div>
</div>

*Note: This table will be augmented with metrics that matter for users of these datasets as well as recommended settings for error control (lossy compression).*

*Dimensions in the Format sections are listed slowest-varying first (C order, as in numpy), e.g. 26x1800x3600 is 26 slices of 1800x3600; the command examples pass them to the tools fastest-varying first (e.g. `-3 3600 1800 26`).*

{% for ds in site.data.datasets %}
<div class="card" id="{{ ds.name | slugify }}">
  <div class="card-header">
    <h3>{{ ds.name }}</h3>
    <span class="badge">{{ ds.type }}</span>
  </div>
  <div class="card-body">

    <p class="source-info">
      <strong>Source:</strong> {{ ds.source }}
      {% if ds.source_url and ds.source_url != "" %}
        (<a href="{{ ds.source_url }}">{{ ds.source_url }}</a>)
      {% endif %}
    </p>
    {% if ds.source_note %}
    <p class="source-info">{{ ds.source_note }}</p>
    {% endif %}

    <div class="dataset-grid">
      <div>
        <div class="detail-group">
          <h4>Format</h4>
          <p>{{ ds.format | newline_to_br }}</p>
        </div>

        <div class="detail-group">
          <h4>Size</h4>
          <p>{{ ds.size | newline_to_br }}</p>
        </div>
      </div>

      <div>
        {% if ds.entropy.size > 0 %}
        <div class="detail-group">
          <h4>Entropy</h4>
          {% for ent in ds.entropy %}
          {% if ent.label and ent.label != "" %}
          <p><strong>{{ ent.label }}</strong></p>
          {% endif %}
          <table class="entropy-table">
            <tr><th></th><th>8-bit Entropy</th><th>32-bit Entropy</th></tr>
            {% for row in ent.rows %}
            <tr><td><strong>{{ row.stat }}</strong></td><td>{{ row.e8 }}</td><td>{{ row.e32 }}</td></tr>
            {% endfor %}
          </table>
          {% endfor %}
        </div>
        {% endif %}
      </div>
    </div>

    <div class="detail-group">
      <h4>Download Links</h4>
      <div class="download-links">
        {% for link in ds.links %}
        <a href="{{ link.url }}">{{ link.label }}</a>
        {% endfor %}
      </div>
    </div>

    {% if ds.commands.sz_compress != "NA" %}
    <details>
      <summary>Command Examples</summary>
<pre><code><strong>SZ (Compress):</strong>   {{ ds.commands.sz_compress }}
<strong>SZ (Decompress):</strong> {{ ds.commands.sz_decompress }}
<strong>ZFP:</strong>              {{ ds.commands.zfp }}{% if ds.commands.libpressio and ds.commands.libpressio != "" %}
<strong>LibPressio:</strong>       {{ ds.commands.libpressio }}{% if ds.commands.libpressio_note %}
                      {{ ds.commands.libpressio_note }}{% endif %}{% endif %}{% if ds.commands.zchecker and ds.commands.zchecker != "" %}
<strong>Z-checker:</strong>        {{ ds.commands.zchecker }}{% endif %}</code></pre>
    </details>
    {% else %}
    {% if ds.commands_note %}
    <div class="info-box">
      <p>{{ ds.commands_note }}</p>
    </div>
    {% endif %}
    {% endif %}

  </div>
</div>
{% endfor %}

</div>
