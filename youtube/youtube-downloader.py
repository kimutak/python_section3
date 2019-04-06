import pytube
import os
import subprocess #파이썬을 실행하면서 별도의 프로세스 생성, 터미널 명령어 실행 및 반환값을 가져올 수 있따.
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

ytUrl = input("input URL:")

yt = pytube.YouTube(ytUrl) #다운 받을 동영상 URL 지정
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) : #range(1,6) 1, 2, 3, 4, 5
    print(i, ', ', videos[i])

cNum = int(input("DownLoad pixel:")) # 사용자한테 키보드로 입력된 값을 할당
down_dir = "C:/synergy/inflearnpython/section2/youtube"

videos[cNum].download(down_dir)
ans = input("change mp3 File?[y/n]")

if ans=='y':
    newFileName = input("change mp3 filename:")
    oriFileName = videos[cNum].default_filename

    subprocess.call(['ffmpeg','-i',
        os.path.join(down_dir, oriFileName),
        os.path.join(down_dir, newFileName)
        ])
    print("Video Download and change mp3 complete!")

else:
    print("Video Download Complete!")
