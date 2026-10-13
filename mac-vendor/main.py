

def load_oui_table(filename="mac-vendor.txt"):
    oui = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            prefix = line[:6].upper()
            vendor = line[6:].strip()
            if len(prefix) == 6 and vendor:
                oui[prefix] = vendor
    return oui


def normalize_mac(mac: str) -> str:
    return "".join(ch for ch in mac if ch.isalnum()).upper()


def main():
    oui_table = load_oui_table()

    mac_input = input("Введите MAC-адрес (например, F0-79-59-70-A7-20): ")
    mac_clean = normalize_mac(mac_input)

    if len(mac_clean) < 6:
        print("Ошибка: MAC-адрес слишком короткий.")
        return

    prefix = mac_clean[:6]

    vendor = oui_table.get(prefix)
    if vendor:
        print(f"Производитель: {vendor}")
    else:
        print("Производитель не найден в базе OUI.")


if __name__ == "__main__":
    main()
