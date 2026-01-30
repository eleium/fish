from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from typing import List, Tuple, Optional, Union
import argparse


class Config:
    """配置类"""

    def __init__(self):
        self.default_font_path = str(Path("c:/windows/fonts/simkai.ttf").resolve())
        self.default_output_dir = str(Path("C:/Users/elei/Desktop/output").resolve())
        self.default_size = 400
        self.default_chars = "龙年大吉"
        self.image_quality = 95
        self.font_scale = 0.75
        self.text_offset = (10, 10)
        self.output_format = 'JPEG'
        self.background_color = '#F8F8F8'
        self.text_color = '#000000'
        self.shadow_config = {
            "positions": [(2, 6), (3, 8), (4, 10)],
            "colors": ['#2a2a2a', '#404040', '#606060']
        }
        self.highlight_config = {
            "positions": [(-3, -3), (-1, -1)],
            "colors": ['#ffffff', '#f0f0f0']
        }
        self.light_direction = "top-left"


class Character3DRenderer:
    """3D汉字渲染器"""

    def __init__(self, config):
        self.config = config
        self.font_cache = {}

    def get_font(self, font_path: Union[str, Path], font_size: int) -> ImageFont.FreeTypeFont:
        """获取字体对象（使用缓存）"""
        key = (str(font_path), font_size)
        if key not in self.font_cache:
            self.font_cache[key] = ImageFont.truetype(str(font_path), font_size)
        return self.font_cache[key]

    def calculate_shadow_positions(self, light_direction: str) -> List[Tuple[int, int]]:
        """根据光源方向计算阴影位置"""
        if light_direction == "top-left":
            return [(2, 6), (3, 8), (4, 10)]
        elif light_direction == "top-right":
            return [(-2, 6), (-3, 8), (-4, 10)]
        elif light_direction == "bottom-left":
            return [(2, -6), (3, -8), (4, -10)]
        elif light_direction == "bottom-right":
            return [(-2, -6), (-3, -8), (-4, -10)]
        else:
            return [(2, 6), (3, 8), (4, 10)]

    def create_realistic_3d(self, draw: ImageDraw.ImageDraw, character: str,
                            font: ImageFont.FreeTypeFont, x: int, y: int, size: int):
        """创建真实3D效果"""
        # 计算阴影位置
        shadow_positions = self.calculate_shadow_positions(self.config.light_direction)

        # 绘制多层阴影
        for offset, color in zip(shadow_positions, self.config.shadow_config["colors"]):
            draw.text((x + offset[0], y + offset[1]), character,
                      font=font, fill=color)

        # 主文本
        draw.text((x, y), character, font=font, fill=self.config.text_color)

        # 绘制高光
        for offset, color in zip(self.config.highlight_config["positions"],
                                 self.config.highlight_config["colors"]):
            draw.text((x + offset[0], y + offset[1]), character,
                      font=font, fill=color)

    def create_realistic_3d_character(self, character: str, font_path: Union[str, Path],
                                      output_dir: Union[str, Path], index: int,
                                      size: Optional[int] = None) -> Optional[Union[str, Path]]:
        """创建真实3D效果汉字"""
        size = size or self.config.default_size

        # 路径处理
        font_path = Path(font_path).resolve()
        output_dir = Path(output_dir).resolve()

        # 检查字体文件是否存在
        if not font_path.exists():
            print(f"错误: 字体文件不存在: {font_path}")
            return None

        # 确保输出目录存在
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            # 测试写入权限
            test_file = output_dir / ".test_write.txt"
            with open(test_file, 'w') as f:
                f.write("test")
            test_file.unlink()
        except Exception as e:
            print(f"错误: 输出目录不可写: {e}")
            return None

        # 创建基础图像
        img = Image.new('RGB', (size, size), color=self.config.background_color)
        draw = ImageDraw.Draw(img)

        try:
            # 加载字体
            font_size = int(size * self.config.font_scale)
            font = self.get_font(font_path, font_size)

            # 获取文本尺寸并计算居中位置
            bbox = draw.textbbox((0, 0), character, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x = (size - text_width) // 2 + self.config.text_offset[0]
            y = (size - text_height) // 2 + self.config.text_offset[1]

            # 创建真实3D效果
            self.create_realistic_3d(draw, character, font, x, y, size)

            # 保存图像
            filename = f"3d_realistic_{index:02d}_{character}.{self.config.output_format.lower()}"
            output_path = output_dir / filename
            img.save(output_path, self.config.output_format, quality=self.config.image_quality)

            print(f"✓ 已生成: {output_path}")
            return output_path

        except Exception as e:
            print(f"错误: {e}")
            return None

    def process_multiple_characters(self, characters: str, font_path: Union[str, Path],
                                    output_dir: Union[str, Path], size: Optional[int] = None) -> List[
        Tuple[int, str, Union[str, Path]]]:
        """处理多个汉字（并行）"""
        size = size or self.config.default_size

        # 路径处理
        output_dir = Path(output_dir).resolve()

        # 确保输出目录存在
        output_dir.mkdir(parents=True, exist_ok=True)

        results = []
        char_list = [c for c in characters if c.strip()]

        if not char_list:
            print("❌ 没有有效的汉字输入")
            return results

        print(f"将处理 {len(char_list)} 个汉字: {''.join(char_list)}")

        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=min(8, len(char_list))) as executor:
            # 提交所有任务
            future_to_char = {}
            for index, char in enumerate(char_list, 1):
                future = executor.submit(
                    self.create_realistic_3d_character,
                    character=char,
                    font_path=font_path,
                    output_dir=output_dir,
                    index=index,
                    size=size
                )
                future_to_char[future] = (index, char)

            # 收集结果（带进度条）
            for future in tqdm(future_to_char, desc="生成3D汉字", unit="个"):
                index, char = future_to_char[future]
                try:
                    result = future.result()
                    if result:
                        results.append((index, char, result))
                except Exception as e:
                    print(f"处理 '{char}' 时出错: {e}")

        # 按索引排序结果
        results.sort(key=lambda x: x[0])
        return results

    def process_from_file(self, file_path: Union[str, Path], font_path: Union[str, Path],
                          output_dir: Union[str, Path], size: Optional[int] = None) -> List[
        Tuple[int, str, Union[str, Path]]]:
        """从文本文件读取汉字并处理"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                characters = f.read().strip()
            return self.process_multiple_characters(characters, font_path, output_dir, size)
        except Exception as e:
            print(f"读取文件时出错: {e}")
            return []

    def generate_preview(self, characters: str, font_path: Union[str, Path],
                         output_path: Union[str, Path], size: int = 800) -> Optional[Union[str, Path]]:
        """生成预览图像（多个汉字合成一张）"""
        char_list = [c for c in characters if c.strip()]
        if not char_list:
            print("❌ 没有有效的汉字输入")
            return None

        # 计算每行显示的汉字数量
        chars_per_row = min(4, len(char_list))
        rows = (len(char_list) + chars_per_row - 1) // chars_per_row

        # 创建预览图像
        preview_width = size
        preview_height = int(size * (rows / chars_per_row))
        preview_img = Image.new('RGB', (preview_width, preview_height), color='#F8F8F8')
        preview_draw = ImageDraw.Draw(preview_img)

        # 计算每个汉字的位置
        char_size = int(size / chars_per_row * 0.8)
        padding = int(size / chars_per_row * 0.1)

        for i, char in enumerate(char_list):
            row = i // chars_per_row
            col = i % chars_per_row

            # 计算位置
            x = col * (char_size + padding) + padding
            y = row * (char_size + padding) + padding

            # 加载字体
            font_size = int(char_size * 0.75)
            font = self.get_font(font_path, font_size)

            # 绘制3D效果
            self.create_realistic_3d(preview_draw, char, font, x, y, char_size)

        # 保存预览图像
        output_path = Path(output_path).resolve()
        preview_img.save(output_path, 'PNG', quality=95)
        print(f"✓ 已生成预览: {output_path}")
        return output_path


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="生成3D效果汉字图像")

    parser.add_argument("-c", "--chars", type=str, default=config.default_chars,
                        help=f"要生成3D效果的汉字，默认: {config.default_chars}")
    parser.add_argument("-f", "--font", type=str, default=config.default_font_path,
                        help=f"字体文件路径，默认: {config.default_font_path}")
    parser.add_argument("-o", "--output", type=str, default=config.default_output_dir,
                        help=f"输出目录，默认: {config.default_output_dir}")
    parser.add_argument("-s", "--size", type=int, default=config.default_size,
                        help=f"图像尺寸，默认: {config.default_size}")
    parser.add_argument("-q", "--quality", type=int, default=config.image_quality,
                        help=f"图像质量 (1-100)，默认: {config.image_quality}")
    parser.add_argument("-fmt", "--format", type=str, default=config.output_format,
                        choices=["JPEG", "PNG"], help=f"输出格式，默认: {config.output_format}")
    parser.add_argument("-dir", "--direction", type=str, default=config.light_direction,
                        choices=["top-left", "top-right", "bottom-left", "bottom-right"],
                        help=f"光源方向，默认: {config.light_direction}")
    parser.add_argument("-p", "--preview", action="store_true",
                        help="生成预览图像（多个汉字合成一张）")

    return parser.parse_args()


if __name__ == "__main__":
    # 创建配置和渲染器实例
    config = Config()
    renderer = Character3DRenderer(config)

    # 解析命令行参数
    args = parse_args()

    # 更新配置
    config.default_chars = args.chars
    config.default_font_path = args.font
    config.default_output_dir = args.output
    config.default_size = args.size
    config.image_quality = args.quality
    config.output_format = args.format
    config.light_direction = args.direction

    # 输入处理
    input_chars = input('请输入您要的汉字(可输入多个): ')

    if not input_chars.strip():
        input_chars = config.default_chars

    print(f"输入的汉字: {input_chars}")

    # 生成3D汉字
    results = renderer.process_multiple_characters(
        characters=input_chars,
        font_path=config.default_font_path,
        output_dir=config.default_output_dir,
        size=config.default_size
    )

    # 生成预览（如果需要）
    if args.preview and results:
        preview_path = Path(config.default_output_dir) / "preview.png"
        renderer.generate_preview(
            characters=input_chars,
            font_path=config.default_font_path,
            output_path=preview_path,
            size=800
        )

    if results:
        print("\n🎉 全部生成完成！")
        print(f"共生成 {len(results)} 个汉字:")
        print("生成顺序:")
        for index, char, path in results:
            print(f"  {index:2d}. {char} -> {Path(path).name}")
        print(f"\n输出文件夹: {config.default_output_dir}")

        # 尝试打开文件夹（Windows）
        try:
            if os.name == 'nt':  # Windows
                os.startfile(config.default_output_dir)
                print("✓ 已自动打开输出文件夹")
            else:
                print("请手动打开文件夹查看结果")
        except:
            print("请手动打开文件夹查看结果")
    else:
        print("❌ 生成失败，请检查字体路径和权限")