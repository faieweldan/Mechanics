import { useEffect, useState } from 'react'
import { testAPI } from './services/api'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await testAPI()
        setMessage(data.message)
      } catch (error) {
        setMessage('Error connecting to API')
      }
    }
    fetchData()
  }, [])

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          Pomen Improved
        </h1>
        <p className="text-gray-600">API Status: {message}</p>
      </div>
    </div>
  )
}

export default App