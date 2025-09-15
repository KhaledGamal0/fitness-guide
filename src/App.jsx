import React, { useMemo, useState, useEffect } from 'react'
import Checklist from './components/Checklist'
import Diet from './components/Diet'
import Training from './components/Training'
import Supplements from './components/Supplements'
import Emergencies from './components/Emergencies'

const TabBtn = ({ id, active, onClick, children }) => (
  <button className={`nav-link ${active===id?'active':''}`} onClick={()=>onClick(id)}>
    {children}
  </button>
)

export default function App(){
  const [tab, setTab] = useState('summary')

  useEffect(()=>{
    const saved = localStorage.getItem('activeTab')
    if(saved) setTab(saved)
  },[])

  useEffect(()=>{
    localStorage.setItem('activeTab', tab)
  },[tab])

  return (
    <div className="container py-3">
      <nav className="navbar rounded mb-3 px-3">
        <div className="d-flex flex-column">
          <strong>الدليل الشامل للياقة والتغذية - خالد</strong>
          <small className="muted">واجهة تفاعلية • تعمل أوفلاين • تدعم الحفظ المحلي</small>
        </div>
      </nav>

      <ul className="nav nav-tabs mb-3">
        <li className="nav-item"><TabBtn id="summary" active={tab} onClick={setTab}>الملخص الأساسي</TabBtn></li>
        <li className="nav-item"><TabBtn id="diet" active={tab} onClick={setTab}>النظام الغذائي</TabBtn></li>
        <li className="nav-item"><TabBtn id="training" active={tab} onClick={setTab}>البرنامج الرياضي</TabBtn></li>
        <li className="nav-item"><TabBtn id="supp" active={tab} onClick={setTab}>المكملات والقياسات</TabBtn></li>
        <li className="nav-item"><TabBtn id="emerg" active={tab} onClick={setTab}>حلول الطوارئ والنصائح</TabBtn></li>
      </ul>

      {tab==='summary' && <Checklist/>}
      {tab==='diet' && <Diet/>}
      {tab==='training' && <Training/>}
      {tab==='supp' && <Supplements/>}
      {tab==='emerg' && <Emergencies/>}

      <div className="sticky-bottom-cta d-flex gap-2 justify-content-between align-items-center">
        <span className="muted">💾 يتم حفظ تقدمك تلقائياً على جهازك</span>
        <button className="btn btn-outline-light btn-sm" onClick={()=>{
          localStorage.clear()
          location.reload()
        }}>تصفير كل البيانات</button>
      </div>
    </div>
  )
}
