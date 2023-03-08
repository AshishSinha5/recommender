import json
import io
import zstandard


with open('data/RC_2023-01.zst', 'rb') as fh:
    dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
    stream_reader = dctx.stream_reader(fh)
    text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
    comments = []
    i = 0
    k = 0
    chunk_size = 500000
    max_chunks = 5
    for line in tqdm(text_stream):
        if i >= chunk_size:
            with open('data/RC_2023_01_{k}.json', 'w') as f1
                json.dump(comments, f1)
            k+=1
            i=0
            comments = []
            if k>=max_chunks:
                break
        comment = json.load(line)
        comments.append(comment)

