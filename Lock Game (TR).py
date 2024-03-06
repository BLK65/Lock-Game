def oyun_alani_ciz(oyun_alani_kenar_parametre, oyun_alani_parametre):

    harfler = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("")
    print("   ", "   ".join(harfler[:oyun_alani_kenar_parametre]))

    for x in range(oyun_alani_kenar_parametre):
        print(" ", "-" * oyun_alani_kenar_parametre * 4, end="-\n")
        print(x+1, end="")
        for y in range(oyun_alani_kenar_parametre):
            print(" |", oyun_alani_parametre[x][y], end="")
        print(" |", x+1)
    print(" ", "-" * oyun_alani_kenar_parametre * 4, end="-\n")

    print("   ", "   ".join(harfler[:oyun_alani_kenar_parametre]))
    print("")


def oyunu_kazanma_sarti(oyun_alani_parametre, birinci_karakter_parametre, ikinci_karakter_parametre):

    kazanma_sarti = 0

    # Oyun alanındaki karakterleri sayarak birinci oyuncunun kazanıp kazanmadığını kontrol eder #
    if sum(x.count(ikinci_karakter_parametre) for x in oyun_alani_parametre) == 1:
        kazanma_sarti = 1

    # Oyun alanındaki karakterleri sayarak ikinci oyuncunun kazanıp kazanmadığını kontrol eder #
    if sum(x.count(birinci_karakter_parametre) for x in oyun_alani_parametre) == 1:
        kazanma_sarti = 2

    return kazanma_sarti


def hamle_yap(oyun_alani_parametre, mevcut_konum_hedef_konum, birinci_karakter_parametre, ikinci_karakter_parametre, hamle_sirasi):

    # Girdilerin index olarak kullanılabilmesi için dönüşümlerin yapıldığı kısım #
    mevcut_konum_satir = int(mevcut_konum_hedef_konum[0:1]) - 1
    mevcut_konum_sutun = mevcut_konum_hedef_konum[1:2]
    hedef_konum_satir = int(mevcut_konum_hedef_konum[3:4]) - 1
    hedef_konum_sutun = mevcut_konum_hedef_konum[4:5]

    sutun_koordinat = ["A", "B", "C", "D", "E", "F", "G", "H"]

    if mevcut_konum_sutun in sutun_koordinat:
        mevcut_konum_sutun = int(sutun_koordinat.index(mevcut_konum_sutun))

    if hedef_konum_sutun in sutun_koordinat:
        hedef_konum_sutun = int(sutun_koordinat.index(hedef_konum_sutun))

    # Mevcut konumu boş hücreye çevir #
    oyun_alani_parametre[mevcut_konum_satir][mevcut_konum_sutun] = " "

    # Hedef konumu oyuncu karakterine çevir #
    if hamle_sirasi == 1:
        oyun_alani_parametre[hedef_konum_satir][hedef_konum_sutun] = birinci_karakter_parametre
    if hamle_sirasi == 0:
        oyun_alani_parametre[hedef_konum_satir][hedef_konum_sutun] = ikinci_karakter_parametre


