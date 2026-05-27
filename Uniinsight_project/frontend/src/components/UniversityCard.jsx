const CHANCE_COLORS = {
  High: '#22c55e',
  Medium: '#f59e0b',
  Low: '#ef4444',
}

export default function UniversityCard({ uni, onFavorite, showAnalysis }) {
  return (
    <div className="uni-card">
      <div className="uni-header">
        <h3 className="uni-name">{uni.name}</h3>
        <button className="btn-star" onClick={onFavorite} title="Добавить в избранное">
          ⭐
        </button>
      </div>

      {uni.website && (
        <a
          href={uni.website}
          target="_blank"
          rel="noopener noreferrer"
          className="uni-link"
        >
          🔗 {uni.website}
        </a>
      )}

      {showAnalysis && (
        <div className="uni-analysis">
          {uni.tuition && (
            <div className="analysis-row">
              <span className="label">💰 Стоимость:</span>
              <span>{uni.tuition}</span>
            </div>
          )}
          {uni.requirements && (
            <div className="analysis-row">
              <span className="label">📋 Требования:</span>
              <span>{uni.requirements}</span>
            </div>
          )}
          {uni.chance && (
            <div className="analysis-row">
              <span className="label">📊 Шанс:</span>
              <span
                className="chance-badge"
                style={{ backgroundColor: CHANCE_COLORS[uni.chance] || '#6b7280' }}
              >
                {uni.chance}
              </span>
            </div>
          )}
          {uni.comment && (
            <p className="uni-comment">💬 {uni.comment}</p>
          )}
        </div>
      )}
    </div>
  )
}
