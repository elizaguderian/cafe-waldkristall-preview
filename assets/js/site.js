/* Café Waldkristall — small site script, no tracking, no external calls until the visitor clicks */
(function () {
  "use strict";

  /* Where a page opens: at the top, or at the #spot the link points to.
     Some viewers keep the old scroll position when switching pages, and photos
     loading late can push a #spot down. Re-check once everything has loaded,
     unless the visitor has already started scrolling themselves. */
  try { if ("scrollRestoration" in history) history.scrollRestoration = "manual"; } catch (e) {}
  var userMoved = false;
  ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (t) {
    window.addEventListener(t, function () { userMoved = true; }, { passive: true, once: true });
  });
  function placePage() {
    if (userMoved) return;
    var id = decodeURIComponent((location.hash || "").slice(1));
    var el = id && document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "instant", block: "start" });
    else if (!id) window.scrollTo({ top: 0, left: 0, behavior: "instant" });
  }
  placePage();
  window.addEventListener("load", function () { placePage(); setTimeout(placePage, 300); });

  /* Mobile menu */
  var btn = document.querySelector(".menu-btn");
  var panel = document.getElementById("mnav");
  if (btn && panel) {
    var setOpen = function (open) {
      panel.classList.toggle("is-open", open);
      document.body.classList.toggle("menu-open", open);
      btn.setAttribute("aria-expanded", String(open));
      btn.querySelector("span").textContent = open ? "Schließen" : "Menü";
    };
    btn.addEventListener("click", function () { setOpen(!panel.classList.contains("is-open")); });
    panel.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setOpen(false); });
  }

  /* Sticky reserve bar (phones/tablets): hidden while the page's own "Tisch reservieren" button is on screen,
     so the visitor never sees two of them. It slides in once that button has scrolled away. */
  var bar = document.querySelector(".reservebar");
  if (bar && "IntersectionObserver" in window) {
    var own = [].slice.call(document.querySelectorAll('a.btn[href$="#reservieren"]')).filter(function (a) {
      return !a.closest(".reservebar, .header, .mnav");
    });
    if (own.length) {
      var seen = [];
      var barIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var i = seen.indexOf(en.target);
          if (en.isIntersecting && i < 0) seen.push(en.target);
          if (!en.isIntersecting && i > -1) seen.splice(i, 1);
        });
        bar.classList.toggle("is-hidden", seen.length > 0);
      }, { rootMargin: "-72px 0px 0px 0px" });
      own.forEach(function (a) { barIO.observe(a); });
    }
  }

  /* Moments strip (phones): arrows + dots so it is clear there is more to slide to, and mouse-drag for desktop browsers */
  var strip = document.querySelector(".moments__grid");
  if (strip && strip.children.length > 1) {
    var cards = [].slice.call(strip.children);
    var nav = document.createElement("div");
    nav.className = "moments__nav";
    nav.innerHTML = '<button type="button" class="moments__btn" aria-label="Zurück">\u2039</button><span class="moments__dots" aria-hidden="true"></span><button type="button" class="moments__btn" aria-label="Weiter">\u203a</button>';
    strip.parentNode.insertBefore(nav, strip.nextSibling);
    var dotWrap = nav.querySelector(".moments__dots"), prevB = nav.children[0], nextB = nav.children[2];
    cards.forEach(function () { dotWrap.appendChild(document.createElement("i")); });
    var step = function () { return cards[1].offsetLeft - cards[0].offsetLeft; };
    var current = function () { return Math.max(0, Math.min(cards.length - 1, Math.round(strip.scrollLeft / step()))); };
    var sync = function () {
      var i = current();
      [].forEach.call(dotWrap.children, function (d, k) { d.classList.toggle("is-on", k === i); });
      prevB.disabled = i === 0; nextB.disabled = i === cards.length - 1;
    };
    var go = function (i) { strip.scrollTo({ left: Math.max(0, Math.min(cards.length - 1, i)) * step(), behavior: "smooth" }); };
    prevB.addEventListener("click", function () { go(current() - 1); });
    nextB.addEventListener("click", function () { go(current() + 1); });
    strip.addEventListener("scroll", function () { window.requestAnimationFrame(sync); }, { passive: true });
    var drag = null;
    strip.addEventListener("pointerdown", function (e) {
      if (e.pointerType !== "mouse") return;
      drag = { x: e.clientX, left: strip.scrollLeft, moved: false };
    });
    window.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var dx = e.clientX - drag.x;
      if (Math.abs(dx) > 4) { drag.moved = true; strip.classList.add("is-drag"); }
      if (drag.moved) strip.scrollLeft = drag.left - dx;
    });
    window.addEventListener("pointerup", function () {
      if (!drag) return;
      var moved = drag.moved; drag = null; strip.classList.remove("is-drag");
      if (moved) go(current());
    });
    window.addEventListener("resize", sync);
    sync();
  }

  /* Gentle reveal on scroll */
  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add("is-in"); }); }

  /* Gastronovi: load only after the visitor clicks (no data goes to Gastronovi before that).
     Same one-line snippet the old site used; Gastronovi builds its booking window itself where the script sits. */
  document.querySelectorAll("[data-gastronovi]").forEach(function (box) {
    var b = box.querySelector("button");
    if (!b) return;
    b.addEventListener("click", function () {
      var type = box.getAttribute("data-gastronovi"); /* reservation | voucher */
      var s = document.createElement("script");
      s.src = "https://services.gastronovi.com/restaurants/107265/scripts/reservation/entry/" + type;
      s.async = true;
      var direct = "https://services.gastronovi.com/restaurants/107265/reservierung/widget?entry=" + type;
      var label = type === "voucher" ? "Gutschein-Shop" : "Online-Reservierung";
      box.innerHTML = '<p class="embed__loading" role="status">' + label + ' wird geladen …</p>';
      box.classList.add("is-loaded");
      box.appendChild(s);
      /* Fallback: if Gastronovi doesn't show up (no connection, ad blocker), never leave an empty box */
      var tries = 0;
      var timer = setInterval(function () {
        tries++;
        var frame = box.querySelector("iframe");
        if (frame) { clearInterval(timer); var l = box.querySelector(".embed__loading"); if (l) l.remove(); return; }
        if (tries >= 16) {
          clearInterval(timer);
          box.classList.remove("is-loaded");
          box.innerHTML = '<p><b>Die ' + label + ' lädt gerade nicht.</b><br>Öffne sie direkt oder ruf uns an.</p>' +
            '<div class="btn-row" style="justify-content:center"><a class="btn btn--primary" href="' + direct + '" target="_blank" rel="noopener">' + label + ' öffnen</a>' +
            '<a class="btn btn--ghost" href="tel:+4957444087">05744 4087</a></div>' +
            '<p class="small">Oder per E-Mail: <a href="mailto:info@cafe-waldkristall.de">info@cafe-waldkristall.de</a></p>';
        }
      }, 500);
    });
  });

  /* Events: hide dates that have passed; show a friendly note if none are left */
  var list = document.querySelector("[data-dates]");
  if (list) {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var left = 0;
    list.querySelectorAll("[data-date]").forEach(function (li) {
      var d = new Date(li.getAttribute("data-date") + "T23:59:59");
      if (d < today) li.remove(); else left++;
    });
    var empty = document.querySelector("[data-dates-empty]");
    if (empty) empty.hidden = left > 0;
    list.hidden = left === 0;
  }

  /* Forms: party inquiry, job application, newsletter.
     PROTOTYPE: in WordPress the form plugin / Mailchimp sends the data. Each conversion event fires
     only after a confirmed send: party_inquiry, job_application, newsletter_signup. */
  var FORMS = { "data-inquiry": "party_inquiry", "data-apply": "job_application", "data-newsletter": "newsletter_signup" };
  Object.keys(FORMS).forEach(function (attr) {
    document.querySelectorAll("[" + attr + "]").forEach(function (form) {
      var dateInput = form.querySelector('input[type="date"]');
      if (dateInput) dateInput.min = new Date().toISOString().slice(0, 10);
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var ok = true;
        form.querySelectorAll("[required]").forEach(function (inp) {
          var field = inp.closest(".field") || inp.closest(".check");
          var bad = inp.type === "checkbox" ? !inp.checked : !inp.value.trim() || (inp.type === "email" && !/^\S+@\S+\.\S+$/.test(inp.value));
          if (field) field.classList.toggle("has-error", bad);
          if (bad && ok) { inp.focus(); ok = false; }
        });
        if (!ok) return;
        form.classList.add("is-sent");
        window.dispatchEvent(new CustomEvent(FORMS[attr], { detail: { page: location.pathname } }));
        form.scrollIntoView({ behavior: "smooth", block: "center" });
      });
    });
  });

  /* Year in footer */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
