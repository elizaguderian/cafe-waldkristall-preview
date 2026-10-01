# Page content for the Café Waldkristall prototype. Texts use Ulrike's own words from the old site.
import json

def home(g):
    img, gastro = g["img"], g["gastro"]
    schema = '<script type="application/ld+json">' + json.dumps(g["SCHEMA"], ensure_ascii=False) + '</script>\n'
    return g["head"]("Frühstücksbuffet in Hüllhorst | Café Waldkristall",
        "Frühstücksbuffet Sa + So 10–13 Uhr, hausgemachte Kuchen mit Dinkelmehl und Waffeln im Fachwerkhaus am Waldrand. Jetzt Tisch reservieren.",
        "/", '<link rel="preload" as="image" href="assets/img/terrasse-garten-800.webp" imagesrcset="assets/img/terrasse-garten-800.webp 800w, assets/img/terrasse-garten-1600.webp 1600w" imagesizes="100vw" fetchpriority="high">\n' + schema) + g["header"]("home") + f'''
<section class="hero" id="start">
  <div class="hero__img">{img("terrasse-garten", "Holzterrasse mit rustikalen Sitzbänken im Garten des Café Waldkristall am Waldrand", eager=True)}</div>
  <div class="wrap">
    <img class="hero__logo" src="assets/img/logo-weiss.webp" width="640" height="414" alt="">
    <h1>Frühstücksbuffet &amp; Kuchen im Wiehengebirge</h1>
    <p class="hero__sub">Kleine Auszeit am Waldrand: im alten Fachwerkhaus in Hüllhorst, direkt am Wittekindsweg.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="#reservieren">Tisch reservieren</a>
      <a class="btn btn--light" href="speisekarte.html">Speisekarte ansehen</a>
    </div>
    <p class="hero__meta"><span>{g["HOURS_SHORT"]}</span><span>{g["BUFFET"]}</span></p>
  </div>
</section>

<div class="wrap">
  <dl class="facts">
    <div class="fact"><dt>Geöffnet</dt><dd>{g["HOURS_SHORT"]}</dd></div>
    <div class="fact"><dt>Frühstück</dt><dd>Buffet 10–13 Uhr</dd></div>
    <div class="fact"><dt>Adresse</dt><dd><a href="#anfahrt">{g["ADDR1"]}, Hüllhorst</a></dd></div>
    <div class="fact"><dt>Telefon</dt><dd><a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a></dd></div>
  </dl>
</div>

<section class="moments" aria-label="Eindrücke aus dem Café Waldkristall">
  <div class="wrap">
    <p class="moments__motto">„Komm als Gast und geh als Freund.“</p>
    <div class="moments__grid">
      <figure>{img("fruehstuecksbuffet", "Frühstücksplatte vom Buffet mit hausgemachten Aufstrichen", "(min-width:700px) 33vw, 80vw")}<figcaption>Für einen perfekten Start in den Tag.</figcaption></figure>
      <figure class="moments__squirrel">{img("eichhoernchen-wald", "Eichhörnchen im Wald", "(min-width:700px) 33vw, 80vw")}<figcaption>Kleine Auszeit am Waldrand.</figcaption></figure>
      <figure>{img("gebaeck", "Frisch gebackenes Gebäck auf dem Buffet", "(min-width:700px) 33vw, 80vw")}<figcaption>Selbstgebacken und handverlesen.</figcaption></figure>
    </div>
  </div>
</section>

<section class="section" id="willkommen">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Ankommen, durchatmen, genießen.</span>
    <h2>Willkommen im Café Waldkristall</h2>
    <p class="lead">Das Café Waldkristall lädt Dich zu einer ganz besonderen Auszeit am Waldrand ein – fernab vom Alltag, mitten in der Natur.</p>
    <p>Hier treffen frische, liebevoll zubereitete Gerichte auf den rustikalen Charme eines alten Fachwerkhauses und die wohltuende Ruhe des Waldes. Lass Deinen Gaumen verwöhnen, gönn Deiner Seele eine Pause und genieß einfach den Moment – und den Ausblick.</p>
    <p>Bei uns ist jeder willkommen – ob jung oder alt, mit oder ohne Instrument, auf zwei oder vier Beinen. Komm einfach vorbei, mach’s Dir gemütlich – wir freuen uns sehr auf Dich!</p>
    <p class="sig">Deine Ulrike Lohrmann<br><span class="small">Inhaberin Café Waldkristall</span></p>
  </div>
</section>

<section class="section section--card" id="genuss">
  <div class="wrap split">
    <div class="split__img split__img--tall reveal">{img("brotzeit", "Brotzeit mit Dinkelbrot, Käse und Schinken auf einem Holzbrett", "(min-width:700px) 50vw, 100vw")}</div>
    <div class="reveal">
      <span class="eyebrow">Für einen perfekten Start in den Tag</span>
      <h2>Frühstücksbuffet am Samstag und Sonntag</h2>
      <img class="cats" src="assets/img/katzen-gold.png" width="316" height="354" alt="" loading="lazy">
      <p class="lead"><b>Perfekt für Langschläfer:</b> Samstags und sonntags sind wir von 10 bis 18 Uhr für Dich da. Unser reichhaltiges Frühstücksbuffet erwartet Dich an beiden Tagen von 10 bis 13 Uhr.</p>
      <p>Brötchen vom Natur-Bäcker, hausgebackenes Dinkelbrot, hausgemachte Fruchtaufstriche, Imkerhonig, Rührei, Lachs und Forelle, Salate der Saison und vieles mehr.</p>
      <div class="pricebox">
        <div class="price"><strong>25,50 €</strong><span>Erwachsene</span></div>
        <div class="price"><strong>9,00 €</strong><span>Kinder 3–13 Jahre</span></div>
      </div>
      <p class="small">Frühstück pro Person, inkl. MwSt., ohne Getränke. Gerne servieren wir Kaffeespezialitäten, Tee, Kakao und kalte Getränke à la carte.</p>
      <div class="btn-row"><a class="btn btn--primary" href="#reservieren">Jetzt reservieren</a><a class="btn btn--ghost" href="speisekarte.html#fruehstueck">Alles, was aufs Buffet kommt</a></div>
    </div>
  </div>
</section>

<section class="section" id="kuchen">
  <div class="wrap">
    <span class="eyebrow">Genuss, der von Herzen kommt</span>
    <h2>Ehrlich, hausgemacht und ohne Schnickschnack</h2>
    <p class="lead" style="max-width:62ch">Wir lieben gutes Essen – ehrlich, hausgemacht und ohne Schnickschnack. Unsere Zutaten kommen aus der Region, unsere Rezepte direkt aus der Seele.</p>
    <p style="max-width:62ch">Bei uns findest Du Leckereien ohne Geschmacksverstärker, Zusätze oder unnötige Hilfsmittelchen – dafür aber mit jeder Menge Liebe. Und: Wir verzichten ganz bewusst auf Weizenmehl und backen ausschließlich mit Dinkelmehl der Porta Mühle aus Minden.</p>
    <p style="max-width:62ch">Du hast Fragen zu Zutaten, Unverträglichkeiten oder möchtest einfach ein bisschen schnacken? Sprich uns gerne an!</p>
    <div class="cards cards--3" style="margin-top:28px">
      <a class="card card--link reveal" href="speisekarte.html#kuchen">
        <div class="card__img">{img("sahnetorte", "Stück Sahnetorte mit Blüten auf einem Holzbrett", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Kaffee &amp; Kuchen – mit einer Prise Kindheit</h3><p>Selbstgebacken und handverlesen: Kuchen, Torten, Waffeln und feines Gebäck, dazu Kaffee und Tee in bester Bioqualität.</p><span class="more">Zur Kuchenkarte</span></div>
      </a>
      <a class="card card--link reveal" href="speisekarte.html#herzhaftes">
        <div class="card__img">{img("fruehstueck-eier", "Strammer Max mit zwei Spiegeleiern auf Dinkelbrot", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Herzhaftes aus der Waldküche</h3><p>Von liebevoll zubereiteten Snacks bis zu wechselnden Tagesgerichten. Frag uns einfach, was heute auf dem Herd steht!</p><span class="more">Zur Speisekarte</span></div>
      </a>
      <a class="card card--link reveal" href="#gutscheine">
        <div class="card__img">{img("cappuccino-kuchen", "Zwei Cappuccino mit Milchschaum-Herz und ein Stück Kuchen", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Verschenke eine Auszeit</h3><p>Ob für Freundinnen, Familie oder Kolleginnen: Mit einem Gutschein verschenkst Du eine Portion Ruhe, Genuss und ganz viel Herz.</p><span class="more">Gutschein bestellen</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--bark" id="ueber-uns">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Über uns</span>
      <p class="quote">„Wie ein Besuch bei Freunden.“</p>
      <p class="sig">Ulrike Lohrmann, Inhaberin Café Waldkristall</p>
      <p class="lead">So fühlt es sich an, wenn Du bei uns im Café Waldkristall bist. Mitten im schönen Wiehengebirge gelegen, mit einem traumhaften Blick ins Teutoburger Land, ist unser Fachwerkhaus seit 2006 ein Ort zum Ankommen, Durchatmen und Verweilen.</p>
      <p>Ob draußen auf der Terrasse bei Sonnenschein oder drinnen am knisternden Kaminfeuer – hier darfst Du einfach Du selbst sein. Und in der kalten Jahreszeit warten unsere gemütlichen Outdoor-Hütten auf Dich.</p>
      <p>Übrigens: Bei uns wird auch musiziert – ganz spontan, ganz herzlich.</p>
      <p><b>Unser Motto: Genuss. Entspannung. Freude.</b> Und genau diese Mischung findest Du bei uns – nicht nur auf dem Teller, sondern auch im Herzen.</p>
    </div>
    <div class="split__img reveal">{img("fachwerkhaus-winter", "Das Fachwerkhaus des Café Waldkristall im Winter, verschneit am Waldrand", "(min-width:700px) 50vw, 100vw")}</div>
  </div>
</section>

<section class="section section--forest" id="feiern">
  <div class="wrap">
    <div class="feature reveal">
      <div class="feature__body">
        <span class="eyebrow">Du planst eine Feier?</span>
        <h2>Feiern im Café Waldkristall</h2>
        <p>Für Familienfeiern, Hochzeiten, Jubiläen und geschlossene Gesellschaften von 20 bis 50 Personen öffnen wir nach Absprache auch außerhalb unserer regulären Öffnungszeiten.</p>
        <ul class="checklist">
          <li>Gruppen von 20 bis 50 Personen</li>
          <li>Drinnen bis zu 50 Gäste, bei gutem Wetter wird draußen weitergefeiert</li>
          <li>Schreib uns oder ruf uns an, dann planen wir gemeinsam Deinen Wunschtermin</li>
        </ul>
        <div class="btn-row"><a class="btn btn--primary" href="feiern.html#anfrage">Feier anfragen</a></div>
      </div>
      <div class="feature__img">{img("terrasse-ausblick", "Sonnige Terrasse am Fachwerkhaus des Café Waldkristall mit Blick ins Grüne", "(min-width:700px) 45vw, 100vw")}</div>
    </div>
  </div>
</section>

<section class="section section--card" id="freude">
  <div class="wrap split split--rev">
    <div class="split__img reveal">{img("livemusik-gitarre", "Nahaufnahme einer Gitarre bei einem Livemusik-Abend", "(min-width:700px) 50vw, 100vw")}</div>
    <div class="reveal">
      <span class="eyebrow">Freude. Musik. Gemeinschaft.</span>
      <h2>Livemusik, Yoga &amp; Workshops</h2>
      <p class="lead">Im Café Waldkristall bist Du nicht einfach nur Gast – Du bist Teil der Gemeinschaft. Regelmäßig verwandeln Musiker aus aller Welt unser Café in einen kleinen, gemütlichen Konzertsaal mit Wohnzimmer-Charme.</p>
      <p>Dazu finden in unseren gemütlichen Räumlichkeiten regelmäßig Kurse und Workshops statt – Yoga und mehr, mit tollen Partnern. Und unser Seminarraum steht auch Dir offen.</p>
      <div class="btn-row"><a class="btn btn--primary" href="veranstaltungen.html">Termine, Yoga &amp; Kurse</a></div>
    </div>
  </div>
</section>

<section class="section" id="anfahrt">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Beliebtes Ausflugsziel mitten in der Natur</span>
      <h2>Mitten im Wiehengebirge, direkt am Wittekindsweg</h2>
      <p class="lead">Suchst Du einen Ort, der Dich runterbringt und inspiriert? Dann schnapp Dir bequeme Schuhe, mach einen Spaziergang durchs Wiehengebirge und komm anschließend bei uns vorbei – mitten auf dem Wiehenkamm, direkt am Wittekindsweg.</p>
      <p>Hier erwartet Dich nicht nur ein herrlicher Ausblick, sondern auch jede Menge Wohlfühlmomente: leckere Speisen, ein warmes Getränk, ein Lächeln – und ganz viel Natur ringsum. Ein echtes Seelenplätzchen für Naturliebhaber – und vielleicht auch für Dich?</p>
      <p><b>Knöllchen-Allergie?</b> Dann haben wir einen kleinen, aber feinen Tipp für Dich: Bitte nutze einen unserer 3 ausgewiesenen Parkplätze … denn wer weiß schon, wann die Waldhexe wieder unterwegs ist 😉</p>
      <div class="btn-row">
        <a class="btn btn--ghost" href="https://www.google.com/maps/dir/?api=1&amp;destination=Caf%C3%A9+Waldkristall+Bergstra%C3%9Fe+141+32609+H%C3%BCllhorst" rel="noopener">Route mit Google Maps planen</a>
        <a class="btn btn--ghost" href="https://www.komoot.de/highlight/115620" rel="noopener">Rad- &amp; Wanderroute auf Komoot</a>
      </div>
    </div>
    <div class="anfahrt__media reveal"><div class="duck">{img("fachwerkhaus-sommer", "Das Fachwerkhaus des Café Waldkristall im Sommer, umgeben von Wald", "(min-width:700px) 50vw, 100vw")}</div>
    <figure class="parkmap"><img src="assets/img/parkplan.svg" width="480" height="520" alt="Lageplan: Das Café Waldkristall liegt an der Bergstraße. Drei ausgewiesene Parkplätze mit 10, 10 und 30 Plätzen." loading="lazy"><figcaption class="small">Unsere 3 ausgewiesenen Parkplätze an der Bergstraße</figcaption></figure></div>
  </div>
</section>

<section class="section section--bark" id="reservieren">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Reservierung</span>
    <h2>Sichere Dir Deinen Lieblingsplatz</h2>
    <p class="lead">Du möchtest Dir Deinen Lieblingsplatz bei uns sichern? Kein Problem! Reserviere online oder ruf uns an: <a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a>.</p>
    <ul class="checklist">
      <li>Gruppen ab 9 Personen reservieren bitte per Telefon oder E-Mail an <a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a></li>
      <li>Feier mit 20 bis 50 Gästen? <a href="feiern.html">Hier geht’s zur Feier-Anfrage</a></li>
    </ul>
    {gastro("reservation")}
  </div>
</section>

<section class="section" id="gutscheine">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Gutscheine</span>
    <h2>Verschenke eine Auszeit</h2>
    <p class="lead">Eine kleine Pause vom Alltag ist manchmal das schönste Geschenk. Ob für Freundinnen, Familie oder Kolleginnen: Mit einem Gutschein vom Café Waldkristall verschenkst Du eine Portion Ruhe, Genuss und ganz viel Herz.</p>
    <p>Bestell Deinen Gutschein einfach über das Formular, er wird Dir automatisch per E-Mail geschickt.</p>
    {gastro("voucher")}
  </div>
</section>

<section class="section section--card" id="jobs">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Jobs im Café Waldkristall</span>
      <h2>Arbeite mit uns am Waldrand</h2>
      <p>Du hast Erfahrung in der Gastronomie und suchst eine neue Herausforderung – am liebsten in einem herzlichen Team und mitten in der Natur? Dann bist Du bei uns genau richtig!</p>
      <p class="small">Aktuell suchen wir: Servicefachkraft (m/w/d) in Teilzeit (20 Std.) · Hauswirtschaftliche Kraft (m/w/d) in Teilzeit</p>
      <div class="btn-row"><a class="btn btn--primary" href="jobs.html">Offene Stellen &amp; Bewerbung</a></div>
    </div>
    <div class="split__img reveal">{img("teig-kneten", "Hände kneten Teig für frisches Gebäck", "(min-width:700px) 50vw, 100vw")}</div>
  </div>
</section>

<section class="section" id="fragen">
  <div class="wrap faq">
    <div class="faq__intro reveal">
      <span class="eyebrow">Gut zu wissen</span>
      <h2>Häufige Fragen</h2>
      <p>Kurze Antworten auf das, was Gäste uns am häufigsten fragen.</p>
      <p class="small">Noch etwas offen? Ruf uns an: <a href="tel:+4957444087">05744 4087</a></p>
    </div>
    <div class="faq__list reveal">
      <details class="faq__item"><summary>Wann hat das Café Waldkristall geöffnet?</summary><p>Samstags und sonntags von 10 bis 18 Uhr. Das Frühstücksbuffet gibt es an beiden Tagen von 10 bis 13 Uhr. Montag bis Freitag ist geschlossen, außer für Feiern nach Absprache.</p></details>
      <details class="faq__item"><summary>Was kostet das Frühstücksbuffet?</summary><p>25,50 € für Erwachsene und 9,00 € für Kinder von 3 bis 13 Jahren, inkl. MwSt., ohne Getränke. Kaffee, Tee und Saft bestellst Du à la carte dazu.</p></details>
      <details class="faq__item"><summary>Wie reserviere ich einen Tisch?</summary><p>Online über den Button „Tisch reservieren“ oder telefonisch unter 05744 4087. Gruppen ab 9 Personen reservieren bitte per Telefon oder E-Mail an info@cafe-waldkristall.de.</p></details>
      <details class="faq__item"><summary>Gibt es vegane oder vegetarische Speisen?</summary><p>Ja. Auf dem Buffet stehen zum Beispiel vegane Fruchtaufstriche, Linsenfrikadellen und eine vegane Gemüsesuppe. Wir backen ohne Weizenmehl, nur mit Dinkelmehl der Porta Mühle. Bei Unverträglichkeiten sprich uns einfach an.</p></details>
      <details class="faq__item"><summary>Wo kann ich parken?</summary><p>An der Bergstraße gibt es 3 ausgewiesene Parkplätze mit zusammen rund 50 Plätzen. Zu Fuß erreichst Du uns direkt über den Wittekindsweg.</p></details>
      <details class="faq__item"><summary>Kann ich im Café Waldkristall feiern oder heiraten?</summary><p>Ja. Familienfeiern, Hochzeiten und Jubiläen mit 20 bis 50 Gästen, nach Absprache auch außerhalb der Öffnungszeiten. Bei gutem Wetter feiert Ihr auf der Terrasse und im Garten weiter.</p></details>
      <details class="faq__item"><summary>Gibt es Gutscheine?</summary><p>Ja. Du bestellst den Gutschein online, er kommt automatisch per E-Mail zu Dir.</p></details>
      <details class="faq__item"><summary>Darf ich meinen Hund mitbringen?</summary><p>Ja, Gäste auf vier Beinen sind bei uns willkommen. Bitte führe Deinen Hund an der Leine.</p></details>
    </div>
  </div>
  <script type="application/ld+json">{{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{{"@type": "Question", "name": "Wann hat das Café Waldkristall geöffnet?", "acceptedAnswer": {{"@type": "Answer", "text": "Samstags und sonntags von 10 bis 18 Uhr. Das Frühstücksbuffet gibt es an beiden Tagen von 10 bis 13 Uhr. Montag bis Freitag ist geschlossen, außer für Feiern nach Absprache."}}}}, {{"@type": "Question", "name": "Was kostet das Frühstücksbuffet?", "acceptedAnswer": {{"@type": "Answer", "text": "25,50 € für Erwachsene und 9,00 € für Kinder von 3 bis 13 Jahren, inkl. MwSt., ohne Getränke. Kaffee, Tee und Saft bestellst Du à la carte dazu."}}}}, {{"@type": "Question", "name": "Wie reserviere ich einen Tisch?", "acceptedAnswer": {{"@type": "Answer", "text": "Online über den Button „Tisch reservieren“ oder telefonisch unter 05744 4087. Gruppen ab 9 Personen reservieren bitte per Telefon oder E-Mail an info@cafe-waldkristall.de."}}}}, {{"@type": "Question", "name": "Gibt es vegane oder vegetarische Speisen?", "acceptedAnswer": {{"@type": "Answer", "text": "Ja. Auf dem Buffet stehen zum Beispiel vegane Fruchtaufstriche, Linsenfrikadellen und eine vegane Gemüsesuppe. Wir backen ohne Weizenmehl, nur mit Dinkelmehl der Porta Mühle. Bei Unverträglichkeiten sprich uns einfach an."}}}}, {{"@type": "Question", "name": "Wo kann ich parken?", "acceptedAnswer": {{"@type": "Answer", "text": "An der Bergstraße gibt es 3 ausgewiesene Parkplätze mit zusammen rund 50 Plätzen. Zu Fuß erreichst Du uns direkt über den Wittekindsweg."}}}}, {{"@type": "Question", "name": "Kann ich im Café Waldkristall feiern oder heiraten?", "acceptedAnswer": {{"@type": "Answer", "text": "Ja. Familienfeiern, Hochzeiten und Jubiläen mit 20 bis 50 Gästen, nach Absprache auch außerhalb der Öffnungszeiten. Bei gutem Wetter feiert Ihr auf der Terrasse und im Garten weiter."}}}}, {{"@type": "Question", "name": "Gibt es Gutscheine?", "acceptedAnswer": {{"@type": "Answer", "text": "Ja. Du bestellst den Gutschein online, er kommt automatisch per E-Mail zu Dir."}}}}, {{"@type": "Question", "name": "Darf ich meinen Hund mitbringen?", "acceptedAnswer": {{"@type": "Answer", "text": "Ja, Gäste auf vier Beinen sind bei uns willkommen. Bitte führe Deinen Hund an der Leine."}}}}]}}</script>
</section>

<section class="section section--card" id="kontakt">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Kontakt</span>
      <h2>Komm als Gast und geh als Freund.</h2>
      <p class="lead">Café Waldkristall<br>Inhaberin Ulrike Lohrmann<br>{g["ADDR1"]}<br>{g["ADDR2"]}</p>
      <p><a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a><br><a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a></p>
      <p class="quicklinks"><a href="#reservieren">Tisch reservieren</a><a href="feiern.html#anfrage">Feier anfragen</a></p>
      <figure class="motto-sign">{img("giebel-schild", "Grüner Giebel des Café Waldkristall mit Holzschild und Laterne", "260px")}</figure>
    </div>
    <div>
      <h3>Öffnungszeiten</h3>
      <table class="hours">
        <tr><td>Samstag</td><td>10–18 Uhr</td></tr>
        <tr><td>Sonntag</td><td>10–18 Uhr</td></tr>
        <tr><td>Frühstücksbuffet</td><td>10–13 Uhr</td></tr>
        <tr><td>Montag bis Freitag</td><td>Geschlossen</td></tr>
      </table>
      <p class="small" style="margin-top:12px">Für Feiern ab 20 Personen öffnen wir nach Absprache auch außerhalb dieser Zeiten.</p>
    </div>
  </div>
</section>
''' + g["footer"]()


