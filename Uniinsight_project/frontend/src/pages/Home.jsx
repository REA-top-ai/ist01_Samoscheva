import { useState } from 'react'
import { analyze, addFavorite } from '../api.js'
import UniversityCard from '../components/UniversityCard.jsx'

export default function Home({ user }) {
  const [query, setQuery] = useState('')
  const [aiResults, setAiResults] = useState(null)
  const [country, setCountry] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleAnalyze = async () => {
    if (!query.trim()) return
    setLoading(true)
    setError('')
    setAiResults(null)

    try {
      const res = await analyze(query.trim())
      setCountry(res.data.country)
      setAiResults(res.data.result)
    } catch (e) {
      const msg = e.response?.data?.detail || 'Ошибка AI анализа. Проверьте GROQ_API_KEY в .env'
      setError(msg)
    } finally {
      setLoading(false)
    }
  }

  const handleAddFavorite = async (uni) => {
    if (!user) {
      alert('Войдите через Google чтобы добавить в избранное')
      return
    }
    try {
      await addFavorite({
        university_name: uni.name,
        website: uni.website || '',
        country: uni.country || country,
      })
      alert(`✅ "${uni.name}" добавлен в избранное`)
    } catch (e) {
      if (e.response?.status === 400) {
        alert('Уже в избранном')
      } else {
        alert('Ошибка при добавлении в избранное')
      }
    }
  }

  return (
    <div className="home">
      <div className="hero">
        <h1>🎓 UniInsight</h1>
        <p>Найди университет мечты с помощью AI</p>
      </div>

      <div className="search-box">
        <input
          className="search-input"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleAnalyze()}
          placeholder='Например: "Хочу учиться в Германии, бюджет 500 евро в месяц"'
          disabled={loading}
        />
        <button className="btn-ai-full" onClick={handleAnalyze} disabled={loading}>
          {loading ? '⏳ AI думает...' : '🤖 AI Анализ'}
        </button>
      </div>

      {error && <div className="error">⚠️ {error}</div>}

      {aiResults && (
        <div className="results">
          <h2>🤖 AI рекомендации — {country}</h2>
          {Array.isArray(aiResults) ? (
            <div className="cards-grid">
              {aiResults.map((uni, i) => (
                <UniversityCard
                  key={i}
                  uni={uni}
                  onFavorite={() => handleAddFavorite(uni)}
                />
              ))}
            </div>
          ) : (
            <div className="error">
              {aiResults.error || 'AI вернул неожиданный формат'}
              {aiResults.raw && <pre className="raw-result">{aiResults.raw}</pre>}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
