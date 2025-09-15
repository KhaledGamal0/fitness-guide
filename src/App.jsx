import React from 'react'
import Checklist from './components/Checklist'
import Diet from './components/Diet'
import Workout from './components/Workout'

function App() {
  return (
    <div className="container py-4">
      <h1 className="mb-4">🏋️ Fitness Guide</h1>
      <Checklist />
      <Diet />
      <Workout />
    </div>
  )
}

export default App
