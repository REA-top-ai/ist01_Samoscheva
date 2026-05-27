import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
})

export const getUniversities = (country) =>
  api.get(`/universities?country=${encodeURIComponent(country)}`)

export const analyze = (query) =>
  api.post('/analyze', { query })

export const getMe = () =>
  api.get('/auth/me')

export const logout = () =>
  api.post('/auth/logout')

export const getFavorites = () =>
  api.get('/favorites')

export const addFavorite = (data) =>
  api.post('/favorites', data)

export const deleteFavorite = (id) =>
  api.delete(`/favorites/${id}`)

export const getTrends = () =>
  api.get('/trends')

export default api
