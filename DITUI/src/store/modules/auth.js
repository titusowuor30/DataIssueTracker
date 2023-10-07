// src/store/auth/auth.js
import axios from '../../axiosConfig'

const state = {
  isAuthenticated: false,
  user: null,
}

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated
  },
  SET_USER(state, user) {
    state.user = user
  },
}

const actions = {
  async login({ commit }, payload) {
    try {
      const response = await axios.post('/login/', payload)
      const { token, user } = response.data

      localStorage.setItem('token', token)
      commit('SET_AUTHENTICATED', true)
      commit('SET_USER', user)
    } catch (error) {
      // Modify this part to include the response message in the error
      let errorMessage = 'An error occurred during login.'
      if (error.response && error.response.data && error.response.data.error) {
        errorMessage = error.response.data.error
      }
      throw new Error(errorMessage)
    }
  },

  logout({ commit }) {
    localStorage.removeItem('token')
    commit('SET_AUTHENTICATED', false)
    commit('SET_USER', null)
  },

  checkAuthentication({ commit }) {
    const token = localStorage.getItem('token')
    if (token) {
      commit('SET_AUTHENTICATED', true)

      // Fetch user data or perform other checks here
    }
  },
}

export default {
  namespaced: true, // Make sure the module is namespaced
  state,
  mutations,
  actions,
}
