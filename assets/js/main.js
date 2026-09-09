document.documentElement.classList.add('js');

(function () {
  'use strict';
  function sourceCategory() {
    var params = new URLSearchParams(window.location.search);
    var utm = (params.get('utm_source') || '').toLowerCase();
    var referrer = (document.referrer || '').toLowerCase();
    if (utm.indexOf('chatgpt') !== -1 || referrer.indexOf('chatgpt.com') !== -1 || referrer.indexOf('openai.com') !== -1) return 'ChatGPT / AI Referral';
    if (/google\.|bing\.|duckduckgo\.|yahoo\.|baidu\./.test(referrer)) return 'Organic';
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
  document.querySelectorAll('.engineering-form').forEach(function (form) {
    var entry = form.querySelector('[name="entry_article"]');
    var cta = form.querySelector('[name="cta_type"]');
    var source = form.querySelector('[name="source"]');
    var stage = form.querySelector('[name="conversion_stage"]');
    var application = form.querySelector('[data-application-field]');
    if (entry) entry.value = sessionStorage.getItem('ouyang_entry_article') || 'Direct landing page';
    if (cta) cta.value = sessionStorage.getItem('ouyang_cta_type') || 'Direct navigation';
    if (source) source.value = sourceCategory();
    if (stage) stage.value = form.dataset.conversionStage || '';
    if (application && !application.value) {
      var savedApplication = sessionStorage.getItem('ouyang_application') || '';
      if (application.tagName === 'SELECT' && Array.from(application.options).some(function (option) { return option.value === savedApplication; })) application.value = savedApplication;
      if (application.tagName === 'INPUT') application.value = savedApplication;
    }
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var status = form.querySelector('.form-status');
      if (!form.checkValidity()) {
        form.reportValidity();
        status.textContent = 'Complete the required engineering and contact fields before review.';
        status.className = 'form-status is-error';
        return;
      }
      status.textContent = 'The form is complete, but no receiving service is connected. Nothing has been transmitted or stored.';
      status.className = 'form-status is-ready';
    });
  });
}());
