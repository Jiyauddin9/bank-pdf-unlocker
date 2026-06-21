import pikepdf
from tqdm import tqdm
from datetime import datetime


def try_password(pdf_path, password):
    try:
        with pikepdf.open(pdf_path, password=password):
            print(f"\n\n🎉 SUCCESS! Password found: {password}")
            return True
    except pikepdf.PasswordError:
        return False
    except Exception:
        return False


def generate_dates_and_years(start_year=1970, end_year=2015):
    """
    DDMM aur YYYY
    """
    ddmm_list = []
    years = [str(y) for y in range(start_year, end_year + 1)]

    # Valid DDMM generate
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                datetime(2024, month, day)
                ddmm_list.append(f"{day:02d}{month:02d}")
            except ValueError:
                continue

    return ddmm_list, years


def generate_name_prefixes(possible_names):
    """
    Names
    """
    prefixes = set()
    for name in possible_names:
        # Spaces
        cleaned = name.strip().replace(" ", "").upper()
        if not cleaned:
            continue

        # 4 letters
        if len(cleaned) >= 4:
            prefixes.add(cleaned[:4])

        if len(cleaned) >= 5:
            prefixes.add(cleaned[:5])

        prefixes.add(cleaned)

    return list(prefixes)


def crack_bank_pdf(pdf_path, name_guesses, start_year=1970, end_year=2015):
    print("🔄 Dates aur Years generate ho rahe hain...")
    ddmm_list, year_list = generate_dates_and_years(start_year, end_year)

    print("🔄 Name prefixes extract ho rahe hain...")
    prefixes = generate_name_prefixes(name_guesses)

    print(f"📋 Testing Prefixes: {prefixes}")
    print(f"📅 Testing Years: {start_year} se {end_year} tak")


    combinations_to_try = []

    for prefix in prefixes:

        for ddmm in ddmm_list:
            combinations_to_try.append(f"{prefix}{ddmm}")


        for year in year_list:
            combinations_to_try.append(f"{prefix}{year}")


        for ddmm in ddmm_list:
            for year in year_list:

                pass

    print(f"🚀 Total {len(combinations_to_try)} combinations check karne ja rahe hain...")


    for pwd in tqdm(combinations_to_try, desc="Trying Fast Formats"):
        if try_password(pdf_path, pwd):
            return True


    print("\n⚠️ Pehle formats me nahi mila. Ab Full DOB (PREFIX + DDMMYYYY) try kar rahe hain...")


    total_heavy = len(prefixes) * len(ddmm_list) * len(year_list)
    pbar = tqdm(total=total_heavy, desc="Trying Full DOB Formats")

    for prefix in prefixes:
        for ddmm in ddmm_list:
            for year in year_list:
                pwd = f"{prefix}{ddmm}{year}"
                pbar.update(1)
                if try_password(pdf_path, pwd):
                    pbar.close()
                    return True

    pbar.close()
    print("❌ Password nahi mila. Ek baar bank ka password format confirm kijiye.")
    return False


if __name__ == "__main__":
    # Apni PDF ka sahi path yahan daalo
    pdf_file = r"C:\Users\Hp\Desktop\New folder\GPAI.pdf"

    # Yahan sirf aam taur par use hone wale naam ke hisse daalo
    name_guesses = [
        "rohit",
        "pawan kumar",
        "raj"
    ]


    start_birth_year = 1990
    end_birth_year = 2000

    crack_bank_pdf(pdf_file, name_guesses, start_birth_year, end_birth_year)