import axios from "axios"
import CryptoJS from "crypto-js"

let tokenString = ''

try {
  if (localStorage.getItem('token') !== '') {
    tokenString = CryptoJS.AES.decrypt(
      JSON.parse(localStorage.getItem('token')),
      'mnopqr',
    )
      .toString(CryptoJS.enc.Utf8)
      .trim()
  }
} catch (e) {
  tokenString = '1987b6dcbe4d90e2ae27387a2e66b951c5607755'
}

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/', // Replace with your Django backend URL
  timeout: 360000, // 6 mins timeout
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`,
  },
})

export default axiosInstance
