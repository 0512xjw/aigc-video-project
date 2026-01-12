const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors');
const app = express();
// 端口改为5002，和你启动的网关端口一致
const PORT = process.env.PORT || 5002;

// 1. 修复跨域：配置允许所有来源，解决前端跨域请求
app.use(cors({
  origin: '*',
  credentials: true,
  methods: ['GET', 'POST', 'OPTIONS']
}));

// 2. 修复JSON解析：前端POST传参能被网关识别
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 3. 修复后端地址：硬编码指向本地后端5001端口（确保代理目标正确）
const BACKEND_URL = process.env.BACKEND_URL || 'http://127.0.0.1:5001';

// 4. 修复代理规则：确保/api开头的请求转发到后端
app.use('/api', createProxyMiddleware({
  target: BACKEND_URL,
  changeOrigin: true, // 关键：模拟请求来自后端地址，避免后端跨域
  pathRewrite: { '^/api': '/api' } // 路径重写保持/api，和后端接口一致
}));

// 5. 新增根路径路由：解决访问5002根路径404
app.get('/', (req, res) => {
  res.json({
    code: 0,
    msg: '网关服务运行正常',
    proxy_target: BACKEND_URL,
    tips: '接口请访问 /api 开头的路径'
  });
});

// 启动网关服务
app.listen(PORT, () => {
  console.log(`网关服务运行在端口 ${PORT}，代理指向 ${BACKEND_URL}`);
});

// 适配Vercel Serverless环境（部署时需要）
module.exports = app;