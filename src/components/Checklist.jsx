import React, { useEffect, useState } from 'react'
import data from '../guide.json'
import { load, save } from '../utils'

export default function Checklist(){
  const [checks, setChecks] = useState(load('checks', {}))
  const [water, setWater] = useState(load('waterLiters', 0))
  const [weekGoals, setWeekGoals] = useState(load('weekGoals', {workouts:0, water:0}))

  useEffect(()=>save('checks', checks),[checks])
  useEffect(()=>save('waterLiters', water),[water])
  useEffect(()=>save('weekGoals', weekGoals),[weekGoals])

  const toggle = (i) => setChecks(prev => ({...prev, [i]: !prev[i]}))

  return (
    <div className="row g-3">
      <div className="col-12 col-lg-6">
        <div className="card p-3 h-100">
          <h5 className="mb-3">☑️ قائمة التدقيق اليومية</h5>
          {data.checklist.map((item, i)=>(
            <div className="form-check d-flex justify-content-between align-items-center py-2 border-bottom border-secondary" key={i}>
              <div>
                <input className="form-check-input me-2" type="checkbox" id={`c${i}`}
                  checked={!!checks[i]} onChange={()=>toggle(i)} />
                <label className="form-check-label" htmlFor={`c${i}`}>{item.label}</label>
              </div>
              <span className="badge text-bg-primary">{item.time}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="col-12 col-lg-6">
        <div className="card p-3">
          <h5>🎯 أهدافي الأسبوعية</h5>
          <div className="row g-2">
            <div className="col-6">
              <label className="form-label">وزن الجسم (كجم)</label>
              <input className="form-control" type="number" inputMode="decimal"
                placeholder="____"
                onChange={(e)=>save('goal_weight', e.target.value)} defaultValue={load('goal_weight','')} />
            </div>
            <div className="col-6">
              <label className="form-label">محيط الخصر (سم)</label>
              <input className="form-control" type="number" inputMode="decimal"
                placeholder="____"
                onChange={(e)=>save('goal_waist', e.target.value)} defaultValue={load('goal_waist','')} />
            </div>
            <div className="col-6">
              <label className="form-label">محيط البطن (سم)</label>
              <input className="form-control" type="number" inputMode="decimal"
                placeholder="____"
                onChange={(e)=>save('goal_abd', e.target.value)} defaultValue={load('goal_abd','')} />
            </div>
            <div className="col-6">
              <label className="form-label">تمارين هذا الأسبوع</label>
              <input className="form-control" type="number" placeholder="0/6"
                onChange={(e)=>setWeekGoals(s=>({...s, workouts: e.target.value}))}
                value={weekGoals.workouts} />
            </div>
            <div className="col-12">
              <label className="form-label">الماء (لتر/الأسبوع)</label>
              <input className="form-range" type="range" min="0" max="28"
                onChange={(e)=>{setWater(e.target.value); setWeekGoals(s=>({...s, water:e.target.value}))}}
                value={water} />
              <div className="muted">{water} لتر</div>
            </div>
          </div>

          <hr/>
          <h6>ملاحظات للدوام 8-5</h6>
          <ul className="mb-0">{data.work_notes.map((n,i)=><li key={i}>{n}</li>)}</ul>
        </div>
      </div>

      <div className="col-12">
        <div className="card p-3">
          <h5>🗓️ الجدول الأسبوعي المختصر</h5>
          <div className="table-responsive">
            <table className="table table-hover align-middle">
              <thead><tr><th>اليوم</th><th>المدة</th><th>التمرين</th></tr></thead>
              <tbody>
                {data.weekly_short.map((r,i)=>(
                  <tr key={i}><td>{r.day}</td><td>{r.dur}</td><td>{r.plan}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  )
}
