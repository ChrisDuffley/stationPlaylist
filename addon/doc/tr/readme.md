# Station Playlist #

* Yazarlar: Christopher Duffley <nvda@chrisduffley.com> (eski adıyla Joseph Lee <joseph.lee22590@gmail.com>, aslen Geoff Shang ve diğer katkıda bulunanlar tarafından yapılmıştır)

Bu eklenti paketi, StationPlaylist Studio ve diğer StationPlaylist uygulamalarının kullanımını iyileştirmenin yanı sıra, Studio'yu her yerden kontrol etmek için yardımcı programlar sağlar. Desteklenen uygulamalar arasında Studio, Creator, Track Tool, VT Recorder ve Streamer'ın yanı sıra SAM, SPL ve AltaCast kodlayıcılar bulunur.

Eklenti hakkında daha fazla bilgi için [eklenti kılavuzunu][1] okuyun.

ÖNEMLİ NOTLAR:

* Bu eklenti, StationPlaylist Suite 6.0 veya sonraki sürümünü gerektirir.
* NVDA oturum açma ekranı gibi güvenli modda çalışıyorsa bazı eklenti özellikleri devre dışı bırakılır veya sınırlandırılır.
* En iyi deneyim için ses zayıflaması modunu devre dışı bırakın.
* 2018'den itibaren [eski eklenti sürümleri için değişiklik günlükleri][2] GitHub'da bulunacaktır. Bu eklenti benioku, 25.01 (2025) sürümünden sonraki değişiklikleri listeleyecektir.
* Studio çalışırken, sırasıyla Control+NVDA+C, Control+NVDA+R'ye bir kez veya Control+NVDA+R'ye üç kez basarak kaydedebilir, kaydedilen ayarları yeniden yükleyebilir veya eklenti ayarlarını varsayılanlara sıfırlayabilirsiniz. Bu, kodlayıcı ayarları için de geçerlidir - kodlayıcı kullanıyorsanız kodlayıcı ayarlarını kaydedebilir ve sıfırlayabilirsiniz (yeniden yükleyemezsiniz).
* NVDA isteğe bağlı konuşma modundayken birçok komut konuşma çıkışı sağlayacaktır (NVDA 2024.1 ve sonrası).

## Kısayol tuşları

Bunların çoğu, aksi belirtilmedikçe yalnızca Studio'da çalışır. Aksi belirtilmedikçe, bu komutlar isteğe bağlı konuşma modunu destekler.

