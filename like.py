# -*- koding: utf8 -*-

impor log

dari selenium impor webdriver
dari selenium.webdriver.common.by import By
dari selenium.webdriver.common.keys mengimpor Kunci Key
dari selenium.webdriver.support.ui impor WebDriverWait
dari selenium.webdriver.support.expected_conditions import element_to_be_clickable
dari Selenium.webdriver.chrome.options impor Opsi
dari Selenium.webdriver impor ActionChains
dari Selenium.webdriver.support impor expected_conditions sebagai EC
dari Selenium.common.exceptions impor TimeoutException, WebDriverException, ElementClickInterceptedException, NoSuchElementException

waktu impor
impor acak
waktu impor
impor configparser

impor file temp
impor os
waktu impor
permintaan impor # dapatkan versi pembaruan

impor tkinter sebagai tk # windows
impor argparse # baris perintah


log_filename = f'fb_log\\facebook_select_en-{datetime.datetime.now().strftime("%d-%m-%Y")}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, filemode='a', format=' %(asctime)s: %(name)s - %(levelname)s - %(message)s')
cetak(log_namafile)
logging.info("============================================ ==================")
logging.info("Mulai bot")



# dapatkan ini
mencoba:
    config = configparser.ConfigParser()
    config.read('settings_en.ini')
    versi = config.get("Pengaturan", "versi")
    chrome_user = config.get("Setelan", "chrome_user")
    lebar_set = int(config.get("Pengaturan", "lebar"))
    height_set = int(config.get("Pengaturan", "tinggi"))
    cerita_set = int(config.get("Pengaturan", "cerita"))
    birthday_set = int(config.get("Pengaturan", "ulang tahun"))
    feed_set = int(config.get("Pengaturan", "umpan"))
    feed_select = int(config.get("Pengaturan", "feed_select"))

    
    cerita_set_akhir = kumpulan cerita - 1
kecuali Pengecualian sebagai e:
    logging.exception("Kesalahan memuat INI")
    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan memuat INI")

# dapatkan versi baru
r_versi = 0
pembaruan_versi = 0
mencoba:
    r_version = request.get('https://skobeev.design/fb/version.txt')
    r_version.encoding = 'utf-8' 
    upd_version = r_version.text
    logging.info(f"Versi saat ini: {version}")
    jika upd_version == versi:
        print(f"Versi saat ini: {versi}")
    lain:
        print(f"Versi Terakhir: {upd_version}")
kecuali Pengecualian sebagai e:
    upd_version = "Tidak tersedia"
    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan dapatkan versi.")
    logging.exception('Kesalahan mendapatkan versi')


pengemudi = 0
ukuran = 0
posisi = 0