MENU_FRUEH = ["gemischte Brötchen vom Natur-Bäcker", "hausgebackenes Dinkelbrot", "Butter und Pflanzen-Margarine",
  "hausgemachte Fruchtaufstriche (vegan)", "Imkerhonig", "Müsli und Cornflakes mit Milch oder Haferdrink",
  "Obstsalat &amp; Joghurtvariante (hausgemacht)", "hausgemachte Salate der Saison", "Linsenfrikadellen (vegan)",
  "frische Gemüseplatte der Saison", "Aufschnittplatten mit Käse und Wurst", "geräucherter Lachs und Forelle mit Sahnemeerrettich",
  "gekochte Eier, Rührei, gebratener Speck", "überbackener Gemüsetoast",
  "Gemüsesuppe der Saison, hausgemacht und vegan, mit verschiedenen Toppings", "hausgemachte Waldlimonade"]
DRINKS = [("Kanne Frühstückskaffee klein", "8,90 €", "4 Tassen"), ("Kanne Frühstückskaffee groß", "14,50 €", "7 Tassen"),
  ("Glas Orangensaft", "3,50 €", "0,2 l"), ("Karaffe Orangensaft", "8,90 €", "1,0 l"), ("Glas Sekt", "5,50 €", "0,1 l"),
  ("Glas Sekt alkoholfrei", "4,90 €", "0,1 l"), ("Glas Sekt mit Orangensaft", "4,50 €", "0,1 l"), ("Aperol Spritz", "7,50 €", "0,4 l")]
