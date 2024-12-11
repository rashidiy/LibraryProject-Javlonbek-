# LibraryProject
Django Project
# Django Library Project

Ushbu loyiha Django yordamida yaratilgan kitoblar kutubxonasi boshqaruv tizimidir. Loyihada kitoblar, mualliflar, toifalar va foydalanuvchilar bilan bog'liq ma'lumotlarni saqlash va boshqarish uchun modellar qo'shildi.

## Asosiy Funksiyalar

1. **Admin Interface**:
   - Django admin interfeysi optimallashtirildi:
     - Modellar uchun maxsus oynalar yaratildi.
     - Fayllar uchun "image preview" funksiyasi qo'shildi.
     - Filtrlar va qidiruv maydonlari qo'shildi.

2. **Modellar**:
   - `Category`: Kitoblar toifalari haqida ma'lumot.
   - `Author`: Mualliflarning ma'lumotlarini boshqarish.
   - `Books`: Kitoblar bilan bog'liq barcha ma'lumotlar (narx, format, toifalar va boshqalar).
   - `Reviews`: Foydalanuvchilar tomonidan berilgan kitob sharhlari va baholari.

3. **Migration**:
   - Modellar database bilan muvaffaqiyatli integratsiya qilindi va migratsiya bajarildi.

## Loyiha O'rnatilishi

1. **Talablar**: Loyiha uchun kerakli Python kutubxonalarini o'rnatish uchun quyidagi buyruqdan foydalaning:

   ```bash
   pip install -r requirements.txt
   ```

2. **Migration Bajarish**: Loyihani database bilan ulash uchun quyidagi buyruqlarni ishga tushiring:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Superuser Yaratish**: Admin panelga kirish uchun superuser yarating:

   ```bash
   python manage.py createsuperuser
   ```

4. **Loyihani Ishga Tushirish**: Django serverni ishga tushiring:

   ```bash
   python manage.py runserver
   ```

## Foydalanilgan Modellar

Quyidagi modellar loyihada ishlatilgan:

### `Category` Modeli:
- **name**: Toifa nomi.
- **description**: Toifa haqida qisqacha ma'lumot.

### `Author` Modeli:
- **name**: Muallif nomi.
- **bio**: Muallifning qisqacha tarjimai holi.

### `Books` Modeli:
- **title**: Kitob nomi.
- **author**: Muallifga chet el kaliti bilan bog'langan.
- **price**: Kitob narxi.
- **category**: Ko'p-to-ko'p bog'lanish orqali toifalar.
- **availability**: Kitobning mavjud holati (In stock, Out of stock, va boshqalar).
- **format**: Kitob formati (Standard, Downloadable, External).
- **book_image**: Kitob rasmi.
- **book_pdf**: Kitobning PDF versiyasi.
- **published_date**: Nashr etilgan sana.
- **owner**: Kitob egasi (foydalanuvchi).
- **average_rating**: Kitobning o'rtacha bahosi (hisoblanadi).

### `Reviews` Modeli:
- **book**: Sharh berilgan kitobga chet el kaliti bilan bog'lanish.
- **user**: Sharhni qoldirgan foydalanuvchi.
- **text**: Sharh matni.
- **rating**: Baholash (1 dan 5 gacha).
- **created_at**: Sharh qo'shilgan vaqt.

## Qo'shimcha Ma'lumotlar

- **Media Fayllar**:
  - Kitoblar uchun rasmlar `images/` papkasida saqlanadi.
  - Kitoblarning PDF fayllari `books_pdf/` papkasida saqlanadi.

- **Validatsiyalar**:
  - Faqat quyidagi fayl turlari qabul qilinadi:
    - Rasmlar: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp`
    - Kitob fayllari: `.pdf`, `.epub`, `.docx`

## Muallif
Loyiha muallifi: [Javlonbek0205](https://github.com/Javlonbek0205)

**Loyiha bo'yicha qo'shimcha savollaringiz bo'lsa, GitHub orqali murojaat qiling!**