def start_browser():
    pengemudi global
    ukuran global
    posisi global
    
    # Opsi Chrome
    opsi = webdriver.ChromeOptions() 
    options.add_argument("disable-infobars")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', Salah)
    options.add_argument(f"user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Google\\Chrome\\User Data\\{chrome_user}")

    mencoba:
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Buat jendela browser...")
        driver = webdriver.Chrome(options=options)
    kecuali WebDriverException:
        logging.exception("Katalog TEMP error")
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan katalog TEMP\n{tempfile.gettempdir()}" )
        mencoba:
            jika os.path.exists(tempfile.gettempdir()) == Salah:
                logging.warning("Direktori tidak ditemukan. Kami membuat yang baru.\n{tempfile.gettempdir()}")
                os.mkdir(tempfile.gettempdir())
        kecuali Pengecualian sebagai e:
            logging.exception("Kesalahan membuat katalog TEMP")
            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan membuat katalog TEMP\n{tempfile.gettempdir()} ")
    kecuali Pengecualian sebagai e:
        logging.exception('Kesalahan Buat jendela browser')

        
    # browser topeng
    driver.execute_cdp_cmd("Halaman.addScriptToEvaluateOnNewDocument", {
        "sumber": """
        Object.defineProperty(navigator, 'webdriver', {
        dapatkan: () => tidak terdefinisi
        })
        """
        })

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})
    
    driver.set_window_rect(10,10, lebar_set, tinggi_set)
    driver.get("https://facebook.com/")
    waktu.tidur(3)
    
    ukuran = driver.get_window_size()
    posisi = driver.get_window_position()
    print(f"Ukuran jendela: lebar = {size['width']}px, tinggi = {size['height']}px, x = {position['x']}, y = {position['y' ]}")
    logging.info(f"Ukuran jendela: lebar = {size['width']}px, tinggi = {size['height']}px, x = {position['x']}, y = {position[' y']}")
    print(driver.capabilities['browserVersion'])
    logging.info(driver.capabilities['browserVersion'])
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    waktu.tidur(1)
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    ActionChains(driver).reset_actions()
    logging.info("Buat jendela browser.")
    
    mencoba:
        #Tutup tab
        driver.implicitly_wait(7)
        count_close = driver.find_elements_by_css_selector('[aria-label="Tutup tab"]')
        print(f'Tutup tab: {len(count_close)}')
        untuk send_close di count_close:
            kirim_tutup.klik()
            waktu.tidur(5)
            mencoba:
                driver.find_element_by_css_selector('[aria-label="ОК"]').click()
                waktu.tidur(5)
            kecuali Pengecualian sebagai e:
                logging.debug(e)
    kecuali Pengecualian sebagai e:
        logging.debug(e)

#------------------------------------------------- ----------
def start_birthday_fb():
    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Mulai fungsi ucapan selamat ulang tahun...")

    start_browser()
    logging.info('Mulai fungsi ucapan selamat ulang tahun')
    
    waktu.tidur(10)
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10) # detik
    waktu.tidur(10)
    tunggu = WebDriverTunggu(driver, 10)
    WebDriverTunggu(pengemudi, 10)

    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    waktu.tidur(2)
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    waktu.tidur(2)
    ActionChains(driver).send_keys(Keys.HOME).perform()
    waktu.tidur(random.randrange(15,20))
    
    mencoba:
        driver.find_element_by_css_selector("[href='/events/birthdays/']").click()
        waktu.tidur(random.randrange(15,20))
    kecuali Pengecualian sebagai e:
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol ulang tahun tidak ditemukan.\n{e}")
        logging.warning(f"Tombol ulang tahun tidak ditemukan.\n{e}")
    lain:
        mencoba:
            ulang tahun_pesan()
        kecuali Pengecualian sebagai e:
            driver.berhenti()
            logging.debug(e)

