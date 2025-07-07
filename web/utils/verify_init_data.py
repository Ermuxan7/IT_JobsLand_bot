import hmac
import hashlib
import urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        if not init_data:
            print("⚠️ init_data bos.")
            return None

        parsed = urllib.parse.parse_qs(init_data, strict_parsing=True)
        
        hash_check = parsed.get('hash', [None])[0]
        if not hash_check:
            print("⚠️ hash joq.")
            return None

        # 'hash' dan boshqa barcha key=value
        data_check_arr = []
        for key in sorted(parsed):
            if key != 'hash':
                value_list = parsed.get(key)
                if not value_list or not value_list[0]:
                    print(f"⚠️ Kalit {key} qiymati yo‘q.")
                    return None
                value = value_list[0]
                data_check_arr.append(f"{key}={value}")
        data_check_string = '\n'.join(data_check_arr)

        # HMAC hash tekshiruvi
        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
        hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

        if hmac_hash != hash_check:
            print("⚠️ HMAC hash qate.")
            return None

        # Ma’lumotlar valid
        return {
            key: parsed[key][0]
            for key in parsed
            if key != 'hash'
        }

    except Exception as e:
        print("❌ verify_init_data ERROR:", e)
        return None
