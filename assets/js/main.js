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
      sessionStorage.setItem('ouyang_entry_article', window.location.pathname);
      sessionStorage.setItem('ouyang_cta_type', eventName);
      sessionStorage.setItem('ouyang_source', sourceCategory());
      sessionStorage.setItem('ouyang_last_conversion', JSON.stringify({event:eventName, source:sourceName, landing_page:window.location.pathname, utm_source:utm[0], utm_medium:utm[1], utm_campaign:utm[2]}));
      if (utm.some(Boolean) && (link.href.indexOf('wa.me/') !== -1 || link.href.indexOf('mailto:') === 0)) link.href += encodeURIComponent('\n\nUTM: ' + utm.join(' / '));
    });
  });
  document.querySelectorAll('.private-inquiry-form').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      var status = form.querySelector('.form-status');
      if (!form.checkValidity()) {
        event.preventDefault();
        form.reportValidity();
        status.textContent = 'Please add your email or WhatsApp and a short question.';
        status.className = 'form-status is-error';
        return;
      }
      if (form.dataset.formConfigured !== 'true') {
        event.preventDefault();
        status.textContent = 'Private form delivery is being connected. Please use WhatsApp, email, or phone for now.';
        status.className = 'form-status is-error';
        return;
      }
      status.textContent = 'Sending your private inquiry…';
      status.className = 'form-status is-ready';
      form.querySelector('button[type="submit"]').disabled = true;
    });
  });
}());
