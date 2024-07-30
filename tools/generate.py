#encoding:UTF-8

from bark import generate_audio
import soundfile as sf

# 要生成语音的文本
text = "为什么科学家不能信任原子？因为它们会制造一切！"

# 生成语音
audio_array = generate_audio(text)

# 保存为WAV文件
file_path = "joke_bark.wav"
sf.write(file_path, audio_array, samplerate=22050)

print(f"语音文件已保存为: {file_path}")