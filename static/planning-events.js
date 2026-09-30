(() => {
  const slug = location.pathname.split('/').filter(Boolean).pop();
  document.querySelectorAll('main a[href]').forEach(link => {
    const url = new URL(link.href, location.href);
    if (url.hostname === 'www.google.com' && url.pathname.startsWith('/maps')) {
      link.dataset.tinylyticsEvent = 'directions.click';
      link.dataset.tinylyticsEventValue = slug;
    } else if (['www.fs.usda.gov', 'www.sgwa.org', 'quickmap.dot.ca.gov'].includes(url.hostname)) {
      link.dataset.tinylyticsEvent = 'planning.official';
      link.dataset.tinylyticsEventValue = slug + ':' + url.pathname;
    }
  });
})();
