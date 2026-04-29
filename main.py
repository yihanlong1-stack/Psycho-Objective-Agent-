main.py
import datetime
import uuid
import sys
import os
import argparse
from journal import save_journal_entry, load_journal_entries, 
generate_weekly_report
from agent import analyze_entry_emotion, get_conversational_response, 
generate_psychodynamic_insight
if not os.path.exists('data'):
 os.makedirs('data')
def create_new_entry():
 print("\n--- IntrospectAI: Conversational Journal ---")
 text = sys.stdin.read()
 if not text: return
 timestamp = datetime.datetime.now().isoformat()
 emotion = analyze_entry_emotion(text)
 conversation = get_conversational_response(text)
 save_journal_entry({
 "id": str(uuid.uuid4()), "timestamp": timestamp, "text": text,
 "emotion": emotion, "conversation": conversation
 })
 print(f"\nAI Insight: {conversation}")
if __name__ == "__main__":
 parser = argparse.ArgumentParser()
 parser.add_argument('action', choices=['write', 'list', 'insight'])
 args = parser.parse_args()
 if args.action == 'write': create_new_entry()
2. AI 智能体逻辑 (agent.py)
agent.py
from openai import OpenAI
client = OpenAI()
def analyze_entry_emotion(text):
 prompt = f"分析此文本的深层心理防御机制: '{text}'。"
 response = client.chat.completions.create(
 model="gpt-4",
 messages=[{"role": "user", "content": prompt}]
 )
 return response.choices[0].message.content
def get_conversational_response(text):
 prompt = f"作为一个冷静的心理分析师，回应此日记: '{text}'。"
 response = client.chat.completions.create(
 model="gpt-4",
 messages=[{"role": "user", "content": prompt}]
 )
 return response.choices[0].message.content
3. 依赖库清单 (requirements.txt)
requirements.txt
openai
python-dotenv
