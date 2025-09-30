import numpy as np
import cv2

def render_animation(head_px_gr, heel_px_gr):
    initial_img, final_img, map_x_end, map_y_end = prepare_morph_data(head_px_gr, heel_px_gr)
    
    # The default arguments (morph_duration_s=3, hold_duration_s=2, fps=30)
    create_morph_video(initial_img, final_img, map_x_end, map_y_end)

def prepare_morph_data(head_px_gr, heel_px_gr):
    W = head_px_gr.width
    H = head_px_gr.height
    pixels = W * H

    map_x_end = np.zeros((H, W), dtype=np.float32)
    map_y_end = np.zeros((H, W), dtype=np.float32)
    final_color_data = cv2.imread("output\\output.png")
    initial_image_data = cv2.imread("temp\\heel.png")
    
    # Map the coordinates
    for pixel_index in range(pixels):
        final_x = head_px_gr.sorted_merged_list[pixel_index].x
        final_y = head_px_gr.sorted_merged_list[pixel_index].y

        source_pixel = heel_px_gr.sorted_merged_list[pixel_index]

        map_x_end[final_y, final_x] = source_pixel.x
        map_y_end[final_y, final_x] = source_pixel.y

    return initial_image_data, final_color_data, map_x_end, map_y_end


def create_morph_video(initial_img, final_img, map_x_end, map_y_end, morph_duration_s=3, hold_duration_s=2, fps=30.0):
    # pre
    H, W, _ = initial_img.shape
    video_path = "output\\output.mp4"
    
    hold_frames = int(hold_duration_s * fps)
    morph_frames = int(morph_duration_s * fps)
    
    map_x_start, map_y_start = np.meshgrid(np.arange(W), np.arange(H))
    map_x_start = map_x_start.astype(np.float32)
    map_y_start = map_y_start.astype(np.float32)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (W, H))

    
    for _ in range(hold_frames):
        out.write(initial_img)


    # Loop from frame 1 up to morph_frames (inclusive)
    for i in range(morph_frames + 1):
        t = i / morph_frames  # Time factor: 0.0 to 1.0

        # Linear interpolation of the coordinate maps
        map_x_t = (1 - t) * map_x_start + t * map_x_end
        map_y_t = (1 - t) * map_y_start + t * map_y_end

        # Apply the warping (pixel shifting) using cv2.remap
        frame = cv2.remap(initial_img, map_x_t, map_y_t, 
                          interpolation=cv2.INTER_LINEAR,
                          borderMode=cv2.BORDER_REPLICATE)
        
        out.write(frame)

    for _ in range(hold_frames):
        out.write(final_img)

    out.release()