def hamle_gecerlimi(oyun_alani_kenar_parametre, oyun_alani_parametre, birinci_oyuncu_karakter, ikinci_oyuncu_karakter, hamle_sirasi):

    mevcut_konum_oyun_alaninda = False
    mevcut_konumda_dogru_tas = False
    hedef_konum_oyun_alaninda = False
    hedef_konum_bos = False
    arada_tas_yok = False
    hamle_duz_yol = False

    while (mevcut_konum_oyun_alaninda is False) or (mevcut_konumda_dogru_tas is False) or (hedef_konum_oyun_alaninda is False) or (hedef_konum_bos is False) or (arada_tas_yok is False) or (hamle_duz_yol is False):

        if hamle_sirasi == 1:
            mevcut_konum_hedef_konum = input("Oyuncu {}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ".format(birinci_oyuncu_karakter))
        if hamle_sirasi == 0:
            mevcut_konum_hedef_konum = input("Oyuncu {}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ".format(ikinci_oyuncu_karakter))

        # Girdinin 5 karakterden uzun olup olmadığını kontrol eder #
        if len(mevcut_konum_hedef_konum) > 5:
            continue

        # Girdinin ortasında boşluk karakteri olup olmadığını kontrol eder #
        if not mevcut_konum_hedef_konum[2] == " ":
            continue

        mevcut_konum_oyun_alaninda = False
        mevcut_konumda_dogru_tas = False
        hedef_konum_oyun_alaninda = False
        hedef_konum_bos = False
        arada_tas_yok = False
        hamle_duz_yol = False

        try:
            mevcut_konum_satir = int(mevcut_konum_hedef_konum[0:1]) - 1
            mevcut_konum_sutun = mevcut_konum_hedef_konum[1:2]
            hedef_konum_satir = int(mevcut_konum_hedef_konum[3:4]) - 1
            hedef_konum_sutun = mevcut_konum_hedef_konum[4:5]
        except ValueError:
            continue

        sutun_koordinat = ["A", "B", "C", "D", "E", "F", "G", "H"][:oyun_alani_kenar_parametre]

        if mevcut_konum_sutun in sutun_koordinat:
            mevcut_konum_sutun = int(sutun_koordinat.index(mevcut_konum_sutun))
        else:
            continue

        if hedef_konum_sutun in sutun_koordinat:
            hedef_konum_sutun = int(sutun_koordinat.index(hedef_konum_sutun))
        else:
            continue

        if mevcut_konum_satir > oyun_alani_kenar_parametre-1:
            continue

        if hedef_konum_satir > oyun_alani_kenar_parametre-1:
            continue

        # Seçilen mevcut konum oyun alanı içinde mi? #
        if mevcut_konum_satir > oyun_alani_kenar_parametre or mevcut_konum_satir < 0 or mevcut_konum_sutun > oyun_alani_kenar_parametre or mevcut_konum_sutun < 0:
            print("Seçilen mevcut konum oyun alanı içinde değil.")
        else:
            mevcut_konum_oyun_alaninda = True

        # Seçilen mevcut konumda senin taşın mı var? #
        if (hamle_sirasi == 1) and (oyun_alani_parametre[mevcut_konum_satir][mevcut_konum_sutun] == ikinci_oyuncu_karakter):
            print("Seçilen mevcut konumdaki taş rakibe ait.")
        elif (hamle_sirasi == 0) and (oyun_alani_parametre[mevcut_konum_satir][mevcut_konum_sutun] == birinci_oyuncu_karakter):
            print("Seçilen mevcut konumdaki taş rakibe ait.")
        elif (oyun_alani_parametre[mevcut_konum_satir][mevcut_konum_sutun]) == " ":
            print("Seçilen mevcut konum boş.")
        else:
            mevcut_konumda_dogru_tas = True

        # Seçilen hedef konum oyun alanı içinde mi? #
        if hedef_konum_satir > oyun_alani_kenar_parametre or hedef_konum_satir < 0 or hedef_konum_sutun > oyun_alani_kenar_parametre or hedef_konum_sutun < 0:
            print("Seçilen hedef konum oyun alanı içinde değil.")
        else:
            hedef_konum_oyun_alaninda = True

        # Seçilen hedef konumda başka taş var mı? #
        if not oyun_alani_parametre[hedef_konum_satir][hedef_konum_sutun] == " ":
            print("Seçilen hedef konumda başka bir taş var.")
        else:
            hedef_konum_bos = True

        # Mevcut konum ile hedef konum arasında taş var mı? #
        if mevcut_konum_satir == hedef_konum_satir and hedef_konum_sutun > mevcut_konum_sutun:      # 3A 3D vb olursa #
            any_tile_filled = False
            for i in range(mevcut_konum_sutun+1, hedef_konum_sutun):
                if oyun_alani_parametre[mevcut_konum_satir][i] == birinci_oyuncu_karakter or oyun_alani_parametre[mevcut_konum_satir][i] == ikinci_oyuncu_karakter:
                    print("Seçilen hedef konum ve mevcut konum arasında bir taş var.")
                    any_tile_filled = True
                    break
            if any_tile_filled is False:
                arada_tas_yok = True

        elif mevcut_konum_satir == hedef_konum_satir and hedef_konum_sutun < mevcut_konum_sutun:    # 3D 3A vb olursa #
            any_tile_filled = False
            for i in range(mevcut_konum_sutun-1, hedef_konum_sutun, -1):
                if oyun_alani_parametre[mevcut_konum_satir][i] == birinci_oyuncu_karakter or oyun_alani_parametre[mevcut_konum_satir][i] == ikinci_oyuncu_karakter:
                    print("Seçilen hedef konum ve mevcut konum arasında bir taş var.")
                    any_tile_filled = True
                    break
            if any_tile_filled is False:
                arada_tas_yok = True

        elif mevcut_konum_sutun == hedef_konum_sutun and hedef_konum_satir > mevcut_konum_satir:    # 1A 4A vb olursa #
            any_tile_filled = False
            for i in range(mevcut_konum_satir+1, hedef_konum_satir):
                if oyun_alani_parametre[i][mevcut_konum_sutun] == birinci_oyuncu_karakter or oyun_alani_parametre[i][mevcut_konum_sutun] == ikinci_oyuncu_karakter:
                    print("Seçilen hedef konum ve mevcut konum arasında bir taş var.")
                    any_tile_filled = True
                    break
            if any_tile_filled is False:
                arada_tas_yok = True

        elif mevcut_konum_sutun == hedef_konum_sutun and hedef_konum_satir < mevcut_konum_satir:    # 4A 1A vb olursa #
            any_tile_filled = False
            for i in range(mevcut_konum_satir-1, hedef_konum_satir, -1):
                if oyun_alani_parametre[i][mevcut_konum_sutun] == birinci_oyuncu_karakter or oyun_alani_parametre[i][mevcut_konum_sutun] == ikinci_oyuncu_karakter:
                    print("Seçilen hedef konum ve mevcut konum arasında bir taş var.")
                    any_tile_filled = True
                    break
            if any_tile_filled is False:
                arada_tas_yok = True

        # Yapılan hamlede taşlar düz mü gidiyor? #
        if mevcut_konum_satir == hedef_konum_satir or mevcut_konum_sutun == hedef_konum_sutun:
            hamle_duz_yol = True
        else:
            print("Taşlar sadece düz gidebilir.")

        if (mevcut_konum_oyun_alaninda is True) and (mevcut_konumda_dogru_tas is True) and (hedef_konum_oyun_alaninda is True) and (hedef_konum_bos is True) and (arada_tas_yok is True) and (hamle_duz_yol is True):
            hamle_yap(oyun_alani_parametre, mevcut_konum_hedef_konum, birinci_oyuncu_karakter, ikinci_oyuncu_karakter, hamle_sirasi)
            break


