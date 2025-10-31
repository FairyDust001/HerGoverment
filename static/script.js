// Chat functionality
const input = document.getElementById('input');
const sendBtn = document.getElementById('sendBtn');
const messages = document.getElementById('messages');
const status = document.getElementById('status');
const quickReplies = document.getElementById('quickReplies');

let convo = JSON.parse(localStorage.getItem('hg_convo') || '[]');

// Render messages
function renderMessages() {
  messages.innerHTML = '';
  convo.forEach(m => {
    const el = document.createElement('div');
    el.className = 'msg ' + (m.role === 'user' ? 'user' : 'bot');
    
    if (m.role === 'bot') {
      // Render bot messages as HTML
      el.innerHTML = m.text;
    } else {
      el.textContent = m.text;
    }

    messages.appendChild(el);
  });
  messages.scrollTop = messages.scrollHeight;
}
renderMessages();

// Push message to convo
function pushMessage(role, text) {
  convo.push({ role, text, ts: Date.now() });
  localStorage.setItem('hg_convo', JSON.stringify(convo));
  renderMessages();
}

// Send message
async function sendMessage(text) {
  if (!text || !text.trim()) return;
  pushMessage('user', text);
  input.value = '';
  status.textContent = 'Civi is typing…';

  // placeholder bot message
  const placeholder = { role: 'bot', text: '…' };
  convo.push(placeholder);
  renderMessages();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    if (!res.ok) throw new Error('Server error');
    const data = await res.json();

    convo.pop(); // remove placeholder
    pushMessage('bot', data.reply || 'Sorry — no response.');
    status.textContent = 'Ready';
  } catch (err) {
    convo.pop();
    pushMessage('bot', 'Error: ' + err.message);
    status.textContent = 'Error';
  }
}

// Event listeners
sendBtn.addEventListener('click', () => sendMessage(input.value));
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage(input.value);
  }
});

// Quick replies
quickReplies.addEventListener('click', (e) => {
  if (e.target.classList.contains('quick')) {
    sendMessage(e.target.textContent);
  }
});

// Smooth scroll buttons
document.querySelectorAll('.scroll-btn, .nav-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const targetId = btn.getAttribute('data-scroll');
    const target = document.getElementById(targetId);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Fade-in animation for mission pillars
const pillars = document.querySelectorAll('.pillar');

function handleFadeIn() {
  const windowBottom = window.innerHeight + window.scrollY;
  pillars.forEach(p => {
    if (windowBottom > p.offsetTop + 50) {
      p.classList.add('visible');
    }
  });
}

window.addEventListener('scroll', handleFadeIn);
window.addEventListener('load', handleFadeIn);