CAKES = [("Streuselkuchen", "5,30 €", ""), ("Käsekuchen", "5,30 €", ""), ("Sahnetorte der Saison", "5,90 €", ""), ("Sahne zum Kuchen", "1,10 €", "")]
WAFFLES = [("Waffeln mit Puderzucker, Zimt &amp; Zucker", "5,50 €", ""), ("heiße Kirschen", "2,90 €", "zur Waffel"),
  ("Sahne", "1,10 €", "zur Waffel"), ("Eis", "1,50 €", "zur Waffel"), ("Eierlikör", "1,60 €", "zur Waffel"), ("Schokosoße", "0,90 €", "zur Waffel")]
SAVORY = [("Tomatensuppe vegan", "6,50 €", ""), ("Tomatensuppe vegetarisch", "7,50 €", "mit Sahne"),
  ("Möhrensuppe vegan", "6,50 €", ""), ("Möhrensuppe vegetarisch", "7,50 €", "mit Sahne"),
  ("Gulaschsuppe", "9,50 €", "mit Rindfleisch gekocht"), ("Strammer Max", "12,50 €", "Dinkelbrot mit Schwarzwälder Schinken und zwei Spiegeleiern"),
  ("Strammer Max &amp; Antje", "14,00 €", "mit Käse überbacken"), ("Brotzeit", "9,90 €", "2 Scheiben Brot, Butter, Schinken, Salami, Käse")]