def kilitlenen_tas_varmi(oyun_alani_parametre, birinci_karakter_parametre, ikinci_karakter_parametre, hamle_sirasi):

    harfler = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # Birinci oyuncunun sırasında #
    if hamle_sirasi == 1:
        for satir in range(len(oyun_alani_parametre)):
            for sutun in range(len(oyun_alani_parametre)):

                # Üstten ve alttan kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir-1][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir+1][sutun] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş üst ve alttan kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    continue

                # Soldan ve sağdan kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun-1] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun+1] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol ve sağdan kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    continue

                # Sol üst köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and satir - 1 < 0 and sutun - 1 < 0 and oyun_alani_parametre[satir+1][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun+1] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol üst köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sol üst köşede kilitlendi ve dışarı çıkarıldı.")

                # Sağ üst köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and satir - 1 < 0 and sutun + 1 >= len(oyun_alani_parametre) and oyun_alani_parametre[satir+1][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun-1] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sağ üst köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sağ üst köşede kilitlendi ve dışarı çıkarıldı.")

                # Sol alt köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and satir + 1 >= len(oyun_alani_parametre) and sutun - 1 < 0 and oyun_alani_parametre[satir-1][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun+1] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol alt köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sol alt köşede kilitlendi ve dışarı çıkarıldı.")

                # Sağ alt köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == ikinci_karakter_parametre and satir + 1 >= len(oyun_alani_parametre) and sutun + 1 >= len(oyun_alani_parametre) and oyun_alani_parametre[satir-1][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun-1] == birinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sağ alt köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sağ alt köşede kilitlendi ve dışarı çıkarıldı.")

    # İkinci oyuncunun sırasında #
    if hamle_sirasi == 0:
        for satir in range(len(oyun_alani_parametre)):
            for sutun in range(len(oyun_alani_parametre)):

                # Üstten ve alttan kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir - 1][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir + 1][sutun] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş üst ve alttan kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    continue

                # Soldan ve sağdan kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and oyun_alani_parametre[satir][sutun - 1] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun + 1] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol ve sağdan kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    continue

                # Sol üst köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and satir - 1 < 0 and sutun - 1 < 0 and oyun_alani_parametre[satir + 1][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun + 1] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol üst köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sol üst köşede kilitlendi ve dışarı çıkarıldı.")

                # Sağ üst köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and satir - 1 < 0 and sutun + 1 >= len(oyun_alani_parametre) and oyun_alani_parametre[satir + 1][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun - 1] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sağ üst köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sağ üst köşede kilitlendi ve dışarı çıkarıldı.")

                # Sol alt köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and satir + 1 >= len(oyun_alani_parametre) and sutun - 1 < 0 and oyun_alani_parametre[satir - 1][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun + 1] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sol alt köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sol alt köşede kilitlendi ve dışarı çıkarıldı.")

                # Sağ alt köşede kilitlenen taşlar #
                try:
                    if oyun_alani_parametre[satir][sutun] == birinci_karakter_parametre and satir + 1 >= len(oyun_alani_parametre) and sutun + 1 >= len(oyun_alani_parametre) and oyun_alani_parametre[satir - 1][sutun] == ikinci_karakter_parametre and oyun_alani_parametre[satir][sutun - 1] == ikinci_karakter_parametre:
                        oyun_alani_parametre[satir][sutun] = " "
                        print(satir+1, harfler[sutun], " konumundaki taş sağ alt köşede kilitlendi ve dışarı çıkarıldı.")
                except IndexError:
                    oyun_alani_parametre[satir][sutun] = " "
                    print(satir + 1, harfler[sutun], " konumundaki taş sağ alt köşede kilitlendi ve dışarı çıkarıldı.")


