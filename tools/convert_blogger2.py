import subprocess
import os
import shutil

DIR = "old"
NEWDIR = "old2"

for fl in os.listdir(DIR):
    print fl
    with open(os.path.join(DIR,fl)) as f:
        text = f.readlines()
    header = text[:6]

    with open(os.path.join(NEWDIR,fl+'.html'),'w') as g:
        g.writelines(text[6:])

    subprocess.call(['pandoc',
        os.path.join(NEWDIR,fl+'.html'),
        "-o",os.path.join(NEWDIR,fl)])

    with open(os.path.join(NEWDIR,fl)) as f:
        text = f.readlines()

    text = header + ['\n','\n'] + text

    with open(os.path.join(NEWDIR,fl), 'w') as f:
        f.writelines(text)