# fungsi ulang tahun
def birthday_message():
    driver.implicitly_wait(40) # detik
    waktu.tidur(random.randrange(18,27))

    mencoba:
        dengan open("birthday_en.txt", "r", encoding="utf-8") sebagai f:
            ulang tahun = f.readlines()
            
            count_post = driver.find_elements_by_css_selector("[method='POST']")
            len_count = len(count_post)-1
            print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Bidang yang ditemukan: {len_count}")
            
            logging.info(f'Ditemukan bidang: {len_count}')
            num_msg = 0 # penghitung pesan terkirim
            
            untuk send_msg dalam range(0, len_count):
                jika len_count <= 0:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tidak ada bidang yang ditemukan : {num_msg}")
                    logging.info(f'Tidak ada bidang yang ditemukan : {num_msg}')
                    istirahat
                elif send_msg >= ulang tahun_set:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Selamat batas : {num_msg}")
                    logging.info(f'Congratulations limit : {num_msg}')
                    istirahat

                untuk cv dalam kisaran (0,13):
                    ActionChains(driver).send_keys(Keys.TAB).perform()
                    elemen = driver.switch_to.active_element
                    driver.implicitly_wait(1)
                    mencoba:
                        if element.find_element_by_tag_name('br').get_attribute('data-text') == 'true':
                            mencoba:
                                cmess = driver.find_elements_by_css_selector('[method="POST"]')
                                cmess[0].location_once_scrolled_into_view
                                txt = str(pilihan acak(ulang tahun).ganti("\n", ""))
                                ActionChains(driver).send_keys_to_element(elemen, txt, Keys.ENTER).perform()
                                
                                num_msg = num_msg + 1
                                waktu.tidur(random.randrange(5,10))
                                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Selamat : {num_msg}")
                                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Teks: {txt}")
                                ActionChains(driver).reset_actions()
                                istirahat
                            
                            kecuali NoSuchElementException sebagai e:
                                cetak (e)
                                logging.info(e)
                            kecuali Pengecualian sebagai e:
                                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan dalam siklus pengiriman ucapan selamat. Selamat : {num_msg} .\n{e}")
                                logging.exception(f"Kesalahan dalam siklus pengiriman ucapan selamat. Selamat : {send_msg}.\n{e}")
                                istirahat
                    
                    kecuali Pengecualian sebagai e:
                        logging.debug(e)
                        waktu.tidur(random.randrange(5,10))
                    
            logging.info(f'Pesan terkirim: {num_msg} dari {len_count}')
            print (f"\n\nPesan terkirim: {num_msg} dari {len_count}")
            print (f"\n\n{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Menunggu...\n")
            f.tutup()
            mencoba:
                driver.berhenti()
            kecuali Pengecualian sebagai e:
                logging.debug(e)

    kecuali Pengecualian sebagai e:
        logging.exception("Pesan eror terkirim.")
        mencoba:
            driver.berhenti()
        kecuali Pengecualian sebagai e:
            logging.debug(e)


#------------------------------------------------- ----------
def start_story_fb():
    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> MULAI Cerita seperti fungsi...")
    start_browser() # оздаем окно
    logging.info('MULAI Cerita seperti fungsi.')
    
    driver.get("https://www.facebook.com/")
    
    driver.implicitly_wait(60) # detik
    waktu.tidur(10)
    tunggu = WebDriverTunggu(driver, 60)
    
    waktu.tidur(random.randrange(15,20))
    mencoba:
        driver.find_element_by_css_selector("[aria-label='Lihat semua cerita']").click()
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol Lihat semua cerita DITEMUKAN.")
        logging.info("Tombol Lihat semua cerita DITEMUKAN.")
        waktu.tidur(15)

        cerita_suka()


    kecuali Pengecualian sebagai e:
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol Lihat semua cerita TIDAK DITEMUKAN.\n{e}" )
        logging.exception("Tombol Lihat semua cerita TIDAK DITEMUKAN.")
        driver.berhenti()

