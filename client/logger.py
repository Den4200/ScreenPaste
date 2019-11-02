from time import ctime

LOGS_DIR = 'log.txt'

def _info(state, info):
    return (
        ctime(),
        f' [{state}] ',
        f'{info}\n',
    )

def log(state, info):
    f_info = _info(state, info)

    with open(LOGS_DIR, 'a') as f:
        for inf in f_info:
            f.write(inf.replace('\\n', '', 2))
