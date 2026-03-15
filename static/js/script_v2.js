
// JobPoint v2 script - scroll reveal, counters, and validation
document.addEventListener('DOMContentLoaded', function(){
  // Scroll reveal
  const revealEls = document.querySelectorAll('.reveal');
  const onScroll = () => {
    const mid = window.innerHeight * 0.85;
    revealEls.forEach(el => {
      const r = el.getBoundingClientRect();
      if(r.top < mid) el.classList.add('visible');
    });
  };
  onScroll();
  window.addEventListener('scroll', onScroll);

  // Navbar scrolled class
  const nav = document.getElementById('mainNav');
  const handleNav = ()=> {
    if(window.scrollY > 40) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
  };
  handleNav(); window.addEventListener('scroll', handleNav);

  // Counters
  const counters = document.querySelectorAll('.counter');
  counters.forEach(c => {
    const target = +c.getAttribute('data-target') || 0;
    let started = false;
    const run = () => {
      if(started) return;
      const rect = c.getBoundingClientRect();
      if(rect.top < window.innerHeight*0.9){
        started = true;
        let current = 0;
        const step = Math.ceil(target / 120);
        const t = setInterval(()=>{
          current += step;
          if(current >= target){ c.textContent = target.toLocaleString(); clearInterval(t); }
          else c.textContent = current.toLocaleString();
        }, 12);
      }
    };
    run();
    window.addEventListener('scroll', run);
  });

  // Basic form validation for login/signup/contact (UI-only)
  const forms = document.querySelectorAll('form[novalidate]');
  forms.forEach(form => {
    form.addEventListener('submit', function(e){
      e.preventDefault();
      let ok = true;
      const inputs = form.querySelectorAll('input,textarea');
      inputs.forEach(inp => {
        if(inp.hasAttribute('required') && !inp.value.trim()){
          inp.classList.add('is-invalid'); inp.classList.remove('is-valid'); ok=false;
        } else if(inp.type === 'email' && inp.value){
          const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if(!re.test(inp.value)){ inp.classList.add('is-invalid'); inp.classList.remove('is-valid'); ok=false; }
          else { inp.classList.remove('is-invalid'); inp.classList.add('is-valid'); }
        } else if(inp.hasAttribute('minlength')){
          const min = parseInt(inp.getAttribute('minlength')||0,10);
          if(inp.value.length < min){ inp.classList.add('is-invalid'); inp.classList.remove('is-valid'); ok=false; }
          else { inp.classList.remove('is-invalid'); inp.classList.add('is-valid'); }
        } else {
          inp.classList.remove('is-invalid'); inp.classList.add('is-valid');
        }
      });
      // if contact form and ok -> show success alert (UI-only)
      if(ok){
        const success = document.getElementById('contactSuccess');
        if(success){ success.classList.remove('d-none'); success.textContent = 'Message sent (UI-only)'; form.reset();
          setTimeout(()=>{ success.classList.add('d-none'); }, 4000);
        } else {
          // simulate sign-in / sign-up success
          alert('Form looks good (UI-only).');
          form.reset();
        }
      } else {
        // scroll to first invalid field
        const firstInvalid = form.querySelector('.is-invalid');
        if(firstInvalid) firstInvalid.scrollIntoView({behavior:'smooth', block:'center'});
      }
    });
  });

  // Password strength (signup)
  const pwd = document.getElementById('signupPassword');
  if(pwd){
    pwd.addEventListener('input', ()=>{
      const v = pwd.value;
      const ok = /[0-9]/.test(v) && v.length >= 8;
      if(ok){ pwd.classList.remove('is-invalid');
	  pwd.classList.add('is-valid');
	  }
	  else { pwd.classList.add('is-invalid');
	  pwd.classList.remove('is-valid'); }
    });
  }
});
