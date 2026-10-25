---
layout: page
title: Search
permalink: /search/
description: "Search all TinyLab tutorials."
sitemap: false
---

<input type="search" id="search-input" placeholder="Search tutorials — e.g. docker layers, kubernetes probes" aria-label="Search tutorials" autofocus>
<p class="text-muted" id="search-status">Type to search.</p>
<ul class="search-results" id="search-results"></ul>

<script>
(function () {
  var input = document.getElementById('search-input');
  var status = document.getElementById('search-status');
  var results = document.getElementById('search-results');
  var index = null;

  function load(cb) {
    if (index) return cb(index);
    fetch('{{ site.baseurl }}/search.json').then(function (r) { return r.json(); })
      .then(function (data) { index = data; cb(index); })
      .catch(function () { status.textContent = 'Search index could not be loaded.'; });
  }

  function score(doc, terms) {
    var s = 0;
    var title = doc.title.toLowerCase(), desc = doc.description.toLowerCase(), body = doc.content.toLowerCase();
    terms.forEach(function (t) {
      if (title.indexOf(t) !== -1) s += 10;
      if (desc.indexOf(t) !== -1) s += 4;
      var n = body.split(t).length - 1;
      s += Math.min(n, 5);
    });
    return s;
  }

  function snippet(doc, terms) {
    var body = doc.content, lower = body.toLowerCase(), pos = -1;
    for (var i = 0; i < terms.length && pos === -1; i++) pos = lower.indexOf(terms[i]);
    if (pos === -1) return doc.description || body.slice(0, 160) + '…';
    var start = Math.max(0, pos - 70);
    return (start > 0 ? '…' : '') + body.slice(start, start + 180) + '…';
  }

  function render(q) {
    var terms = q.toLowerCase().split(/\s+/).filter(function (t) { return t.length > 1; });
    results.innerHTML = '';
    if (!terms.length) { status.textContent = 'Type to search.'; return; }
    load(function (docs) {
      var hits = docs.map(function (d) { return { d: d, s: score(d, terms) }; })
        .filter(function (h) { return h.s > 0; })
        .sort(function (a, b) { return b.s - a.s; })
        .slice(0, 25);
      status.textContent = hits.length ? hits.length + ' result' + (hits.length === 1 ? '' : 's') : 'No results.';
      hits.forEach(function (h) {
        var li = document.createElement('li');
        var crumb = h.d.track + (h.d.section ? ' › ' + h.d.section : '');
        li.innerHTML = '<div class="result-track">' + crumb + (h.d.level ? ' · ' + h.d.level : '') + '</div>' +
          '<a href="' + h.d.url + '"><strong>' + h.d.title + '</strong></a>' +
          '<div class="text-muted" style="font-size:0.9rem">' + snippet(h.d, terms).replace(/</g, '&lt;') + '</div>';
        results.appendChild(li);
      });
    });
  }

  var timer;
  input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(function () { render(input.value); }, 150); });
  var initial = new URLSearchParams(location.search).get('q');
  if (initial) { input.value = initial; render(initial); }
})();
</script>
