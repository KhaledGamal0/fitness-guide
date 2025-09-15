import React from 'react'

const Block = ({title, children}) => (
  <div className="card p-3 mb-3">
    <h5 className="mb-2">{title}</h5>
    <div>{children}</div>
  </div>
)

export default function Training(){
  return (
    <div className="col-12 col-lg-10 mx-auto">
      <Block title="📅 الجدول الأسبوعي">
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead><tr><th>اليوم</th><th>الوقت المثالي</th><th>البديل</th><th>المدة</th><th>التمرين</th></tr></thead>
            <tbody>
              <tr><td>الأحد</td><td>6:00-6:40 ص</td><td>7:00-7:40 م</td><td>35-40 د</td><td>صدر وترايسبس</td></tr>
              <tr><td>الاثنين</td><td>6:00-6:40 ص</td><td>7:00-7:40 م</td><td>35-40 د</td><td>كارديو ومرونة</td></tr>
              <tr><td>الثلاثاء</td><td>6:00-6:40 ص</td><td>7:00-7:40 م</td><td>35-40 د</td><td>ظهر وبايسبس</td></tr>
              <tr><td>الأربعاء</td><td>6:00-6:40 ص</td><td>7:00-7:40 م</td><td>35-40 د</td><td>أرجل وأكتاف</td></tr>
              <tr><td>الخميس</td><td>6:00-6:25 ص</td><td>7:00-7:25 م</td><td>20-25 د</td><td>تمرين خفيف</td></tr>
              <tr><td>الجمعة</td><td colSpan="4">راحة وسهر</td></tr>
              <tr><td>السبت</td><td>11:00-12:00</td><td>4:00-5:00 م</td><td>50-60 د</td><td>تمرين تعويضي</td></tr>
            </tbody>
          </table>
        </div>
        <p className="muted">لو اخترت التمرين المسائي، خُد سناك خفيف قبلها بـ30 دقيقة.</p>
      </Block>

      <Block title="💪 تفاصيل أساسية لكل يوم">
        <ul>
          <li>الأحد: صدر (2-3 تمارين) + ترايسبس (2 تمارين) + بطن (5 دقائق)</li>
          <li>الاثنين: كارديو 20-25د + بطن 8د + إطالة 7د</li>
          <li>الثلاثاء: ظهر (3) + بايسبس (2)</li>
          <li>الأربعاء: أرجل (3) + أكتاف (3)</li>
          <li>الخميس: يوغا / مشي سريع / تمارين وزن الجسم</li>
          <li>السبت: قوة (سكوات/دِيدلفت/ضغط/سحب) + كارديو مكثف</li>
        </ul>
      </Block>

      <Block title="🏋️ تمارين الكرش المتخصصة + مجموعة صباحية 7 دقائق">
        <ul>
          <li>Vacuum 3×20ث، Russian Twists 3×20/جانب، Plank مع Hip Dips 3×10/جانب</li>
          <li>Mountain Climbers 3×30ث، Dead Bug 3×10/جانب</li>
          <li>الصباح: Plank 30ث، Bicycle 30ث، Mountain 30ث، Russian 30ث، Plank 30ث، Leg Raises 30ث، Side Plank 15ث/جانب</li>
        </ul>
      </Block>

      <Block title="🔄 بدائل للأيام المزدحمة (5:30-6:15 ص / المكتب / بعد العمل)">
        <ul>
          <li>دائرة وزن جسم: Push-ups / Squats / Mountain / Lunges / Plank / Jumping Jacks</li>
          <li>تمارين مكتب: Desk Push-ups, Chair Squats, Core Twists, Calf Raises, Desk Dips</li>
          <li>Quick HIIT بعد العمل: 4 دورات (40ث عمل / 20ث راحة)</li>
        </ul>
      </Block>
    </div>
  )
}
