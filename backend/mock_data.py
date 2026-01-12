from faker import Faker
import random
import re

fake = Faker(locale='zh_CN')

# 生成AIGC视频项目Mock数据
def generate_video_list(count=10):
    videos = []
    for _ in range(count):
        video = {
            "id": fake.uuid4(),
            "title": fake.sentence(nb_words=5),
            "author": fake.name(),
            "views": random.randint(100, 100000),
            "create_time": fake.date_time().strftime("%Y-%m-%d %H:%M:%S"),
            "cover_url": fake.image_url(width=640, height=360),
            "video_url": fake.url()
        }
        videos.append(video)
    return videos

def generate_video_detail(video_id):
    # 新增：UUID格式校验
    uuid_pattern = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
    if not video_id:
        raise ValueError("video_id 不能为空")
    if not uuid_pattern.match(video_id):
        raise ValueError("video_id 格式错误，必须为UUID")
    return {
        "id": video_id,
        "title": fake.sentence(nb_words=6),
        "author": fake.name(),
        "author_avatar": fake.image_url(width=100, height=100),
        "views": random.randint(100, 100000),
        "likes": random.randint(0, 5001),
        "comments": random.randint(0, 1000),
        "create_time": fake.date_time().strftime("%Y-%m-%d %H:%M:%S"),
        "cover_url": fake.image_url(width=640, height=360),
        "video_url": fake.url(),
        "description": fake.paragraph(nb_sentences=3)
    }