def items(rows):
    return '<ul class="menu-list">' + "".join(
        f'<li class="menu-item"><b>{n}</b><span class="p">{p}</span>{f"<small>{s}</small>" if s else ""}</li>' for n, p, s in rows) + "</ul>"

def menu(g):
    img = g["img"]
    return g["head"]("Speisekarte & Preise | Café Waldkristall Hüllhorst",
        "Frühstücksbuffet 25,50 €, hausgemachte Kuchen ab 5,30 €, Waffeln, Suppen und Strammer Max: die ganze Speisekarte vom Café Waldkristall im Wiehengebirge.",
        "/speisekarte/") + g["header"]("menu") + f'''
<section class="pagehero pagehero--photo">
  <div class="pagehero__bg">{img("streuselkuchen", "Hausgemachter Streuselkuchen mit Sahne", eager=True)}</div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Speisekarte</p>
    <h1>Speisekarte &amp; Preise</h1>
    <p class="lead">Ehrlich, hausgemacht und regional. Wir backen ausschließlich mit frisch gemahlenem Dinkelmehl der Porta Mühle aus Minden.</p>
    <nav class="chips" aria-label="Bereiche der Speisekarte">
      <a class="chip" href="#fruehstueck">Frühstücksbuffet</a><a class="chip" href="#getraenke">Getränke</a>
      <a class="chip" href="#kuchen">Kuchen &amp; Waffeln</a><a class="chip" href="#herzhaftes">Herzhaftes</a>
    </nav>
  </div>
</section>

<div class="wrap">
  <section class="menu-sec" id="fruehstueck">
    <div class="menu-grid">
      <div>
        <span class="eyebrow">Samstag &amp; Sonntag, 10–13 Uhr</span>
        <h2>Frühstücksbuffet</h2>
        <ul class="buffet-list">{"".join(f"<li>{x}</li>" for x in MENU_FRUEH)}</ul>
        <div class="pricebox">
          <div class="price"><strong>25,50 €</strong><span>Erwachsene</span></div>
          <div class="price"><strong>9,00 €</strong><span>Kinder 3–13 Jahre</span></div>
        </div>
        <p class="small">Frühstück pro Person, inkl. MwSt., ohne Getränke.</p>
        <a class="btn btn--primary" href="index.html#reservieren">Tisch reservieren</a>
      </div>
      <div class="split__img split__img--tall">{img("fruehstuecksbuffet", "Frühstücksplatte vom Buffet des Café Waldkristall", "(min-width:700px) 50vw, 100vw")}</div>
    </div>
  </section>

  <section class="menu-sec" id="getraenke">
    <div class="menu-grid">
      <div>
        <span class="eyebrow">Zum Frühstück</span>
        <h2>Getränke</h2>
        <p>Gerne servieren wir Kaffeespezialitäten, Tee, Kakao und kalte Getränke à la carte, in bester Bioqualität.</p>
        {items(DRINKS)}
      </div>
      <div class="split__img">{img("fruehstuecksgetraenke", "Kaffee in weißen Tassen, frischer Orangensaft und ein Glas Sekt auf einem Holztisch", "(min-width:700px) 50vw, 100vw")}</div>
    </div>
  </section>

  <section class="menu-sec" id="kuchen">
    <div class="menu-grid">
      <div>
        <span class="eyebrow">Mit einer Prise Kindheit</span>
        <h2>Kuchen &amp; Torten</h2>
        <p>Wenn es bei uns nach warmem Apfelkuchen duftet, liegt oft ein Hauch von Kindheit in der Luft. In liebevoller Handarbeit backen wir Kuchen, Torten, Waffeln und feines Gebäck – mit regionalen Zutaten und viel Herz.</p>
        <p class="signoff">Unsere Gäste sagen oft: „Man schmeckt, dass hier mit Leidenschaft gebacken wird.“ Und das stimmt – jedes Stück ist ein kleines Glück.</p>
        <p>Dazu servieren wir Dir ausgewählte Kaffee- und Teesorten in bester Bioqualität. Schau einfach mal in unsere Karte – vielleicht findest Du ja Deinen neuen Lieblingskuchen.</p>
        {items(CAKES)}
      </div>
      <div class="split__img">{img("erdbeertorte", "Erdbeer-Sahnetorte mit Holunderblüten auf einem Holzbrett", "(min-width:700px) 50vw, 100vw")}</div>
    </div>
  </section>

  <section class="menu-sec" id="waffeln">
    <div class="menu-grid">
      <div>
        <span class="eyebrow">Vom heißen Eisen direkt auf den Teller</span>
        <h2>Waffeln</h2>
        {items(WAFFLES)}
      </div>
      <div class="split__img">{img("waffeln-erdbeeren", "Waffeln mit frischen Erdbeeren und Puderzucker, hausgemacht im Café Waldkristall", "(min-width:700px) 50vw, 100vw")}</div>
    </div>
  </section>

  <section class="menu-sec" id="herzhaftes">
    <div class="menu-grid">
      <div>
        <span class="eyebrow">Aus der Waldküche</span>
        <h2>Herzhaftes für Zwischendurch</h2>
        <p>Neben süßen Köstlichkeiten bieten wir Dir natürlich auch herzhafte Genüsse – von liebevoll zubereiteten Snacks bis hin zu wechselnden Tagesgerichten.</p>
        {items(SAVORY)}
      </div>
      <div class="split__img">{img("brotzeit", "Brotzeit mit Dinkelbrot, Käse und Schinken auf einem Holzbrett", "(min-width:700px) 50vw, 100vw")}</div>
    </div>
    <p class="signoff signoff--end">Frag uns einfach, was heute auf dem Herd steht – oder lass Dich überraschen und komm einfach gleich vorbei! Wir freuen uns auf Deinen Besuch!</p>
  </section>

  <p class="menu-foot">Fragen zu Zutaten oder Unverträglichkeiten? Sprich uns gerne an.<br>Preise inkl. MwSt., Stand: 1. Januar 2026. Änderungen vorbehalten.</p>
</div>
''' + g["footer"]()


