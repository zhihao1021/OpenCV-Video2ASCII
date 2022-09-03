import os, subprocess, time, mimetypes
# pip_list = subprocess.run('pip list', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
# os.system('cls')
# os.system('color 7')
# if 'opencv-python' not in pip_list:
#     os.system('cls')
#     os.system('color 7')
#     print('\n缺少套件:opencv-python\n')
#     time.sleep(1)
#     os.system('pip install -U opencv-python')
# if 'pygame' not in pip_list:
#     os.system('cls')
#     os.system('color 7')
#     print('\n缺少套件:pygame\n')
#     time.sleep(1)
#     os.system('pip install -U pygame')
# if 'requests' not in pip_list:
#     os.system('cls')
#     os.system('color 7')
#     print('\n缺少套件:requests\n')
#     time.sleep(1)
#     os.system('pip install -U requests')

# import requests

# ffmpeg = str(subprocess.run('ffmpeg -version', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8'))
ffmpeg_path = ''
# if 'version' not in ffmpeg:
#     os.system('cls')
#     os.system('color 7')
#     print('\n缺少ffmpeg，下載中......\n')
#     with open('ffmpeg-release-essentials.zip', mode='wb') as zfile:
#         zfile.write(requests.get('https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip').content)
#         zfile.close()
#     zipfile.ZipFile('ffmpeg-4.4-essentials_build.zip').extractall()
#     os.remove('ffmpeg-4.4-essentials_build.zip')
#     ffmpeg_path = './ffmpeg-4.4-essentials_build/bin/'

import cv2, pygame, sys
from threading import Thread

pygame.mixer.init()
pygame.mixer.music.set_volume(0.15)

os.system('cls')
os.system('color 7')
media_list = []
count = 0

PRINT_HEIGH = 90

print('選擇影片:')
for i in range(len(os.listdir())):
    file_name = os.listdir()[i]
    if mimetypes.guess_type(file_name)[0] != None:
        if mimetypes.guess_type(file_name)[0].split('/')[0] == 'video':
            media_list.append(file_name)
            print(f'{count}:{file_name}')
            count += 1

while True:
    try:
        number = int(input('\n'))
        if number >= len(media_list):
            print('選擇失敗:超出範圍。')
            input('按下Enter繼續......')
            os.system('cls')
            os.system('color 7')
        else:
            print(f'\n選擇:{media_list[number]}')
            input('按下Enter繼續......')
            os.system('cls')
            os.system('color 7')
            break
    except:
        print('選擇失敗:輸入的不是數字。')
        input('按下Enter繼續......')
        os.system('cls')
        os.system('color 7')
    print('選擇影片:')
    for i in range(len(media_list)):
        print(f'{i}:{media_list[i]}')