def story_likes():
 
    count_like = 0
    count_super = 0
    hitung_berikutnya = 0
    hitung_bersama = 0
    hitung_skip = 0
    
    next_refrash = 0
    tunggu = WebDriverTunggu(driver, 30)
    driver.implicitly_wait(5) # detik

    ActionChains(driver).send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.RETURN).perform()
    waktu.tidur(random.randrange(4,8))

    coba: # Suara mati
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Mute"]'))).click()
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Bisu")
    kecuali Pengecualian sebagai e:
        print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Error Mute... \n{e}")
        logging.info("Kesalahan Bisukan...\n{e}")
        
    mencoba:
        untuk cerita dalam rentang (0, story_set):
            tunggu = WebDriverTunggu(driver, 3)
            rnd_like = random.randrange(1,9)
            jika rnd_like == 1:
                # satu klik suka
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="1"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol SEPERTI tidak ditemukan.\n{e}")
                    logging.info(f'tombol Suka tidak ditemukan\n{e}')
                lain:
                    count_like = count_like + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Suka...")
                
            elif rnd_like == 2:
                # satu klik cinta
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="2"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol cinta tidak ditemukan.\n{e}")
                    logging.info(f"Tombol cinta tidak ditemukan.\n{e}")
                lain:
                    count_super = count_super + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Love...")
            
            elif rnd_like == 3:
                # generator suka
                untuk mkmk dalam range (0,random.randrange(2,5)):
                    mencoba:
                        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="1"]'))).click()
                    kecuali Pengecualian sebagai e:
                        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol SEPERTI tidak ditemukan.\n{e}")
                        logging.info(f'tombol Suka tidak ditemukan\n{e}')
                    lain:
                        count_like = count_like + 1
                        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Suka...")

            elif rnd_like == 4:
                #generator super
                untuk mkmk dalam range(0, random.randrange(2,5)):
                    mencoba:
                        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="2"]'))).click()
                    kecuali Pengecualian sebagai e:
                        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol cinta tidak ditemukan.\n{e}")
                        logging.info(f"Tombol cinta tidak ditemukan.\n{e}")
                    lain:
                        waktu.tidur(random.randrange(0,3))
                        count_super = count_super + 1
                        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Love...")
            
            elif rnd_like == 5:
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="1"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol SEPERTI tidak ditemukan.\n{e}")
                    logging.info(f'tombol Suka tidak ditemukan\n{e}')
                lain:
                    count_like = count_like + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Suka...")
                    waktu.tidur(random.randrange(1,4))
                
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="2"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol cinta tidak ditemukan.\n{e}")
                    logging.info(f"Tombol cinta tidak ditemukan.\n{e}")
                lain:
                    count_super = count_super + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Love...")
            
            elif rnd_like == 6:
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="2"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol cinta tidak ditemukan.\n{e}")
                    logging.info(f"Tombol cinta tidak ditemukan.\n{e}")
                lain:
                    count_super = count_super + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Love...")
                    waktu.tidur(random.randrange(1,4))
                

                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="1"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol SEPERTI tidak ditemukan.\n{e}")
                    logging.info(f'tombol Suka tidak ditemukan\n{e}')
                lain:
                    count_like = count_like + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Suka...")
            
            elif rnd_like == 7:
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="1"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol SEPERTI tidak ditemukan.\n{e}")
                    logging.info(f'tombol Suka tidak ditemukan\n{e}')
                lain:
                    count_like = count_like + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Suka...")
                    waktu.tidur(random.randrange(1,4))
                
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="2"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol cinta tidak ditemukan.\n{e}")
                    logging.info(f"Tombol cinta tidak ditemukan.\n{e}")
                lain:
                    count_super = count_super + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Love...")
                    waktu.tidur(random.randrange(0,3))
                
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="16"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol Peduli tidak ditemukan.\n{e}")
                    logging.info(f"Tombol Peduli tidak ditemukan.\n{e}")
                lain:
                    hitung_bersama = hitung_bersama + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Peduli...")
                    waktu.tidur(random.randrange(1,4))
                
                
            elif rnd_like == 8:
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-reaction="16"]'))).click()
                kecuali Pengecualian sebagai e:
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tombol Peduli tidak ditemukan.")
                    logging.info(f"Tombol Peduli tidak ditemukan.\n{e}")
                lain:
                    hitung_bersama = hitung_bersama + 1
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Peduli..")
            
            # LANJUT
            mencoba:
                tunggu = WebDriverTunggu(driver, 0)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Next Bucket Button']"))).click()
                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} Tombol Bucket Berikutnya")
                waktu.tidur(random.randrange(1,2))
                next_refrash = 0 # hapus kesalahan penghitungan
            kecuali Pengecualian sebagai e:
                mencoba:
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Next Card Button']"))).click()
                    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} Tombol Kartu Berikutnya")
                    waktu.tidur(random.randrange(1,2))
                    next_refrash = 0 # hapus kesalahan penghitungan
                kecuali Pengecualian sebagai e:
                    mencoba:
                        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Next bucket button']"))).click()
                        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} Tombol ember berikutnya")
                        waktu.tidur(random.randrange(1,2))
                        next_refrash = 0 # hapus kesalahan penghitungan
                    kecuali Pengecualian sebagai e:
                        mencoba:
                            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Next card button']"))).click()
                            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} Tombol kartu berikutnya")
                            waktu.tidur(random.randrange(1,2))
                            next_refrash = 0 # hapus kesalahan penghitungan
                        kecuali Pengecualian sebagai e:
                            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tidak ditemukan tombol NEXT. Segarkan...")
                            logging.warning("Tidak ditemukan tombol NEXT. Segarkan..\n{e}")
                            
                            next_refrash = next_refrash + 1
                            
                            if next_refrash == 3: # jika kesalahan berulang tidak ada tombol NEXT - keluar 
                                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Tidak ditemukan tombol NEXT. Keluar...")
                                logging.info("Tidak ditemukan tombol NEXT. Keluar.")
                                driver.berhenti()
                                istirahat
                            
                            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Segarkan...")
                            driver.refresh()
                            waktu.tidur(random.randrange(10,15))
                            ActionChains(driver).send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.RETURN).perform()
                            waktu.tidur(random.randrange(4,8))
                            coba: # Bisukan
                                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Mute"]'))).click()
                                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Bisu")
                            kecuali Pengecualian sebagai e:
                                print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Error Mute... \n{e}")
                                logging.info("Kesalahan bisu...\n{e}")
                            waktu.tidur(random.randrange(2,4))
                            logging.info('Refresh browser. Tidak ada tombol NEXT')
                    
            
            hitung_berikutnya = hitung_berikutnya + 1
            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Cerita selanjutnya...")
            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} dari {stories_set_end} ...\n ")
            waktu.tidur(random.randrange(2,4))
            
            jika story_set_end == cerita:
                print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {stories} - Bagus")
                logging.info(f"Кол-во: {stories} - Bagus.")
                
                driver.berhenti()
                print (f"\n\nSuka: {count_like}\nSuka: {count_super}\nPeduli: {count_together}\nBerikutnya: {count_next}\nSemua: {cerita + 1}")
                print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Menunggu...\n")
                
    kecuali Pengecualian sebagai e:
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Kesalahan {e}")
        logging.exception("Error menyukai cerita")
        driver.berhenti()


