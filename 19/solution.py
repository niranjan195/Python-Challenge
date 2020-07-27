import os
import re
import wave
import base64
import array


sol_no = re.findall('(\d+).py', __file__)[0]
file_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "../../%s" % sol_no))
file_name = file_path + "/audio.txt"
file_name1 = file_path + "/india.wav"
file_name2 = file_path + "/sol.wav"

with open(file_name) as infile:
    audio_data = infile.read()

# print(audio_data)

with open(file_name1, "wb") as audiofile:
    audiofile.write(base64.decodebytes(audio_data.encode()))

audio = wave.open(file_name1)
frames = audio.readframes(audio.getnframes())
frames = array.array("H", frames)
frames.byteswap()

# New audio
new_audio = wave.open(file_name2, 'w')
#necessary_data
new_audio.setnchannels(audio.getnchannels())
new_audio.setsampwidth(audio.getsampwidth())
new_audio.setframerate(audio.getframerate())
new_audio.writeframes(frames)

audio.close()
new_audio.close()

