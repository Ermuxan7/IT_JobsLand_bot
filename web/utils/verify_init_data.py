import hmac, hashlib, urllib.parse, json
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        # 1. init_data stringini dictionary (dict) ga aylantirish
        parsed_data = dict(urllib.parse.parse_qsl(init_data))

        # 2. hashdi ajiratip aliw
        received_hash = parsed_data.pop("hash", None)

        # 3. qalg'an mag'liwmatlardi ta'rtiplep string qiliw
        data_check_str = "\n".join([f"{k}={v}" for k, v in sorted(parsed_data.items())])

        # 4. secret key jasaw
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()

        # 5. expected hash (Telegram boliwi kerek bolgan)
        expected_hash = hmac.new(
            key=secret_key,
            msg = data_check_str.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(received_hash, expected_hash):
            raise ValueError("❌ init_data verification failed")
        
        # 6. user mag'liwmatlarin json qilib qaytariw
        return {
            "user": json.loads(parsed_data["user"])
        }

    except Exception as e:
        print("❌ Exception:", e)
        return None


