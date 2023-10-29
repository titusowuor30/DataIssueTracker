import axios from "axios"

const tokenString = localStorage.getItem('token')
const baseURL = process.env.VUE_APP_BASE_URL || 'http://146.190.61.0:8000/api/'

console.log(process.env.VUE_APP_BASE_URL)

const axiosInstance = axios.create({
  baseURL: baseURL, // Replace with your Django backend URL
  timeout: 360_000, // 6 mins timeout
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`,
  },
})

export default axiosInstance
