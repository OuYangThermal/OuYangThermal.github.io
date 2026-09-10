# Private inquiry form activation

The public form UI is intentionally blocked until the receiving endpoint is verified. Direct WhatsApp, email, and phone links remain active.

1. Create a Formspree account at `https://formspree.io/register` using `5672306@gmail.com`.
2. Create one form named `OUYANG THERMAL Private Inquiry` and verify the notification email.
3. Copy the endpoint shown on the form's Integration page. It has the format `https://formspree.io/f/FORM_ID`.
4. In `_config.yml`, replace the empty value of `formspree_endpoint` with that complete HTTPS endpoint.
5. In the Formspree form settings, set the allowed/restricted domain to `ouyangthermal.github.io`.
6. Set the post-submission redirect to `https://ouyangthermal.github.io/inquiry-received/`.
7. Keep Formspree spam filtering enabled. The HTML form also includes the standard `_gotcha` honeypot.
8. Deploy, submit one clearly labelled test inquiry, and confirm it arrives at `5672306@gmail.com` before announcing that the form is active.

Never commit an account password, email password, secret token, or private API credential. The Formspree form endpoint ID is designed to appear in public HTML; it is not an email credential.