def main():

    while True:
        birinci_karakter = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")
        if len(birinci_karakter) > 1:
            print("Oyun alanının düzgün yazdırılabilmesi için lütfen tek bir karakter giriniz.")
        else:
            break

    while True:
        ikinci_karakter = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")
        if len(ikinci_karakter) > 1:
            print("Oyun alanının düzgün yazdırılabilmesi için lütfen tek bir karakter giriniz.")
        else:
            break

    while True:
        try:
            oyun_alani_kenar = int(input("Oyun alanının satır/sütun sayısını giriniz [4-8]: "))
            while oyun_alani_kenar > 8 or oyun_alani_kenar < 4:
                oyun_alani_kenar = int(input("Satır/sütun sayısı [4-8] aralığında olmalıdır, lütfen tekrar giriniz: "))
            break
        except ValueError:
            continue

    oyun_alani = []

    for i in range(oyun_alani_kenar):
        liste = [" "] * oyun_alani_kenar
        oyun_alani.append(liste)

    # Mod alındıktan sonra çıkan değer 1 ise birinci oyuncunun sırası, 0 ise ikinci oyuncunun sırasıdır #
    hamle_no = 1
    hamle_sirasi = hamle_no % 2

    # Oyun alanındaki ilk taşları yerleştirir #
    for i in range(oyun_alani_kenar):
        oyun_alani[0][i] = ikinci_karakter
        oyun_alani[-1][i] = birinci_karakter

    oyun_alani_ciz(oyun_alani_kenar, oyun_alani)

    hamle_gecerlimi(oyun_alani_kenar, oyun_alani, birinci_karakter, ikinci_karakter, hamle_sirasi)

    kilitlenen_tas_varmi(oyun_alani, birinci_karakter, ikinci_karakter, hamle_sirasi)

    oyun_alani_ciz(oyun_alani_kenar, oyun_alani)

    hamle_no += 1

    kazanma_sarti = oyunu_kazanma_sarti(oyun_alani, birinci_karakter, ikinci_karakter)

    while kazanma_sarti == 0:

        # Mod alındıktan sonra çıkan değer 1 ise birinci oyuncunun sırası, 0 ise ikinci oyuncunun sırasıdır #
        hamle_sirasi = hamle_no % 2

        hamle_gecerlimi(oyun_alani_kenar, oyun_alani, birinci_karakter, ikinci_karakter, hamle_sirasi)

        kilitlenen_tas_varmi(oyun_alani, birinci_karakter, ikinci_karakter, hamle_sirasi)

        oyun_alani_ciz(oyun_alani_kenar, oyun_alani)

        hamle_no += 1

        kazanma_sarti = oyunu_kazanma_sarti(oyun_alani, birinci_karakter, ikinci_karakter)

    else:

        if kazanma_sarti == 1:
            print("Oyuncu", birinci_karakter, ", oyunu kazandı.")

        if kazanma_sarti == 2:
            print("Oyuncu", ikinci_karakter, ", oyunu kazandı.")

    tekrar_oyna = input("Tekrar oynamak ister misiniz(E/H): ")
    while tekrar_oyna not in ["E", "H"]:
        tekrar_oyna = input("Hatalı giriş, lütfen tekrar giriniz(E/H): ")
    if tekrar_oyna == "E":
        main()
    else:
        print("Program sonlandırıldı.")


main()
