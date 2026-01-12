import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173, // 前端端口
    proxy: {
      '/api': {
        target: 'https://aigc-video-project-gateway.vercel.app', // 网关地址
        changeOrigin: true
      }
    }
  }
})