document.documentElement.classList.add('js');

(function () {
  'use strict';
  function sourceCategory() {
    var params = new URLSearchParams(window.location.search);
    var utm = (params.get('utm_source') || '').toLowerCase();
    var referrer = (document.referrer || '').toLowerCase();
    if (utm.indexOf('chatgpt') !== -1 || referrer.indexOf('chatgpt.com') !== -1 || referrer.indexOf('openai.com') !== -1) return 'ChatGPT / AI Referral';
    if (/google\./.test(referrer)) return 'Google';
    if (/bing\./.test(referrer)) return 'Bing';
    if (/duckduckgo\.|yahoo\.|baidu\./.test(referrer)) return 'Organic Search';
    if (!referrer) return 'Direct';
    return 'Other';
  }
  function recordEvent(name, parameters) {
    var detail = Object.assign({ event: name, page_path: window.location.pathname }, parameters || {});
    if (typeof window.gtag === 'function') window.gtag('event', name, detail);
    else if (Array.isArray(window.dataLayer)) window.dataLayer.push(Object.assign({ event: name }, detail));
    try { sessionStorage.setItem('ouyang_last_analytics_event', JSON.stringify(detail)); } catch (error) { /* Storage may be unavailable. */ }
    document.dispatchEvent(new CustomEvent('ouyang:analytics', { detail: detail }));
  }
  var pageStartedAt = Date.now();
  var dwellRecorded = false;
  function recordDwellTime() {
    if (dwellRecorded) return;
    dwellRecorded = true;
    recordEvent('page_engaged_time', { engaged_seconds: Math.max(0, Math.round((Date.now() - pageStartedAt) / 1000)) });
  }
  window.addEventListener('pagehide', recordDwellTime);
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') recordDwellTime(); });
  if ('IntersectionObserver' in window) {
    var viewedVisuals = {};
    var visualObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting || entry.intersectionRatio < 0.5) return;
        var cta = entry.target.nextElementSibling;
        var visualId = cta && cta.dataset ? cta.dataset.visualCta : '';
        if (!visualId || viewedVisuals[visualId]) return;
        viewedVisuals[visualId] = true;
        recordEvent('engineering_visual_view', { visual_id: visualId });
        visualObserver.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    document.querySelectorAll('.engineering-visual').forEach(function (visual) { visualObserver.observe(visual); });
  }
  document.querySelectorAll('a[data-cta-type]').forEach(function (link) {
    link.addEventListener('click', function () {
      sessionStorage.setItem('ouyang_entry_article', window.location.pathname);
      sessionStorage.setItem('ouyang_cta_type', link.dataset.ctaType || 'contextual');
      sessionStorage.setItem('ouyang_application', link.dataset.application || '');
    });
  });
  document.querySelectorAll('a[data-contact-channel], a[data-conversion]').forEach(function (link) {
    link.addEventListener('click', function () {
      var params = new URLSearchParams(window.location.search);
      var utm = ['utm_source', 'utm_medium', 'utm_campaign'].map(function (key) { return params.get(key) || ''; });
      var eventName = link.dataset.conversion || ((link.dataset.contactChannel || 'contact') + '_click');
      var sourceName = link.dataset.source || document.title.split(' | ')[0];
      recordEvent(eventName, { source: sourceName, visual_id: link.dataset.visualId || '', channel: link.dataset.contactChannel || '' });
      sessionStorage.setItem('ouyang_entry_article', window.location.pathname);
      sessionStorage.setItem('ouyang_cta_type', eventName);
      sessionStorage.setItem('ouyang_source', sourceCategory());
      sessionStorage.setItem('ouyang_last_conversion', JSON.stringify({event:eventName, source:sourceName, landing_page:window.location.pathname, utm_source:utm[0], utm_medium:utm[1], utm_campaign:utm[2]}));
      if (utm.some(Boolean) && (link.href.indexOf('wa.me/') !== -1 || link.href.indexOf('mailto:') === 0)) link.href += encodeURIComponent('\n\nUTM: ' + utm.join(' / '));
    });
  });
  document.querySelectorAll('.private-inquiry-form').forEach(function (form) {
    form.addEventListener('submit', async function (event) {
      event.preventDefault();
      var status = form.querySelector('.form-status');
      if (!form.checkValidity()) {
        form.reportValidity();
        status.textContent = 'Please add your email or WhatsApp and a short question.';
        status.className = 'form-status is-error';
        return;
      }
      if (form.dataset.formConfigured !== 'true') {
        status.textContent = 'Private form delivery is being connected. Please use WhatsApp, email, or phone for now.';
        status.className = 'form-status is-error';
        return;
      }
      status.textContent = 'Sending your private inquiry…';
      status.className = 'form-status is-ready';
      var submitButton = form.querySelector('button[type="submit"]');
      submitButton.disabled = true;
      try {
        var response = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' }
        });
        if (!response.ok) throw new Error('Form delivery failed');
        window.location.assign('/inquiry-received/');
      } catch (error) {
        status.textContent = 'Your inquiry could not be sent. Please use WhatsApp or email and try again later.';
        status.className = 'form-status is-error';
        submitButton.disabled = false;
      }
    });
  });
}());