* Stüdyo penceresinde Alt+Shift+T: o anda çalınan parça için geçen süreyi duyurur.
* Stüdyo penceresinde Kontrol+Alt+T (SPL dokunmatik modunda iki parmakla aşağı kaydırma): o anda çalınan parça için kalan süreyi duyurur.
* Stüdyo penceresinde NVDA+Shift+F12 (SPL dokunmatik modunda iki parmakla yukarı kaydırma): yayıncının saatin başına 5 dakika kala zamanını duyurur. Bu komuta iki kez basıldığında saatin başına kadar dakika ve saniyeler duyurulacaktır.
* Stüdyo penceresinde Alt+NVDA+1 (SPL modunda iki parmakla sağa kaydırma): Studio eklenti yapılandırma iletişim kutusunda alarmlar kategorisini açar (talep üzerine konuşmayı desteklemez).
* Oluşturucu Çalma Listesi Düzenleyicisinde ve Uzaktan VT çalma listesi düzenleyicisinde Alt+NVDA+1: Yüklenen çalma listesi için planlanan zamanı duyurur.
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+2: Toplam çalma listesi süresini duyurur.
* Stüdyo penceresinde Alt+NVDA+3: Sepet atamalarını öğrenmek için sepet gezginine geçiş yapar (talep üzerine konuşmayı desteklemez).
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+3: Seçilen parçanın ne zaman çalınacağını duyurur.
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+4: Yüklenen çalma listesiyle ilişkili rotasyonu ve kategoriyi duyurur.
* Studio penceresinde Kontrol+NVDA+f: Sanatçı veya şarkı adına göre parça bulmak için bir iletişim kutusu açar. Sonrakini bulmak için NVDA+F3 tuşlarına veya Öncekini bulmak için NVDA+Shift+F3 tuşlarına basın (talep üzerine konuşmayı desteklemez).
* Studio penceresinde Shift+NVDA+R: Kitaplık taraması duyuru ayarlarında adımlar (talep üzerine konuşmayı desteklemez).
* Studio penceresinde Kontrol+Shift+X: Braille zamanlayıcı ayarlarında adım adım ilerler (talep üzerine konuşmayı desteklemez).
* Kontrol+Alt+sol/sağ ok (Studio, Oluşturucu, Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında): Önceki/sonraki parça sütununa git (talep üzerine konuşmayı desteklemez).
* Kontrol+Alt+yukarı/aşağı ok (Studio, Oluşturucu, Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında): Önceki/sonraki parçaya geçer ve belirli sütunları duyurur (talep üzerine konuşmayı desteklemez).
* Kontrol+NVDA+1'den 0'a kadar (Studio, Oluşturucu (Çalma Listesi Düzenleyici dahil), Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında): Belirli bir sütun için sütun içeriğini duyurur (varsayılan olarak ilk on sütun). Bu komuta iki kez basıldığında, gözatma modu penceresinde sütun bilgileri görüntülenecektir.
* Kontrol+NVDA+- (Studio, Oluşturucu, Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında kısa çizgi): bir göz atma modu penceresinde bir parçadaki tüm sütunlara ait verileri görüntüler (talep üzerine konuşmayı desteklemez).
* NVDA+V bir parçaya odaklanmışken (yalnızca Studio'nun çalma listesi görüntüleyicisi): Parça sütunu duyurusunu ekran sırası ve özel sıralama arasında değiştirir (talep üzerine konuşmayı desteklemez).
* Bir parçaya odaklanıldığında Alt+NVDA+C (yalnızca Studio'nun çalma listesi görüntüleyicisi): varsa parça yorumlarını duyurur.
* Studio penceresinde Alt+NVDA+0 (SPL modunda sola iki parmak hareketi): Studio eklenti yapılandırma iletişim kutusunu açar (talep üzerine konuşmayı desteklemez).
* Stüdyo penceresinde Alt+NVDA+P: Studio yayın profilleri iletişim kutusunu açar (talep üzerine konuşmayı desteklemez).
* Alt+NVDA+F1: Karşılama iletişim kutusunu açar (talep üzerine konuşmayı desteklemez).

## Atanmamış komutlar

Aşağıdaki komutlar varsayılan olarak atanmamıştır; bunları atamak isterseniz, özel komutlar eklemek için Girdi Hareketleri iletişim kutusunu kullanın. Bunu yapmak için Studio penceresinden NVDA menüsünü, Tercihler'i ve ardından Girdi Hareketleri'ni açın. StationPlaylist kategorisini genişletin, ardından aşağıdaki listeden atanmamış komutları bulun ve "Ekle"yi seçin. Sonra, kullanmak istediğiniz hareketi yazın.

Önemli: NVDA oturum açma ekranı gibi güvenli modda çalışıyorsa bu komutlardan bazıları çalışmayacaktır. Tüm komutlar talep üzerine konuşmayı desteklemez.

* Herhangi bir programdan SPL Studio penceresine geçiş (güvenli modda kullanılamaz, isteğe bağlı konuşmayı desteklemez).
* SPL Denetleyici katmanı (güvenli modda kullanılamaz).
* Diğer programlardan parça Çalma gibi Studio durumunun duyurulması (güvenli modda kullanılamaz).
* Kodlayıcı bağlantı durumu herhangi bir programdan duyurulur (güvenli modda kullanılamaz).
* SPL Studio'da SPL Yardımcısı katmanı.
* SPL Studio'da saniyeler dahil süreyi duyurur.
* Sıcaklık duyurusu.
* Planlandığı takdirde bir sonraki parçanın başlığının duyurulması.
* Şu anda çalınan parçanın başlığı duyuruluyor.
* Parça süresi analizinin başlangıcı için mevcut parçayı işaretleme.
* Parça süresi analizi gerçekleştirme.
* Çalma listesi anlık görüntüleri alır.
* Belirli sütunlardaki metni bulur (talep üzerine konuşmayı desteklemez).
* Zaman aralığı bulucu aracılığıyla süresi belirli bir aralığa giren parçaları bulur (talep üzerine konuşmayı desteklemez).
* Meta veri akışını hızla etkinleştirir veya devre dışı bırakır (talep üzerine konuşmayı desteklemez).

## Kodlayıcıları kullanırken ek komutlar

Kodlayıcılar kullanılırken aşağıdaki komutlar kullanılabilir: Studio'ya odaklanma, ilk parçayı çalma ve arka plan izlemeyi açma/kapama gibi bağlantı davranışları için seçenekleri değiştirmeye yarayan komutlar, NVDA menüsündeki Tercihler, Girdi Hareketleri, StationPlaylist kategorisi altındaki Girdi Hareketleri iletişim kutusundan atanabilir. Bu komutlar isteğe bağlı konuşma özelliğini desteklemez.

* F9: seçilen kodlayıcıyı bağlar.
* F10 (yalnızca SAM kodlayıcı): Seçilen kodlayıcının bağlantısını keser.
* Kontrol+F9: Tüm kodlayıcıları bağlar.
* Kontrol+F10 (yalnızca SAM kodlayıcı): Tüm kodlayıcıların bağlantısını keser.
* Kontrol+Shift+F11: NVDA'nın bağlı olması durumunda seçilen kodlayıcı için Studio penceresine geçip geçmeyeceğini değiştirir.
* Shift+F11: Kodlayıcı bir akış sunucusuna bağlandığında Studio'nun seçilen ilk parçayı çalıp çalmayacağını değiştirir.
* Kontrol+F11: Seçilen kodlayıcının arka plan izlemesini açar veya kapatır.
* Kontrol+F12: Sildiğiniz kodlayıcıyı seçmek için bir iletişim kutusu açar (kodlayıcı etiketlerini ve ayarlarını yeniden hizalamak için).
* Alt+NVDA+0 veya F12: Kodlayıcı etiketi gibi seçenekleri yapılandırmak için kodlayıcı ayarları iletişim kutusunu açar.

Ayrıca aşağıdakiler de dahil olmak üzere sütun inceleme komutları mevcuttur (talep üzerine konuşmayı destekler):

* Kontrol+NVDA+1: Kodlayıcı konumu.
* Kontrol+NVDA+2: kodlayıcı etiketi.
* SAM Kodlayıcıda Kontrol+NVDA+3: Kodlayıcı formatı.
* SPL ve AltaCast Kodlayıcıda Kontrol+NVDA+3: Kodlayıcı ayarları.
* SAM Kodlayıcıda Kontrol+NVDA+4: Kodlayıcı bağlantı durumu.
* SPL ve AltaCast Kodlayıcıda Kontrol+NVDA+4: Aktarım hızı veya bağlantı durumu.
* SAM Kodlayıcıda Kontrol+NVDA+5: Bağlantı durumu açıklaması.

## SPL Yardımcısı katmanı

Bu katman komut seti, SPL Studio'da bir parçanın çalınıp çalınmadığı, tüm parçaların bir saat içindeki toplam süresi vb. gibi çeşitli durumları elde etmenize olanak tanır. Herhangi bir SPL Studio penceresinden SPL Yardımcısı katman komutuna basın, ardından aşağıdaki listedeki tuşlardan birine basın (bir veya daha fazla komut çalma listesi görüntüleyiciye özeldir). NVDA'yı diğer ekran okuyuculardan gelen komutları taklit edecek şekilde de yapılandırabilirsiniz.

Kullanılabilir komutlar şunlardır (çoğu komut talep üzerine konuşmayı destekler):

* A: Otomasyon.
* C (JAWS düzeninde Shift+C): O anda çalınan parçanın başlığı.
* C (JAWS düzeni): Sepet gezginini aç/kapat (yalnızca çalma listesi görüntüleyici, isteğe bağlı konuşmayı desteklemez).
* D (JAWS düzeninde R): Çalma listesinin kalan süresi (bir hata mesajı verilirse çalma listesi görüntüleyiciye gidin ve ardından bu komutu verin).
* Kontrol+D (Studio 6.10 ve üzeri): Kontrol tuşları etkin/devre dışı.
* E: Meta veri akış durumu.
* Shift+1 ila Shift+4, Shift+0: Bireysel meta veri akışı URL'lerinin durumu (0, DSP kodlayıcı içindir).
* F: Parçayı bul (yalnızca çalma listesi görüntüleyicide, isteğe bağlı konuşmayı desteklemez).
* H: Geçerli saat dilimi için müzik süresi.
* Shift+H: Saat aralığı için kalan parça süresi.
* I (JAWS düzeninde L): Dinleyici sayısı.
* K: İşaretli parçaya gider (yalnızca çalma listesi görüntüleyicisinde).
* Kontrol+K: Geçerli parçayı yer işaretleyici parça olarak ayarlar (yalnızca çalma listesi görüntüleyici).
* L (JAWS düzeninde Shift+L): Line in.
* M: Mikrofon.
* N: Bir sonraki programlanmış parçanın adı.
* O: Oynatma listesi Zaman Kalan/geçen süre.
* P: Çalma durumu (Çalınıyor veya durduruldu).
* Shift+P: Geçerli parçanın perdesi.
* R (JAWS düzeninde Shift+E): Dosyaya kaydetme etkin/devre dışı.
* Shift+R: Devam eden kitaplık taramasını izler.
* S: Parça başlangıçları (planlanmış).
* Shift+S: Seçilen parça çalınana kadar geçecek süre (parça başlar).
* T: Sepet düzenleme/ekleme modu açık/kapalı.
* U: Stüdyo çalışma zamanı.
* W: Yapılandırılmışsa hava durumu ve sıcaklık.
* Y: Çalma listesi değişiklik durumu.
* F8: Çalma listesi anlık görüntülerini alır (parça sayısı, en uzun parça vb.).
* Shift+F8: Çeşitli biçimlerde çalma listesi transkriptlerini ister.
* F9: Çalma listesi analizinin başlatılması için geçerli parçayı işaretler (yalnızca çalma listesi görüntüleyicide).
* F10: Parça süresi analizini gerçekleştirir (yalnızca çalma listesi görüntüleyicide).
* F12: Geçerli profil ile önceden tanımlanmış profil arasında geçiş yapar.
* F1: Katman yardımı.

## SPL Denetleyicisi

SPL denetleyicisi, SPL Studio'yu her yerde kontrol etmek için kullanabileceğiniz bir dizi katmanlı komuttur. SPL denetleyici katmanı komutuna basın, NVDA "SPL Denetleyicisi" der. Mikrofon açma/kapalı gibi çeşitli stüdyo ayarlarını kontrol etmek veya bir sonraki parçayı çalmak için başka bir komut tuşuna basın. Ayrıca NVDA'yı SPL denetleyici katmanı komutuna (varsayılan olarak etkinleştirilen geçiş modu) basarak SPL asistan katmanını (yukarıya bakınız) girecek şekilde yapılandırabilirsiniz.

Önemli: NVDA güvenli modda çalışıyorsa SPL Denetleyici katmanı komutları devre dışı bırakılır.

Studio dışında, kullanılabilir SPL Denetleyicisi komutları şunlardır (bazı komutlar isteğe bağlı konuşmayı destekler):

* P: Sonraki seçilen parçayı çalar.
* U: Çalmayı duraklat veya sürdür.
* S: Parçayı kısarak durdurur.
* T: Anında Durdur.
* M: Mikrofonu açar.
* Shift+M: Mikrofonu kapatır.
* N: Mikrofonu sesi kısık olmadan açar.
* A: Otomasyonu açar.
* Shift+A: Otomasyonu kapatır.
* L: Line in girişini açar.
* Shift+L: Line-in girişini kapatır.
* R: Çalmakta olan parçanın kalan süresi.
* Shift+R: Kitaplık tarama ilerlemesi.
* C: O anda çalınan parçanın başlığı ve süresi (talep üzerine konuşmayı destekler).
* Shift+C: Varsa gelecek parçanın başlığı ve süresi (talep üzerine konuşmayı destekler).
* E: Kodlayıcı bağlantı durumu (talep üzerine konuşmayı destekler).
* I: Dinleyici sayısı (talep üzerine konuşmayı destekler).
* Q: Bir parçanın çalınıp çalınmadığı, mikrofonun açık olup olmadığı ve diğerleri gibi stüdyo durumu bilgileri (talep üzerine konuşmayı destekler).
* Sepet tuşları (örneğin F1, Control+1): Atanan sepetleri istediğiniz yerden çalın.
* H: Katman yardımı.

Studio'nun içinden, SPL Denetleyici katmanı komutu varsayılan olarak SPL Asistan katmanını çağıracaktır.

## Parça ve mikrofon alarmları

Varsayılan olarak, NVDA parçada (outro) ve/veya introda beş saniye kaldığında bir bip sesi çalacak ve mikrofon bir süredir aktifse bir bip sesi duyacaktır. Parça ve mikrofon alarmlarını yapılandırmak için Alt+NVDA+1 tuşlarına basarak Studio eklenti ayarları ekranında alarm ayarlarını açın. Bu ekranı ayrıca alarmlar açıldığında bir bip sesi mi, bir mesaj mı yoksa her ikisini birden mi duyacağınızı yapılandırmak için de kullanabilirsiniz.

## Parça Bulucu

Bir şarkıyı sanatçıya veya şarkı adına göre hızlı bir şekilde bulmak isterseniz, parça listesinde Control+NVDA+F tuşlarına basın. Sanatçının adını veya şarkı adını yazın yada seçin. NVDA, bulunursa sizi şarkıya odaklar ya da aradığınız şarkıyı bulamazsa bir hata görüntüler. Daha önce girilmiş bir şarkıyı veya sanatçıyı bulmak için NVDA+F3 veya NVDA+Shift+F3 tuşlarına basarak ileri veya geri gidin.

Not: Parça Bulucu büyük/küçük harfe duyarlıdır.

## Sepet Gezgini

Sürüme bağlı olarak SPL Studio, çalma için 96'ya kadar otomasyonun atanmasına izin verir. NVDA, bu komutlara hangi otomasyonun veya şarkının atandığını duymanıza olanak tanır.

Sepet atamalarını öğrenmek için SPL Studio'dan Alt+NVDA+3 tuşlarına basın. Sepet komutuna bir kez bastığınızda, komuta hangi jingle'ın atandığı size söylenecektir. Sepet komutuna iki kez basıldığında jingle çalınır. Sepet gezgininden çıkmak için Alt+NVDA+3 tuşlarına basın. Sepet gezgini hakkında daha fazla bilgi için eklenti kılavuzuna bakın.

## Parça zaman analizi

Seçilen parçaları çalmak için uzunluk elde etmek üzere, parça süresi analizinin başlangıcı için geçerli parçayı işaretleyin (SPL Yardımcısı, F9), ardından seçimin sonuna ulaştığınızda SPL Yardımcısı, F10'a basın.

## Sütun Gezgini

Kontrol+NVDA+1'den 0'a kadar basarak belirli sütunların içeriğini elde edebilirsiniz. Varsayılan olarak, bunlar bir parça öğesi için ilk on sütundur (Studio'da: sanatçı, başlık, süre, giriş, çıkış, kategori, yıl, albüm, tür, ruh hali). Studio'da, Oluşturucu'nun ana parça listesi ve çalma listesi düzenleyicisinde, Parça Araçları'nda ve Remote VT'de, sütun yuvaları ekrandaki sütun sırasından bağımsız olarak önceden ayarlanmıştır ve sütun gezgini kategorisi altındaki eklenti ayarları iletişim kutusundan yapılandırılabilir.

## Parça sütunu anonsu

NVDA'dan, Studio'nun çalma listesi görüntüleyicisinde bulunan parça sütunlarını ekranda göründüğü sırayla veya özel bir sırayla duyurmasını ve/veya belirli sütunları hariç tutmasını isteyebilirsiniz. Studio'nun çalma listesi görüntüleyicisinde bir parçaya odaklanırken NVDA+V tuşlarına basarak bu davranışı değiştirebilirsiniz. Sütunların dahil edilmesini ve sırasını özelleştirmek için, eklenti ayarlarında sütun duyurusu ayarları panelinden “Sütunları ekranda gösterildiği sırayla duyur” seçeneğinin işaretini kaldırın ve ardından dahil edilecek sütunları ve/veya sütun sırasını özelleştirin.

## Oynatma listesi anlık görüntüleri

Çalma listesindeki parça sayısı, en uzun parça, en iyi sanatçılar vb. dahil olmak üzere bir çalma listesi hakkında çeşitli istatistikler elde etmek için Studio'da bir çalma listesine odaklanmışken SPL Yardımcısı ve F8 tuşlarına basabilirsiniz. Bu özellik için özel bir komut atadıktan sonra, özel komuta iki kez basmak, NVDA'nın çalma listesi anlık görüntü bilgilerini bir web sayfası olarak sunmasına neden olur, böylece gezinmek için göz atma modunu kullanabilirsiniz (kapatmak için Escape tuşuna basın).

## Çalma Listesi Transkriptleri

SPL Yardımcısı'na bastığınızda, Shift+F8, düz metin biçimi, HTML tablosu veya liste dahil olmak üzere çeşitli biçimlerde çalma listesi transkriptlerini istemenize izin veren bir iletişim kutusu sunar.

## Yapılandırma iletişim kutusu

Eklenti yapılandırma iletişim kutusunu açmak için stüdyo penceresinden Alt+NVDA+0 tuşlarına basabilirsiniz. Alternatif olarak, NVDA'nın tercihler menüsüne gidin ve SPL Studio Ayarları öğesini seçin. NVDA güvenli modda çalışıyorsa tüm ayarlar kullanılamaz.

## Yayın profilleri iletişim kutusu

Belirli programların ayarlarını yayın profillerine kaydedebilirsiniz. Bu profiller, Studio penceresinden Alt+NVDA+P tuşlarına basılarak erişilebilen SPL yayın profilleri iletişim kutusu aracılığıyla yönetilebilir.

## SPL dokunma modu

Studio'yu NVDA kurulu dokunmatik ekranlı bir bilgisayarda kullanıyorsanız, bazı Studio komutlarını dokunmatik ekrandan gerçekleştirebilirsiniz. Önce SPL moduna geçmek için üç parmakla dokunmayı kullanın, ardından komutları gerçekleştirmek için yukarıda listelenen dokunma komutlarını kullanın.

## Sürüm 25.10/25.06.8-LTS

* 25.10: Hata ayıklama günlüğü etkinken, NVDA artık Studio API'ye özgü hata ayıklama mesajlarını kaydetmeyecek. Studio API hata ayıklama mesajlarını içerecek şekilde yeni bir komut satırı seçeneği (--spl-apideBug) eklendi ve eklenti geliştiricileri tarafından yönlendirildiği gibi kullanılmalıdır.
* Studio'da, parça bulucudaki arama geçmişi (Kontrol+NVDA+F), NVDA'nın kendi bul iletişim kutusu deneyimiyle uyumlu hale getirmek için bir arama düzenleme alanıyla değiştirilir.
* Studio'da, braille zamanlayıcı etkinleştirildiğinde, NVDA, parçanın kalan süresini görüntülemek yerine, görüntülenen değer parçanın/şarkının sonundaki rampa alarm değerinin altına düştüğünde yalnızca kalan parça/giriş süresini duyurur.

## Sürüm 25.09/25.06.6-LTS

* 25.09: NVDA 2025.1.2 veya üstü gereklidir.
* Studio'da, parça bulucudaki arama geçmişi (Control+NVDA+F) kullanımdan kaldırılmıştır ve NVDA'nın kendi arama diyalog deneyimine uyum sağlamak için gelecek bir sürümde kaldırılacaktır.
* Studio'da, SPL Denetleyici katmanı giriş komutu gerçekleştirildiğinde SPL Asistan katmanına girer ve bu seçeneği yapılandırmak için eklenti ayarı yeni kurulumlarda varsayılan olarak işaretlidir.

## Sürüm 25.08/25.06.5-LTS

* 25.08: bakımı yapılmamış yerelleştirmeler kaldırıldı (eklenti mesajları ve belgeler).
* Studio'da, SPL eklenti ayarlarını açmak için SPL dokunma modunda iki parmakla sola kaydırma hareketi eklendi.
* Dikey sütun gezinme seçeneklerinden “Durum” kaldırıldı.
* Sütun gezgininde (Studio, Parça aracı, Oluşturucu, Uzak VT), NVDA artık boş sütun içeriği için "boş" mesajını vermeyecektir (yalnızca sütun başlığı duyurulacaktır).
* Studio, Parça Aracı, Oluşturucu ve Uzak VT'de, konum komutu gerçekleştirildiğinde (NVDA+Numpad Delete (masaüstü)/NVDA+Delete (dizüstü) ve inceleme imleci sürümü için Shift eklendiğinde) NVDA parça konumunu ve sayısını bildirecektir.

## Sürüm 25.07.2/25.06.4-LTS

* Studio'nun çalma listesi görüntüleyicisinde parça yorumu duyurusu da dahil olmak üzere eksik yerelleştirilmiş mesajlar geri yüklendi.
* NVDA, eklenti için gereken sürümden önceki Studio sürümlerini çalıştırırken bir hata iletişim kutusu gösterecek.
* Studio'da, bul iletişim kutusunu açmadan NVDA+Shift+F3 tuşlarına ilk kez basmak, NVDA'nın geriye doğru arama yapmasına neden olur.
* Parça aracı'nda, NVDA artık parçalar arasında ilerlerken, özellikle de giriş seti olmayan parçalar için bip sesi çıkarmayacak.

## Sürüm 25.07.1/25.06.3-LTS

* Studio'nun çalma listesi görüntüleyicisinde, dikey sütun gezintisi “incelediğim sütun” dışındaki değerlere ayarlanmışsa, NVDA artık sütun içeriklerini bildirirken hiçbir şey yapmıyor veya hata sesleri çalmıyor gibi görünmeyecek.
* Dikey sütun dolaşımını "Durum" sütunu olarak ayarlamak kullanımdan kaldırılmıştır ve gelecekteki bir eklenti sürümünde kaldırılacaktır.

## Sürüm 25.07/25.06.2-LTS

Sürüm 25.07 SPL Studio 6.0 ve sonraki sürümlerini destekler.

* 25.07: Kod, Pyright (Python statik tip denetleyici) kullanımı dahil olmak üzere yeniden düzenlendi. Bazı önemli kod değişiklikleri de 25.06.2-lts'e geri döndü.
* Sütun gezgini (Control+NVDA+numara satırı) artık Yaratıcı ve Kumanda VT'nin oynatma listesi düzenleyicisi için yapılandırılabilir. Sütun gezgini eklenti ayarları ekranından yeni bir düğme olan “oynatma listesi düzenleyicisi için sütun gezgini” kullanılabilir.
* Sütun gezgini eklenti ayarlarında, "sütun gezgini", "SPL Studio için sütun gezgini" olarak yeniden adlandırıldı.
* Çalma listesi transkript formatı olarak JSON (JavaScript Object Notation) formatı eklendi.
* Kodlayıcılarda, ondan fazla kodlayıcı varsa 10 ve üzeri kodlayıcı ayarlarını kaldırmak için Control+F12 tuşlarına basıldığında NVDA kodlayıcı ayarlarını kaldıracaktır.

## Sürüm 25.06-LTS

Sürüm 25.06.x, Studio 6.x gerektiren gelecekteki sürümlerle Studio 5.x'i destekleyen son sürüm serisidir. Gerekirse bazı yeni özellikler 25.06.x'e geri aktarılacaktır.

* Yaklaşan 64 bit NVDA ile eklentiyi daha uyumlu hale getirmek için dahili değişiklikler.
* NVDA artık eklentiyi güncellerken yayın profillerini aktarmayı unutmayacak (25.05'te tanıtılan bir gerileme düzeltildi).
* SPL Assistant'a oynatma listesi zamanı Kalan/geçen dakika ve saniye cinsinden (O) bildirmek için yeni bir komut eklendi.
* Studio'da, kütüphane tarama duyurusu ayarlarında adım atma komutu Alt+NVDA+R'den Shift+NVDA+R'ye değiştirildi, çünkü eski komut NVDA 2025.1'deki uzaktan erişim özelliğini değiştiriyor.
* NVDA artık Studio penceresini yeniden boyutlandırdıktan sonra bazı SPL Assistant komutlarını gerçekleştirirken hata tonları çalmayacak veya hiçbir şey yapmıyor gibi görünmeyecek.
* Yayın profillerini silerken gösterilen onay iletişim kutusu için kullanıcı arayüzü artık NVDA'nın yapılandırma profili silme arabirimine benziyor.
* Eklenti ayarlarında, NVDA artık sütun gezgini ve sıfırlama iletişim kutularını kapattıktan sonra klavye odağını Tamam düğmesine taşımayacak.
* NVDA, Yaratıcı ve Track Aracı 6.11'de tanıtılan parça sütun değişikliklerini tanıyacaktır.
* Oluşturucu için sütun gezgininde “Tarih Kısıtlaması” sütunu artık “Kısıtlamalar” oldu.
* NVDA, SPL Denetleyici katmanı aracılığıyla oynatırken artık yanlış kartları oynatmayacak.

## Sürüm 25.05

* Python 3.11 yükseltmesi nedeniyle NVDA 2024.1 veya sonrası gereklidir.
* Windows 8.1 için sınırlı destek geri yüklendi.
* Eklenti değişiklik günlüğü gibi eklenti viki belgeleri ana kod deposuna taşındı.
* Oynatma listesi anlık görüntülerine, çalma listesi transkriptlerine ve SPL Asistanı ve Denetleyici katmanı yardım ekranlarına (NVDA 2025.1 ve üstü) kapat düğmesi eklendi.
* NVDA, Studio 6.x'te (SPL Assistant, W) hava durumu ve sıcaklık bilgilerini duyururken artık hiçbir şey yapmayacak veya hata tonları çalmayacak.

## Sürüm 25.01

* 64 bit Windows 10 21H2 (derleme 19044) veya sonrası gereklidir.
* Eklenti sürümlerinin indirme bağlantıları artık eklenti belgelerine dahil edilmemektedir. Eklentiyi NV Access eklenti mağazasından indirebilirsiniz.
* Linting aracı Flake8'den Ruff'a değiştirildi ve NVDA kodlama standartlarıyla daha iyi uyum sağlamak için eklenti modülleri yeniden biçimlendirildi.
* Eklenti Güncelleyici eklentisinden otomatik eklenti güncelleme desteği kaldırıldı.
* Studio 6.10 ve sonraki sürümlerde, kontrol tuşlarının etkin/devre dışı durumunu (Kontrol+D) duyurmak için SPL Yardımcısı'na yeni bir komut eklendi.

## Eski sürümler

Eski eklenti sürümlerine ilişkin sürüm notları için lütfen [değişiklik günlüğüne][2] bakın.

[1]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