#------------------------------------------------- ----------
# ачала айков енте
def start_feed_likes():
    logging.info("MULAI fungsi seperti umpan berita.")
    print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> MULAI fungsi seperti umpan berita...")
    
    start_browser()

    jika feed_select == 0:
        driver.get("https://www.facebook.com/")
    lain:
        driver.get("https://www.facebook.com/?sk=h_chr")
        
    waktu.tidur(random.randrange(10,15))
    feed_likes()

# овная айков
def feed_likes():
    err_like = 0
    count_like = 0
    count_super = 0
    hitung_bersama = 0
    hitung_pilih = 0
    
    untuk x_all dalam rentang (0, feed_set):
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        waktu.tidur(random.randrange(1,3))
        
        
        coba: # jika server lambat memori 1GB (free amason micro) error: "Memori habis"
            driver.find_element_by_tag_name('div')
        kecuali Pengecualian:
            driver.refresh()
            logging.info('Memori habis')
            waktu.tidur(random.randrange(15,20))

        ActionChains(driver).send_keys("j").perform()
        waktu.tidur(random.randrange(6,10))
        ActionChains(driver).send_keys("l").perform()
        ActionChains(driver).reset_actions()
        waktu.tidur(random.randrange(7,10))

        rnd_like_feed = random.randrange(1,4)
        jika rnd_like_feed == 1:
            ActionChains(driver).send_keys(Keys.SPACE).perform()
            count_like = count_like + 1
            print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Suka: {count_like}")

        elif rnd_like_feed == 2:
            ActionChains(driver).send_keys(Keys.TAB).perform()
            waktu.tidur(random.randrange(2,4))
            ActionChains(driver).send_keys(Keys.SPACE).perform()
            count_super = count_super + 1
            print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Cinta: {count_super}")

            
        elif rnd_like_feed == 3:
            ActionChains(driver).send_keys(Keys.TAB + Keys.TAB).perform()
            waktu.tidur(random.randrange(2,4))
            ActionChains(driver).send_keys(Keys.SPACE).perform()
            hitung_bersama = hitung_bersama + 1
            print (f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Peduli: {count_together}")
                    
        print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> {x_all} dari {feed_set - 1}\n")
        ActionChains(driver).reset_actions()
            
        waktu.tidur(random.randrange(1,5))
        
        
        jika x_all == feed_set - 1:
            print(f"{datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')} >> Bagus.")
            print(f"\Suka: {count_like}\Cinta: {count_super}\nPeduli: {count_together}\n{x_all} dari {feed_set - 1}")
            logging.info("Bagus")
            driver.berhenti()
        
        waktu.tidur(random.randrange(1,5))

#buka ini
def open_file():
    dengan open('settings_en.ini', "r") sebagai input_file:
        teks = input_file.read()
        txt_edit.insert(tk.END, teks)
    window.title(f"Facebook autoclicker")

# simpan ini
def save_file():
    dengan open('settings_en.ini', "w") sebagai output_file:
        teks = txt_edit.get(1.0, tk.END)
        output_file.tulis(teks)


jendela = tk.Tk()
window.title("facebook-auto-liker-bot")
window.rowconfigure(0, minsize=500, berat=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Teks(jendela)
fr_buttons = tk.Frame(jendela, relief=tk.RAISED)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, teks="Simpan", perintah=save_file)

button1 = tk.Button(fr_buttons, text="Suka cerita", bg="biru", fg="kuning", command=start_stories_fb)
button2 = tk.Button(fr_buttons, text="News feed", bg="orange", fg="blue", command=start_feed_likes)
button3 = tk.Button(fr_buttons, teks="Ulang Tahun", bg="ungu", fg="putih", perintah=start_birthday_fb)

label1 = tk.Label(fr_buttons, text=f"Setelan\n")
label2 = tk.Label(fr_buttons, teks=f"\nFungsi\n")
label3 = tk.Label(fr_buttons, text=f"\n\nVersi saat ini: {version}\nVersi terakhir: {upd_version}")
label4 = tk.Label(fr_buttons, text=f"\n\ndisclaimer: harap dicatat bahwa ini\nadalah proyek penelitian. saya sama sekali tidak\nbertanggung jawab atas penggunaan\nalat ini. gunakan atas nama Anda sendiri. i Saya juga tidak bertanggung jawab jika\nakun Anda diblokir karena\penggunaan alat ini secara berlebihan..")

site_link = tk.Entry(fr_buttons)
label1.grid(baris=0, kolom=0)
btn_open.grid(row=1, column=0, sticky="ew")
btn_save.grid(baris=2, kolom=0, sticky="ew")

label2.grid(baris=3, kolom=0)
fr_buttons.grid(baris=0, kolom=0, sticky="ns")
txt_edit.grid(baris=0, kolom=1, sticky="nsew")

button1.grid(baris=4, kolom=0)
button2.grid(baris=5, kolom=0)
button3.grid(baris=6, kolom=0)
label3.grid(baris=7, kolom=0)
site_link.grid(baris=8, kolom=0)
site_link.insert(0,'https://github.com/doevent/facebook-auto-liker')
label4.grid(baris=9, kolom=0)


jika __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument ('nama', nargs='?')
    namespace = parser.parse_args()

    # апуск омандной оки
    jika namespace.name == 'cerita':
        mulai_cerita_fb()
    elif namespace.name == 'feed':
        start_feed_likes()
    elif namespace.name == 'ulang tahun':
        mulai_ulang tahun_fb()
    lain:
        jendela.mainloop()
