import { BrowserRouter, Routes, Route, Link, Navigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import Home from './pages/Home.jsx'
import Favorites from './pages/Favorites.jsx'
import { getMe, logout } from './api.js'

export default function App() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getMe()
      .then((res) => setUser(res.data.user))
      .catch(() => setUser(null))
      .finally(() => setLoading(false))
  }, [])

  const handleLogout = async () => {
    await logout()
    setUser(null)
  }

  if (loading) return <div className="loading">Загрузка...</div>

  return (
    <BrowserRouter>
      <nav className="navbar">
        <Link to="/" className="nav-brand">🎓 UniInsight</Link>

        <div className="nav-links">
          <Link to="/">Поиск</Link>
          {user && <Link to="/favorites">⭐ Избранное</Link>}

          {user ? (
            <div className="nav-user">
              {user.picture && (
                <img src={user.picture} alt={user.name} className="avatar" />
              )}
              <span className="nav-name">{user.name}</span>
              <button onClick={handleLogout} className="btn-logout">
                Выйти
              </button>
            </div>
          ) : (
            <a href="http://localhost:8000/auth/login" className="btn-google">
              🔑 Войти через Google
            </a>
          )}
        </div>
      </nav>

      <main className="main">
        <Routes>
          <Route path="/" element={<Home user={user} />} />
          <Route
            path="/favorites"
            element={user ? <Favorites /> : <Navigate to="/" />}
          />
        </Routes>
      </main>
    </BrowserRouter>
  )
}