def events(g):
    img = g["img"]
    return g["head"]("Veranstaltungen: Livemusik & Yoga | Café Waldkristall",
        "Livemusik-Abende mit Wohnzimmer-Charme, Yoga, Kurse und Workshops im Fachwerkhaus im Wiehengebirge. Alle nächsten Termine im Café Waldkristall.",
        "/veranstaltungen/") + g["header"]("events") + f'''
<section class="hero" style="min-height:60svh">
  <div class="hero__img">{img("abend-livemusik", "Stimmungsbild: Gitarre, Kerzen und Lichterketten an einem Holztisch am Abend", eager=True)}</div>
  <div class="wrap">
    <p class="crumbs" style="color:rgba(255,255,255,.85)"><a href="index.html" style="color:inherit">Start</a> / Veranstaltungen</p>
    <h1>Veranstaltungen im Café Waldkristall</h1>
    <p class="hero__sub">Im Café Waldkristall bist Du nicht einfach nur Gast, Du bist Teil der Gemeinschaft. Hier darf geschmaust, gelacht und getanzt werden.</p>
  </div>
</section>

<section class="section" id="termine">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Nächste Termine</span>
    <h2>Was als Nächstes ansteht</h2>
    <!-- In WordPress: Ulrike trägt Termine ein. Vergangene Termine verschwinden automatisch.
         Beispiel: <li class="date" data-date="2026-10-24"><div class="date__day">24<small>Okt</small></div><div><h3>Livemusik: Name</h3><p>Sa, 19 Uhr · Eintritt frei, Hut geht rum</p></div></li> -->
    <ul class="dates" data-dates></ul>
    <div class="dates-empty" data-dates-empty>
      <p><b>Gerade sind keine neuen Termine eingetragen.</b><br>Die nächsten Konzerte und Kurse verraten wir zuerst im Newsletter und auf Instagram.</p>
      {g["newsletter_form"](compact=True)}
      <p class="small" style="margin-top:14px">Oder folge uns auf <a href="https://www.instagram.com/cafe_waldkristall/" rel="noopener">Instagram @cafe_waldkristall</a>.</p>
    </div>
  </div>
</section>

<section class="section section--card" id="livemusik">
  <div class="wrap split">
    <div class="split__img reveal">{img("livemusik-gitarre", "Gitarre bei einem Livemusik-Abend im Café", "(min-width:700px) 50vw, 100vw")}</div>
    <div class="reveal">
      <span class="eyebrow">Livemusik mit Herz</span>
      <h2>Ein kleiner Konzertsaal mit Wohnzimmer-Charme</h2>
      <p class="lead">Regelmäßig verwandeln Musiker aus aller Welt unser Café in einen kleinen, gemütlichen Konzertsaal mit Wohnzimmer-Charme. Unsere Livemusik-Abende sind etwas ganz Besonderes.</p>
      <p>Mal leise und berührend, mal rhythmisch und mitreißend, aber immer voller Gefühl. Schnapp Dir ein Glas Wein, lehn Dich zurück, wipp mit dem Fuß oder tanz einfach mit.</p>
      <p>Übrigens: Bei uns wird auch spontan musiziert, ganz herzlich.</p>
    </div>
  </div>
</section>

<section class="section" id="kurse">
  <div class="wrap">
    <span class="eyebrow">Wohlfühl-Faktoren</span>
    <h2>Yoga, Kurse &amp; Workshops</h2>
    <p class="lead" style="max-width:60ch">Seit über 14 Jahren verwandeln inspirierende Menschen unseren Raum in einen Ort für Austausch, Kreativität und Begegnung. Vielleicht ist ja auch für Dich etwas dabei?</p>
    <div class="partners" style="margin-top:24px">
      <div class="partner"><h3>Yoga mit Brigitte Kottkamp</h3><p><a href="http://www.aktiv-mit-yoga.de/" rel="noopener">www.aktiv-mit-yoga.de</a><br><a href="mailto:bk@aktiv-mit-yoga.de">bk@aktiv-mit-yoga.de</a><br>Fon 0163 4592845</p></div>
      <div class="partner"><h3>Yoga aus der Quelle</h3><p>Tanja Meier<br>Faszienyoga, Hormonyoga, Yoga mit Mantra-Begleitung, Entspannung + Meditation<br><a href="https://www.instagram.com/yoga_aus_der_quelle/" rel="noopener">Instagram: yoga_aus_der_quelle</a><br><a href="mailto:Yoga_aus_derquelle@web.de">Yoga_aus_derquelle@web.de</a><br>Fon 0176 39905390</p></div>
      <div class="partner"><h3>Hatha Yoga mit Alexa</h3><p>Alexa Murillo<br><a href="mailto:alexa@murillo-mendoza.de">alexa@murillo-mendoza.de</a><br>Fon 0179 9180446</p></div>
      <div class="partner"><h3>Herzreich</h3><p>Valentina Knappe<br>Bewegt – leicht – frei<br><a href="https://herzreich-minden.de" rel="noopener">herzreich-minden.de</a><br><a href="mailto:herzreich@gmx.de">herzreich@gmx.de</a><br>Fon 0173 9262359</p></div>
    </div>
    <p class="small" style="margin-top:14px">Anmeldung zu den Kursen direkt bei den Kursleitern.</p>
  </div>
</section>

<section class="section section--card" id="seminarraum">
  <div class="wrap split split--rev">
    <div class="split__img reveal">{img("yoga-terrasse", "Yoga-Übung im Freien auf einer Holzterrasse", "(min-width:700px) 50vw, 100vw")}</div>
    <div class="reveal">
      <span class="eyebrow">Wusstest Du schon?</span>
      <h2>Unser Seminarraum steht Dir offen</h2>
      <p class="lead">Ob für kreative Workshops, inspirierende Kurse oder besondere Herzensprojekte: Bei uns findest Du den passenden Raum für Deine Ideen.</p>
      <p>Sprich uns einfach an. Wir freuen uns, wenn Du bei uns etwas bewegen möchtest!</p>
      <div class="btn-row"><a class="btn btn--primary" href="mailto:{g["EMAIL"]}?subject=Seminarraum">Seminarraum anfragen</a><a class="btn btn--ghost" href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="feature reveal">
      <div class="feature__body">
        <span class="eyebrow">Eigene Feier geplant?</span>
        <h2>Familienfeier, Hochzeit oder Jubiläum</h2>
        <p>Für Gruppen von 20 bis 50 Personen öffnen wir nach Absprache auch außerhalb der Öffnungszeiten.</p>
        <a class="btn btn--primary" href="feiern.html">Mehr zu Feiern</a>
      </div>
      <div class="feature__img">{img("garten-huetten", "Biergarten des Café Waldkristall mit Holzhütten, Sitzplätzen und Brunnen im Wald", "(min-width:700px) 45vw, 100vw")}</div>
    </div>
  </div>
</section>
''' + g["footer"]()


