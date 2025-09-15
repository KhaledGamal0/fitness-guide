import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

// Register SW
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/public/sw.js').catch(() => {})
  })
}

createRoot(document.getElementById('root')).render(<App />)
