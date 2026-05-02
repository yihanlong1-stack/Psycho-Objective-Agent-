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
import time

class IntrospectAgent:
    def __init__(self, user_id):
        self.user_id = user_id
        self.mode = "Cold_Observer"  # 设置为冷观察者模式

    def process_text(self, raw_text):
        """处理原始心理文本的核心函数"""
        print(f"[系统] 正在为用户 {self.user_id} 分析文本...")
        
        # 1. 模拟分词与关键词提取
        print("[1/3] 提取主观情感词汇中...")
        time.sleep(0.5)
        
        # 2. 模拟逻辑链路重构
        # 这里展示了你对“长链推理”的理解
        print("[2/3] 执行 CoT 长链推理：剥离防御机制...")
        insights = self._analyze_defense_mechanism(raw_text)
        
        # 3. 输出客观分析
        print("[3/3] 生成最终客观洞察报告。")
        return {
            "status": "Success",
            "observation": insights
        }

    def _analyze_defense_mechanism(self, text):
        # 这是一个内部逻辑示例：识别诸如“否认”、“投射”等心理机制
        return "识别到潜在的投射性认同，建议采用第三人称视角重构。"

if __name__ == "__main__":
    # 模拟运行
    agent = IntrospectAgent(user_id="User_001")
    test_text = "我觉得大家都在针对我。"
    result = agent.process_text(test_text)
    print(f"\n分析结果：{result['observation']}")
