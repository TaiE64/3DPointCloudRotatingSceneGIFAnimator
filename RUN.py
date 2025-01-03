import open3d as o3d
import numpy as np
import cv2
import os
import subprocess
from mp4_to_gif import GifConverter
from ply_to_mp4 import mp4

first_step=mp4("ply_test") #input ply file folder path
second_step=GifConverter('mp4', 'gif') #input mp4 folder and gif folder paths