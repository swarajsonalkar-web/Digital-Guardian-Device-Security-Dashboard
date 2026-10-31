from fastapi import FastAPI,HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3,pathlib,random
DB=pathlib.Path(__file__).with_name('guardian.db')
def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
with db() as c:c.executescript("CREATE TABLE IF NOT EXISTS devices(id INTEGER PRIMARY KEY,name TEXT,kind TEXT); CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY,device TEXT,event TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);")
app=FastAPI(title='Digital Guardian')
class Device(BaseModel):name:str;kind:str
@app.get('/api/devices')
def devices():
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM devices ORDER BY id DESC')]
@app.post('/api/devices')
def add(x:Device):
 if not x.name.strip():raise HTTPException(400,'Name required')
 with db() as c:cur=c.execute('INSERT INTO devices(name,kind) VALUES(?,?)',(x.name,x.kind));return {'id':cur.lastrowid}
@app.delete('/api/devices/{i}')
def delete(i:int):
 with db() as c:c.execute('DELETE FROM devices WHERE id=?',(i,))
 return {'ok':True}
@app.get('/api/events')
def events():
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM events ORDER BY id DESC LIMIT 30')]
@app.post('/api/demo-event')
def demo():
 with db() as c:
  d=c.execute('SELECT name FROM devices ORDER BY RANDOM() LIMIT 1').fetchone();name=d['name'] if d else 'Demo device'
  event=random.choice(['Demo login notification','Demo software update notice','Demo connection status change'])
  cur=c.execute('INSERT INTO events(device,event) VALUES(?,?)',(name,event));return {'id':cur.lastrowid}
app.mount('/',StaticFiles(directory='static',html=True),name='static')
