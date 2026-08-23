/* =========================================================================
   nikheel_ck_portfolio — shared behavior
   One file, loaded on every page. Every init function checks that its
   elements exist before doing anything, so it's safe to include everywhere.
   ========================================================================= */
(function(){
  "use strict";

  document.addEventListener("DOMContentLoaded", function(){
    initTheme();
    initNav();
    initScrollProgress();
    initReveal();
    initTyping();
    initCounters();
    initCopy();
    initBackToTop();
    initKernel();
    initContactForm();
  });

  /* ---------------- Theme ---------------- */
  function initTheme(){
    var saved = null;
    try{ saved = localStorage.getItem("nck-theme"); }catch(e){}
    if(saved) document.documentElement.setAttribute("data-theme", saved);
    var btn = document.querySelector("[data-theme-toggle]");
    if(!btn) return;
    updateIcon();
    btn.addEventListener("click", function(){
      var cur = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
      var next = cur === "light" ? "dark" : "light";
      if(next === "dark"){ document.documentElement.removeAttribute("data-theme"); }
      else{ document.documentElement.setAttribute("data-theme","light"); }
      try{ localStorage.setItem("nck-theme", next); }catch(e){}
      updateIcon();
    });
    function updateIcon(){
      var isLight = document.documentElement.getAttribute("data-theme") === "light";
      btn.innerHTML = '<i class="fa-solid ' + (isLight ? "fa-moon" : "fa-sun") + '"></i>';
      btn.setAttribute("aria-label", isLight ? "Switch to dark mode" : "Switch to light mode");
    }
  }

  /* ---------------- Nav (active tab + mobile panel) ---------------- */
  function initNav(){
    var page = document.body.getAttribute("data-page");
    if(page){
      document.querySelectorAll('[data-page-link="' + page + '"]').forEach(function(el){
        el.classList.add("active");
      });
    }
    var burger = document.querySelector("[data-hamburger]");
    var panel = document.querySelector("[data-mobile-panel]");
    if(burger && panel){
      burger.addEventListener("click", function(){
        panel.classList.toggle("open");
        var open = panel.classList.contains("open");
        burger.innerHTML = '<i class="fa-solid ' + (open ? "fa-xmark" : "fa-bars") + '"></i>';
      });
    }
  }

  /* ---------------- Scroll progress bar ---------------- */
  function initScrollProgress(){
    var bar = document.querySelector("[data-scroll-progress]");
    if(!bar) return;
    window.addEventListener("scroll", function(){
      var h = document.documentElement;
      var pct = (h.scrollTop) / ((h.scrollHeight - h.clientHeight) || 1) * 100;
      bar.style.width = pct + "%";
    }, { passive:true });
  }

  /* ---------------- Scroll reveal (notebook "execution") ---------------- */
  function initReveal(){
    var cells = document.querySelectorAll(".cell");
    if(!cells.length) return;
    if(!("IntersectionObserver" in window)){
      cells.forEach(function(c){ c.classList.add("in-view"); });
      return;
    }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add("in-view");
          io.unobserve(entry.target);
        }
      });
    }, { threshold:0.18, rootMargin:"0px 0px -60px 0px" });
    cells.forEach(function(c){ io.observe(c); });
  }

  /* ---------------- Hero typing effect ---------------- */
  function initTyping(){
    var el = document.querySelector("[data-typed]");
    if(!el) return;
    var words = (el.getAttribute("data-typed") || "").split("|").filter(Boolean);
    if(!words.length) return;
    var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var textSpan = document.createElement("span");
    var caret = document.createElement("span");
    caret.className = "caret";
    caret.setAttribute("aria-hidden","true");
    el.textContent = "";
    el.appendChild(textSpan);
    el.appendChild(caret);
    if(reduced){ textSpan.textContent = words[0]; return; }

    var wi = 0, ci = 0, deleting = false;
    function tick(){
      var word = words[wi];
      if(!deleting){
        ci++;
        textSpan.textContent = word.slice(0, ci);
        if(ci === word.length){
          deleting = true;
          setTimeout(tick, 1400);
          return;
        }
        setTimeout(tick, 55);
      } else {
        ci--;
        textSpan.textContent = word.slice(0, ci);
        if(ci === 0){
          deleting = false;
          wi = (wi + 1) % words.length;
          setTimeout(tick, 300);
          return;
        }
        setTimeout(tick, 28);
      }
    }
    setTimeout(tick, 500);
  }

  /* ---------------- Animated counters (About stats) ---------------- */
  function initCounters(){
    var nums = document.querySelectorAll("[data-count-to]");
    if(!nums.length) return;
    var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(!entry.isIntersecting) return;
        io.unobserve(entry.target);
        var el = entry.target;
        var end = parseFloat(el.getAttribute("data-count-to"));
        var suffix = el.getAttribute("data-count-suffix") || "";
        var decimals = el.getAttribute("data-count-decimals") ? parseInt(el.getAttribute("data-count-decimals"),10) : 0;
        if(reduced){ el.textContent = end.toFixed(decimals) + suffix; return; }
        var start = 0, dur = 1100, t0 = null;
        function step(ts){
          if(!t0) t0 = ts;
          var p = Math.min(1, (ts - t0) / dur);
          var eased = 1 - Math.pow(1 - p, 3);
          var val = start + (end - start) * eased;
          el.textContent = val.toFixed(decimals) + suffix;
          if(p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold:0.4 });
    nums.forEach(function(el){ io.observe(el); });
  }

  /* ---------------- Click-to-copy ---------------- */
  function initCopy(){
    document.querySelectorAll("[data-copy]").forEach(function(btn){
      btn.addEventListener("click", function(){
        var text = btn.getAttribute("data-copy");
        var done = function(){ showToast("Copied " + text); };
        if(navigator.clipboard && navigator.clipboard.writeText){
          navigator.clipboard.writeText(text).then(done, done);
        } else {
          done();
        }
      });
    });
  }
  function showToast(msg){
    var t = document.querySelector("[data-toast]");
    if(!t){
      t = document.createElement("div");
      t.className = "toast";
      t.setAttribute("data-toast","");
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add("show");
    clearTimeout(t._tm);
    t._tm = setTimeout(function(){ t.classList.remove("show"); }, 2200);
  }

  /* ---------------- Back to top ---------------- */
  function initBackToTop(){
    var btn = document.querySelector("[data-top-btn]");
    if(!btn) return;
    window.addEventListener("scroll", function(){
      btn.classList.toggle("show", window.scrollY > 480);
    }, { passive:true });
    btn.addEventListener("click", function(){
      window.scrollTo({ top:0, behavior:"smooth" });
    });
  }

  /* ---------------- Contact form (Formspree) ---------------- */
  function initContactForm(){
    var form = document.querySelector("[data-contact-form]");
    if(!form) return;
    var status = form.querySelector("[data-form-status]");
    var endpoint = form.getAttribute("data-endpoint") || "";
    var fallbackEmail = form.getAttribute("data-fallback-email") || "";
    form.addEventListener("submit", function(e){
      e.preventDefault();
      if(!endpoint || endpoint.indexOf("{{") === 0 || endpoint.indexOf("your-form-id") !== -1){
        var name = form.querySelector('[name="name"]');
        var email = form.querySelector('[name="email"]');
        var subject = form.querySelector('[name="subject"]');
        var message = form.querySelector('[name="message"]');
        var mailto = "mailto:" + fallbackEmail +
          "?subject=" + encodeURIComponent((subject && subject.value) || "Portfolio contact") +
          "&body=" + encodeURIComponent(
            "From: " + ((name && name.value) || "") + " (" + ((email && email.value) || "") + ")\n\n" +
            ((message && message.value) || "")
          );
        window.location.href = mailto;
        setStatus("No form endpoint set yet — opening your email app instead.", "err");
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      var originalHTML = btn ? btn.innerHTML : "";
      if(btn){ btn.disabled = true; btn.innerHTML = "sending…"; }
      setStatus("", "");
      fetch(endpoint, {
        method:"POST",
        headers:{ "Accept":"application/json" },
        body:new FormData(form)
      }).then(function(res){
        if(res.ok){
          form.reset();
          setStatus(">>> message sent ✓  thanks — I'll reply soon.", "ok");
        } else {
          setStatus("Something went wrong. Email me directly at " + fallbackEmail, "err");
        }
      }).catch(function(){
        setStatus("Network error. Email me directly at " + fallbackEmail, "err");
      }).finally(function(){
        if(btn){ btn.disabled = false; btn.innerHTML = originalHTML; }
      });
    });
    function setStatus(msg, cls){
      if(!status) return;
      status.textContent = msg;
      status.className = "form-status" + (cls ? " " + cls : "");
    }
  }

  /* ---------------- Kernel chatbot ---------------- */
  function initKernel(){
    var mount = document.querySelector("[data-kernel-mount]");
    if(!mount) return;

    mount.innerHTML =
      '<button class="kernel-toggle" data-k-toggle aria-expanded="false" aria-label="Open the kernel chat">' +
        '&gt;_<span class="kdot" aria-hidden="true"></span>' +
      '</button>' +
      '<div class="kernel-panel" data-k-panel role="dialog" aria-label="Kernel chat">' +
        '<div class="kernel-head">' +
          '<span class="dot"></span><span class="dot"></span><span class="dot"></span>' +
          '<span class="kernel-title">nikheel-kernel — zsh</span>' +
          '<button class="kernel-close" data-k-close aria-label="Close chat"><i class="fa-solid fa-xmark"></i></button>' +
        '</div>' +
        '<div class="kernel-log" data-k-log></div>' +
        '<div class="kernel-chips" data-k-chips></div>' +
        '<div class="kernel-input-row">' +
          '<span class="prompt">$</span>' +
          '<input type="text" data-k-input placeholder="ask about skills, projects, contact…" aria-label="Message the kernel">' +
          '<button class="kernel-send" data-k-send aria-label="Send"><i class="fa-solid fa-paper-plane"></i></button>' +
        '</div>' +
      '</div>';

    var toggle = mount.querySelector("[data-k-toggle]");
    var panel = mount.querySelector("[data-k-panel]");
    var closeBtn = mount.querySelector("[data-k-close]");
    var log = mount.querySelector("[data-k-log]");
    var input = mount.querySelector("[data-k-input]");
    var sendBtn = mount.querySelector("[data-k-send]");
    var chipsWrap = mount.querySelector("[data-k-chips]");

    var chips = ["Skills","Projects","Education","Contact","Resume","Fun fact"];
    chips.forEach(function(label){
      var c = document.createElement("button");
      c.className = "kchip";
      c.type = "button";
      c.textContent = label;
      c.addEventListener("click", function(){ send(label); });
      chipsWrap.appendChild(c);
    });

    var opened = false;
    toggle.addEventListener("click", function(){
      opened = !opened;
      panel.classList.toggle("open", opened);
      toggle.setAttribute("aria-expanded", String(opened));
      if(opened && !log.dataset.greeted){
        log.dataset.greeted = "1";
        botSay("Hey, I'm the kernel running this portfolio 👋 Ask me about Nikheel's skills, projects, education, or how to reach him.");
      }
      if(opened) setTimeout(function(){ input.focus(); }, 200);
    });
    closeBtn.addEventListener("click", function(){
      opened = false;
      panel.classList.remove("open");
      toggle.setAttribute("aria-expanded","false");
    });
    sendBtn.addEventListener("click", function(){ send(input.value); });
    input.addEventListener("keydown", function(e){
      if(e.key === "Enter"){ send(input.value); }
    });

    function send(text){
      text = (text || "").trim();
      if(!text) return;
      userSay(text);
      input.value = "";
      var reply = getReply(text);
      setTimeout(function(){ botSay(reply); }, 260);
    }

    function userSay(text){
      var row = document.createElement("div");
      row.className = "kmsg user";
      row.innerHTML = '<div class="who">you&gt;</div><p></p>';
      row.querySelector("p").textContent = text;
      log.appendChild(row);
      log.scrollTop = log.scrollHeight;
    }

    function botSay(text){
      var row = document.createElement("div");
      row.className = "kmsg bot";
      row.innerHTML = '<div class="who">kernel&gt;</div><p></p>';
      log.appendChild(row);
      var p = row.querySelector("p");
      log.scrollTop = log.scrollHeight;
      var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if(reduced){ p.textContent = text; log.scrollTop = log.scrollHeight; return; }
      var i = 0;
      var t = setInterval(function(){
        i++;
        p.textContent = text.slice(0, i);
        log.scrollTop = log.scrollHeight;
        if(i >= text.length) clearInterval(t);
      }, 14);
    }

    function getReply(raw){
      var q = raw.toLowerCase();
      var has = function(){ 
        for(var i=0;i<arguments.length;i++){ if(q.indexOf(arguments[i]) !== -1) return true; }
        return false;
      };
      if(has("skill","tech","stack","language","tool")){
        return "Core stack: Python, Machine Learning & Data Analysis on the AI/ML side, plus HTML5/CSS3/JavaScript for the web. Also comfortable with databases, and generally good at problem-solving in a team. Check the Skills page for the full breakdown.";
      }
      if(has("project","built","made","work")){
        return "Two to point you to right now: a Healthcare AI Assistant (Python + Streamlit) that does symptom checking, health tracking, and medication reminders — and this very portfolio, built with HTML5/CSS3/JS. Both are linked with code + live demo on the Projects page.";
      }
      if(has("education","study","college","cgpa","marks","grade","school","10th","12th")){
        return "Currently a first-year B.Tech student in AI & ML at MIT Academy of Engineering, first-semester CGPA 8.9. Before that: 82.3% in 12th, and 99.52% in 10th (school topper, 4th in state under KSEEB). Full timeline on the Education page.";
      }
      if(has("achieve","award","topper","rank","laptop")){
        return "Highlights: school topper + 4th rank in the state (KSEEB board, 10th grade) — recognised with a laptop from the government — plus a district-level cultural performance built around social awareness. More on the Achievements page.";
      }
      if(has("contact","email","reach","phone","hire","mail","connect")){
        return "Best way in: email at 202401110020@mitaoe.ac.in or use the form on the Contact page. He's based near MIT Academy of Engineering, Alandi, Pune. LinkedIn, GitHub and Instagram links are all on that page too.";
      }
      if(has("resume","cv")){
        return "You can view/download the resume from the Contact page — there's a dedicated button for it.";
      }
      if(has("github")){
        return "GitHub: github.com/Nikheel108 — that's where the source for both the Healthcare AI Assistant and this portfolio lives.";
      }
      if(has("linkedin")){
        return "LinkedIn is linked on the Contact page — good place to connect professionally.";
      }
      if(has("ai","ml","machine learning","artificial intelligence")){
        return "AI/ML is the main focus — currently studying it formally at MIT Academy of Engineering and applying it hands-on, like the Healthcare AI Assistant project.";
      }
      if(has("hi","hello","hey","yo","sup")){
        return "Hey there 👋 I can talk about skills, projects, education, achievements, or how to get in touch — what do you want to know?";
      }
      if(has("who are you","what are you")){
        return "I'm a small rule-based assistant built into this site — a nod to Nikheel's AI/ML focus. No live model behind me, just a fast way to explore the portfolio by asking questions.";
      }
      if(has("thank")){
        return "Anytime 🙂 Anything else you want to know?";
      }
      if(has("help","what can you")){
        return "Try asking about: skills, projects, education, achievements, contact, or resume. Or tap one of the quick chips below.";
      }
      return "Not sure about that one — try asking about skills, projects, education, achievements, contact, or resume.";
    }
  }

})();
