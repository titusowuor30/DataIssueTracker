import axios from "@/axiosConfig"

const state = {
  baseUrl: axios.defaults.baseURL.replace("/api/", ""),
}


const mutations = {}

const actions = {}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
}
