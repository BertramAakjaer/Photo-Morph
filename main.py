
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from art import text2art


import modules.animation as ani
import modules.pixels as pix


HEAD_PATH = "temp\\head.png"
HEEL_PATH = "temp\\heel.png"
OUTPUT_PATH = "output\\output.png"
OUT_VID_PATH = "output\\output.mp4"


def reload_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    header = text2art("// Photo-Morph //")
    print(header)


def save_n_resize_image(is_head, input_path, sizes=(0,0), max_width=2000):
    new_width, new_height = (0, 0)
    img = Image.open(input_path)
    output_path = ""

    if is_head:
        output_path = HEAD_PATH
        H, W = img.size

        if W > max_width:
            new_width = max_width
            new_height = H * (W // new_width)

            img = img.resize((new_width, new_height))
    else:
        output_path = HEEL_PATH
        img = img.resize(sizes)

    rgb_img = img.convert("RGB")
    
    rgb_img.save(output_path, format="PNG")



def new_head_n_heel(sizes=(0, 0), is_head=False, is_heel=False):
    if is_head:
        path = get_file("Pick image for template usage")

        save_n_resize_image(True, path, sizes)
        return extract_pixels(HEAD_PATH)
    
    if is_heel:
        path = get_file("Choose image for mapping to template")

        save_n_resize_image(False, path, sizes)
        return extract_pixels(HEEL_PATH)
    



def setup_clean_directory(clean_directory = False):
    if not os.path.exists(os.path.dirname(HEAD_PATH)):
        os.makedirs(os.path.dirname(HEAD_PATH))

    if not os.path.exists(os.path.dirname(OUTPUT_PATH)):
        os.makedirs(os.path.dirname(OUTPUT_PATH))

    if clean_directory:
        for file in os.listdir(os.path.dirname(HEAD_PATH)):
            os.remove(os.path.join(os.path.dirname(HEAD_PATH), file))

def user_prompt(prompt):
    while True:
        answer = input(f"{prompt} (Y/n): ").strip().lower()
        if answer in ('y', 'yes'):
            return True
        
        elif answer in ('n', 'no'):
            return False
        
        else:
            print("Invalid input. Please answer with 'y' or 'n'.")


def extract_pixels(img_path):
    img = Image.open(img_path)
    width, height = img.size

    new_pixel_group = pix.PixelGroups(width, height)
    
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            new_pixel_group.add_pixel(color, x, y)
    
    new_pixel_group.get_sorted_groups()

    return new_pixel_group




def map_pixels(head_px_gr: pix.PixelGroups, heel_px_gr: pix.PixelGroups):
    try:
        mode = 'RGB'
        black = (0, 0, 0)
        mapped_img = Image.new(mode, (head_px_gr.width, head_px_gr.height), color=black)

        pixels = (head_px_gr.width * head_px_gr.height)

        for pixel_index in range(pixels):
            x = head_px_gr.sorted_merged_list[pixel_index].x
            y = head_px_gr.sorted_merged_list[pixel_index].y

            R = heel_px_gr.sorted_merged_list[pixel_index].R
            G = heel_px_gr.sorted_merged_list[pixel_index].G
            B = heel_px_gr.sorted_merged_list[pixel_index].B


            color = (R, G, B)

            mapped_img.putpixel((x, y), color)
        

        mapped_img.save(OUTPUT_PATH, format="PNG")

        return True
    except:
        return False


def get_file(prompt="No promt given :'("):
    print(f"\n// {prompt} //")
    temp_file_path = filedialog.askopenfilename(title=prompt, filetypes=[("Image", "*.png;*.jpg;*.jpeg;*.webp")])
    return temp_file_path



def main():
    root = tk.Tk() # Load Tkinter for file submit
    root.withdraw()  # Hide the root window

    reload_menu()
    setup_clean_directory()

    if os.path.exists(HEAD_PATH):

        if user_prompt("Keep cached template?"):
            print("Loading in previous template image...")
            Head_pixel_group = extract_pixels(HEAD_PATH)

        else:
            print("Creating new template image...")
            Head_pixel_group = new_head_n_heel(is_head=True)

    else:
        Head_pixel_group = new_head_n_heel(is_head=True)


    template_sizes = (Head_pixel_group.width, Head_pixel_group.height)


    Heel_pixel_group = new_head_n_heel(template_sizes, is_heel=True)


    if map_pixels(Head_pixel_group, Heel_pixel_group):
        print(f"Image is succesfully saved in the {os.path.dirname(OUTPUT_PATH)} folder")

    if user_prompt("\n\nMake image mapping into an animation?"):
        ani.render_animation(Head_pixel_group, Heel_pixel_group)


if __name__ == "__main__":
    main()