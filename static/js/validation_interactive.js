
document.addEventListener('DOMContentLoaded', function(){
  function validateForm(form){
    let valid = true;
    const email = form.querySelector('input[type="email"]');
    const pass = form.querySelector('input[type="password"]');
    if(email){
      const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(".+"))@(([^<>()[\]\\.,;:\s@\"]+\.)+[^<>()[\]\\.,;:\s@\"]{2,})$/i;
      if(!re.test(email.value)){ valid=false; email.classList.add('is-invalid'); }
      else email.classList.remove('is-invalid');
    }
    if(pass){
      if(pass.value.length < 6){ valid=false; pass.classList.add('is-invalid'); }
      else pass.classList.remove('is-invalid');
    }
    return valid;
  }

  document.querySelectorAll('form.needs-validation').forEach(function(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      if(validateForm(form)){
        const alert = document.createElement('div');
        alert.className='alert alert-success mt-3';
        alert.innerText = 'Form submitted (demo)';
        const prev = form.querySelector('.alert');
        if(prev) prev.remove();
        form.appendChild(alert);
      } else {
        const alert = document.createElement('div');
        alert.className='alert alert-danger mt-3';
        alert.innerText = 'Please fix validation errors.';
        const prev = form.querySelector('.alert');
        if(prev) prev.remove();
        form.appendChild(alert);
      }
    });
  });

  document.querySelectorAll('.btn-like').forEach(function(btn){
    btn.addEventListener('click', function(){
      const countEl = btn.querySelector('.like-count');
      let count = parseInt(countEl.innerText || '0');
      if(btn.classList.contains('liked')){ count--; btn.classList.remove('liked'); }
      else { count++; btn.classList.add('liked'); }
      countEl.innerText = count;
    });
  });

  document.querySelectorAll('.chat-form').forEach(function(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      const input = form.querySelector('input[type="text"]');
      if(!input || !input.value.trim()) return;
      const box = form.closest('.chat-container').querySelector('.chat-box');
      const msg = document.createElement('div');
      msg.className = 'mb-2 text-end';
      msg.innerHTML = '<span class="badge bg-primary">'+input.value+'</span>';
      box.appendChild(msg);
      input.value='';
      box.scrollTop = box.scrollHeight;
    });
  });

  document.querySelectorAll('.btn-edit-profile').forEach(function(btn){
    btn.addEventListener('click', function(){
      const form = btn.closest('.profile-section').querySelector('form');
      form.querySelectorAll('input, textarea').forEach(function(inp){
        inp.toggleAttribute('readonly');
        inp.classList.toggle('border-primary');
      });
    });
  });
});