def party(g):
    img = g["img"]
    return g["head"]("Feier & Hochzeit im Wiehengebirge | Café Waldkristall",
        "Familienfeier, Hochzeit oder Jubiläum für 20 bis 50 Gäste im Fachwerkhaus am Waldrand in Hüllhorst, auch außerhalb der Öffnungszeiten. Jetzt anfragen.",
        "/feiern/") + g["header"]("party") + f'''
<section class="hero" style="min-height:70svh">
  <div class="hero__img">{img("gartenfest", "Festlich geschmückter Garten vor dem Fachwerkhaus des Café Waldkristall", eager=True, cls="hero-party")}</div>
  <div class="wrap">
    <p class="crumbs" style="color:rgba(255,255,255,.85)"><a href="index.html" style="color:inherit">Start</a> / Feiern</p>
    <h1>Feiern &amp; Hochzeiten im Wiehengebirge</h1>
    <p class="hero__sub">Deine Familienfeier, Hochzeit oder Dein Jubiläum im Fachwerkhaus am Waldrand, für 20 bis 50 Gäste.</p>
    <div class="btn-row"><a class="btn btn--primary" href="#anfrage">Feier anfragen</a><a class="btn btn--light" href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Feiern im Café Waldkristall</span>
      <h2>Wie viele Gäste passen ins Café Waldkristall?</h2>
      <p class="lead">Drinnen finden bis zu 50 Gäste Platz. Bei gutem Wetter kann draußen auf der Terrasse und im Garten weitergefeiert werden.</p>
      <ul class="checklist">
        <li>Für Gruppen von 20 bis 50 Personen</li>
        <li>Nach Absprache auch außerhalb unserer regulären Öffnungszeiten</li>
        <li>Familienfeiern, Hochzeiten, Jubiläen und geschlossene Gesellschaften</li>
        <li>Fachwerkhaus mit Kaminfeuer, Terrasse und Garten mitten in der Natur</li>
      </ul>
    </div>
    <div class="split__img split__img--tall split__img--wedding reveal">{img("hochzeitspaar-wald", "Brautpaar Hand in Hand auf einem Waldweg im Herbst", "(min-width:700px) 50vw, 100vw")}</div>
  </div>
</section>

<section class="section section--bark" id="gruppenangebote">
  <div class="wrap">
    <div class="reveal" style="max-width:640px">
      <span class="eyebrow">Angebote für Gruppen</span>
      <h2>Für Geburtstage, Familienfeiern und gesellige Nachmittage</h2>
      <p class="lead">Für Gruppen von 20 bis 50 Personen. Such Dir eins der Angebote aus, den Rest besprechen wir gemeinsam.</p>
    </div>
    <div class="groups reveal">
      <article class="card">
        <div class="card__img">{img("gruppen-waffeln", "Waffelherzen mit heißen Kirschen und Minze auf dunklem Teller", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Kaffeezeit im Waldkristall</h3>
          <ul class="menu-list"><li class="menu-item"><b>Kaffee &amp; Kuchen</b><span class="p">13,50 €</span><small>1 Stück hausgemachter Kuchen, dazu frisch gebackene Waffelherzen mit heißen Kirschen und Sahne</small></li></ul><a class="groups__ask" href="#anfrage">Anfragen</a></div>
      </article>
      <article class="card">
        <div class="card__img">{img("gruppen-strammer-max", "Strammer Max mit Spiegeleiern auf Dinkelbrot", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Herzhaft &amp; Gemütlich</h3>
          <ul class="menu-list"><li class="menu-item"><b>Reibekuchen</b><span class="p">19,50 €</span><small>mit Apfelmus, Kräuterquark und gemischtem Blattsalat</small></li><li class="menu-item"><b>Strammer Max</b><span class="p">19,50 €</span><small>mit gemischtem Blattsalat</small></li><li class="menu-item"><b>Brotzeit</b><span class="p">16,50 €</span><small>hausgebackenes Dinkelbrot mit gemischtem Aufschnitt, Käse und kleinem Salat</small></li></ul><a class="groups__ask" href="#anfrage">Anfragen</a></div>
      </article>
      <article class="card card--wide">
        <div class="card__img">{img("gruppen-suppe", "Hausgemachte Suppe mit Dinkelbrot auf dunklem Holztisch", "(min-width:1024px) 33vw, (min-width:700px) 50vw, 100vw")}</div>
        <div class="card__body"><h3>Für Wandergruppen &amp; Ausflügler</h3>
          <p>Nach einer schönen Wanderung schmeckt eine warme Mahlzeit besonders gut. Wir reservieren Euch einen Tisch und bereiten etwas Passendes vor, zum Beispiel:</p>
          <ul class="menu-list"><li class="menu-item"><b>Gulaschsuppe</b><span class="p">16,50 €</span><small>mit gemischtem Salat und Canapés mit Aufschnitt und Käse</small></li><li class="menu-item"><b>Kürbis-Tomaten-Cremesuppe</b><span class="p">6,50 / 7,50 €</span><small>mit einer Scheibe hausgebackenem Dinkelbrot · vegan / vegetarisch</small></li><li class="menu-item"><b>Möhrensuppe</b><span class="p">6,50 / 7,50 €</span><small>mit einer Scheibe hausgebackenem Dinkelbrot · vegan / vegetarisch</small></li></ul>
          <p class="small">Dazu gern Salat und verschiedene Brotaufstriche.</p><a class="groups__ask" href="#anfrage">Anfragen</a></div>
      </article>
    </div>
    <div class="groups__winter reveal">
      <p><b>Für die kalte Jahreszeit:</b> Bratwurst &amp; Glühwein oder Gulaschsuppe &amp; Glühwein.</p>
    </div>
    <div class="groups__foot reveal">
      <p class="small">Alle Preise pro Person, inkl. MwSt.</p>
      <a class="btn btn--primary" href="#anfrage">Gruppe anfragen</a>
    </div>
  </div>
</section>

<section class="section section--card">
  <div class="wrap">
    <span class="eyebrow">So einfach geht's</span>
    <h2>Von der Anfrage zur Feier</h2>
    <ol class="steps" style="margin-top:24px">
      <li><b>Anfrage senden</b>Schreib uns kurz, was Du feiern möchtest, wann und mit wie vielen Gästen.</li>
      <li><b>Wir melden uns</b>Wir rufen Dich an oder schreiben Dir zurück.</li>
      <li><b>Gemeinsam planen</b>Dann planen wir zusammen Deinen Wunschtermin.</li>
    </ol>
  </div>
</section>

<section class="section" id="anfrage">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Anfrage</span>
      <h2>Feier unverbindlich anfragen</h2>
      <p class="lead">Füll das Formular aus oder ruf uns an: <a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a>.</p>
      <p class="small">Lieber per E-Mail? <a href="mailto:{g["EMAIL"]}?subject=Anfrage%20Feier">{g["EMAIL"]}</a></p>
    </div>
    <form class="form" data-inquiry novalidate>
      <div class="field--row">
        <div class="field"><label for="f-name">Name <span class="req">*</span></label><input id="f-name" name="name" autocomplete="name" required><span class="err">Bitte gib Deinen Namen an.</span></div>
        <div class="field"><label for="f-tel">Telefon <span class="hint">(für Rückfragen)</span></label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="f-mail">E-Mail <span class="req">*</span></label><input id="f-mail" name="email" type="email" autocomplete="email" required><span class="err">Bitte gib eine gültige E-Mail-Adresse an.</span></div>
      <div class="field--row">
        <div class="field"><label for="f-anlass">Anlass <span class="req">*</span></label>
          <select id="f-anlass" name="anlass" required>
            <option value="">Bitte wählen</option><option>Familienfeier / Geburtstag</option><option>Hochzeit</option><option>Jubiläum</option><option>Geschlossene Gesellschaft</option><option>Etwas anderes</option>
          </select><span class="err">Bitte wähle einen Anlass.</span></div>
        <div class="field"><label for="f-gaeste">Anzahl Gäste <span class="req">*</span> <span class="hint">(20–50)</span></label><input id="f-gaeste" name="gaeste" type="number" min="20" max="50" inputmode="numeric" required><span class="err">Bitte gib die Anzahl der Gäste an.</span></div>
      </div>
      <div class="field"><label for="f-datum">Wunschdatum</label><input id="f-datum" name="datum" type="date"></div>
      <div class="field"><label for="f-msg">Deine Nachricht</label><textarea id="f-msg" name="nachricht" placeholder="Zum Beispiel: Uhrzeit, Kaffee &amp; Kuchen oder Buffet, besondere Wünsche"></textarea></div>
      <label class="check"><input type="checkbox" name="datenschutz" required><span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage gespeichert werden. Mehr in der <a href="datenschutz.html#kontaktformular">Datenschutzerklärung</a>. <span class="req">*</span></span></label>
      <button class="btn btn--primary" type="submit">Anfrage senden</button>
      <p class="small" style="margin:0">* Pflichtfeld</p>
      <div class="form__ok" role="status">
        <div class="tick">✓</div>
        <h3>Danke für Deine Anfrage!</h3>
        <p>Wir melden uns so schnell wie möglich bei Dir.</p>
      </div>
    </form>
  </div>
</section>
''' + g["footer"]()


def impressum(g):
    return g["head"]("Impressum | Café Waldkristall", "Impressum des Café Waldkristall, Inh. Ulrike Lohrmann, Bergstraße 141, 32609 Hüllhorst.", "/impressum/") + g["header"]("") + f'''
<section class="pagehero"><div class="wrap"><h1>Impressum</h1></div></section>
<section class="section"><div class="wrap legal">
  <div class="draft"><b>Entwurf, bitte prüfen.</b> Dieser Text basiert auf dem alten Impressum. Markierte Stellen muss Ulrike bestätigen. Den finalen Text bitte mit einem Generator (z. B. eRecht24) oder einer Anwältin/einem Anwalt abgleichen. Die Verantwortung für die Rechtstexte liegt bei der Inhaberin.</div>
  <h2>Angaben gemäß § 5 DDG</h2>
  <p>Ulrike Lohrmann<br>Café Waldkristall<br>{g["ADDR1"]}<br>{g["ADDR2"]}</p>
  <h2>Kontakt</h2>
  <p>Telefon: {g["PHONE"]}<br><mark>Telefax: 05744 507496 (noch aktuell?)</mark><br>E-Mail: {g["EMAIL"]}</p>
  <h2>Umsatzsteuer-ID</h2>
  <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:<br>DE247241845</p>
  <h2>Verbraucherstreitbeilegung</h2>
  <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</div></section>
''' + g["footer"]()