raw_size = subprocess.run(f'{ffmpeg_path}ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0:s=x "{media_list[number]}"', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('x')
height = int(raw_size[0])
width = int(raw_size[1])
print('進行轉檔......')
os.system(f'{ffmpeg_path}ffmpeg -v error -i "{media_list[number]}" -s {int(height * (PRINT_HEIGH / width))}x{PRINT_HEIGH} -y temp.mp4')
os.system(f'{ffmpeg_path}ffmpeg -v error -i "{media_list[number]}" -vn -y temp.mp3')
pygame.mixer.music.load('temp.mp3')
print('轉檔完成!')

video = cv2.VideoCapture('temp.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
bar_leng = int(height * (90 / width)) - 10
total_time = float(subprocess.run(f'{ffmpeg_path}ffprobe -v error -select_streams v -show_entries stream=duration -of csv=p=0:s=x temp.mp4', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8'))
total_time = int(total_time)
out_list = []
#ASCII_CODE = ["@", "#", "&", "$", "S", "%", "?", "!", "*", "=", "+", "~", "-", ";", ":", ",", ".", " "]
ASCII_CODE = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
def load():
    global out_list
    for _ in range(int(frames)):
        _, img = video.read()
        img_list = []
        img_0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for i in range(len(ASCII_CODE)):
            img_list.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        for i in range(len(ASCII_CODE)):
            img_0[img_list[i] < (256 * (len(ASCII_CODE) - i) / len(ASCII_CODE))] = i
        temp = img_0.astype('U2')
        for i in range(len(ASCII_CODE)):
            temp[temp == str(i)] = ASCII_CODE[i]
        #print(str(temp.tolist()))
        temp = str(temp.tolist()).replace('\'], [\'', '\n').replace('\', \'', '')
        out_list.append("\n" +temp[3:-3])

def play_music():
    # pygame.mixer.music.load('temp.mp3')
    # time.sleep(0.27)
    pygame.mixer.music.play()

def play_video():
    global sleep_time, now_fps
    #time.sleep(0.05)
    played = 0
    now_fps = 0
    proc = [0, 0, bar_leng]
    p_time = [0, total_time]
    time_1 = [0, 0]
    time_2 = [0, 0]
    st_time = time.time()
    for content in out_list:
        played += 1
        proc[0] = int(bar_leng * played / frames)
        proc[1] = int(bar_leng * len(out_list) / frames) - proc[0]
        proc[2] = bar_leng - proc[0] - proc[1]
        # p_time[0] = int(time.time() - st_time)
        # p_time[1] = int(total_time - p_time[0])
        p_time[0] = pygame.mixer.music.get_pos() // 1000
        p_time[1] = total_time - p_time[0]
        time_1[1] = p_time[0] % 60
        time_1[0] = p_time[0] // 60
        time_2[1] = p_time[1] % 60
        time_2[0] = p_time[1] // 60
        if time_1[1] < 10: time_1[1] = '0' + str(time_1[1])
        if time_2[1] < 10: time_2[1] = '0' + str(time_2[1])
        sys.stdout.write(f'{content}\n{time_1[0]}:{time_1[1]}[{"=" * proc[0]}{"-" * proc[1]}{" " * proc[2]}]{time_2[0]}:{time_2[1]}\nP/C/A:{played}/{len(out_list)}/{frames} T:{format(time.time() - st_time, ".2f")}s FPS(avg./tgt.):{now_fps}/{fps} SleepTime:{format(sleep_time / 10, ".1f")}ms debug:{pygame.mixer.music.get_pos()}')
        """
        sys.stdout.write(f"{content}\n")
        """
        #out_list.remove(content)
        time.sleep(sleep_time / 10000)
        """
        # Time Controlor v1
        try:
            now_fps = float(format(played / (time.time() - st_time), '.2f'))
        except:
            pass
        if abs(now_fps - fps) > 0.05:
            if sleep_time + 2 * int(200 * (now_fps - fps)) > 0:
                sleep_time += 2 * int(200 * (now_fps - fps))
            else:
                sleep_time = 0
        else:
            sleep_time = def_sleep_time
        """
        # Time Controlor v2
        try:
            now_pos = (1000 * played / fps) + 50
            m_pos = pygame.mixer.music.get_pos()
            now_fps = float(format(1000 * played / m_pos, '.2f'))
            if abs(now_pos - m_pos) > 15:
                if sleep_time + (now_pos - m_pos) > 0:
                    sleep_time += now_pos - m_pos
                else:
                    sleep_time = 0
            else:
                sleep_time = def_sleep_time
        except:
            pass
        # """

thr = Thread(target=load)
thr.start()
#thr.join()
def_sleep_time = 220 * 30 / fps
sleep_time = def_sleep_time
now_fps = fps
thr_music = Thread(target=play_music)
thr_video = Thread(target=play_video)
input('按下Enter開始......')
thr_music.start()
thr_video.start()
thr_video.join()
input('\n結束......')
os.remove('temp.mp4')
os.remove('temp.mp3')