import { useState, useEffect } from 'react'
import { getFavorites, deleteFavorite } from '../api.js'

export default function Favorites() {
  const [favorites, setFavorites] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getFavorites()
      .then((res) => setFavorites(res.data))
      .catch(() => setFavorites([]))
      .finally(() => setLoading(false))
  }, [])

  const handleDelete = async (id, name) => {
    if (!confirm(`Удалить "${name}" из избранного?`)) return
    try {
      await deleteFavorite(id)
      setFavorites((prev) => prev.filter((f) => f.id !== id))
    } catch {
      alert('Ошибка при удалении')
    }
  }

  if (loading) return <div className="loading">Загрузка избранного...</div>

  return (
    <div className="favorites-page">
      <h1>⭐ Избранные университеты</h1>

      {favorites.length === 0 ? (
        <div className="empty">
          <p>Нет сохранённых университетов</p>
          <a href="/">← Вернуться к поиску</a>
        </div>
      ) : (
        <div className="fav-list">
          {favorites.map((fav) => (
            <div key={fav.id} className="fav-card">
              <div className="fav-info">
                <h3>{fav.university_name}</h3>
                {fav.country && (
                  <span className="fav-country">🌍 {fav.country}</span>
                )}
                {fav.website && (
                  <a
                    href={fav.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="fav-link"
                  >
                    🔗 Перейти на сайт
                  </a>
                )}
              </div>
              <button
                className="btn-delete"
                onClick={() => handleDelete(fav.id, fav.university_name)}
              >
                🗑️ Удалить
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
