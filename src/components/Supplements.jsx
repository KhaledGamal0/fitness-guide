import React, { useState, useEffect } from 'react'
import { load, save } from '../utils'

const Row = ({label}) => (
  <tr><td>{label}</td><td><input className="form-check-input" type="checkbox" onChange={(e)=>{}}/></td></tr>
)

export default function Supplements(){
  const [measure, setMeasure] = useState(load('measure', {weight:'', waist:'', abdomen:'', chest:'', arm:'', thigh:''}))
  useEffect(()=>save('measure', measure),[measure])

  return (
    <div className="col-12 col-lg-10 mx-auto">
      <div className="card p-3 mb-3">
        <h5>💊 المكملات الأساسية (تذكير سريع)</h5>
        <div className="table-responsive">
          <table className="table">
            <thead><tr><th>المكمل</th><th>تَمَّ ✓</th></tr></thead>
            <tbody>
              <Row label="فيتامين B-Complex (صباحًا)"/>
              <Row label="فيتامين C (صباحًا)"/>
              <Row label="الكارنيتين (قبل التمرين)"/>
              <Row label="واي بروتين (بعد التمرين)"/>
              <Row label="كرياتين (أي وقت)"/>
              <Row label="فيتامين D3 (مع الغداء)"/>
              <Row label="أوميجا 3 (مع الغداء)"/>
              <Row label="شاي أخضر (مع الغداء)"/>
              <Row label="زنك (مع العشاء)"/>
              <Row label="ماغنسيوم (قبل النوم)"/>
            </tbody>
          </table>
        </div>
        <p className="muted">اختياري: CLA / بروبيوتيك / ALA حسب الميزانية.</p>
      </div>

      <div className="card p-3">
        <h5>📏 قياسات أسبوعية (صباح كل أحد قبل الفطار)</h5>
        <div className="row g-2">
          {['weight','waist','abdomen','chest','arm','thigh'].map((k,i)=>(
            <div className="col-6 col-md-4" key={i}>
              <label className="form-label">
                {{
                  weight:'الوزن (كجم)',
                  waist:'محيط الخصر (سم)',
                  abdomen:'محيط البطن (سم)',
                  chest:'محيط الصدر (سم)',
                  arm:'محيط الذراع (سم)',
                  thigh:'محيط الفخذ (سم)',
                }[k]}
              </label>
              <input className="form-control" type="number" inputMode="decimal"
                value={measure[k]} onChange={(e)=>setMeasure(s=>({...s, [k]: e.target.value}))} />
            </div>
          ))}
          <div className="col-12">
            <small className="muted">الوزن: قبل الفطار وبعد الحمام وبنفس الميزان. الخصر: أضيق نقطة. البطن: أوسع نقطة فوق السُرّة بـ2سم.</small>
          </div>
        </div>
      </div>
    </div>
  )
}
