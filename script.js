// simple chat UI + fetch to /chat
const input = document.getElementById('input');
const sendBtn = document.getElementById('sendBtn');
const messages = document.getElementById('messages');
const status = document.getElementById('status');
const quickReplies = document.getElementById('quickReplies');

let convo = JSON.parse(localStorage.getItem('hg_convo') || '[]');

function renderMessages(){
  messages.innerHTML = '';
  convo.forEach(m => {
    const el = document.createElement('div');
    el.className = 'msg ' + (m.role === 'user' ? 'user' : 'bot');
    el.textContent = m.text;
    messages.appendChild(el);
  });
  messages.scrollTop = messages.scrollHeight;
}
renderMessages();

function pushMessage(role, text){
  convo.push({role, text, ts: Date.now()});
  localStorage.setItem('hg_convo', JSON.stringify(convo));
  renderMessages();
}

async function sendMessage(text){
  if(!text || !text.trim()) return;
  pushMessage('user', text);
  input.value = '';
  status.textContent = 'Her Government is typing…';

  // show a placeholder bot message so the UI shows typing
  const placeholder = {role:'bot', text: '…'};
  convo.push(placeholder);
  renderMessages();

  try{
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({message:text})
    });
    if(!res.ok) throw new Error('Server error');
    const data = await res.json();
    // replace last placeholder bot message
    convo.pop();
    pushMessage('bot', data.reply || 'Sorry — no response.');
    status.textContent = 'Ready';
  }catch(err){
    convo.pop();
    pushMessage('bot', 'Error: '+ err.message);
    status.textContent = 'Error';
  }
}

// send on click or enter
sendBtn.addEventListener('click', ()=> sendMessage(input.value));
input.addEventListener('keydown', (e)=> {
  if(e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage(input.value);
  }
});

// quick replies
quickReplies.addEventListener('click', (e)=>{
  if(e.target.classList.contains('quick')){
    sendMessage(e.target.textContent);
  }
});
