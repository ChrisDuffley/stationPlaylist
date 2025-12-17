# Station Playlist #

* Yazarlar: Christopher Duffley <nvda@chrisduffley.com> (eski adıyla Joseph Lee <joseph.lee22590@gmail.com>, aslen Geoff Shang ve diğer katkıda bulunanlar tarafından yapılmıştır)

Bu eklenti paketi, StationPlaylist Studio ve diğer StationPlaylist uygulamalarının gelişmiş kullanımını sağlamanın yanı sıra Studio'yu her yerden kontrol etmek için yardımcı programlar sağlar. Desteklenen uygulamalar arasında Studio, Remote Studio, Creator, Track Tool, VT Recorder ve Streamer'ın yanı sıra SAM, SPL ve AltaCast kodlayıcılar bulunur.

Eklenti hakkında daha fazla bilgi için [eklenti kılavuzunu][1] okuyun.

ÖNEMLİ NOTLAR:

* Bu eklenti, StationPlaylist Suite 6.0 veya sonraki sürümünü gerektirir.
* NVDA oturum açma ekranı gibi güvenli modda çalışıyorsa bazı eklenti özellikleri devre dışı bırakılır veya sınırlandırılır.
* En iyi deneyim için ses zayıflaması modunu devre dışı bırakın.
* 2018'den itibaren GitHub'da [eski eklenti sürümleri için değişiklik günlükleri][2] bulunacaktır. Bu eklenti benioku sürümü 26.01 (2026) ve sonrasındaki değişiklikleri listeleyecektir.
* Studio çalışırken, sırasıyla Control+NVDA+C, Control+NVDA+R'ye bir kez veya Control+NVDA+R'ye üç kez basarak kaydedebilir, kaydedilen ayarları yeniden yükleyebilir veya eklenti ayarlarını varsayılanlara sıfırlayabilirsiniz. Bu, kodlayıcı ayarları için de geçerlidir - kodlayıcı kullanıyorsanız kodlayıcı ayarlarını kaydedebilir ve sıfırlayabilirsiniz (yeniden yükleyemezsiniz).
* NVDA isteğe bağlı konuşma modundayken birçok komut konuşma çıkışı sağlayacaktır (NVDA 2024.1 ve sonrası).
* Studio'ya başvurulduğunda hem yerel (orijinal) Studio hem de Remote Studio varsayılacaktır. StationPlaylist Studio'ya (orijinal) özel bir şey olduğunda "local Studio" terimi kullanılacaktır.
* Hem Studio'nun (yerel/orijinal) hem de Remote Studio'nun aynı bilgisayara kurulması önerilmez.

## Kısayol tuşları

Bunların çoğu, aksi belirtilmedikçe yalnızca Studio'da çalışır. Aksi belirtilmedikçe, bu komutlar isteğe bağlı konuşma modunu destekler.

