import os
from tqdm import *
import torch.multiprocessing as mp
import glob
import shutil


def process(content, start, end):
    for wav in tqdm(content[start:end]):

        target_path = wav.replace("\\VALLE-X", "\\VALLE-X2")
        # import ipdb; ipdb.set_trace()
        if os.path.exists(target_path):
            continue
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        os.system(f"ffmpeg -i {wav} -ar 16000 {target_path}")

src_dir = r"C:\Users\happyelements\Desktop\zero-shot_speech\对比实验\VALLE-X"
wavs = list(glob.glob('{}/*.wav'.format(src_dir)))
wavs += list(glob.glob('{}/*/*.wav'.format(src_dir)))
process(wavs,0,len(wavs) - 1)

# processes = []
# num_processes = 32
# part_size = len(wavs) // num_processes
# processes = []
# for i in range(num_processes):
#     start = i * part_size
#     end = (i + 1) * part_size if i != num_processes - 1 else None
#     p = mp.Process(target=process, args=(wavs, start, end))
#     p.start()
#     processes.append(p)

# for p in processes:
#     p.join()