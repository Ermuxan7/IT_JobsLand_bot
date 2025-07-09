import hmac
import hashlib
import urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        if not init_data:
            print("⚠️ init_data bos.")
            return None

        print("📦 Kelgen init_data:", init_data)

        parsed = dict(urllib.parse.parse_qsl(init_data, strict_parsing=True))
        print("🧩 Parsed init_data:", parsed)

        hash_check = parsed.pop('hash', None)
        parsed.pop('signature', None)
        if not hash_check:
            print("⚠️ hash joq.")
            return None

        print("🔐 hash (Telegramnan):", hash_check)

        # Hash hisoblash uchun string yasaymiz
        data_check_arr = [f"{k}={v}" for k, v in sorted(parsed.items())]
        data_check_string = '\n'.join(data_check_arr)
        print("📄 HMAC ushin data_check_string:", repr(data_check_string))

        # HMAC hisoblash
        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
        hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        print("🔑 HMAC esaplangan hash:", hmac_hash)

        if hmac_hash != hash_check:
            print("❌ HMAC hash mas emes!")
            return None

        print("✅ HMAC hash duris!")
        return parsed

    except Exception as e:
        print("❌ verify_init_data ERROR:", e)
        return None
