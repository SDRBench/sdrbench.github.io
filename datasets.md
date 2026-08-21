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

*Note: This table will be augmented with metrics that matter for users of these datasets as well as recommended settings for error control (lossy compression).*

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
