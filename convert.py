from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path


def create_realistic_3d_character(character, font_path, output_dir, index, size=300):
    """
    创建真实3D效果汉字

    参数:
    character: 单个汉字
    font_path: 字体路径
    output_dir: 输出目录
    index: 字符在输入序列中的索引
    size: 图像尺寸
    """
    # 创建基础图像
    img = Image.new('RGB', (size, size), color='#F8F8F8')
    draw = ImageDraw.Draw(img)

    try:
        # 加载字体
        font_size = int(size * 0.75)
        font = ImageFont.truetype(font_path, font_size)

        # 获取文本尺寸并计算居中位置
        bbox = draw.textbbox((0, 0), character, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (size - text_width) // 2 + 10
        y = (size - text_height) // 2 + 10

        # 创建真实3D效果
        create_realistic_3d(draw, character, font, x, y, size)

        # 保存图像 - 使用索引确保顺序和避免覆盖
        filename = f"3d_realistic_{index:02d}_{character}.jpg"
        output_path = os.path.join(output_dir, filename)
        img.save(output_path, 'JPEG', quality=95)

        print(f"✓ 已生成: {output_path}")
        return output_path

    except Exception as e:
        print(f"错误: {e}")
        return None


def create_realistic_3d(draw, character, font, x, y, size):
    """创建真实3D效果"""
    # 多层阴影 - 模拟左上光源
    shadow_positions = [(2, 6)]
    shadow_colors = ['#2a2a2a', '#404040', '#606060']

    # 绘制多层阴影
    for offset, color in zip(shadow_positions, shadow_colors):
        draw.text((x + offset[0], y + offset[1]), character,
                  font=font, fill=color)

    # 主文本
    draw.text((x, y), character, font=font, fill='#000000')

    # 高光 - 左上方向
    highlight_x, highlight_y = x - 3, y - 3
    draw.text((highlight_x, highlight_y), character,
              font=font, fill='#ffffff')

    # 额外的高光层，增强立体感
    draw.text((x - 1, y - 1), character,
              font=font, fill='#f0f0f0')


def process_multiple_characters(characters, font_path, output_dir, size=400):
    """
    处理多个汉字

    参数:
    characters: 多个汉字组成的字符串
    font_path: 字体路径
    output_dir: 输出目录
    size: 图像尺寸
    """
    # 确保输出目录存在
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    results = []
    # 将字符转换为列表并过滤空白字符，同时记录原始索引
    char_list = [c for c in characters if c.strip()]

    if not char_list:
        print("❌ 没有有效的汉字输入")
        return results

    print(f"将处理 {len(char_list)} 个汉字: {''.join(char_list)}")

    for index, char in enumerate(char_list, 1):  # 从1开始编号
        print(f"\n正在为第 {index} 个汉字 '{char}' 创建3D效果...")
        result = create_realistic_3d_character(
            character=char,
            font_path=font_path,
            output_dir=output_dir,
            index=index,  # 传递索引
            size=size
        )
        if result:
            results.append((index, char, result))  # 保存索引、字符和路径

    return results


# 使用示例
if __name__ == "__main__":
    FONT_PATH = r"c:/windows/fonts/simkai.ttf"
    OUTPUT_DIR = r"C:\Users\elei\Desktop\output"

    # 输入多个汉字
    input_chars = input('请输入您要的汉字(可输入多个): ')

    if not input_chars.strip():
        input_chars = "龙年大吉"  # 默认汉字

    print(f"输入的汉字: {input_chars}")

    # 生成3D汉字
    results = process_multiple_characters(
        characters=input_chars,
        font_path=FONT_PATH,
        output_dir=OUTPUT_DIR,
        size=400  # 可以调整尺寸
    )

    if results:
        print("\n🎉 全部生成完成！")
        print(f"共生成 {len(results)} 个汉字:")
        print("生成顺序:")
        for index, char, path in results:
            print(f"  {index:2d}. {char} -> {os.path.basename(path)}")
        print(f"\n输出文件夹: {OUTPUT_DIR}")

        # 尝试打开文件夹（Windows）
        try:
            os.startfile(OUTPUT_DIR)
            print("✓ 已自动打开输出文件夹")
        except:
            print("请手动打开文件夹查看结果")
    else:
        print("❌ 生成失败，请检查字体路径和权限")