# redisを使用した queueの お試しサービス
import random, string
from time import sleep
from redis import Redis

# redis初期化(だるいので環境変数なし) (起動したら繋ぎっぱなし)
_redis = Redis(host='redis', port=6379, db=0)
queue_keys = ['AAA', 'BBB']
wait_timeout = 180

"""
:return str: キー作成
"""
def make_key() -> str:
    # 10桁ランダム文字列
    return make_random(10)

"""
:param int n 指定桁数
:return str: ランダム文字列
"""
def make_random(n: int) -> str:
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

"""
待ち行列ありのサービス作成
:param str key:トランザクションキー的な
"""
def execute(key: str):
    # 待ち行列管理 先検索
    kvs_key = find_index_by_min_length_of_queue()
    # 待ち行列に登録（後ろ）
    append_queue(kvs_key, key)
    # 待たせてでもさせたい作業の実行
    return wait_execute(kvs_key, key)

"""
待ち行列の作業実行
"""
def wait_execute(kvs_key: str, key: str) -> str:
    # 待ち行列にの順番取得
    val = find_queue_by_key(kvs_key)
    # 待ち行列の何番目取得
    index = list(val).index(key)

    # 先頭が自分の場合 後続処理実行
    if index == 0:
        # 待たせてでもしたい作業実行
        wait_service(key)
        # 待ち行列から削除
        pop_queue(kvs_key, key)
        return 'success'
    # それ以外 順番待ち(数秒後に実行)
    else:
        # 数秒後に際実行
        sleep(3)
        return wait_execute(kvs_key, key)
"""
待たせてでもしたい作業
"""
def wait_service(key: str):
    sleep(10)
    print(key)

"""
:return str: 待ち行列管理 最小の配列数 のキー名取得
"""
def find_index_by_min_length_of_queue() -> str:
    # 指定キー分 待ち行列管理 Redisの値取得
    queue_dict = {}
    for kvs_key in queue_keys:
        # キーごとの 待ち行列管理
        queue_dict[kvs_key] = find_queue_by_key(kvs_key)

    # 最小の配列数のキー検索
    min_length = 999
    min_key = None
    for k, v in queue_dict.items():
        # 配列数
        length = len(v)
        # 最小
        if min_length > length:
            min_length = length
            min_key = k
    return min_key

"""
:param str kvs_key:KVS設定のキー
:return list:待ち行列
"""
def find_queue_by_key(kvs_key: str) -> list:
    # 指定キーの値取得
    val = _redis.get(kvs_key)
    # 未定義 → 空
    if val is None:
        return list()

    # 値変換
    val = val.decode('utf-8')
    # 型変換 = カンマ区切り文字 → 配列
    val = val.split(',') if val.find(',') > 0 else [val] # カンマ区切り文字 → 配列
    # 空の値除外
    return list(filter(lambda v: v != '', val))

"""
待ち行列登録（後ろ）
"""
def append_queue(kvs_key: str, append_key: str):
    # 待ち行列取得
    val = find_queue_by_key(kvs_key)
    # 待ち行列に追加
    val.append(append_key)
    # 待ち行列保存
    _redis.set(kvs_key, ','.join(val))

"""
取り除く
"""
def pop_queue(kvs_key: str, pop_key: str):
    # 待ち行列取得
    val = find_queue_by_key(kvs_key)
    # 待ち行列から指定ポップするキー除く
    val.pop(val.index(pop_key))
    # 待ち行列保存
    _redis.set(kvs_key, ','.join(val) if len(val) >= 1 else '')