def datenschutz(g):
    return g["head"]("Datenschutzerklärung | Café Waldkristall", "Datenschutzerklärung des Café Waldkristall in Hüllhorst: welche Daten wir verarbeiten, wofür und welche Rechte Du hast.", "/datenschutz/") + g["header"]("") + f'''
<section class="pagehero"><div class="wrap"><h1>Datenschutzerklärung</h1></div></section>
<section class="section"><div class="wrap legal">
  <p class="lead">Kurz gesagt: Diese Website setzt keine Cookies, nutzt kein Google Analytics und kein anderes Tracking. Daten verarbeiten wir nur, wenn Du uns schreibst, reservierst, Dich bewirbst oder den Newsletter bestellst. Hier steht genau, was dabei passiert.</p>

  <h2>1. Verantwortliche</h2>
  <p>Ulrike Lohrmann, Café Waldkristall<br>{g["ADDR1"]}, {g["ADDR2"]}<br>Telefon: <a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a><br>E-Mail: <a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a></p>
  <p>Eine Datenschutzbeauftragte bzw. einen Datenschutzbeauftragten müssen wir als kleiner Betrieb nicht benennen. Bei Fragen zum Datenschutz schreib uns einfach an die oben genannte Adresse.</p>

  <h2>2. Hosting und Server-Logfiles</h2>
  <p>Unsere Website liegt bei datenchef, Inhaber Klaas Kleinschmidt, Westfalenstraße 31, 58135 Hagen. Wenn Du die Seite aufrufst, speichert der Server automatisch technische Daten, die Dein Browser übermittelt: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, die zuvor besuchte Seite (Referrer), Browser und Betriebssystem.</p>
  <p>Diese Daten brauchen wir, damit die Website funktioniert, sicher bleibt und Fehler gefunden werden können. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und stabilen Betrieb (Art. 6 Abs. 1 lit. f DSGVO). Wir führen diese Daten nicht mit anderen Daten zusammen. Sie werden gelöscht, sobald sie für diesen Zweck nicht mehr nötig sind. Mit unserem Hoster haben wir einen Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO geschlossen.</p>

  <h2>3. Verschlüsselung</h2>
  <p>Die Website nutzt eine SSL- bzw. TLS-Verschlüsselung. Das erkennst Du am Schloss-Symbol und an „https://“ in der Adresszeile. So können Daten, die Du uns über die Website schickst, nicht von Dritten mitgelesen werden.</p>

  <h2>4. Schriftarten</h2>
  <p>Die Schriften werden direkt von unserem eigenen Server geladen. Es wird keine Verbindung zu Google Fonts oder anderen Anbietern aufgebaut.</p>

  <h2 id="kontaktformular">5. Kontakt per E-Mail, Telefon und Anfrageformular</h2>
  <p>Wenn Du uns anrufst, eine E-Mail schreibst oder das Formular für Feier-Anfragen nutzt, verarbeiten wir die Angaben, die Du uns gibst: zum Beispiel Name, E-Mail-Adresse, Telefonnummer, Anlass, Anzahl der Gäste, Wunschdatum und Deine Nachricht. Die Formulardaten kommen per E-Mail bei uns an.</p>
  <p>Wir nutzen diese Daten nur, um Deine Anfrage zu beantworten und Deine Feier zu planen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn es um einen Vertrag oder dessen Vorbereitung geht, sonst unser berechtigtes Interesse, Anfragen zu beantworten (Art. 6 Abs. 1 lit. f DSGVO). Wir geben die Daten nicht weiter und löschen sie, sobald Deine Anfrage erledigt ist, außer gesetzliche Aufbewahrungspflichten (zum Beispiel für Rechnungen) verlangen etwas anderes.</p>

  <h2 id="gastronovi">6. Online-Reservierung und Gutscheine (Gastronovi)</h2>
  <p>Für Tischreservierungen und den Gutschein-Shop nutzen wir Gastronovi, einen Dienst der gastronovi GmbH, Buschhöhe 2, 28357 Bremen. Der Dienst wird erst geladen, wenn Du auf „Reservierung öffnen“ bzw. „Gutschein-Shop öffnen“ tippst. Vorher wird keine Verbindung zu Gastronovi aufgebaut.</p>
  <p>Nach dem Klick überträgt Dein Browser technische Daten an Gastronovi, zum Beispiel Deine IP-Adresse. Gastronovi setzt dabei keine Cookies. Die Daten werden auf Servern in Deutschland verarbeitet. Bei einer Reservierung verarbeitet Gastronovi für uns die Angaben, die Du dort einträgst (Name, Kontaktdaten, Datum, Uhrzeit, Personenzahl, Anmerkungen). Beim Gutscheinkauf kommen die Angaben zur Bestellung und Zahlung dazu.</p>
  <p>Rechtsgrundlage für das Laden des Dienstes ist Deine Einwilligung durch den Klick (Art. 6 Abs. 1 lit. a DSGVO). Die Reservierung bzw. der Gutscheinkauf selbst erfolgt zur Erfüllung des Vertrags mit Dir (Art. 6 Abs. 1 lit. b DSGVO). Gastronovi arbeitet für uns als Auftragsverarbeiter nach Art. 28 DSGVO. Mehr dazu in der <a href="https://gastronovi.com/de/datenschutz/" rel="noopener">Datenschutzerklärung von Gastronovi</a>. Du kannst auch ganz ohne Gastronovi reservieren: Ruf uns einfach an.</p>

  <h2 id="newsletter">7. Newsletter (Mailchimp)</h2>
  <p>Wenn Du unseren Newsletter bestellst, brauchen wir Deine E-Mail-Adresse. Vor- und Nachname sind freiwillig. Nach der Anmeldung bekommst Du eine E-Mail mit einem Bestätigungslink. Erst wenn Du ihn anklickst, bist Du angemeldet (Double-Opt-in). Den Zeitpunkt der Anmeldung und der Bestätigung sowie die IP-Adresse speichern wir, um Deine Anmeldung nachweisen zu können.</p>
  <p>Für den Versand nutzen wir Mailchimp, einen Dienst der The Rocket Science Group LLC d/b/a Mailchimp, 675 Ponce de Leon Ave NE, Suite 5000, Atlanta, GA 30308, USA (ein Unternehmen von Intuit Inc.). Deine Daten werden dabei auch in den USA verarbeitet. Mailchimp ist nach dem EU-U.S. Data Privacy Framework zertifiziert. Damit gilt nach einem Beschluss der EU-Kommission ein angemessenes Datenschutzniveau (Art. 45 DSGVO). Zusätzlich hat Mailchimp Standardvertragsklauseln der EU-Kommission vereinbart. Mit Mailchimp besteht ein Vertrag zur Auftragsverarbeitung. Mailchimp kann auswerten, ob ein Newsletter geöffnet und welche Links angeklickt werden. Das hilft uns, den Newsletter besser zu machen.</p>
  <p>Rechtsgrundlage ist Deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO). Du kannst Dich jederzeit über den Link am Ende jedes Newsletters abmelden oder uns kurz schreiben. Danach löschen wir Deine Daten aus dem Verteiler. Damit wir Dir nicht aus Versehen wieder schreiben, kann Deine E-Mail-Adresse in einer Sperrliste bleiben (Art. 6 Abs. 1 lit. f DSGVO). Mehr dazu in der <a href="https://www.intuit.com/privacy/statement/" rel="noopener">Datenschutzerklärung von Mailchimp/Intuit</a>.</p>

  <h2 id="bewerbungen">8. Bewerbungen</h2>
  <p>Wenn Du Dich bei uns bewirbst, per Formular, E-Mail, Telefon oder persönlich, verarbeiten wir Deine Angaben: Name, Kontaktdaten, Deine Nachricht und Unterlagen, falls Du welche mitschickst, sowie Notizen aus einem Kennenlerngespräch. Diese Daten sieht nur die Inhaberin. Wir nutzen sie ausschließlich, um über Deine Bewerbung zu entscheiden.</p>
  <p>Rechtsgrundlage ist die Anbahnung eines Arbeitsverhältnisses (Art. 6 Abs. 1 lit. b DSGVO). Wenn wir zusammenkommen, wandern die Daten in Deine Personalakte. Wenn nicht, löschen wir sie spätestens 6 Monate nach unserer Absage, damit wir auf mögliche Rückfragen oder Ansprüche nach dem Allgemeinen Gleichbehandlungsgesetz (AGG) reagieren können. Möchtest Du, dass wir Deine Bewerbung länger für spätere Stellen aufbewahren, fragen wir Dich vorher.</p>

  <h2>9. Links zu Instagram, Komoot und Google Maps</h2>
  <p>Diese Dienste sind auf unserer Website nur verlinkt, nicht eingebettet. Es werden also keine Daten an sie übertragen, solange Du nur unsere Seite ansiehst. Erst wenn Du einen Link anklickst, öffnest Du die Seite des jeweiligen Anbieters. Dort gelten dessen Datenschutzregeln.</p>

  <h2>10. Deine Rechte</h2>
  <p>Du hast jederzeit das Recht auf:</p>
  <ul>
    <li><b>Auskunft</b> über Deine bei uns gespeicherten Daten (Art. 15 DSGVO)</li>
    <li><b>Berichtigung</b> falscher Daten (Art. 16 DSGVO)</li>
    <li><b>Löschung</b> Deiner Daten (Art. 17 DSGVO)</li>
    <li><b>Einschränkung</b> der Verarbeitung (Art. 18 DSGVO)</li>
    <li><b>Datenübertragbarkeit</b> (Art. 20 DSGVO)</li>
    <li><b>Widerruf</b> einer Einwilligung, mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO)</li>
  </ul>
  <p><b>Widerspruchsrecht:</b> Wenn wir Daten auf Grundlage unseres berechtigten Interesses verarbeiten (Art. 6 Abs. 1 lit. f DSGVO), kannst Du dieser Verarbeitung aus Gründen, die sich aus Deiner besonderen Situation ergeben, jederzeit widersprechen (Art. 21 DSGVO).</p>
  <p>Eine kurze E-Mail an <a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a> genügt.</p>
  <p><b>Beschwerderecht:</b> Du kannst Dich bei einer Datenschutz-Aufsichtsbehörde beschweren (Art. 77 DSGVO). Für uns zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2–4, 40213 Düsseldorf, <a href="https://www.ldi.nrw.de" rel="noopener">www.ldi.nrw.de</a>.</p>

  <h2>11. Pflicht zur Angabe von Daten</h2>
  <p>Du musst uns keine Daten geben. Ohne Kontaktdaten können wir Dir aber nicht antworten, Deine Reservierung nicht annehmen und Deine Bewerbung nicht bearbeiten. Eine automatisierte Entscheidungsfindung oder ein Profiling findet nicht statt.</p>

  <p class="small">Stand: Oktober 2026</p>
</div></section>
''' + g["footer"]()

