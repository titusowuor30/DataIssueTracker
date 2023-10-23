import axios from "axios"

const tokenString = localStorage.getItem('token')

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8001/api/', // Replace with your Django backend URL
  timeout: 360_000, // 6 mins timeout
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`,
  },
})

export default axiosInstance
