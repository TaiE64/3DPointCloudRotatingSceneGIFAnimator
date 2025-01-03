import open3d as o3d
import numpy as np
import cv2
import os

class mp4():
    def __init__(self,address):
        folder_path = address

        # 获取文件夹下所有文件的名字
        file_names = [f for f in os.listdir(folder_path) if f.endswith('.ply')]
        output_folder_path = "mp4"
        for name in file_names:
            # 读取点云文件
            pcd = o3d.io.read_point_cloud(f"ply_test/{name}")

            # 设置输出视频参数
            video_filename = os.path.join(output_folder_path, f"{os.path.splitext(name)[0]}.mp4")
            # video_filename = f"{name}.mp4"
            frame_width = 800  # 窗口宽度
            frame_height = 600  # 窗口高度
            fps = 60  # 每秒帧数
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码格式
            video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

            # 初始化可视化
            vis = o3d.visualization.Visualizer()
            vis.create_window(window_name="Rotating PLY Viewer", width=frame_width, height=frame_height)
            vis.add_geometry(pcd)

            # 获取视图控制器
            view_ctrl = vis.get_view_control()
            ctr_params = view_ctrl.convert_to_pinhole_camera_parameters()  # 初始参数保存

            # 自动旋转并录制帧
            angle_step = 3  # 每次旋转角度（度数）
            num_frames = int(2090/ angle_step)  # 总帧数（360度旋转一圈）

            for i in range(num_frames):
                # 旋转视图
                view_ctrl.rotate(int(angle_step), 0)  # 水平旋转角度（度）
                
                # 截屏
                frame = np.asarray(vis.capture_screen_float_buffer(True))
                frame = (frame * 255).astype(np.uint8)  # 转换为 8-bit
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # 转换为 BGR 格式
                
                # 写入视频
                video_writer.write(frame_bgr)

            # 恢复初始参数
            view_ctrl.convert_from_pinhole_camera_parameters(ctr_params)

            # 释放资源
            vis.clear_geometries()
            vis.destroy_window()
            del vis
            video_writer.release()
            print(f"Video saved as {name}")


