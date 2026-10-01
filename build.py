# Builds the Café Waldkristall prototype pages from shared parts.
import json, pathlib
OUT = pathlib.Path(__file__).parent

PHONE = "05744 4087"
PHONE_TEL = "+4957444087"
EMAIL = "info@cafe-waldkristall.de"
ADDR1 = "Bergstraße 141"
ADDR2 = "32609 Hüllhorst-Schnathorst"
HOURS_SHORT = "Sa + So 10–18 Uhr"
BUFFET = "Frühstücksbuffet 10–13 Uhr"

ICON_IG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>'
ICON_MAIL = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 6.5 12 13l8.5-6.5"/></svg>'

NAV = [("speisekarte.html", "Speisekarte", "menu"),
       ("index.html#ueber-uns", "Über uns", "about"), ("veranstaltungen.html", "Veranstaltungen", "events"),
       ("feiern.html", "Feiern", "party"), ("index.html#kontakt", "Kontakt", "contact")]

def img(name, alt, sizes="100vw", eager=False, cls=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="assets/img/{name}-1600.webp" srcset="assets/img/{name}-800.webp 800w, assets/img/{name}-1600.webp 1600w" '
            f'sizes="{sizes}" alt="{alt}" {load}{(" class=%s" % cls) if cls else ""}>')

def _ld(canonical, title):
    """JSON-LD for inner pages: breadcrumb for every page, plus the menu on the Speisekarte page (helps Google and AI answers)."""
    import json as _j
    if canonical == "/": return ""
    base = "https://www.cafe-waldkristall.de"
    name = title.split(" | ")[0].replace("&amp;", "&")
    data = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Start", "item": base + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": base + canonical}]}]
    if canonical.strip("/") == "speisekarte":
        def offer(p): return {"@type": "Offer", "price": p, "priceCurrency": "EUR"}
        data.append({"@context": "https://schema.org", "@type": "Menu", "name": "Speisekarte Café Waldkristall", "url": base + canonical, "inLanguage": "de",
            "hasMenuSection": [
                {"@type": "MenuSection", "name": "Frühstücksbuffet", "description": "Samstag und Sonntag 10–13 Uhr, Getränke extra", "hasMenuItem": [
                    {"@type": "MenuItem", "name": "Frühstücksbuffet für Erwachsene", "offers": offer("25.50")},
                    {"@type": "MenuItem", "name": "Frühstücksbuffet für Kinder von 3 bis 13 Jahren", "offers": offer("9.00")}]},
                {"@type": "MenuSection", "name": "Getränke"},
                {"@type": "MenuSection", "name": "Kuchen & Torten", "description": "Hausgemacht mit Dinkelmehl, ab 5,30 €"},
                {"@type": "MenuSection", "name": "Waffeln"},
                {"@type": "MenuSection", "name": "Herzhaftes für Zwischendurch", "description": "Suppen, Strammer Max und mehr"}]})
    return "".join('<script type="application/ld+json">' + _j.dumps(d, ensure_ascii=False) + '</script>\n' for d in data)

def head(title, desc, canonical, extra=""):
    extra = extra + _ld(canonical, title)
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.cafe-waldkristall.de{canonical}">
<meta name="theme-color" content="#3E2C22">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:image" content="https://www.cafe-waldkristall.de/assets/img/fruehstuecksbuffet-1600.webp">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preload" href="assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
{extra}</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
'''

def header(active):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if k == active else ""}>{t}</a>' for h, t, k in NAV)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t, k in NAV)
    return f'''<header class="header">
  <div class="wrap header__in">
    <a class="header__logo" href="index.html" aria-label="Café Waldkristall – Startseite"><img src="assets/img/logo-weiss.webp" width="640" height="414" alt="Café Waldkristall"></a>
    <nav class="nav" aria-label="Hauptmenü">{links}</nav>
    <a class="btn btn--primary header__cta" href="index.html#reservieren">Tisch reservieren</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><span>Menü</span>
    </button>
  </div>
</header>
<nav class="mnav" id="mnav" aria-label="Menü">
  {mlinks}
  <a class="btn btn--primary mnav__cta" href="index.html#reservieren">Tisch reservieren</a>
  <p class="mnav__facts">{HOURS_SHORT} · {BUFFET}<br><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</nav>
<main id="inhalt">
'''

def footer():
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <img class="footer__logo" src="assets/img/logo-weiss.webp" width="640" height="414" alt="Café Waldkristall" loading="lazy">
        <p>Genuss. Freude. Entspannung.<br>Mitten im Wiehengebirge.</p>
        <ul class="social-list">
          <li><a class="social" href="https://www.instagram.com/cafe_waldkristall/" rel="noopener">{ICON_IG}<span>@cafe_waldkristall</span></a></li>
          <li><a class="social" href="newsletter.html">{ICON_MAIL}<span>Newsletter abonnieren</span></a></li>
        </ul>
      </div>
      <div>
        <h2>Besuch</h2>
        <p><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Caf%C3%A9+Waldkristall+Bergstra%C3%9Fe+141+32609+H%C3%BCllhorst" rel="noopener" aria-label="Route zum Café Waldkristall in Google Maps">{ADDR1}<br>{ADDR2}</a></p>
        <p>{HOURS_SHORT}<br>{BUFFET}</p>
      </div>
      <div>
        <h2>Kontakt</h2>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h2>Mehr</h2>
        <ul>
          <li><a href="speisekarte.html">Speisekarte</a></li>
          <li><a href="veranstaltungen.html">Veranstaltungen</a></li>
          <li><a href="feiern.html">Feiern &amp; Hochzeiten</a></li>
          <li><a href="index.html#gutscheine">Gutscheine</a></li>
          <li><a href="jobs.html">Jobs</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year></span> Café Waldkristall — Ulrike Lohrmann · Website von Aptifex Works</span>
      <span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span>
    </div>
  </div>
</footer>
<div class="reservebar">
  <a class="btn btn--primary" href="index.html#reservieren">Tisch reservieren</a>
  <a class="btn btn--ghost" href="tel:{PHONE_TEL}" aria-label="Anrufen: {PHONE}">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>Anrufen
  </a>
</div>
<script src="assets/js/site.js" defer></script>
</body>
</html>
'''

