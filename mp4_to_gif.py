import subprocess
import os

class GifConverter:
    def __init__(self, mp4_address, gif_address):
        # 保存输入和输出文件夹路径
        self.mp4_add = mp4_address
        self.gif_add = gif_address

        # 获取所有 MP4 文件
        all_filenames = [f for f in os.listdir(self.mp4_add) if f.endswith('.mp4')]

        # 转换每个 MP4 文件到 GIF
        for name in all_filenames:
            # 构建文件路径
            mp4_filename = os.path.join(self.mp4_add, name)
            gif_filename = os.path.join(self.gif_add, f"{os.path.splitext(name)[0]}.gif")

            # 调用 FFmpeg 转换 MP4 到 GIF
            subprocess.run([
                "ffmpeg", "-i", mp4_filename,
                "-vf", "fps=30,scale=800:-1:flags=lanczos",  # 调整帧率和分辨率
                "-c:v", "gif", gif_filename
            ])

            print(f"GIF 文件已保存为 {gif_filename}")

