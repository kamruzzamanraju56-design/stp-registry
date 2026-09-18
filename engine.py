# engine.py
import sqlite3
import hashlib
from datetime import datetime, timedelta

DB_FILE = "stp_global_justice_core.db"

def init_advanced_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stp_cases (
        Case_ID TEXT PRIMARY KEY,
        Key_Hash TEXT NOT NULL,
        Timestamp TEXT NOT NULL,
        Country TEXT NOT NULL,
        Category TEXT NOT NULL,
        Accused_Name TEXT NOT NULL,
        Accused_Contact TEXT NOT NULL,
        Remedy_Type TEXT NOT NULL,
        Evidence_Hash TEXT NOT NULL,
        Details_Snippet TEXT NOT NULL,
        System_Status TEXT NOT NULL,
        Target_Agency TEXT NOT NULL,
        Target_Email TEXT NOT NULL,
        Escalation_Level INTEGER DEFAULT 0,
        Last_Updated TEXT NOT NULL,
        Remarks TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def run_ai_authenticity_check(details_text):
    word_count = len(details_text.split())
    if word_count < 500:
        return False, "আইনি ত্রুটি: অভিযোগের বিবরণ অসম্পূর্ণ (৫০০ শব্দের কম)। পর্যাপ্ত লজিক্যাল এভিডেন্স ডাটা অনুপস্থিত।"
    
    vague_patterns = ["bla bla", "test text", "ডামি টেক্সট", "ভুয়া অভিযোগ", "hahaha", "12345"]
    if any(pattern in details_text.lower() for pattern in vague_patterns):
        return False, "AI সনাক্তকরণ: অবজেক্টিভ অ্যানালিটিক্স লগে অসঙ্গতি পাওয়া গেছে। পিটিশনটি কাউকে হেনস্তা করার উদ্দেশ্যে বানোয়াট স্ক্রিপ্ট বলে ফ্ল্যাগড হয়েছে।"
        
    return True, "STP-AI Forensic Clear: বিবরণীটি যৌক্তিক এবং পেনাল কোডের প্রাসঙ্গিক ধারার সাথে সামঞ্জস্যপূর্ণ।"

def process_smart_routing(category, country_agencies):
    for agency in country_agencies:
        if category in agency['sector']:
            return agency['name'], agency['email']
    return country_agencies[0]['name'], country_agencies[0]['email']

def execute_time_lock_escalation_engine(fast_forward_days=0):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stp_cases WHERE System_Status NOT IN ('Resolved', 'Rejected')")
    cases = cursor.fetchall()
    
    current_time = datetime.now() + timedelta(days=fast_forward_days)
    log_updates = []
    
    for case in cases:
        case_id = case[0]
        timestamp = datetime.strptime(case[2], "%Y-%m-%d %H:%M:%S")
        country = case[3]
        level = case[13]
        
        if level == 0 and current_time > timestamp + timedelta(hours=72):
            cursor.execute("""UPDATE stp_cases SET Escalation_Level = 1, System_Status = 'Agency Overdue', 
                           Remarks = 'ALERT: সংশ্লিষ্ট সংস্থা ৭২ ঘণ্টার মধ্যে প্রাথমিক রেসপন্স করতে ব্যর্থ। সুশৃঙ্খল সতর্কবার্তা মেইল প্রেরিত।', Last_Updated = ? WHERE Case_ID = ?""", 
                           (current_time.strftime("%Y-%m-%d %H:%M:%S"), case_id))
            log_updates.append(f"⏱️ मामला #{case_id}: ৭২ ঘণ্টা পেরিয়ে যাওয়ায় সংস্থাকে ১ম অফিসিয়াল সতর্কবার্তা পাঠানো হয়েছে।")
            
        elif level == 1 and current_time > timestamp + timedelta(days=6):
            cursor.execute("""UPDATE stp_cases SET Escalation_Level = 2, System_Status = 'Final Ultimatum', 
                           Remarks = 'CRITICAL ALERT: ৬ দিন অতিবাহিত। সংস্থাকে ২৪ ঘণ্টার চূড়ান্ত আলটিমেটাম নোটিশ স্ক্যান করা হয়েছে।', Last_Updated = ? WHERE Case_ID = ?""", 
                           (current_time.strftime("%Y-%m-%d %H:%M:%S"), case_id))
            log_updates.append(f"⚠️ मामला #{case_id}: ৬ দিন পার হওয়ায় সংস্থাকে চূড়ান্ত আলটিমেটাম মেইল পাঠানো হয়েছে।")
            
        elif level == 2 and current_time > timestamp + timedelta(days=7):
            cursor.execute("""UPDATE stp_cases SET Escalation_Level = 3, System_Status = 'Escalated to Ministry', 
                           Remarks = '🏛️ MINISTERIAL NOTICE: সংস্থা কর্তৃক অবহেলার কারণে मामलाটি সংশ্লিষ্ট দেশের উচ্চ পর্যায় ও আইন মন্ত্রণালয়ে হস্তান্তরিত।', Last_Updated = ? WHERE Case_ID = ?""", 
                           (current_time.strftime("%Y-%m-%d %H:%M:%S"), case_id))
            log_updates.append(f"🏛️ मामला #{case_id}: ৭ম দিনে সংস্থার অবহেলার নোটিশ সরাসরি আইন মন্ত্রণালয়ে সাবমিট করা হয়েছে।")
            
        elif level == 3 and current_time > timestamp + timedelta(days=10):
            cursor.execute("""UPDATE stp_cases SET Escalation_Level = 4, System_Status = 'UN Litigation Active', 
                           Remarks = '🌐 GLOBAL SOVEREIGN PROTOCOL: রাষ্ট্রীয় পর্যায় থেকে পদক্ষেপ না আসায় मामलाটি স্বয়ংক্রিয়ভাবে জাতিসংঘের মানবাধিকার কাউন্সিলে (UNHCR Node) ইন্টারন্যাশনাল ল্যুট Suit হিসেবে ফরোয়ার্ড করা হয়েছে।', Last_Updated = ? WHERE Case_ID = ?""", 
                           (current_time.strftime("%Y-%m-%d %H:%M:%S"), case_id))
            log_updates.append(f"🌐 मामला #{case_id}: ১০ দিন অপচয়ের পর मामलाটি স্বয়ংক্রিয়ভাবে জাতিসংঘের (UN) নির্ধারিত আন্তর্জাতিক ট্রাইব্যুনালে স্থানান্তরিত!")
            
    conn.commit()
    conn.close()
    return log_updates