def gastro(kind):
    if kind == "reservation":
        t, b = "Tisch online reservieren", "Reservierung öffnen"
    else:
        t, b = "Gutschein online bestellen", "Gutschein-Shop öffnen"
    return f'''<div class="embed" data-gastronovi="{kind}">
  <p><b>{t}</b><br>Wir nutzen dafür den Dienst Gastronovi. Er wird erst geladen, wenn Du auf den Button tippst.</p>
  <button class="btn btn--primary" type="button">{b}</button>
  <p class="small">Mehr dazu in unserer <a href="datenschutz.html#gastronovi">Datenschutzerklärung</a>. Lieber persönlich? <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
</div>'''

def newsletter_form(compact=False):
    names = "" if compact else '''
  <div class="field--row">
    <div class="field"><label for="n-vorname">Vorname</label><input id="n-vorname" name="FNAME" autocomplete="given-name"></div>
    <div class="field"><label for="n-nachname">Nachname</label><input id="n-nachname" name="LNAME" autocomplete="family-name"></div>
  </div>'''
    return f'''<form class="form form--nl" data-newsletter novalidate>
  <div class="field"><label for="n-mail{'c' if compact else ''}">E-Mail-Adresse <span class="req">*</span></label><input id="n-mail{'c' if compact else ''}" name="EMAIL" type="email" autocomplete="email" required><span class="err">Bitte gib eine gültige E-Mail-Adresse an.</span></div>{names}
  <button class="btn btn--primary" type="submit">Newsletter abonnieren</button>
  <p class="small" style="margin:0">Du bekommst zuerst eine E-Mail, in der Du Deine Anmeldung bestätigst. Abmelden kannst Du Dich jederzeit über den Link im Newsletter. Mehr in der <a href="datenschutz.html#newsletter">Datenschutzerklärung</a>.</p>
  <div class="form__ok" role="status"><div class="tick">✓</div><h3>Fast geschafft!</h3><p>Bitte schau in Dein Postfach und bestätige Deine Anmeldung.</p></div>
</form>'''

SCHEMA = {
  "@context": "https://schema.org", "@type": "CafeOrCoffeeShop",
  "name": "Café Waldkristall", "url": "https://www.cafe-waldkristall.de/",
  "telephone": "+49 5744 4087", "email": EMAIL,
  "image": "https://www.cafe-waldkristall.de/assets/img/fruehstuecksbuffet-1600.webp",
  "priceRange": "10–20 €",
  "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "postalCode": "32609",
              "addressLocality": "Hüllhorst", "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"],
                                 "opens": "10:00", "closes": "18:00"}],
  "servesCuisine": ["Frühstück", "Kaffee und Kuchen"],
  "acceptsReservations": True,
  "menu": "https://www.cafe-waldkristall.de/speisekarte/",
  "sameAs": ["https://www.instagram.com/cafe_waldkristall/"]
}


import re as _re
# Keep things together that must never split across two lines (emails, E-Mail, phone, times, amounts, short hyphen words)
_NOBR=[r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', r'E-Mail(?:-Adresse)?', r'(?:\+49 |0)\d{3,5}[ /]\d{3,8}',
       r'\d+,\d{2}\s€', r'\d{1,2}(?::\d{2})?\s?[–-]\s?\d{1,2}(?::\d{2})?\s(?:Uhr)', r'\d+\s(?:Uhr|Std\.|Personen|Gäste|Jahre|Jahren|Plätze|Plätzen|Tassen|Minuten)',
       r'Sa \+ So', r'(?<![\w-])[A-Za-zÄÖÜäöüß]+-[A-Za-zÄÖÜäöüß]+(?![\w-])']
_NOBR_RE=_re.compile('|'.join('(?:%s)'%p for p in _NOBR))
def _nobr_text(t):
    def f(m):
        s=m.group(0)
        if '-' in s and '@' not in s and not s.startswith('E-Mail') and len(s)>22: return s  # very long compounds may still break
        return '<span class="nobr">'+s+'</span>'
    return _NOBR_RE.sub(f,t)
def nobr(html):
    head,sep,body=html.partition('<body')
    parts=_re.split(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)',body,flags=_re.S)
    return head+sep+''.join(p if p.startswith('<') else _nobr_text(p) for p in parts)

def write(name, html):
    html = nobr(html)
    (OUT / name).write_text(html, encoding="utf-8")
    print("wrote", name, len(html))

import pages
G = dict(globals())
for name, fn in pages.PAGES.items():
    write(name, fn(G))