* Studio penceresinde Alt+Shift+T: Oynatılan parça, ses parçası veya sepet için geçen süreyi duyurur.
* Studio penceresinde Control+Alt+T (SPL dokunmatik modunda iki parmağınızı aşağı doğru kaydırın): şu anda çalınan parça, ses parçası veya kart için kalan süreyi duyurun.
* Stüdyo penceresinde NVDA+Shift+F12 (SPL dokunmatik modunda iki parmakla yukarı kaydırma): yayıncının saatin başına 5 dakika kala zamanını duyurur. Bu komuta iki kez basıldığında saatin başına kadar dakika ve saniyeler duyurulacaktır.
* Stüdyo penceresinde Alt+NVDA+1 (SPL modunda iki parmakla sağa kaydırma): Studio eklenti yapılandırma iletişim kutusunda alarmlar kategorisini açar (talep üzerine konuşmayı desteklemez).
* Oluşturucu Çalma Listesi Düzenleyicisinde ve Uzaktan VT çalma listesi düzenleyicisinde Alt+NVDA+1: Yüklenen çalma listesi için planlanan zamanı duyurur.
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+2: Toplam çalma listesi süresini duyurur.
* Stüdyo penceresinde Alt+NVDA+3: Sepet atamalarını öğrenmek için sepet gezginine geçiş yapar (talep üzerine konuşmayı desteklemez).
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+3: Seçilen parçanın ne zaman çalınacağını duyurur.
* Oluşturucunun Çalma Listesi Düzenleyicisinde ve Remote VT çalma listesi düzenleyicisinde Alt+NVDA+4: Yüklenen çalma listesiyle ilişkili rotasyonu ve kategoriyi duyurur.
* Studio penceresinde Kontrol+NVDA+f: Sanatçı veya şarkı adına göre parça bulmak için bir iletişim kutusu açar. Sonrakini bulmak için NVDA+F3 tuşlarına veya Öncekini bulmak için NVDA+Shift+F3 tuşlarına basın (talep üzerine konuşmayı desteklemez).
* Studio penceresinden Shift+NVDA+R (yalnızca yerel Studio): Kitaplık tarama duyuru ayarlarını adım adım ilerler (istek üzerine konuşma özelliğini desteklemez).
* Studio penceresinde Kontrol+Shift+X: Braille zamanlayıcı ayarlarında adım adım ilerler (talep üzerine konuşmayı desteklemez).
* Kontrol+Alt+sol/sağ ok (yerel ve Remote Studio, Creator, Remote VT ve Track Tool'da bir parçaya odaklanırken): Önceki/sonraki parça sütununa git (istek üzerine konuşma özelliğini desteklemez).
* Kontrol+Alt+yukarı/aşağı ok (yerel ve Remote Studio, Creator, Remote VT ve Track Tool'da bir parçaya odaklanırken): Önceki/sonraki parçaya geçer ve belirli sütunları duyurur (istek üzerine konuşma özelliğini desteklemez).
* Kontrol+NVDA+1'den 0'a kadar (Studio, Oluşturucu (Çalma Listesi Düzenleyici dahil), Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında): Belirli bir sütun için sütun içeriğini duyurur (varsayılan olarak ilk on sütun). Bu komuta iki kez basıldığında, gözatma modu penceresinde sütun bilgileri görüntülenecektir.
* Kontrol+NVDA+- (Studio, Oluşturucu, Remote VT ve Parça Araçlarında bir parçaya odaklanıldığında kısa çizgi): bir göz atma modu penceresinde bir parçadaki tüm sütunlara ait verileri görüntüler (talep üzerine konuşmayı desteklemez).
* NVDA+V bir parçaya odaklanmışken (yalnızca Studio'nun çalma listesi görüntüleyicisi): Parça sütunu duyurusunu ekran sırası ve özel sıralama arasında değiştirir (talep üzerine konuşmayı desteklemez).
* Bir parçaya odaklanıldığında Alt+NVDA+C (yalnızca Studio'nun çalma listesi görüntüleyicisi): varsa parça yorumlarını duyurur.
* Yerel ve Uzaktan Stüdyo, Yaratıcı, Uzaktan VT ve Parça Aracı'ndan Alt+NVDA+0 (SPL modunda iki parmakla sola kaydırma): Stüdyo eklenti yapılandırma iletişim kutusunu açar (isteğe bağlı konuşma özelliğini desteklemez).
* Stüdyo penceresinde Alt+NVDA+P: Studio yayın profilleri iletişim kutusunu açar (talep üzerine konuşmayı desteklemez).
* Alt+NVDA+F1: Karşılama iletişim kutusunu açar (talep üzerine konuşmayı desteklemez).

## Atanmamış komutlar

Aşağıdaki komutlar varsayılan olarak atanmamıştır; bunları atamak isterseniz, özel komutlar eklemek için Girdi Hareketleri iletişim kutusunu kullanın. Bunu yapmak için Studio penceresinden NVDA menüsünü, Tercihler'i ve ardından Girdi Hareketleri'ni açın. StationPlaylist kategorisini genişletin, ardından aşağıdaki listeden atanmamış komutları bulun ve "Ekle"yi seçin. Sonra, kullanmak istediğiniz hareketi yazın.

Önemli: NVDA oturum açma ekranı gibi güvenli modda çalışıyorsa bu komutlardan bazıları çalışmayacaktır. Tüm komutlar İsteğe bağlı konuşmayı desteklemez ve/veya Remote Studio'da kullanılamaz.

* Herhangi bir programdan SPL Studio penceresine geçiş (güvenli modda kullanılamaz, isteğe bağlı konuşmayı desteklemez).
* SPL Denetleyici katmanı (güvenli modda kullanılamaz).
* Diğer programlardan parça Çalma gibi Studio durumunun duyurulması (güvenli modda kullanılamaz).
* Kodlayıcı bağlantı durumu herhangi bir programdan duyurulur (güvenli modda kullanılamaz).
* SPL Studio'da SPL Yardımcısı katmanı.
* Studio'da saniyeler de dahil olmak üzere zamanı duyurur.
* Sıcaklık duyurusu.
* Planlandığı takdirde bir sonraki parçanın başlığının duyurulması.
* Şu anda çalınan parçanın başlığı duyuruluyor.
* Parça süresi analizinin başlangıcı için mevcut parçayı işaretleme.
* Parça süresi analizi gerçekleştirme.
* Çalma listesi anlık görüntüleri alır.
* Belirli sütunlardaki metni bulur (talep üzerine konuşmayı desteklemez).
* Zaman aralığı bulucu aracılığıyla süresi belirli bir aralığa giren parçaları bulur (talep üzerine konuşmayı desteklemez).
* Meta veri akışını hızlı bir şekilde etkinleştirin veya devre dışı bırakın (talep üzerine konuşmayı desteklemez, Remote Studio'da mevcut değildir).

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

Bu katman komut seti, Studio'da bir parçanın çalınıp çalınmadığı, tüm parçaların bir saat içindeki toplam süresi vb. gibi çeşitli durumları elde etmenize olanak tanır. Herhangi bir yerel veya Remote Studio penceresinden SPL Assistant katman komutuna basın, ardından aşağıdaki listedeki tuşlardan birine basın (bir veya daha fazla komut çalma listesi görüntüleyiciye özeldir). NVDA'yı diğer ekran okuyuculardan gelen komutları taklit edecek şekilde de yapılandırabilirsiniz.

Kullanılabilir komutlar şunlardır (çoğu komut isteğe bağlı konuşmayı destekler ve bazı komutlar Remote Studio'da kullanılamaz):

* A: Otomasyon.
* C (JAWS düzeninde Shift+C): Şu anda çalınan parçanın başlığı.
* C (JAWS düzeni): Sepet gezginini aç/kapat (yalnızca çalma listesi görüntüleyici, isteğe bağlı konuşmayı desteklemez).
* D (JAWS düzeninde R): Çalma listesinin kalan süresi (bir hata mesajı verilirse çalma listesi görüntüleyiciye gidin ve ardından bu komutu verin).
* Kontrol+D (Studio 6.10 ve üzeri sürümlerde, Remote Studio'da kullanılamaz): Kontrol tuşları etkinleştirilir/devre dışı bırakılır.
* E (Remote Studio'da kullanılamaz): Meta veri akış durumu.
* Shift+1 ila Shift+4, Shift+0: (Remote Studio'da kullanılamaz) Bireysel meta veri akışı URL'lerinin durumu (0, DSP kodlayıcı içindir).
* F: Parçayı bul (yalnızca çalma listesi görüntüleyicide, isteğe bağlı konuşmayı desteklemez).
* H (JAWS düzeninde T): Geçerli saat dilimi için müzik süresi.
* Shift+H (JAWS düzeninde H): Saat aralığı için kalan izleme süresi.
* I (JAWS düzeninde L, Remote Studio'da mevcut değildir): Dinleyici sayısı.
* K (Remote Studio'da kullanılamaz): İşaretli parçaya gider (yalnızca çalma listesi görüntüleyicisinde).
* Kontrol+K (Remote Studio'da kullanılamaz): Geçerli parçayı yer işaretleyici parça olarak ayarlar (yalnızca çalma listesi görüntüleyici).
* L (JAWS düzeninde Shift+L): Line in.
* M: Mikrofon.
* N: Bir sonraki programlanmış parçanın adı.
* O: Oynatma listesi Zaman Kalan/geçen süre.
* P: Çalma durumu (Çalınıyor veya durduruldu).
* Shift+P: (Remote Studio'da kullanılamaz) Geçerli parçanın perdesi.
* R (JAWS düzeninde Shift+E): (Remote Studio'da kullanılamaz) Dosyaya kaydetme etkin/devre dışı.
* Shift+R (JAWS düzeninde Alt+T; Remote Studio'da kullanılamaz): Devam eden kitaplık taramasını izleyin.
* S: Parça başlangıçları (planlanmış).
* Shift+S: Seçilen parça çalınana kadar geçecek süre (parça başlar).
* T (JAWS düzeninde sayı satırı 0 (sıfır); Remote Studio'da kullanılamaz): Sepet düzenleme/ekleme modu açık/kapalı.
* U (Remote Studio'da kullanılamaz): Stüdyo çalışma zamanı.
* W: Yapılandırılmışsa hava durumu ve sıcaklık.
* Y (Remote Studio'da kullanılamaz): Çalma listesi değişiklik durumu.
* F8: Çalma listesi anlık görüntülerini alır (parça sayısı, en uzun parça vb.).
* Shift+F8: Çeşitli biçimlerde çalma listesi transkriptlerini ister.
* F9: Çalma listesi analizinin başlatılması için geçerli parçayı işaretler (yalnızca çalma listesi görüntüleyicide).
* F10: Parça süresi analizini gerçekleştirir (yalnızca çalma listesi görüntüleyicide).
* F12: Geçerli profil ile önceden tanımlanmış profil arasında geçiş yapar.
* F1: Katman yardımı.

## SPL Denetleyicisi

SPL Denetleyicisi, SPL (yerel) Studio'yu ve/veya Remote Studio'yu herhangi bir yerde kontrol etmek için kullanabileceğiniz bir dizi katmanlı komuttur. SPL Denetleyici katmanı komutuna bastığınızda NVDA, Remote Studio kullanılıyorsa "SPL Denetleyici" veya "SPL Uzaktan Denetleyici" diyecektir. Mikrofonu açma/kapama gibi çeşitli Studio ayarlarını kontrol etmek veya sonraki parçayı oynatmak için başka bir komuta basın. Ayrıca SPL Denetleyici katmanı komutuna (geçiş modu, varsayılan olarak etkindir) basarak NVDA'yı SPL Assistant katmanına (yukarı bakın) girecek şekilde yapılandırabilirsiniz.

Önemli: NVDA güvenli modda çalışıyorsa SPL Denetleyici katmanı komutları devre dışı bırakılır.

Studio dışında mevcut SPL Denetleyici komutları şunlardır (bazı komutlar isteğe bağlı konuşmayı destekler ve bazıları yalnızca yerel Studio'da kullanılabilir):

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
* Shift+R (Remote Studio'da kullanılamaz): Kitaplık tarama ilerlemesi.
* C: O anda çalınan parçanın başlığı ve süresi (talep üzerine konuşmayı destekler).
* Shift+C: Varsa gelecek parçanın başlığı ve süresi (talep üzerine konuşmayı destekler).
* E (Remote Studio'da kullanılamaz): Kodlayıcı bağlantı durumu (talep üzerine konuşmayı destekler).
* I (Remote Studio'da mevcut değil): Dinleyici sayısı (talep üzerine konuşmayı destekler).
* Q: Bir parçanın çalınıp çalınmadığı, mikrofonun açık olup olmadığı ve diğerleri gibi stüdyo durumu bilgileri (talep üzerine konuşmayı destekler).
* Sepet tuşları (örneğin F1, Control+1; Remote Studio'da mevcut değildir): Atanan sepetleri istediğiniz yerden çalın.
* H: Katman yardımı.

Studio'nun içinden (yerel ve Remote Studio), SPL Denetleyici katmanı komutu varsayılan olarak SPL Assistant katmanını çağıracaktır.

## Parça ve mikrofon alarmları

Varsayılan olarak, NVDA parçada (outro) ve/veya introda beş saniye kaldığında bir bip sesi çalacak ve mikrofon bir süredir aktifse bir bip sesi duyacaktır. Parça ve mikrofon alarmlarını yapılandırmak için Alt+NVDA+1 tuşlarına basarak Studio eklenti ayarları ekranında alarm ayarlarını açın. Bu ekranı ayrıca alarmlar açıldığında bir bip sesi mi, bir mesaj mı yoksa her ikisini birden mi duyacağınızı yapılandırmak için de kullanabilirsiniz.

## Parça Bulucu

Bir şarkıyı sanatçıya veya şarkı adına göre hızlı bir şekilde bulmak isterseniz, parça listesinde Control+NVDA+F tuşlarına basın. Sanatçının adını veya şarkı adını yazın yada seçin. NVDA, bulunursa sizi şarkıya odaklar ya da aradığınız şarkıyı bulamazsa bir hata görüntüler. Daha önce girilmiş bir şarkıyı veya sanatçıyı bulmak için NVDA+F3 veya NVDA+Shift+F3 tuşlarına basarak ileri veya geri gidin.

Not: Parça Bulucu büyük/küçük harfe duyarlıdır.

## Sepet Gezgini

Sürüm ve yerel veya uzak stüdyo erişimine bağlı olarak, SPL Studio oynatma için 96 adede kadar otomasyon atanmasına izin verir. NVDA, bu komutlara hangi otomasyonun veya Tanıtımın atandığını duymanızı sağlar.

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

Eklenti yapılandırma iletişim kutusunu açmak için stüdyo penceresinde Alt+NVDA+0 tuşlarına basabilirsiniz. Alternatif olarak NVDA'nın tercihler menüsüne gidin ve SPL Studio Ayarları öğesini seçin. NVDA güvenli modda çalışıyorsa ve Remote Studio kullanılırken tüm ayarlar kullanılamaz.

## Yayın profilleri iletişim kutusu

Belirli programların ayarlarını yayın profillerine kaydedebilirsiniz. Bu profiller, Studio penceresinden Alt+NVDA+P tuşlarına basılarak erişilebilen SPL yayın profilleri iletişim kutusu aracılığıyla yönetilebilir.

## SPL dokunma modu

Studio'yu NVDA kurulu dokunmatik ekranlı bir bilgisayarda kullanıyorsanız, bazı Studio komutlarını dokunmatik ekrandan gerçekleştirebilirsiniz. Önce SPL moduna geçmek için üç parmakla dokunmayı kullanın, ardından komutları gerçekleştirmek için yukarıda listelenen dokunma komutlarını kullanın.

## Sürüm 26.01

* NVDA 2025.3.2 veya sonrası gereklidir.
* Eklenti ayarları ekranı artık Creator, Remote VT ve Track Tool kullanılırken her uygulama için farklı ayarlarla kullanılabilir.
* Yerel ve Remote Studio'da NVDA, parça ekle iletişim kutusunun arama kriterleri kontrolleri, parça özellikleri ve Stüdyo seçenekleri iletişim kutusu için etiketleri duyuracaktır.
* Yerel Studio'da, NVDA, parça ekleme iletişim kutusundan (Kontrol+Shift+R) kitaplığı yeniden tararken daha az ayrıntılı bilgi verecektir.
* Yerel Studio'da NVDA, eklenti ayarlarından "durum duyuruları için bip sesi" ayarından bağımsız olarak kütüphane tarama sayısını duyuracaktır.
* Remote Studio'da, sepet gezgini etkinken seçenekler ekranını (Control+O) kapatırken, güncellenmiş sepet atamalarını görüntülemek için artık Sepet Gezgini'ne yeniden girmenize gerek yoktur.
* Remote Studio'da parça ekle iletişim kutusunu kullanırken, Control+Shift+R tuşlarına basıldığında NVDA'nın "tarama başlat" demesi ve arama sonuçları durumu için ayrıntılı çıktı dahil olmak üzere çeşitli sorunlar çözüldü.
* Yaratıcı ve Parça Aracı'ndaki parça listesinde, sütun sıralama düzenini değiştirmek için Alt+sayı satırı tuşlarına basıldığında, NVDA seçilen sütuna göre yeni sıralama düzenini duyurur.
* Parça Aracı'nda, durum çubuğu komutunu okurken (NVDA+End/masaüstü düzeni, NVDA+Shift+End/dizüstü bilgisayar düzeni) durum çubuğunun içeriği duyurulacaktır.

## Eski sürümler

Eski eklenti sürümlerine ilişkin sürüm notları için lütfen [değişiklik günlüğüne][2] bakın.

[1]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
