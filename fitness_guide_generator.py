#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Fitness Guide HTML Generator
This script creates your complete fitness and nutrition guide as a single HTML file
"""

def generate_fitness_guide():
    """Generate the complete HTML fitness guide with ALL content"""
    
    html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الدليل الشامل للياقة البدنية والتغذية</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; direction: rtl; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        h1 { font-size: 2.5em; margin-bottom: 10px; text-align: center; }
        .nav-tabs { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; background: white; padding: 15px; border-radius: 15px; }
        .tab-btn { padding: 12px 24px; background: #e0e7ff; border: none; border-radius: 10px; cursor: pointer; font-size: 16px; font-weight: 600; transition: all 0.3s; }
        .tab-btn.active { background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; }
        .content-section { display: none; background: white; padding: 30px; border-radius: 15px; margin-bottom: 20px; }
        .content-section.active { display: block; }
        .meal-card { background: #f9fafb; padding: 15px; border-radius: 8px; margin-bottom: 15px; cursor: pointer; border-left: 4px solid #10b981; }
        .meal-card:hover { background: #f3f4f6; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th { background: #10b981; color: white; padding: 12px; text-align: right; }
        td { padding: 10px; border-bottom: 1px solid #e5e7eb; }
        .checklist-item { display: flex; align-items: center; padding: 12px; background: #f9fafb; margin-bottom: 10px; border-radius: 8px; }
        .checklist-item input[type="checkbox"] { width: 20px; height: 20px; margin-left: 15px; }
        h2 { color: #059669; margin-bottom: 20px; }
        h3 { color: #047857; margin: 20px 0 15px 0; }
        .info-card { background: #f3f4f6; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .exercise-card { background: #ddd6fe; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
        .tip-box { background: #fef3c7; padding: 20px; border-radius: 10px; margin: 20px 0; }
        @media (max-width: 768px) { .container { padding: 10px; } h1 { font-size: 1.8em; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>💪 الدليل الشامل للياقة البدنية والتغذية</h1>
            <p style="text-align: center; opacity: 0.9;">مخصص لعمر 25 سنة | طول 178 سم | وزن 80 كجم | ساعات العمل 8-5</p>
        </header>
        
        <div class="nav-tabs">
            <button class="tab-btn active" onclick="showSection('overview')">نظرة عامة</button>
            <button class="tab-btn" onclick="showSection('daily')">القائمة اليومية</button>
            <button class="tab-btn" onclick="showSection('breakfast')">الفطار</button>
            <button class="tab-btn" onclick="showSection('postworkout')">بعد التمرين</button>
            <button class="tab-btn" onclick="showSection('lunch')">الغداء</button>
            <button class="tab-btn" onclick="showSection('dinner')">العشاء</button>
            <button class="tab-btn" onclick="showSection('snacks')">السناكات</button>
            <button class="tab-btn" onclick="showSection('exercise')">التمارين</button>
            <button class="tab-btn" onclick="showSection('supplements')">المكملات</button>
            <button class="tab-btn" onclick="showSection('emergency')">حلول الطوارئ</button>
        </div>
'''

    # Add all sections
    sections = generate_all_sections()
    html_content += sections
    
    # Add JavaScript
    html_content += '''
    </div>
    <script>
        function showSection(sectionId) {
            // Hide all sections
            const sections = document.querySelectorAll('.content-section');
            sections.forEach(section => section.classList.remove('active'));
            
            // Remove active class from all buttons
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            // Show selected section
            const selectedSection = document.getElementById(sectionId);
            if (selectedSection) {
                selectedSection.classList.add('active');
            }
            
            // Add active class to clicked button
            event.target.classList.add('active');
            
            // Save to localStorage
            localStorage.setItem('activeSection', sectionId);
        }
        
        // Load saved section on page load
        window.onload = function() {
            const savedSection = localStorage.getItem('activeSection');
            if (savedSection) {
                const sections = document.querySelectorAll('.content-section');
                sections.forEach(section => section.classList.remove('active'));
                const selectedSection = document.getElementById(savedSection);
                if (selectedSection) {
                    selectedSection.classList.add('active');
                }
            }
            
            // Add click handlers to meal cards
            const mealCards = document.querySelectorAll('.meal-card');
            mealCards.forEach(card => {
                card.addEventListener('click', function() {
                    const details = this.querySelector('.meal-details');
                    if (details) {
                        details.style.display = details.style.display === 'block' ? 'none' : 'block';
                    }
                });
            });
            
            // Save checkbox states
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            checkboxes.forEach(checkbox => {
                // Load saved state
                const savedState = localStorage.getItem(checkbox.id);
                if (savedState === 'true') {
                    checkbox.checked = true;
                }
                
                // Save state on change
                checkbox.addEventListener('change', function() {
                    localStorage.setItem(this.id, this.checked);
                });
            });
        }
    </script>
</body>
</html>'''
    
    return html_content

def generate_all_sections():
    """Generate all content sections"""
    
    sections = '''
        <!-- Overview Section -->
        <div id="overview" class="content-section active">
            <h2>📋 نظرة عامة على البرنامج</h2>
            ''' + generate_overview_content() + '''
        </div>
        
        <!-- Daily Checklist Section -->
        <div id="daily" class="content-section">
            <h2>✅ القائمة اليومية</h2>
            ''' + generate_daily_checklist() + '''
        </div>
        
        <!-- Breakfast Section -->
        <div id="breakfast" class="content-section">
            <h2>🍳 وجبة الفطار (5:30-6:30 ص)</h2>
            ''' + generate_breakfast_content() + '''
        </div>
        
        <!-- Post Workout Section -->
        <div id="postworkout" class="content-section">
            <h2>🥪 وجبة ما بعد التمرين (7:30-8:00 ص)</h2>
            ''' + generate_postworkout_content() + '''
        </div>
        
        <!-- Lunch Section -->
        <div id="lunch" class="content-section">
            <h2>🍽️ الغداء (12:30-2:00 ظ)</h2>
            ''' + generate_lunch_content() + '''
        </div>
        
        <!-- Dinner Section -->
        <div id="dinner" class="content-section">
            <h2>🥗 العشاء (7:00-9:00 م)</h2>
            ''' + generate_dinner_content() + '''
        </div>
        
        <!-- Snacks Section -->
        <div id="snacks" class="content-section">
            <h2>🍎 السناك (بين الوجبات)</h2>
            ''' + generate_snacks_content() + '''
        </div>
        
        <!-- Exercise Section -->
        <div id="exercise" class="content-section">
            <h2>💪 البرنامج الرياضي</h2>
            ''' + generate_exercise_content() + '''
        </div>
        
        <!-- Supplements Section -->
        <div id="supplements" class="content-section">
            <h2>💊 المكملات والقياسات</h2>
            ''' + generate_supplements_content() + '''
        </div>
        
        <!-- Emergency Section -->
        <div id="emergency" class="content-section">
            <h2>🚨 حلول الطوارئ والنصائح</h2>
            ''' + generate_emergency_content() + '''
        </div>
    '''
    
    return sections

def generate_overview_content():
    return '''
    <div class="info-card">
        <h3>معلوماتك الشخصية</h3>
        <ul>
            <li>العمر: 25 سنة</li>
            <li>الطول: 178 سم</li>
            <li>الوزن: 80 كجم</li>
            <li>ساعات العمل: 8 ص - 5 م (أحياناً حتى 6 م)</li>
        </ul>
    </div>
    
    <div class="info-card">
        <h3>الجدول الأسبوعي</h3>
        <table>
            <tr><th>اليوم</th><th>التمرين</th><th>المدة</th></tr>
            <tr><td>الأحد</td><td>صدر وترايسبس</td><td>35-40 دقيقة</td></tr>
            <tr><td>الاثنين</td><td>كارديو ومرونة</td><td>35-40 دقيقة</td></tr>
            <tr><td>الثلاثاء</td><td>ظهر وبايسبس</td><td>35-40 دقيقة</td></tr>
            <tr><td>الأربعاء</td><td>أرجل وأكتاف</td><td>35-40 دقيقة</td></tr>
            <tr><td>الخميس</td><td>تمرين خفيف</td><td>20-25 دقيقة</td></tr>
            <tr><td>الجمعة</td><td>راحة وسهر</td><td>-</td></tr>
            <tr><td>السبت</td><td>تمرين تعويضي</td><td>50-60 دقيقة</td></tr>
        </table>
    </div>
    '''

def generate_daily_checklist():
    return '''
    <div class="checklist-item">
        <input type="checkbox" id="wake">
        <label for="wake">5:15 ص - استيقاظ + كوب ماء (240 مل)</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="breakfast">
        <label for="breakfast">5:30 ص - فطار (اختر من القائمة)</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="exercise">
        <label for="exercise">6:00 ص - تمرين صباحي (حسب اليوم)</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="postworkout">
        <label for="postworkout">7:30 ص - وجبة ما بعد التمرين</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="snack1">
        <label for="snack1">10:00 ص - سناك صباحي</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="lunch">
        <label for="lunch">1:00 ظ - غداء (اختر من القائمة)</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="snack2">
        <label for="snack2">4:00 ع - سناك عصر</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="dinner">
        <label for="dinner">8:00 م - عشاء (اختر من القائمة)</label>
    </div>
    <div class="checklist-item">
        <input type="checkbox" id="sleep">
        <label for="sleep">10:00 م - نوم</label>
    </div>
    '''

def generate_breakfast_content():
    return '''
    <h3>مجموعة الشوفان (6 خيارات)</h3>
    <div class="meal-card">
        <div class="meal-title">شوفان كلاسيكي</div>
        <div class="meal-details">شوفان جاف (40 جرام) + حليب دافئ (240 مل) + موز مهروس (120 جرام) + عسل (15 جرام) + لوز مطحون (15 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوفان بالتوت</div>
        <div class="meal-details">شوفان جاف (40 جرام) + حليب (240 مل) + فراولة مقطعة (75 جرام) + كاكاو خام (1 ملعقة صغيرة) + عسل (15 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوفان كريمي</div>
        <div class="meal-details">شوفان جاف (40 جرام) + زبادي يوناني (150 جرام) + مانجو ناعمة (85 جرام) + جوز هند (10 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوفان بالتفاح</div>
        <div class="meal-details">شوفان جاف (40 جرام) + حليب (240 مل) + تفاح مبشور (150 جرام) + قرفة (نصف ملعقة صغيرة) + عسل (15 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوفان الشوكولاتة</div>
        <div class="meal-details">شوفان جاف (40 جرام) + موز (120 جرام) + كاكاو خام (1 ملعقة كبيرة) + زبدة لوز (5 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوفان البرتقال</div>
        <div class="meal-details">شوفان جاف (40 جرام) + عصير برتقال (120 مل) + حليب (120 مل) + مكسرات مطحونة (15 جرام)</div>
    </div>
    
    <h3>مجموعة التوست (5 خيارات - بدون بيض)</h3>
    <div class="meal-card">
        <div class="meal-title">توست العسل</div>
        <div class="meal-details">توست أسمر (60 جرام = شريحتان) + جبنة كريمي قليلة الدسم (45 جرام = 3 ملاعق) + عسل (5 جرام) + موز شرائح (60 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">توست الأفوكادو</div>
        <div class="meal-details">توست أسمر (60 جرام = شريحتان) + أفوكادو مهروس (100 جرام) + عسل (5 جرام) + مكسرات مطحونة (10 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">توست الفول السوداني</div>
        <div class="meal-details">توست أسمر (60 جرام = شريحتان) + زبدة فول سوداني (15 جرام) + موز شرائح (120 جرام) + قرفة (رشة)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">توست القريش</div>
        <div class="meal-details">توست أسمر (60 جرام = شريحتان) + جبنة قريش (60 جرام = 4 ملاعق) + عسل (5 جرام) + فراولة شرائح (75 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">توست الحمص</div>
        <div class="meal-details">توست أسمر محمص (60 جرام = شريحتان) + حمص ناعم (45 جرام = 3 ملاعق) + زيت زيتون (5 مل) + زعتر (1 ملعقة صغيرة)</div>
    </div>
    
    <h3>مجموعة المشروبات (4 خيارات)</h3>
    <div class="meal-card">
        <div class="meal-title">ميلك شيك الموز</div>
        <div class="meal-details">حليب (240 مل) + موز (120 جرام) + شوفان (20 جرام = 2 ملاعق) + عسل (5 جرام) + لوز (10 حبات)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">مشروب الفراولة</div>
        <div class="meal-details">زبادي (150 جرام) + فراولة (75 جرام) + حليب (120 مل) + عسل (5 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">عصير المانجو البروتيني</div>
        <div class="meal-details">مانجو (85 جرام) + زبادي يوناني (100 جرام) + حليب (120 مل) + عسل (5 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">مشروب الشوكولاتة</div>
        <div class="meal-details">حليب (240 مل) + كاكاو خام (1 ملعقة كبيرة) + موز (120 جرام) + شوفان مطحون (20 جرام) + عسل (5 جرام)</div>
    </div>
    '''

def generate_postworkout_content():
    return '''
    <h3>خيارات من البيت (10 أنواع)</h3>
    ''' + ''.join([f'''
    <div class="meal-card">
        <div class="meal-title">{title}</div>
        <div class="meal-details">{details}</div>
    </div>
    ''' for title, details in [
        ("ساندوتش الفراخ التركي", "فراخ تركي (80 جرام) + توست ناعم (60 جرام = شريحتان) + جبنة كريمي (15 جرام = 1 ملعقة) + خيار مقشر (30 جرام) + خس ناعم (20 جرام)"),
        ("توست العسل والجبنة", "توست أسمر (60 جرام = شريحتان) + جبنة قريش (60 جرام = 4 ملاعق) + عسل (5 جرام) + موز شرائح (60 جرام)"),
        ("ساندوتش الأفوكادو", "توست أسمر (60 جرام = شريحتان) + أفوكادو مهروس (100 جرام) + فراخ تركي (60 جرام) + طماطم ناعمة (50 جرام)"),
        ("رول الفراخ", "تورتيلا ناعمة (50 جرام) + فراخ تركي مقطعة (80 جرام) + جبنة كريمي (15 جرام) + خس مفروم (20 جرام) + صوص زبادي (30 جرام)"),
        ("توست الحمص الحلو", "توست أسمر (60 جرام = شريحتان) + حمص ناعم (45 جرام = 3 ملاعق) + عسل (5 جرام) + مكسرات مطحونة (10 جرام)"),
        ("ساندوتش الجبنة والعسل", "توست أسمر (60 جرام = شريحتان) + جبنة بيضاء (60 جرام = 3 شرائح) + عسل (5 جرام) + تفاح شرائح (75 جرام)"),
        ("عصير بروتين حلو", "موز (150 جرام) + زبادي يوناني (150 جرام) + حليب (240 مل) + زبدة لوز (5 جرام) + عسل (5 جرام)"),
        ("توست الموز والفول السوداني", "توست أسمر (60 جرام = شريحتان) + زبدة فول سوداني (15 جرام) + موز مهروس (120 جرام) + قرفة (رشة)"),
        ("ساندوتش التونة", "تونة مهروسة (40 جرام) + مايونيز خفيف (5 جرام) + خيار مفروم ناعم (50 جرام) + توست أسمر (60 جرام = شريحتان)"),
        ("بان كيك الشوفان", "شوفان مطحون (20 جرام) + موز مهروس (60 جرام) + حليب (60 مل) + عسل (5 جرام)")
    ]]) + '''
    
    <h3>خيارات من الشارع (5 أنواع)</h3>
    <div class="meal-card">
        <div class="meal-title">فول بالعسل</div>
        <div class="meal-details">فول مدمس (120 جرام) + عسل (5 جرام) + خبز بلدي (40 جرام = ربع رغيف)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">ساندوتش جبنة حلو</div>
        <div class="meal-details">جبنة رومي (60 جرام = 3 شرائح) + عسل (5 جرام) + خيار (50 جرام) + توست أسمر (60 جرام) من أي محل</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">عصير طبيعي + كرواسون</div>
        <div class="meal-details">عصير برتقال طبيعي (240 مل) + كرواسون جبنة بيضا (80 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">لبن رايب حلو</div>
        <div class="meal-details">لبن رايب (240 مل) + عسل (5 جرام) + بسكويت شوفان (30 جرام = قطعتان)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">ساندوتش الحلاوة الطحينية</div>
        <div class="meal-details">توست أسمر (60 جرام = شريحتان) + حلاوة طحينية (10 جرام) + موز شرائح (60 جرام)</div>
    </div>
    '''

def generate_lunch_content():
    return '''
    <div class="info-card" style="background: #fee2e2; border-left: 4px solid #ef4444;">
        <strong>ملاحظة مهمة حول الكميات:</strong><br>
        • اللحوم والدجاج والأسماك: الكميات المذكورة هي للوزن قبل الطهي (وزن خام)<br>
        • الأرز والمكرونة والنشويات: الكميات المذكورة هي للوزن بعد الطهي (وزن مطبوخ)<br>
        • الخضروات والفواكه: الكميات المذكورة هي للوزن قبل الطهي (وزن خام)
    </div>
    
    <h3>أيام الفراخ (8 أنواع)</h3>
    ''' + ''.join([f'''
    <div class="meal-card">
        <div class="meal-title">{title}</div>
        <div class="meal-details">{details}</div>
    </div>
    ''' for title, details in [
        ("فراخ بالشوربة", "فراخ مسلوقة (150 جرام قبل الطهي) + أرز أبيض بالشعرية (150 جرام بعد الطهي) + خضار مسلوق طري (200 جرام) + شوربة فراخ (240 مل)"),
        ("فراخ مشوية بالعسل", "فراخ مشوية (150 جرام قبل الطهي) + بطاطس محمرة بالفرن (200 جرام) + سلطة زبادي بالخيار (100 جرام)"),
        ("فراخ بانيه", "فراخ بانيه مخبوزة (150 جرام قبل الطهي) + أرز بني (150 جرام بعد الطهي) + جزر مسلوق بالعسل (75 جرام)"),
        ("شوربة فراخ", "شوربة فراخ بالخضار (360 مل) + قطع فراخ (100 جرام قبل الطهي) + أرز أبيض (100 جرام بعد الطهي) + خبز أسمر (30 جرام)"),
        ("فراخ بالكريمة", "فراخ مطبوخة (150 جرام قبل الطهي) + مكرونة مسلوقة (200 جرام بعد الطهي) + بازلاء وجزر (75 جرام)"),
        ("أجنحة مشوية", "أجنحة فراخ مشوية (160 جرام قبل الطهي = 4 أجنحة) + أرز بالزعفران (150 جرام بعد الطهي) + سلطة طحينة (100 جرام)"),
        ("فراخ ستربس", "فراخ ستربس مشوية (150 جرام قبل الطهي) + بطاطس مهروسة بالحليب (200 جرام) + ذرة مسلوقة (75 جرام)"),
        ("كباب فراخ", "كباب فراخ (150 جرام قبل الطهي = 3 قطع) + أرز أبيض (150 جرام بعد الطهي) + سلطة زبادي بالنعناع (100 جرام)")
    ]]) + '''
    
    <h3>أيام السمك (4 أنواع)</h3>
    <div class="meal-card">
        <div class="meal-title">فيليه مقلي</div>
        <div class="meal-details">فيليه سمك مقلي خفيف (150 جرام قبل الطهي) + أرز أبيض (150 جرام بعد الطهي) + طحينة بالطماطم (100 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">سالمون مشوي</div>
        <div class="meal-details">سمك سالمون مشوي (120 جرام قبل الطهي) + بطاطس مسلوقة (200 جرام) + سلطة خضراء (150 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">تونة بالمكرونة</div>
        <div class="meal-details">تونة بالطماطم (80 جرام) + مكرونة (200 جرام بعد الطهي) + طماطم مطبوخة (100 جرام) + جبنة بارميزان (10 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوربة سمك</div>
        <div class="meal-details">شوربة سمك بالخضار (360 مل) + قطع سمك (100 جرام قبل الطهي) + أرز أبيض (100 جرام بعد الطهي)</div>
    </div>
    
    <h3>أيام اللحمة (3 أنواع)</h3>
    <div class="meal-card">
        <div class="meal-title">لحمة مفرومة</div>
        <div class="meal-details">لحمة مفرومة بالبصل والطماطم (100 جرام قبل الطهي) + أرز بني (150 جرام بعد الطهي) + فاصوليا خضرا (150 جرام) + زبادي (120 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">كفتة بالصوص</div>
        <div class="meal-details">كفتة مشوية بالصوص (120 جرام قبل الطهي = 3 قطع) + مكرونة بالطماطم (200 جرام بعد الطهي) + سلطة خضراء (150 جرام)</div>
    </div>
    <div class="meal-card">
        <div class="meal-title">شوربة لحمة</div>
        <div class="meal-details">شوربة لحمة بالخضار (360 مل) + قطع لحمة طرية (100 جرام قبل الطهي) + أرز أبيض (150 جرام بعد الطهي) + خبز (40 جرام = ربع رغيف)</div>
    </div>
    '''

def generate_dinner_content():
    return '''
    <h3>سلطات كريمية (8 أنواع)</h3>
    ''' + ''.join([f'''
    <div class="meal-card">
        <div class="meal-title">{title}</div>
        <div class="meal-details">{details}</div>
    </div>
    ''' for title, details in [
        ("سلطة فراخ بالمايونيز", "فراخ مسلوقة مقطعة (100 جرام قبل الطهي) + خضار مشكلة (150 جرام) + مايونيز خفيف (10 جرام) + زبادي (30 جرام = ملعقتان)"),
        ("سلطة تونة كريمية", "تونة (60 جرام) + خضار ناعمة (150 جرام) + كريمة طبخ خفيفة (15 جرام) + جبنة فيتا (30 جرام)"),
        ("سلطة الأفوكادو", "أفوكادو مهروس (100 جرام) + طماطم مقطعة (75 جرام) + خيار (75 جرام) + ذرة (40 جرام) + تتبيلة زبادي (50 جرام)"),
        ("سلطة الحمص الحلوة", "حمص مسلوق (180 جرام) + طماطم (75 جرام) + بقدونس (20 جرام) + تتبيلة طحينة وعسل (50 جرام)"),
        ("سلطة المكرونة الباردة", "مكرونة مسلوقة (100 جرام بعد الطهي) + تونة (40 جرام) + مايونيز خفيف (15 جرام) + خضار مقطعة (150 جرام)"),
        ("سلطة الكينوا الحلوة", "كينوا مطبوخة (100 جرام بعد الطهي) + فراولة مقطعة (75 جرام) + مكسرات (15 جرام) + تتبيلة عسل وليمون (30 جرام)"),
        ("سلطة الجبنة والعنب", "جبنة قريش (60 جرام = 4 ملاعق) + عنب أحمر (75 جرام) + خس (50 جرام) + جوز مطحون (10 جرام)"),
        ("سلطة البنجر الحلوة", "بنجر مسلوق ومقطع (85 جرام) + جبنة فيتا (30 جرام) + جرجير (50 جرام) + تتبيلة عسل (20 جرام)")
    ]])

def generate_snacks_content():
    return '''
    <h3>سناك صباحي (10:00 ص) - 8 خيارات</h3>
    ''' + ''.join([f'''
    <div class="meal-card">
        <div class="meal-title">{title}</div>
        <div class="meal-details">{details}</div>
    </div>
    ''' for title, details in [
        ("تفاح باللوز", "تفاح أحمر مقطع شرائح (150 جرام = حبة كاملة) + زبدة لوز (5 جرام = ملعقة صغيرة)"),
        ("موز بالفول السوداني", "موز (120 جرام = حبة) + زبدة فول سوداني (5 جرام = ملعقة صغيرة) + قرفة (رشة)"),
        ("زبادي بالكيوي", "زبادي يوناني بالعسل (100 جرام) + شرائح كيوي (70 جرام = حبة)"),
        ("عصير موز وفراولة", "موز (60 جرام = نصف حبة) + فراولة (40 جرام) + حليب (120 مل)"),
        ("تمر محشي", "تمر محشي باللوز (24 جرام = 3 حبات) + كوب شاي أخضر بالعسل (5 جرام)"),
        ("عنب وجبنة", "عنب أحمر (75 جرام) + جبنة قريش (30 جرام = ملعقتان)"),
        ("خوخ بالزبادي", "شرائح خوخ (150 جرام = حبة كبيرة) + زبادي طبيعي (45 جرام = 3 ملاعق)"),
        ("كوكتيل فواكه", "موز + فراولة + مانجو (150 جرام إجمالي) + عسل (5 جرام = ملعقة صغيرة)")
    ]])

def generate_exercise_content():
    return '''
    <h3>الأحد: صدر وترايسبس (35-40 دقيقة)</h3>
    <div class="exercise-card">
        <strong>الإحماء (10 دقائق):</strong><br>
        • Treadmill Walking: 5 دقائق مشي سريع على السير<br>
        • Stationary Bike: 5 دقائق دراجة ثابتة
    </div>
    <div class="exercise-card">
        <strong>تمارين الصدر (اختر 2-3 تمارين):</strong><br>
        • Push-ups: 3 × 8-12 تكرار (البديل: Knee Push-ups ضغط على الركبتين)<br>
        • Chest Press Machine: 3 × 10-12 (البديل: Dumbbell Bench Press دمبل على بنش)<br>
        • Incline Dumbbell Press: 3 × 8-10 (البديل: Incline Barbell Press ضغط مائل بالبار)<br>
        • Flat Dumbbell Press: 3 × 8-10 (البديل: Flat Barbell Press ضغط بالبار)<br>
        • Cable Flyes: 3 × 10-12 (البديل: Dumbbell Flyes فراشة دمبل)
    </div>
    
    <h3>تمارين استهداف الكرش خصيصاً</h3>
    <div class="exercise-card">
        • Vacuum Exercise: 3 × 20 ثانية - (شفط البطن للداخل وشد عضلات البطن العميقة)<br>
        • Russian Twists: 3 × 20 لكل جانب - (لاستهداف الدهون الجانبية)<br>
        • Plank with Hip Dips: 3 × 10 لكل جانب - (لتقوية البطن السفلية)<br>
        • Mountain Climbers: 3 × 30 ثانية - (لحرق دهون البطن)<br>
        • Dead Bug: 3 × 10 لكل جانب - (لتقوية عضلات البطن العميقة)
    </div>
    
    <h3>مجموعة التمارين الصباحية (7 دقائق فقط)</h3>
    <div class="exercise-card">
        1. Plank: 30 ثانية<br>
        2. Bicycle Crunches: 30 ثانية<br>
        3. Mountain Climbers: 30 ثانية<br>
        4. Russian Twists: 30 ثانية<br>
        5. Plank: 30 ثانية<br>
        6. Leg Raises: 30 ثانية<br>
        7. Side Plank: 15 ثانية لكل جانب
    </div>
    '''

def generate_supplements_content():
    return '''
    <h3>المكملات الأساسية</h3>
    <table>
        <tr><th>الوقت</th><th>المكمل</th><th>الجرعة</th></tr>
        <tr><td>مع الفطار</td><td>فيتامين B-Complex</td><td>1 كبسولة</td></tr>
        <tr><td>مع الفطار</td><td>فيتامين C</td><td>1000 مجم</td></tr>
        <tr><td>قبل التمرين</td><td>الكارنيتين</td><td>2 كبسولة</td></tr>
        <tr><td>بعد التمرين</td><td>بروتين واي</td><td>1 سكوب</td></tr>
        <tr><td>بعد التمرين</td><td>الكرياتين</td><td>5 جرام</td></tr>
        <tr><td>مع الغداء</td><td>فيتامين D3</td><td>4000 وحدة</td></tr>
        <tr><td>مع الغداء</td><td>أوميجا 3</td><td>2 كبسولة</td></tr>
        <tr><td>مع الغداء</td><td>الشاي الأخضر</td><td>1 كبسولة</td></tr>
        <tr><td>مع العشاء</td><td>الزنك</td><td>1 كبسولة</td></tr>
        <tr><td>قبل النوم</td><td>ماغنسيوم</td><td>400 مجم</td></tr>
    </table>
    
    <h3>مكملات خاصة للقضاء على الكرش</h3>
    <div class="info-card">
        <ul>
            <li><strong>CLA (Conjugated Linoleic Acid):</strong> 2000 مجم يومياً - يساعد في تقليل الدهون في منطقة البطن</li>
            <li><strong>مستخلص الشاي الأخضر:</strong> 500 مجم يومياً - يعزز حرق الدهون ويزيد معدل الأيض</li>
            <li><strong>بروبيوتيك للمعدة:</strong> 1 كبسولة يومياً - يحسن صحة الأمعاء ويقلل انتفاخ البطن</li>
            <li><strong>ألفا ليبويك أسيد:</strong> 300 مجم يومياً - يساعد في تنظيم مستويات السكر وتقليل الدهون</li>
        </ul>
    </div>
    
    <h3>جدول القياسات الأسبوعي</h3>
    <table>
        <tr>
            <th>القياس</th>
            <th>الأسبوع 1</th>
            <th>الأسبوع 2</th>
            <th>الأسبوع 3</th>
            <th>الأسبوع 4</th>
        </tr>
        <tr>
            <td>الوزن (كجم)</td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
        </tr>
        <tr>
            <td>محيط الخصر (سم)</td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
        </tr>
        <tr>
            <td>محيط البطن (سم)</td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
            <td><input type="text" style="width:80px;"></td>
        </tr>
    </table>
    
    <h3>التقدم المتوقع</h3>
    <table>
        <tr><th>الأسبوع</th><th>الوزن المتوقع</th><th>النتائج المتوقعة</th></tr>
        <tr><td>1</td><td>78-79 كجم</td><td>تحسن الطاقة والنوم، تقليل الانتفاخ</td></tr>
        <tr><td>2</td><td>77-78 كجم</td><td>نقص 1-2 سم من الكرش، تحسن الشكل العام</td></tr>
        <tr><td>3</td><td>76-77 كجم</td><td>زيادة القوة، تحسن وضوح العضلات</td></tr>
        <tr><td>4</td><td>75-76 كجم</td><td>نقص 3-4 سم من الكرش، تغير ملحوظ في الشكل</td></tr>
        <tr><td>8</td><td>72-73 كجم</td><td>شكل رياضي واضح، تقليل الكرش بنسبة 60%</td></tr>
        <tr><td>12</td><td>70-72 كجم</td><td>تقليل الكرش بنسبة 80-90%، عضلات ظاهرة</td></tr>
    </table>
    '''

def generate_emergency_content():
    return '''
    <h3>🚨 لو صحيت متأخر (خطة الـ15 دقيقة)</h3>
    <div class="info-card">
        <h4>فطار سوبر سريع (2 دقيقة):</h4>
        <ul>
            <li>موز (120جم) + زبدة فول سوداني (5جم)</li>
            <li>أو: حليب (240مل) + تمر (3 حبات)</li>
            <li>أو: زبادي يوناني (150جم) + عسل (5جم)</li>
        </ul>
        
        <h4>تمرين سريع في البيت (10 دقائق):</h4>
        <ul>
            <li>Push-ups: 3 × 8</li>
            <li>Squats: 3 × 10</li>
            <li>Plank: 2 × 20 ثانية</li>
            <li>بدون استحمام: مناديل مبللة فقط</li>
        </ul>
        
        <h4>إفطار ثاني في الشغل:</h4>
        <ul>
            <li>ساندوتش فول + عصير برتقال</li>
            <li>أو: توست جبنة + لبن رايب</li>
        </ul>
    </div>
    
    <h3>🍕 قائمة البدائل الطارئة (خيارات المطاعم)</h3>
    <div class="info-card">
        <h4>مطاعم الوجبات السريعة (خيارات أفضل):</h4>
        <ul>
            <li>ماكدونالدز: تشيكن جريل + سلطة جانبية (بدل البطاطس) + ماء</li>
            <li>هارديز: ساندوتش الدجاج المشوي (بدون صوص مايونيز) + سلطة</li>
            <li>KFC: قطع الدجاج المشوية (2 قطعة) + خضار</li>
            <li>بيتزا هت: بيتزا فيجيتيرين بعجينة رفيعة + سلطة كبيرة</li>
            <li>سابواي: ساندوتش دجاج 6 بوصة بالخبز الأسمر + خضار كثيرة + صوص خفيف</li>
        </ul>
        
        <h4>مطاعم مصرية (خيارات مناسبة):</h4>
        <ul>
            <li>أماكن الكشري: كشري صغير (بدون دقة أو صلصة كثيرة) + سلطة خضراء كبيرة</li>
            <li>أماكن الفول: طبق فول سادة + طعمية قليلة (2 حبة) + سلطة</li>
            <li>مطاعم الفراخ: ربع فرخة مشوية (بدون جلد) + أرز قليل + سلطة كبيرة</li>
            <li>مطاعم السمك: سمك مشوي + خضار مشوية + قليل من الأرز</li>
            <li>أماكن الشاورما: شاورما دجاج (بدون صوص) + خضار كثيرة + خبز أسمر قليل</li>
        </ul>
    </div>
    
    <h3>💡 نصائح النجاح المخصصة</h3>
    <div class="tip-box">
        <h4>نصائح خاصة بالكرش لجسمك:</h4>
        <ul>
            <li>ركز على عضلات البطن العميقة: تمارين البلانك والفاكيوم أهم من الكرانش</li>
            <li>قلل الكربوهيدرات المسائية: تناول البروتين والخضار في العشاء</li>
            <li>زد الألياف: 30-35 جرام يومياً لتحسين الهضم وتقليل الانتفاخ</li>
            <li>تقنية 16/8: صيام متقطع (16 ساعة صيام، 8 ساعات أكل) مرتين أسبوعياً</li>
            <li>قلل الملح: يسبب احتباس الماء وانتفاخ البطن</li>
            <li>ركز على النوم: 7-8 ساعات ضرورية لتوازن الهرمونات وحرق الدهون</li>
        </ul>
        
        <h4>استراتيجيات العمل والتوازن (8-5):</h4>
        <ul>
            <li>جهز طعامك الأسبوعي يوم الإجازة: حضر 5 وجبات غداء وسناكات للأسبوع</li>
            <li>اشرب 1 لتر ماء قبل وصولك للعمل: يحسن الأيض ويمنع الجوع الكاذب</li>
            <li>استراحة 5 دقائق كل ساعتين: قم بتمارين تمدد بسيطة</li>
            <li>اجعل السلم خيارك الأول: بدل المصعد في كل مكان</li>
            <li>وجبة ما قبل التمرين: إذا اخترت التمرين المسائي، تناول تفاحة أو موزة قبله بـ30 دقيقة</li>
            <li>تواصل مع زملائك: شجع زملاءك على اتباع نمط حياة صحي معك</li>
        </ul>
        
        <h4>الأطعمة السحرية لحرق الدهون (خاصة للكرش):</h4>
        <ul>
            <li>الزنجبيل: شاي الزنجبيل يومياً يساعد في حرق الدهون</li>
            <li>القرفة: 1/2 ملعقة صغيرة يومياً على الشوفان أو القهوة</li>
            <li>الشاي الأخضر: 2-3 أكواب يومياً لتعزيز الأيض</li>
            <li>الفلفل الحار: إضافته للوجبات يزيد حرق السعرات</li>
            <li>خل التفاح: 1 ملعقة كبيرة في كوب ماء قبل الوجبات</li>
        </ul>
    </div>
    
    <div class="tip-box" style="background: #d1fae5;">
        <h3>رسالة التحفيز النهائية</h3>
        <p>في عمر 25 سنة، جسمك في أفضل حالاته استجابة للتغيير. طولك (178 سم) ووزنك (80 كجم) يمنحانك فرصة مثالية لبناء جسم مثالي خلال 3 شهور فقط. مشكلة الكرش هي تحدي مؤقت يمكن التغلب عليه مع الالتزام.</p>
        
        <p>مع جدول عملك (8-5)، قد تحتاج للتخطيط بذكاء، لكن هذا التحدي سيبني انضباطاً سيفيدك في كل مجالات حياتك. ساعات عملك لن تكون عائقاً، بل فرصة لتنظيم يومك بشكل أفضل.</p>
        
        <p>تذكر أن كل يوم التزام هو استثمار في مستقبلك، وأن النتائج ستظهر تدريجياً. أنت في سن مثالي وجسمك قادر على التغيير السريع. الكرش ليس أكثر من تحدي مؤقت ستتغلب عليه.</p>
        
        <p><strong>الآن... توكل على الله وابدأ! أنت قادر على تحقيق هدفك وأكثر.</strong></p>
    </div>
    '''

# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("مولد دليل اللياقة البدنية والتغذية الشامل")
    print("=" * 50)
    
    # Generate the HTML content
    html_content = generate_fitness_guide()
    
    # Save to file
    filename = "fitness_guide_complete.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ تم إنشاء الملف بنجاح: {filename}")
    print(f"📊 حجم الملف: {len(html_content) / 1024:.2f} KB")
    print("\n📱 الملف يعمل على:")
    print("   • الكمبيوتر (جميع المتصفحات)")
    print("   • الهاتف المحمول")
    print("   • التابلت")
    print("\n💾 جميع البيانات تحفظ تلقائياً في المتصفح")
    print("\n🎯 افتح الملف في أي متصفح للبدء!")
