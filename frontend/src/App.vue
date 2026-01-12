<template>
  <div id="app-container">
    <h1>视频项目测试页面</h1>
    <button @click="fetchVideoList">获取视频列表</button>
    <div v-if="videoList.length > 0" class="video-list">
      <h3>视频列表（{{ videoList.length }}条）</h3>
      <ul>
        <li v-for="video in videoList" :key="video.id">{{ video.id }} - {{ video.title }}</li>
      </ul>
    </div>
    <div v-else-if="isLoaded" class="empty">暂无视频数据</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getVideoList } from './api/video.js'

const videoList = ref([])
const isLoaded = ref(false)

const fetchVideoList = async () => {
  try {
    const res = await getVideoList({ count: 5 })
    videoList.value = res
    isLoaded.value = true
  } catch (err) {
    isLoaded.value = true
  }
}
</script>

<style scoped>
#app-container {
  width: 800px;
  margin: 50px auto;
  font-family: Arial;
}
button {
  padding: 8px 16px;
  background: #409eff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.video-list {
  margin-top: 20px;
  border: 1px solid #eee;
  padding: 20px;
}
.empty {
  margin-top: 20px;
  color: #999;
}
</style>