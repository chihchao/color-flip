import gradio as gr
import colorsys

def rgb_to_hsb_logic(r, g, b):
    # 將 0-255 轉為 0-1
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    return round(h * 360, 1), round(s * 100, 1), round(v * 100, 1)

def hsb_to_rgb_logic(h, s, b):
    # 將度數與百分比轉為 0-1
    r, g, b_res = colorsys.hsv_to_rgb(h/360, s/100, b/100)
    return round(r * 255), round(g * 255), round(b_res * 255)

def update_from_rgb(r, g, b):
    h, s, b_val = rgb_to_hsb_logic(r, g, b)
    hex_color = f'#{int(r):02x}{int(g):02x}{int(b):02x}'
    preview = f'<div style="width: 100%; height: 100px; background-color: {hex_color}; border-radius: 10px; border: 2px solid #ddd;"></div>'
    return h, s, b_val, preview

def update_from_hsb(h, s, b_val):
    r, g, b = hsb_to_rgb_logic(h, s, b_val)
    hex_color = f'#{int(r):02x}{int(g):02x}{int(b):02x}'
    preview = f'<div style="width: 100%; height: 100px; background-color: {hex_color}; border-radius: 10px; border: 2px solid #ddd;"></div>'
    return r, g, b, preview

with gr.Blocks(title="色彩模式轉換教學") as demo:
    gr.Markdown("## 色彩模式互動教學：RGB ↔ HSB")
    gr.Markdown("透過調整下方的滑桿，觀察兩種色彩模型是如何相互轉換的。")
    
    with gr.Row():
        # 左側：RGB 調整區
        with gr.Column():
            gr.Markdown("### RGB 模式 (硬體/光學)")
            r = gr.Slider(0, 255, value=255, step=1, label="Red (R)")
            g = gr.Slider(0, 255, value=128, step=1, label="Green (G)")
            b = gr.Slider(0, 255, value=0, step=1, label="Blue (B)")
        
        # 右側：HSB 調整區
        with gr.Column():
            gr.Markdown("### HSB 模式 (直覺/設計)")
            h = gr.Slider(0, 360, value=30, step=0.1, label="Hue (H) - 色相 °")
            s = gr.Slider(0, 100, value=100, step=0.1, label="Saturation (S) - 飽和度 %")
            br = gr.Slider(0, 100, value=100, step=0.1, label="Brightness (B) - 亮度 %")
    
    with gr.Row():
        color_preview = gr.HTML()

    # 建立連動邏輯
    # 當 RGB 改變時，更新 HSB 和 預覽
    rgb_inputs = [r, g, b]
    hsb_outputs = [h, s, br, color_preview]
    
    # 使用 .input 讓滑動過程即時觸發
    for obj in rgb_inputs:
        obj.input(update_from_rgb, inputs=rgb_inputs, outputs=hsb_outputs)

    # 當 HSB 改變時，更新 RGB 和 預覽
    hsb_inputs = [h, s, br]
    rgb_outputs = [r, g, b, color_preview]
    
    for obj in hsb_inputs:
        obj.input(update_from_hsb, inputs=hsb_inputs, outputs=rgb_outputs)

    # 初始載入
    demo.load(update_from_rgb, inputs=rgb_inputs, outputs=hsb_outputs)

demo.launch()
