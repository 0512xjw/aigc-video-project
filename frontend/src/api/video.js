import request from '../utils/request'

// 获取视频列表
export const getVideoList = (params) => {
  return request.get('/videos', { params })
}

// 获取视频详情
export const getVideoDetail = (videoId) => {
  return request.get(`/videos/${videoId}`)
}