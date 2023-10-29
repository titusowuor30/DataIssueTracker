import axios from "axios"

const tokenString = localStorage.getItem('token')
const baseURL = process.env.VUE_APP_BASE_URL || 'http://localhost:8001/api/'

const axiosInstance = axios.create({
  baseURL: baseURL, // Replace with your Django backend URL
  timeout: 360_000, // 6 mins timeout
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`,
  },
})

export default axiosInstance
