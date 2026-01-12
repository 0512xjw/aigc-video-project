import axios from 'axios'

const request = axios.create({
  baseURL: 'http://127.0.0.1:5002', // 网关地址
  timeout: 30000,
  headers: { 'Content-Type': 'application/json;charset=utf-8' }
})

// 请求拦截器：添加/api前缀
request.interceptors.request.use(
  (config) => {
    if (config.url && !config.url.startsWith('/api')) {
      config.url = `/api${config.url}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// 响应拦截器：统一处理返回值
request.interceptors.response.use(
  (response) => {
    const res = response.data
    if (res.code === 0) return res.data
    else {
      alert(`请求失败：${res.msg}`)
      return Promise.reject(res)
    }
  },
  (error) => {
    alert(`网络错误：${error.message}`)
    return Promise.reject(error)
  }
)

export default request