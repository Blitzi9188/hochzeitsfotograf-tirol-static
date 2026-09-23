/* ANDREAS KISS — shared site script */
(function(){
  "use strict";
  var root = document.documentElement;

  /* ---- Language (persisted) ---- */
  function apply(l){
    root.setAttribute('data-lang', l);
    root.setAttribute('lang', l);
    document.querySelectorAll('[data-set-lang]').forEach(function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-set-lang') === l ? 'true' : 'false');
    });
    try{ localStorage.setItem('ak-lang', l); }catch(e){}
  }
  var saved = null;
  try{ saved = localStorage.getItem('ak-lang'); }catch(e){}
  var urlLang = null;
  try{ urlLang = new URLSearchParams(window.location.search).get('lang'); }catch(e){}
  apply((urlLang === 'de' || urlLang === 'en') ? urlLang : (saved === 'de' || saved === 'en') ? saved : 'de');
  document.querySelectorAll('[data-set-lang]').forEach(function(b){
    b.addEventListener('click', function(){ apply(b.getAttribute('data-set-lang')); });
  });

  /* ---- Header scroll ---- */
  var hdr = document.getElementById('hdr');
  if(hdr){
    var onScroll = function(){ hdr.classList.toggle('scrolled', window.scrollY > 20); };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }

  /* ---- Dropdown: hover/focus handled by CSS; JS toggle only on touch ---- */
  var hoverCap = window.matchMedia('(hover: hover)').matches;
  document.querySelectorAll('.has-dd').forEach(function(dd){
    var btn = dd.querySelector('.dd-btn');
    var close = function(){ dd.setAttribute('data-open','false'); btn.setAttribute('aria-expanded','false'); };
    var toggle = function(){ var o = dd.getAttribute('data-open')==='true';
      dd.setAttribute('data-open', o?'false':'true'); btn.setAttribute('aria-expanded', o?'false':'true'); };
    if(!hoverCap){ btn.addEventListener('click', function(e){ e.stopPropagation(); toggle(); }); }
    document.addEventListener('click', function(e){ if(!dd.contains(e.target)) close(); });
    document.addEventListener('keydown', function(e){ if(e.key==='Escape') close(); });
  });

  /* ---- Mobile nav ---- */
  var burger = document.getElementById('burger');
  var mnav = document.getElementById('mobilenav');
  if(burger && mnav){
    var toggle = function(){
      var open = mnav.getAttribute('data-open')==='true';
      mnav.setAttribute('data-open', open?'false':'true');
      burger.setAttribute('aria-expanded', open?'false':'true');
      document.body.style.overflow = open ? '' : 'hidden';
    };
    burger.addEventListener('click', toggle);
    mnav.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){
      mnav.setAttribute('data-open','false'); burger.setAttribute('aria-expanded','false');
      document.body.style.overflow=''; }); });
  }

  /* ---- Image fallback: local assets/img/ -> live site -> placeholder ---- */
  var LIVE = 'https://hochzeitsfotograf.tirol/assets/uploads/';
  function handleErr(img){
    if(!img.dataset.fbTried){
      var m = (img.getAttribute('src')||'').match(/assets\/img\/(.+)$/);
      if(m){ img.dataset.fbTried='1'; img.src = LIVE + m[1]; return; }
    }
    img.classList.add('failed');
  }
  document.querySelectorAll('img').forEach(function(img){
    img.addEventListener('error', function(){ handleErr(img); });
    if(img.complete && img.naturalWidth===0 && img.getAttribute('src')) handleErr(img);
  });

  /* ---- Reveal on scroll (with failsafe) ---- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('.reveal');
  var revealAll = function(){ reveals.forEach(function(el){ el.classList.add('in'); }); };
  if(reduce || !('IntersectionObserver' in window)){
    revealAll();
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {rootMargin:'0px 0px -8% 0px', threshold:0.06});
    reveals.forEach(function(el){ io.observe(el); });
    setTimeout(revealAll, 4000);
    document.addEventListener('visibilitychange', function(){ if(document.hidden) revealAll(); });
  }

  /* ---- Lightbox ---- */
  var figs = document.querySelectorAll('[data-lightbox] figure');
  if(figs.length){
    var lb = document.createElement('dialog');
    lb.className = 'lb';
    lb.innerHTML = '<button class="close" aria-label="Schließen">&times;</button><img alt="">';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img');
    figs.forEach(function(f){
      f.addEventListener('click', function(){
        var im = f.querySelector('img'); if(!im) return;
        lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt||'';
        if(lb.showModal) lb.showModal();
      });
    });
    lb.querySelector('.close').addEventListener('click', function(){ lb.close(); });
    lb.addEventListener('click', function(e){ if(e.target===lb) lb.close(); });
  }

  /* ---- Contact form -> mailto ---- */
  var form = document.getElementById('contactForm');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var de = root.getAttribute('data-lang')==='de';
      var g = function(id){ var el=document.getElementById(id); return el?el.value.trim():''; };
      var subject = (de?'Anfrage von ':'Enquiry from ') + g('name');
      var body =
        'Name: '+g('name')+'\n'+
        'E-Mail: '+g('email')+'\n'+
        (de?'Wunschdatum: ':'Preferred date: ')+g('date')+'\n'+
        (de?'Ort / Anlass: ':'Place / occasion: ')+g('place')+'\n\n'+
        g('msg')+'\n';
      window.location.href='mailto:foto@blitzkneisser.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
    });
  }

  /* ---- Year ---- */
  var y = document.getElementById('yr'); if(y) y.textContent = new Date().getFullYear();
})();
