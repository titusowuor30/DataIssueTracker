// src/store/auth/auth.js
import axios from '../../axiosConfig'

const state = {
  isAuthenticated: false,
  user: null,
  isAdmin: false,
}

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated, isAdmin) {
    state.isAuthenticated = isAuthenticated,
    state.isAdmin = isAdmin
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

      if (user.role === "Admin") {
        commit('SET_AUTHENTICATED', true, true)
      } else {
        commit('SET_AUTHENTICATED', true, false)
      }
      localStorage.setItem('token', token)
      localStorage.setItem('user', user)
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
    localStorage.removeItem('user')
    commit('SET_AUTHENTICATED', false, false)
    commit('SET_USER', null)
  },

  checkAuthentication({ commit }) {
    const token = localStorage.getItem('token')
    const user = this.localStorage.getItem('user')
    if (token) {
      if (user.role === "Admin") {
        commit('SET_AUTHENTICATED', true, true)
      } else {
        commit('SET_AUTHENTICATED', true, false)
      }

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