JOBS = [("Servicefachkraft (m/w/d)", "Teilzeit (20 Std.)"),
        ("Hauswirtschaftliche Kraft (m/w/d)", "Teilzeit")]
# Only what Ulrike's site says. Job descriptions: ask Ulrike (Parked).

def jobs(g):
    img = g["img"]
    cards = "".join(f'<div class="partner"><h3>{t}</h3><p>{h}</p></div>' for t, h in JOBS)
    opts = "".join(f"<option>{t}</option>" for t, h in JOBS) + "<option>Initiativbewerbung</option>"
    return g["head"]("Jobs in Hüllhorst: Service & Hauswirtschaft | Café Waldkristall",
        "Jobs im Café Waldkristall im Wiehengebirge: Servicefachkraft und Hauswirtschaftliche Kraft in Teilzeit. Faire Bezahlung, kleines Team. Jetzt bewerben.",
        "/jobs/") + g["header"]("") + f"""
<section class="pagehero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Jobs</p>
    <h1>Jobs im Café Waldkristall</h1>
    <p class="lead">Du hast Erfahrung in der Gastronomie und suchst eine neue Herausforderung – am liebsten in einem herzlichen Team und mitten in der Natur? Dann bist Du bei uns genau richtig!</p>
  </div>
</section>

<section class="section" id="stellen">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Offene Stellen</span>
      <h2>Wen suchen wir gerade?</h2>
      <p>Wir suchen Verstärkung für unser kleines, familiäres Café – mit abwechslungsreicher Arbeit, fairer Bezahlung und ganz viel Herz.</p>
      <!-- In WordPress: Ulrike fügt Stellen hinzu oder entfernt sie selbst. -->
      <div class="partners" style="grid-template-columns:1fr">{cards}</div>
    </div>
    <div class="split__img">{img("gebaeck", "Frisch gebackenes Gebäck auf dem Buffet im Café Waldkristall", "(min-width:700px) 50vw, 100vw")}</div>
  </div>
</section>

<section class="section section--card" id="bewerben">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Bewerbung</span>
      <h2>Jetzt bewerben</h2>
      <p class="lead">Schick uns einfach eine Nachricht oder ruf direkt an – wir freuen uns darauf, Dich kennenzulernen!</p>
      <p><a href="tel:{g["PHONE_TEL"]}">{g["PHONE"]}</a><br><a href="mailto:{g["EMAIL"]}?subject=Bewerbung">{g["EMAIL"]}</a></p>
    </div>
    <form class="form" data-apply novalidate>
      <div class="field--row">
        <div class="field"><label for="j-name">Name <span class="req">*</span></label><input id="j-name" name="name" autocomplete="name" required><span class="err">Bitte gib Deinen Namen an.</span></div>
        <div class="field"><label for="j-tel">Telefon</label><input id="j-tel" name="telefon" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="j-mail">E-Mail <span class="req">*</span></label><input id="j-mail" name="email" type="email" autocomplete="email" required><span class="err">Bitte gib eine gültige E-Mail-Adresse an.</span></div>
      <div class="field"><label for="j-stelle">Stelle <span class="req">*</span></label><select id="j-stelle" name="stelle" required><option value="">Bitte wählen</option>{opts}</select><span class="err">Bitte wähle eine Stelle.</span></div>
      <div class="field"><label for="j-msg">Ein paar Sätze über Dich</label><textarea id="j-msg" name="nachricht" placeholder="Zum Beispiel: Erfahrung, ab wann Du anfangen kannst, welche Tage passen"></textarea></div>
      <div class="field"><label for="j-cv">Lebenslauf <span class="hint">(optional, PDF, max. 5 MB)</span></label><input id="j-cv" name="lebenslauf" type="file" accept=".pdf,.doc,.docx"></div>
      <label class="check"><input type="checkbox" name="datenschutz" required><span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung meiner Bewerbung gespeichert werden. Mehr in der <a href="datenschutz.html#bewerbungen">Datenschutzerklärung</a>. <span class="req">*</span></span></label>
      <button class="btn btn--primary" type="submit">Bewerbung senden</button>
      <p class="small" style="margin:0">* Pflichtfeld</p>
      <div class="form__ok" role="status"><div class="tick">✓</div><h3>Danke für Deine Bewerbung!</h3><p>Wir melden uns so schnell wie möglich bei Dir.</p></div>
    </form>
  </div>
</section>
""" + g["footer"]()


def newsletter(g):
    img = g["img"]
    return g["head"]("Newsletter | Café Waldkristall im Wiehengebirge",
        "Ein Stück Waldkristall in Deinem Postfach: saisonale Köstlichkeiten, Neuigkeiten aus dem Café und Einladungen zu Livemusik und Events.",
        "/newsletter/") + g["header"]("") + f"""
<section class="pagehero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Start</a> / Newsletter</p>
    <h1>Ein Stück Waldkristall in Deinem Postfach</h1>
    <p class="lead">Melde Dich zu unserem Newsletter an und erhalte kleine Einblicke in unsere Welt aus Genuss, Natur und Gemütlichkeit.</p>
  </div>
</section>
<section class="section" id="anmelden">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow">Jetzt zum Newsletter anmelden</span>
      <h2>Das erwartet Dich</h2>
      <ul class="checklist">
        <li>Saisonale Köstlichkeiten</li>
        <li>Neuigkeiten aus dem Café</li>
        <li>Besondere Einladungen zu unseren Events und Konzerten</li>
      </ul>
      <p>Einfach Deine E-Mail-Adresse eintragen – und schon bist Du Teil der Waldkristall-Familie.</p>
      <p><a href="https://mailchi.mp/cafe-waldkristall/092026-newsletter" rel="noopener">Letzten Newsletter ansehen</a> <span class="small">(Link wird in WordPress bei jedem neuen Newsletter aktualisiert)</span></p>
    </div>
    {g["newsletter_form"]()}
  </div>
</section>
""" + g["footer"]()


PAGES = {"index.html": home, "speisekarte.html": menu, "veranstaltungen.html": events, "feiern.html": party,
         "impressum.html": impressum, "datenschutz.html": datenschutz,
         "jobs.html": jobs, "newsletter.html": newsletter}
