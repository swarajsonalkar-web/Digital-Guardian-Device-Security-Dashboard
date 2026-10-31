const $=s=>document.querySelector(s),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
async function api(u,o={}){let r=await fetch(u,{headers:{'Content-Type':'application/json'},...o});return r.json()}
async function load(){let d=await api('/api/devices'),e=await api('/api/events');$('#devices').innerHTML=d.map(x=>`<div class="item row"><span style="flex:1">${esc(x.name)} · ${esc(x.kind)}</span><button class="danger" onclick="removeDevice(${x.id})">Remove</button></div>`).join('')||'<p class="muted">No devices registered.</p>';$('#events').innerHTML=e.map(x=>`<div class="item">${esc(x.event)}<br><small>${esc(x.device)} · ${x.created_at}</small></div>`).join('')||'<p class="muted">No events.</p>'}
window.removeDevice=async i=>{await api('/api/devices/'+i,{method:'DELETE'});load()};
$('#f').onsubmit=async e=>{e.preventDefault();await api('/api/devices',{method:'POST',body:JSON.stringify({name:$('#name').value,kind:$('#kind').value})});e.target.reset();load()};
$('#demo').onclick=async()=>{await api('/api/demo-event',{method:'POST'});load()};load();
