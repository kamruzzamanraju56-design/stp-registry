# localization.py
TRANSLATIONS = {
    "Bangladesh": {
        "lang_code": "bn",
        "title": "🚨 সেভ দ্য পিপল (STP) | গ্লোবাল সোভেরেন রেজিস্ট্রি",
        "subtitle": "গণপ্রজাতন্ত্রী বাংলাদেশের আইন মন্ত্রণালয় ও জাতিসংঘের প্রটোকল ভিত্তিক সার্বভৌম বিচারিক ডেমো প্ল্যাটফর্ম",
        "header_filing": "📝 বেনামী অভিযোগ দাখিল প্যানেল (বাংলাদেশ জোন)",
        "lbl_cat": "হয়রানি বা সংকটের খাতটি চিহ্নিত করুন:",
        "lbl_accused_name": "অপরাধী বা প্রতিষ্ঠানের নাম (Accused Name) *বাধ্যতামূলক*:",
        "lbl_accused_desig": "অপরাধীর পদবি, কর্মস্থল বা সম্পর্ক (Designation) *বাধ্যতামূলক*:",
        "lbl_accused_contact": "অপরাধীর সুনির্দিষ্ট ঠিকানা, phone নম্বর বা সোশ্যাল আইডি *বাধ্যতামূলক*:",
        "lbl_remedy": "আপনি এই অভিযোগের বিপরীতে কোন পদক্ষেপ চান?",
        "lbl_details": "YOUR সমস্যার সুনির্দিষ্ট বিবরণ দিন (নূন্যতম ৫০০ শব্দ):",
        "lbl_evidence": "ডিজিটাল প্রমাণ (ছবি, চ্যাট স্ক্রিনশট, অডিও বা ডকুমেন্ট - সর্বোচ্চ ১০ এমবি):",
        "lbl_captcha": "মানুষ বনাম রোবট যাচাইকরণ ক্যাপচা:",
        "btn_submit": "🚨 বাংলাদেশ জুডিশিয়াল প্রটোকলে অভিযোগ দাখিল করুন",
        "err_fields": "❌ ত্রুটি: অনুগ্রহ করে ফর্মের প্রতিটি তথ্য এবং প্রমাণ সঠিকভাবে দিন।",
        "err_captcha": "❌ ত্রুটি: ক্যাপচা উত্তর ভুল হয়েছে !",
        "err_word_count": "❌ ত্রুটি: আইনি কার্যকারিতার জন্য বিবরণ অবশ্যই নূন্যতম ৫০০ শব্দের হতে হবে!",
        "ai_processing": "🤖 আমাদের এআই ইঞ্জিন আপনার অভিযোগের সত্যতা ও প্রাসঙ্গিকতা স্ক্রিন করছে...",
        "success_hide": "🎉 আপনার পরিচয় সফলভাবে চিরতরে হাইড করা হয়েছে! ফাইলটি AES-256 দ্বারা এনক্রিপ্ট করে সিকিউরড নোডে লক করা হয়েছে।"
    },
    "United States": {
        "lang_code": "en",
        "title": "🚨 Safe The People (STP) | Global Sovereign Registry",
        "subtitle": "Sovereign Judicial Infrastructure aligned with US Department of Justice & UN Protocols",
        "header_filing": "📝 Secure Anonymous Filing Panel (USA Zone)",
        "lbl_cat": "Select Crisis / Harassment Category:",
        "lbl_accused_name": "Name of the Accused Person / Institution *Mandatory*:",
        "lbl_accused_desig": "Accused Position / Relation / Rank *Mandatory*:",
        "lbl_accused_contact": "Accused Specific Address, Phone or Digital ID *Mandatory*:",
        "lbl_remedy": "What legal/social remedy do you require?",
        "lbl_details": "Describe the Incident / Violation in Detail (Minimum 500 words):",
        "lbl_evidence": "Upload Encrypted Digital Evidence / Proof Files (Max 10MB):",
        "lbl_captcha": "Sovereign Human Verification CAPTCHA:",
        "btn_submit": "🚨 Submit Secure Complaint to US Sovereign Registry",
        "err_fields": "❌ Error: Please ensure Accused Profile, Details, and Evidence are fully provided.",
        "err_captcha": "❌ Error: Incorrect CAPTCHA Answer!",
        "err_word_count": "❌ Error: Legal descriptions must be at least 500 words long!",
        "ai_processing": "🤖 Our AI Forensic Engine is running cryptographic and empirical verification...",
        "success_hide": "🎉 Identity Hidden Permanently! File encrypted with military-grade AES-256."
    }
}

def get_country_infrastructure(country_name):
    infrastructure = {
        "Bangladesh": {
            "agencies": [
                {"name": "জাতীয় জরুরি সেবা (Emergency Rescue)", "contact": "999", "email": "help@police.gov.bd", "sector": "Cyber/Domestic/Labor"},
                {"name": "সাইবার ক্রাইম ইনভেস্টিগেশন ডিভিশন (DMP)", "contact": "01769691522", "email": "cyberhelp@dmp.gov.bd", "sector": "🔒 Cyber Crimes"},
                {"name": "বাংলাদেশ সেনাবাহিনী সদরদপ্তর (National Security)", "contact": "16201", "email": "info@army.mil.bd", "sector": "🌾 Corruption/Fundamental Rights"},
                {"name": "জাতীয় আইনগত সহায়তা প্রদান সংস্থা (আইন মন্ত্রণালয়)", "contact": "16430", "email": "nlaso.gov.bd@gmail.com", "sector": "🏠 Domestic Violence"}
            ],
            "attorneys": [
                {"name": "বাংলাদেশ সুপ্রিম কোর্ট লিগ্যাল এইড কমিটি", "contact": "sc.legalaid@gmail.com", "type": "Pro-Bono Government Panel (৪০ জন ডেডিকেটেড আইনজীবী)"},
                {"name": "জাতীয় মহিলা আইনজীবী সমিতি (BNWLA Panel)", "contact": "bnwla@bdmail.net", "type": "Women & Children Rights Desk"},
                {"name": "বাংলাদেশ লিগ্যাল এইড অ্যান্ড সার্ভিসেস ট্রাস্ট (BLAST)", "contact": "mail@blast.org.bd", "type": "Fundamental Liberties Support"}
            ]
        },
        "United States": {
            "agencies": [
                {"name": "Federal Bureau of Investigation (FBI Cyber)", "contact": "1-800-CALL-FBI", "email": "cyber-reporting@fbi.gov", "sector": "🔒 Cyber Crimes"},
                {"name": "Department of Labor (Wage & Hour Division)", "contact": "1-866-487-9243", "email": "whd-strike@dol.gov", "sector": "🏭 Labor Exploitation"}
            ],
            "attorneys": [
                {"name": "American Civil Liberties Union (ACLU)", "contact": "legal-aid@aclu.org", "type": "Constitutional Rights Defense"},
                {"name": "Human Rights First Attorneys", "contact": "defense@humanrightsfirst.org", "type": "International Refugee & Protection"}
            ]
        }
    }
    return infrastructure.get(country_name, {"agencies": [], "attorneys": []})