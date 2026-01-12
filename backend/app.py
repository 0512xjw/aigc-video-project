from flask import Flask, jsonify, request
from flask_cors import CORS
from mock_data import generate_video_list, generate_video_detail
import uuid

app = Flask(__name__)
CORS(app)  # 解决跨域问题

# 确保根路径有测试接口
@app.route('/')
def index():
    return {"status": "success", "message": "后端服务正常运行"}

# 接口1：获取视频列表
@app.route('/api/videos', methods=['GET'])
def get_video_list():
    count = request.args.get('count', 10, type=int)
    count = max(1, min(count, 100))  # 新增范围限制
    data = generate_video_list(count)
    return jsonify({
        "code": 0,
        "message": "success",
        "data": data
    })

# 接口2：获取视频详情
@app.route('/api/videos/<video_id>', methods=['GET'])
def get_video_detail(video_id):
    if not video_id:  # 新增错误分支
        return jsonify({
            "code": 1,
            "message": "video_id 不能为空",
            "data": None
        }), 400
    data = generate_video_detail(video_id)
    return jsonify({
        "code": 0,
        "message": "success",
        "data": data
    })

# 接口3：创建视频（模拟）
@app.route('/api/videos', methods=['POST'])
def create_video():
    req_data = request.get_json()or{}
    video_id = str(uuid.uuid4())
    return jsonify({
        "code": 0,
        "message": "视频创建成功",
        "data": {
            "id": video_id,
            "title": req_data.get("title", ""),
            "status": "pending"
        }
    })

# 修复调试模式（生产环境强制关闭）
if __name__ == '__main__':
    import os
    is_local = os.getenv("RUN_ENV", "local") == "local"
    debug_mode = False
    if is_local:
        debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host='127.0.0.1', port=int(os.environ.get("PORT", 5001)))