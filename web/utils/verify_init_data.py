import hmac
import hashlib
import urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        if not init_data:
            print("⚠️ init_data bos.")
            return None

        parsed = dict(urllib.parse.parse_qsl(init_data, strict_parsing=True))
        hash_check = parsed.pop('hash', None)
        if not hash_check:
            print("⚠️ hash joq.")
            return None

        data_check_arr = [f"{k}={v}" for k, v in sorted(parsed.items())]
        data_check_string = '\n'.join(data_check_arr)

        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
        hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

        if hmac_hash != hash_check:
            print("⚠️ HMAC hash qa'te.")
            return None

        return parsed

    except Exception as e:
        print("❌ verify_init_data ERROR:", e)
        return None
