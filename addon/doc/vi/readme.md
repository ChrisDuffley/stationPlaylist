# StationPlaylist #

* Tác giả: Geoff Shang, Joseph Lee và các cộng tác viên khác
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA tương thích: 2019.3 đến 2020.1

Gói add-on này cung cấp sự cải thiện cho việc sử dụng StationPlaylist Studio
và các ứng dụng StationPlaylist khác, cũng như cung cấp các tiện ích để điều
khiển Studio ở bất cứ đâu. Các ứng dụng được hỗ trợ bao gồm Studio, Creator,
Track Tool, VT Recorder và Streamer, cả các bộ mã hóa SAM, SPL và AltaCast.

Để biết thêm thông tin về add-on này, xem [hướng dẫn sử dụng add-on][4]. Với
những người phát triển add-on quan tâm đến việc tạo add-on, xem tập tin
buildInstructions.txt ở thư mục gốc trong mã nguồn của add-on.

CÁC LƯU Ý QUAN TRỌNG:

* Add-on này yêu cầu bộ StationPlaylist 5.20 trở lên.
* Nếu dùng Windows 8 trở lên, hãy tắt chế độ giảm âm thanh để có trải nghiệm
  tốt nhất.
* Từ 2018, [bản ghi những thay đổi cho các bản phát hành cũ của add-on][5]
  sẽ được tìm thấy trên GitHub. Tập tin readme này sẽ liệt kê các thay đổi
  từ phiên bản 18.09 (2018 trở đi).
* Vài tính năng nhất định của add-on sẽ không hoạt động trong vài điều kiện,
  bao gồm chạy NVDA trong chế độ bảo vệ.
* Vì những giới hạn kĩ thuật, bạn không thể cài hay dùng add-on này với
  phiên bản NVDA từ Windows Store.
* Các tính năng được đánh dấu "thử nghiệm" là để kiểm tra vài thứ trước khi
  phát hành rộng rãi, vậy nên chúng sẽ không được bật trong các bản phát
  hành chính thức.
* Khi đang chạy Studio, bạn có thể lưu, gọi các thiết lập đã lưu hoặc khôi
  phục các thiết lập của add-on về mặc định bằng cách bấm Control+NVDA+C,
  Control+NVDA+R một lần, hoặc Control+NVDA+R ba lần. điều này cũng được áp
  dụng cho các thiết lập mã hóa - bạn có thể lưu và khôi phục (không gọi
  lại) các thiết lập mã hóa nếu đang sử dụng chúng.
* Tính năng các hồ sơ phát thanh theo thời gian  đã được lược bỏ và sẽ được
  gỡ bỏ ở một phiên bản trong tương lai.

## Các phím tắt

Hầu hết chúng chỉ hoạt động trong Studio cho đến khi thực hiện một số thiết
lập khác.

* Alt+Shift+T từ cửa sổ Studio: thông báo thời gian đã trôi qua của track
  đang phát.
* Control+Alt+T (vuốt xuống bằng hai ngón trong chế độ cảm ứng SPL) từ cửa
  sổ Studio: thông báo thời gian còn lại của track đang phát.
* NVDA+Shift+F12 (vuốt lên hai ngón trong chế độ chạm của SPL) từ cửa sổ
  Studio: thông báo thời gian phát thanh như là 5 phút đến đầu giờ. Bấm hai
  lần sẽ thông báo số phút và giây đến đầu giờ.
* Alt+NVDA+1 (vuốt hai ngón qua trái trong chế độ SPL ) từ cửa sổ Studio: mở
  phân loại báo hiệu trong hộp thoại cấu hình add-on Studio.
* Alt+NVDA+1 từ cửa sổ Creator's Playlist Editor và Remote VT playlist
  editor: thông báo thời gian đã lên lịch cho danh sách phát đã tải.
* Alt+NVDA+2 từ cửa sổ Playlist Editor của Creator và Remote VT playlist
  editor: thông báo tổng thời gian của danh sách phát.
* Alt+NVDA+3 từ cửa sổ Studio: bật tắt cart explorer để tìm hiểu cách gán
  cart.
* Alt+NVDA+3 từ cửa sổ  Playlist Editor của Creator và Remote VT playlist
  editor: thông báo khi các track được chọn đã lên lịch phát.
* Alt+NVDA+4 từ cửa sổ Playlist Editor của Creator và Remote VT playlist
  editor: thông báo vòng xoay và phân loại đã kết hợp với danh sách phát đã
  tải.
* Control+NVDA+f từ cửa sổ Studio: mở hộp thoại để tìm một track theo tên ca
  sĩ hay bài hát. Bấm NvDA+F3 để tìm tiếp hoặc NVDA+Shift+F3 để tìm lùi.
* Alt+NVDA+R từ cửa sổ Studio: chuyển đến các cài đặt thông báo quét thư
  viện.
* Control+Shift+X từ cửa sổ Studio: đi qua các cài đặt hẹn giờ chữ nổi.
* Control+Alt+mũi tên trái phải (khi đứng ở một track trong Studio, Creator,
  Remote VT và Track Tool): thông báo các cột trước / sau của track.
* Control+Alt+Home/End (khi đứng tại một track trong Studio, Creator, Remote
  VT và Track Tool): thông báo cột đầu / cuối của track.
* Control+Alt+mũi tên lên / xuống (chỉ khi đứng ở tại một track trong
  Studio): chuyển đến track trước hoặc kế và thông báo các cột cụ thể.
* Control+NVDA+1 đến 0 (khi đứng ở tại một track trong Studio, Creator (bao
  gồm Playlist Editor), Remote VT và Track Tool): thông báo nội dung cho một
  cột đã định. Bấm hai lần sẽ hiển thị thông tin trên cửa sổ duyệt tài liệu.
* Control+NVDA+- (trừ trong Studio, Creator và Track Tool): hiển thị dữ liệu
  của tất cả các cột trong một track trên một cửa sổ ở chế độ duyệt.
* Alt+NVDA+C khi đứng tại một track (chỉ trong Studio): thông báo chú thích
  track nếu có.
* Alt+NVDA+0 từ cửa sổ Studio: mở hộp thoại cấu hình add-on của Studio.
* Alt+NVDA+P từ cửa sổ Studio: mở hộp thoại các hồ sơ phát thanh của Studio.
* Alt+NVDA+- (trừ) từ cửa sổ Studio: gửi phản hồi cho nhóm phát triển add-on
  bằng trình gửi thư điện tử mặc định.
* Alt+NVDA+F1: mở hộp thoại chào mừng.

## Các lệnh chưa được gán thao tác

Các lệnh sau mặc định không được gán thao tác; nếu muốn gán cho chúng, hãy
dùng hộp thoại quản lý thao tác để thêm các lệnh tùy biến. Để làm điều này,
từ cửa sổ Studio, mở trình đơn NVDA, tùy chỉnh, Quản lý thao tác. mở phân
loại StationPlaylist, tìm đến các lệnh chưa gán thao tác từ danh sách bên
dưới rồi chọn "Thêm", và nhập vào thao tác bạn muốn sử dụng.

* Chuyển từ một chương trình bất kì đến cửa sổ SPL Studio .
* Lệnh cho bộ điều khiển SPL.
* Thông báo trạng thái Studio như track đang phát từ một chương trình bất
  kì.
* Thông báo trạng thái kết nối mã hóa từ bất kì chương trình nào.
* SPL Assistant layer từ SPL Studio.
* Thông báo giờ bao gồm giây từ SPL Studio.
* Thông báo nhiệt độ.
* Thông báo tên track kế nếu được lên lịch.
* Thông báo tựa đề của track đang phát.
* Đánh dấu track hiện tại làm track bắt đầu phân tích track theo thời gian.
* Thực hiện phân tích thời gian track.
* Chụp ảnh danh sách phát.
* Tìm kiếm văn bản trong các cột cụ thể.
* Tìm track với  thời lượng trong khoảng thời gian cho trước thông qua tìm
  kiếm theo khoảng thời gian.
* Nhanh chóng bật hay tắt truyền siêu dữ liệu.

## Những lệnh cho thêm khi dùng các bộ mã hóa

Các phím lệnh sau  đây hoạt động khi sử dụng các bộ mã hóa:

* F9: kết nối tới một máy chủ đang phát.
* F10 (chỉ khi dùng SAM encoder): ngắt kết nối khỏi một máy chủ đang phát.
* Control+F9/Control+F10 (chỉ khi dùng SAM encoder): kết nối hay ngắt kết
  nối tất cả các bộ mã hóa.
* F11: bật tắt chế độ để NVDA chuyển đến cửa sổ Studio cho bộ mã hóa được
  chọn nếu đã kết nối.
* Shift+F11: bật tắt chế độ để Studio sẽ phát track đầu tiên được chọn khi
  bộ mã hóa được kết nối đến một máy chủ đang phát.
* Control+F11: bật tắt chế độ theo dõi ngầm của bộ mã hóa được chọn.
* F12: mở một hộp thoại để nhập nhãn tùy chỉnh cho bộ mã hóa hay chương
  trình phát được chọn.
* Control+F12: mở hộp thoại chọn bộ mã hóa đã xóa (sắp xếp lại các cài đặt
  của nhãn phát và các bộ mã hóa).
* Alt+NVDA+0: mở hộp thoại cài đặt mã hóa để cấu hình các tùy chọn như nhãn
  phát.

Ngoài ra, có các lệnh để xem lại cột bao gồm:

* Control+NVDA+1: vị trí mã hóa.
* Control+NVDA+2: nhãn phát thanh.
* Control+NVDA+3 từ SAM Encoder: định dạng mã hóa.
* Control+NVDA+3 từ SPL và AltaCast Encoder: cài đặt mã hóa.
* Control+NvDA+4 từ SAM Encoder: trạng thái kết nối bộ mã hóa.
* Control+NVDA+4 từ SPL và AltaCast Encoder: tốc độ đường truyền hay trạng
  thái kết nối.
* Control+NVDA+5 từ SAM Encoder: mô tả trạng thái kết nối.

## SPL Assistant layer

Các lệnh này cho phép bạn thu thập nhiều trạng thái khác nhau trên SPL
Studio, như là một track đang phát, thời lượng của tất cả track trong khung
giờ và nhiều nữa. Từ bất cứ cửa sổ SPL Studio nào, bấm các lệnh SPL
Assistant layer rồi bấm một trong các phím trong danh sách dưới đây (một hay
nhiều lệnh chỉ dành riêng cho trình xem danh sách phát). Bạn cũng có thể cấu
hình NvDA để mô phỏng lệnh theo kiểu của các trình đọc màn hình khác.

Các lệnh được hỗ trợ bao gồm:

* A: tự động hóa.
* C (Shift+C trong kiểu phím lệnh của JAWS và Window-Eyes): tên của track
  đang phát.
* C (Kiểu phím lệnh JAWS và Window-Eyes): bật tắt cart explorer (chỉ trong
  trình xem danh sách phát).
* D (R trong kiểu phím lệnh của JAWS): thời lượng còn lại của danh sách phát
  (nếu có thông báo lỗi, di chuyển đến trình xem danh sách phát và thực hiện
  lệnh này).
* `E (G trong kiểu phím lệnh Window-Eyes): trạng thái truyền siêu dữ liệu.
* Shift+1 đến Shift+4, Shift+0: trạng thái của URL truyền siêu dữ liệu cụ
  thể (0 cho DSP encoder).
* E (kiểu phím lệnh của Window-Eyes): thời gian đã phát của track hiện tại.
* F: tìm kiếm track (chỉ  khi ở trong trình xem danh sách phát).
* H: thời lượng phát nhạc của khung giờ hiện tại.
* Shift+H: thời lượng còn lại cho track của khung giờ hiện tại.
* I (L trong kiểu phím lệnh của JAWS hay Window-Eyes): lượt người nghe.
* K: chuyển đến track đã đánh dấu (chỉ khi ở trong trình xem danh sách
  phát).
* Control+K: chọn track hiện tại làm track đánh dấu (chỉ khi ở trong trình
  xem danh sách phát).
* L (Shift+L trong kiểu phím lệnh của JAWS và Window-Eyes): Line in.
* M: Microphone.
* N: tên của track kế được lên lịch.
* P: trạng thái phát nhạc (đang phát hay dừng).
* Shift+P: độ cao của track hiện tại.
* R (Shift+E trong kiểu phím lệnh của JAWS và Window-Eyes): bật / tắt thu ra
  tập tin.
* Shift+R: theo dõi tiến trình quét thư viện.
* S: Track bắt đầu (được lên lịch).
* Shift+S: thời gian đến khi sẽ phát track được chọn (track bắt đầu).
* T: bật / tắt chèn / chỉnh sửa Cart.
* U: Studio tăng thời gian.
* W: thời tiết và nhiệt độ nếu được cấu hình.
* Y: trạng thái chỉnh sửa danh sách phát.
* `F8: lấy ảnh chụp danh sách phát (số track, track dài nhất, v...v....).
* Shift+F8: yêu cầu bảng điểm danh sách phát ở nhiều định dạng.
* F9: đánh dấu track hiện tại là nơi bắt đầu phân tích danh sách phát (chỉ
  khi ở trong trình xem danh sách phát).
* F10: thực hiện phân tích track theo thời gian (chỉ khi ở trong trình xem
  danh sách phát).
* F12: chuyển đổi giữa hồ sơ hiện tại và hồ sơ được chỉ định trước.
* F1: trợ giúp phím lệnh.
* Shift+F1: mở tài liệu hướng dẫn trực tuyến.

## Bộ điều khiển SPL

Bộ điều khiển SPL là tập hợp các lệnh bạn có thể dùng để điều khiển SPL
Studio bất cứ đâu. Bấm các lệnh của bộ điều khiển SPL, và NVDA sẽ đọc, "bộ
điều khiển SPL." Bấm các phím lệnh khác để thực hiện nhiều cài đặt của
Studio như bật / tắt microphone hoặc phát track kế.

Các lệnh của bộ điều khiển SPL bao gồm:

* Bấm P để phát track kế được chọn.
* Bấm U để tạm dừng và tiếp tục phát.
* Bấm S để dừng một track nhỏ dần, hoặc dừng nhanh một track, bấm T.
* Bấm M hay Shift+M để bật / tắt microphone, hoặc bấm N để bật microphone mà
  không có hiệu ứng fade.
* Bấm A để bật tự động hóa hoặc Shift+A để tắt.
* Bấm L để bật đầu vào line-in hoặc Shift+L để tắt.
* Bấm R để biết thời gian còn lại của track đang phát.
* Bấm Shift+R để xem báo cáo về tiến trình quét thư viện.
* Bấm C để NVDA thông báo tên và thời lượng của track đang phát.
* Bấm Shift+C để NVDA thông báo tên và thời lượng của track sắp tới nếu có.
* Bấm E để biết bộ mã hóa nào đã kết nối.
* Bấm I để thu thập số lượng người nghe.
* Bấm Q để thu thập nhiều thông tin trạng thái về Studio bao gồm việc có một
  track đang phát, microphone đang bật và các thông tin khác.
* Bấm các phím cart (ví dụ F1, Control+1) để phát cart được gán từ bất cứ
  đâu.
* Bấm H để hiện hộp thoại trợ giúp với toàn bộ các lệnh được liệt kê.

## Báo hiệu track và microphone

Mặc định, NvDA sẽ phát tiếng beep nếu track còn 5 giây (ở cuối track) hoặc
đầu track, hoặc microphone đã được kích hoạt một thời gian. Để thiết lập báo
hiệu track và microphone, bấm Alt+NVDA+1 để mở cài đặt báo hiệu trong cài
đặt Studio add-on. Cái này cũng có thể dùng để cấu hình khi nghe tiếng beep,
một thông điệp hoặc cả hai khi báo hiệu đã được bật.

## Tìm kiếm track

Nếu muốn nhanh chóng tìm kiếm một bài hát theo tên hay theo ca sĩ, từ danh
sách track, bấm Control+NVDA+F. Nhập hoặc chọn tên ca sỉ hay tên bài
hát. NVDA sẽ đưa bạn đến bài hát nếu tìm thấy hoặc hiển thị thông báo lỗi
nếu không tìm thấy bài hát đó. Để tìm lại bài hát hay ca sĩ đã tìm trước đó,
bấm NVDA+F3 hoặc NVDA+Shift+F3 để tìm tiếp hay tìm lùi.

Lưu ý: tìm kiếm track có phân biệt chữ hoa / thường.

## Khám phá cart

Tùy vào phiên bản, SPL Studio cho phép gán đến 96 cart cho việc phát
thanh. NVDA cho phép bạn nghe để biết cart, hay tiếng chuông nào được gán
cho các  lệnh này.

Để xem các  cart được gán, từ SPL Studio, bấm Alt+NVDA+3. Bấm lệnh của cart
một lần sẽ cho biết tiếng chuông nào được gán cho lệnh đó. Bấm hai lần sẽ
phát tiếng chuông. Bấm Alt+NvDA+3 để thoát cart explorer. Xem hướng dẫn sử
dụng add-on để biết thêm thông tin về cart explorer.

## Phân tích thời gian track

Để biết tổng thời lượng phát các track được chọn, đánh dấu track hiện tại
làm điểm bắt đầu phân tích thời gian track (SPL Assistant, F9), rồi bấm SPL
Assistant, F10 khi kết thúc vùng chọn.

## Khám phá các cột

Bấm Control+NVDA+1 đến 0, bạn có thể thu thập các nội dung của các cột cụ
thể. Mặc định là mười cột đầu tiên (trong Studio: ca sĩ, tựa đề, thời lượng,
nhạc dạo, nhạc kết thúc, loại, năm, album, thể loại, trạng thái) cho
playlist editor trong Creator và Remote VT client, dữ lieu các cột phụ thuộc
vào việc sắp xếp cột được hiển thị trên màn hình. Trong Studio, danh sách
các track chính của Creator và track tool, các cột được xếp theo sắp xếp cột
trên màn hình và có thể cấu hình trong hộp thoại cài đặt add-on, ở phân loại
khám phá cột.

## Ảnh chụp danh sách phát

Bạn có thể bấm SPL Assistant, F8 khi đứng ở tại một danh sách phát trong
Studio để thu thập nhiều thông tin thống kê về danh sách phát đó, bao gồm số
track trong danh sách phát, track dài nhất, ca sĩ tiêu biểu và nhiều
nữa. Sau khi gán một lệnh tùy chỉnh cho tính năng này, bấm phím lệnh đó hai
lần để NVDA trình bày thông tin ảnh chụp của danh sách phát như một trang
web và bạn có thể dùng chế độ duyệt để di chuyển (bấm escape để đóng).

## Bảng điểm của danh sách phát

Bấm SPL Assistant, Shift+F8 sẽ mở một hộp thoại cho phép bạn yêu cầu bảng
điểm của danh sách phát ở nhiều định dạng, bao gồm văn bản thô, bảng HTML
hoặc một danh sách.

## Hộp thoại cấu hình

Từ cửa sổ studio, bạn có thể bấm Alt+NVDA+0 để mở hộp thoại cấu hình
add-on. Cách khác, vào trình đơn tùy chỉnh của NVDA và chọn mục Cài đặt SPL
Studio. Hộp thoại này cũng dùng để quản lý các hồ sơ phát thanh.

## Hộp thoại hồ sơ phát thanh

Bạn có thể lưu các thiết lập cụ thể cho các chương trình biểu diễn cụ thể
vào các hồ sơ phát thanh. Chúng có thể được quản lý qua hộp thoại các hồ sơ
phát thanh SPL, có thể truy cập bằng cách bấm Alt+NVDA+P từ cửa sổ Studio.

## Chế độ chạm của SPL

Nếu dùng Studio trên một máy tính cảm ứng chạy Windows 8 trở lên và cài đặt
NVDA 2012.3 trở lên, bạn có thể thực hiện vài lệnh của Studio từ mành hình
cảm ứng. Trước tiên, dùng thao tác chạm ba ngón để chuyển sang chế độ SPL,
và sử dụng các thao tác cảm ứng đã liệt kê ở trên để thực hiện các lệnh.

## Phiên bản 20.05

* Bắt đầu hỗ trợ cho Remote VT (voice track) client, bao gồm remote playlist
  editor với các lệnh giống như Creator's playlist editor.
* Những lệnh dùng để mở các hộp thoại cài đặt báo hiệu riêng lẻ (Alt+NVDA+1,
  Alt+NVDA+2, Alt+NVDA+4) đã được gom lại thành Alt+NvDA+1 và giờ đây sẽ mở
  cài đặt báo hiệu trong cài đặt SPL add-on, nơi có thể tìm thấy cài đặt
  giới thiệu / kết thúc track và microphone.
* Ở hộp thoại các tác nhân được tìm thấy trong hộp thoại hồ sơ phát thanh,
  gỡ bỏ giao diện người dùng được gắn với tính năng hồ sơ phát thanh theo
  thời gian như các ô chuyển hồ sơ theo ngày / giờ / thời lượng.
* Đã gỡ bỏ các thiết lập chuyển hồ sơ đếm ngược được tìm thấy trong hộp
  thoại hồ sơ phát thanh.
* Vì Window-Eyes không còn được hỗ trợ bởi Vispero từ 2017, kiểu phím lệnh
  SPL Assistant cho Window-Eyes đã được lược đi và sẽ bị gỡ bỏ ở một phiên
  bản trong tương lai của add-on. Một cảnh báo sẽ hiển thị khi khởi động yêu
  cầu người dùng thay đổi kiểu lệnh SPL Assistant sang kiểu lệnh của NVDA
  (mặc định) hay JAWS.
* Khi dùng các lệnh khám phá cột (Control+NvDA+phím số) hay các lệnh điều
  hướng cột (Control+Alt+home/end/mũi tên trái/phải) trong Creator và Remote
  VT client, NVDA sẽ không còn tình trạng thông báo sai cột dữ liệu sau khi
  thay đổi vị trí cột trên màn hình bằng chuột.
* Trong các bộ mã hóa và Streamer, NVDA sẽ không còn tình trạng không làm gì
  hoặc phát âm thanh báo lỗi khi khởi động trong lúc một cửa sổ mã hóa đang
  có focus.

## Phiên bản 20.04

* Tính năng các hồ sơ phát thanh theo thời gian đã được lược bỏ. Sẽ có một
  thông điệp cảnh báo hiện lên ở lần khởi động Studio đầu tiên sau khi cài
  đặt add-on 20.04 trong trường hợp bạn đã quy định một hay một vài hồ sơ
  phát thanh theo thời gian.
* Việc quản lý các hồ sơ phát thanh đã được tách từ hộp thoại cài đặt add-on
  SPL thành một hộp thoại riêng. Bạn có thể truy cập hộp thoại này bằng cách
  bấm Alt+NVDA+P từ cửa sổ Studio.
* Vì sự trùng lặp với các lệnh Control+NVDA+phím số của Studio tracks, các
  lệnh khám phá cột từ SPL Assistant (phím số) đã bị gỡ bỏ.
* Thay đổi thông điệp báo lỗi hiển thị khi nỗ lực mở một hộp thoại cài đặt
  add-on của Studio (hộp thoại truyền siêu dữ liệu chẳng hạn) trong khi một
  hộp thoại cài đặt khác (hộp thoại báo hiệu cuối track chẳng hạn) đang hoạt
  động. Thông điệp báo lỗi mới giống với thông điệp hiển thị khi nỗ lực mở
  nhiều hộp thoại cài đặt của NVDA.
* NVDA sẽ không còn phát âm thanh báo lỗi hoặc không làm gì khi bấm nút OK
  từ hộp thoại khám phá côt sau khi cấu hình các phần của cột.
* Trong các bộ mã hóa, giờ bạn có thể lưu và phục hồi các thiết lập của bộ
  mã hóa (bao gồm nhãn phát thanh) bằng cách bấm Control+NVDA+C hay
  Control+NVDA+R nhanh ba lần.

## Phiên bản 20.03

* Hộp thoại khám phá cột giờ đây sẽ mặc định thông báo 10 cột đầu tiên (các
  cài đặt có sẵn vẫn sẽ dung thiết lập cũ).
* Đã bỏ tính năng tự thông báo tên của track đang phát ở các cửa sổ khác
  Studio. Tính năng này được giới thiệu trong add-on 5.6 như một giải pháp
  cho Studio 5.1x, nó không còn hoạt động nữa. Người dùng giờ đây phải sử
  dụng lệnh của SPL Controller hay Assistant layer để nghe tên của  track
  đang phát từ bất cứ đâu (C).
* Do việc gỡ bỏ tính năng tự thông báo tên của track đang phát, phần thiết
  lập cho tính năng này cũng được gỡ bỏ trong bản cài đặt add-on.
* Trong các bộ mã hóa, NVDA sẽ phát âm báo kết nối mỗi nửa giây khi một bộ
  mã hóa đang kết nối.
* Trong các bộ mã hóa, NVDA giờ đây sẽ đọc thông điệp đang kết nối cho đến
  khi thật sự có một bộ mã hóa được kết nối. Trước đây NVDA bị dừng khi có
  lỗi xảy ra.
* Một thiết lập mới đã được thêm vào bảng cài đặt mã hóa để NVDA đọc thông
  điệp đang kết nối cho đến khi bộ mã hóa đã chọn được kết nối. Thiết lập
  này mặc định được bật.

## Phiên bản 20.02

* Bắt đầu hỗ trợ cho StationPlaylist Creator's Playlist Editor.
* Đã thêm các lệnh Alt+NVDA+phím số để thông báo nhiều thông tin trạng thái
  trong Playlist Editor. Chúng bao gồm ngày và giờ cho danh sách phát (1),
  tổng thời gian danh sách phát (2), khi track được chọn đã lên lịch phát
  (3), vòng xoay và phân loại (4).
* Khi đứng ở một track trong Creator và Track Tool (ngoại trừ trong
  Creator's Playlist Editor), bấm Control+NVDA+trừ sẽ hiển thị dữ liệu của
  tất cả các cột trên một cửa sổ chế độ duyệt.
* Nếu NVDA nhận ra một thành phần trong danh sách track có ít hơn 10 cột,
  NVDA sẽ không thông báo tiêu đề các cột không tồn tại khi bấm
  Control+NVDA+các số ngoài vùng có tiêu đề cột.
* Trong creator, NVDA sẽ không còn thông báo thông tin cột nếu bấm
  Control+NVDA+các phím số khi không đứng tại danh sách track.
* Khi một track đang phát, NVDA sẽ không còn thông báo "không có track nào
  đang phát" nếu lấy thông tin về track hiện tại và kế tiếp thông qua SPL
  Assistant hay SPL Controller.
* Nếu một hộp thoại tùy chỉnh báo hiệu (nhạc hiệu, nhạc kết thúc,
  microphone) được mở, NVDA sẽ không còn phát âm thanh báo lỗi hoặc không
  làm gì nếu dự định mở một hộp thoại báo hiệu thứ hai.
* Khi nỗ lực chuyển giữa hồ sơ đang hoạt động và một hồ sơ chuyển nhanh
  thông qua SPL Assistant (F12), NVDA sẽ hiện một thông điệp nếu làm vậy khi
  đang mở màn hình cài đặt add-on.
* Trong các bộ mã hóa, NVDA sẽ không còn quên áp dụng âm báo không có kết
  nối cho các bộ mã hóa khi NVDA bị khởi động lại.

## Phiên bản 20.01

* Yêu cầu NVDA 2019.3 trở lên vì sử dụng Python 3.

## Phiên bản 19.11.1/18.09.13-LTS

* Bắt đầu hỗ trợ cho StationPlaylist suite 5.40.
* Trong Studio, ảnh chụp danh sách phát (SPL Assistant, F8) và nhiều lệnh
  báo thời gian như thời gian còn lại (Control+Alt+T) sẽ không còn làm NVDA
  phát các âm thanh báo lỗi hoặc không làm gì nếu dùng NVDA 2019.3 hay cao
  hơn.
* Trong các thành phần danh sách track của Creator, cột "ngôn ngữ" được thêm
  trong Creator 5.31 và cao hơn nhận dạng đúng.
* Nhiều danh sách trong Creator ngoài danh sách track, NVDA sẽ không còn đọc
  các thông tin cột lẻ nếu bấm các lệnh có Control+NVDA+các phím số.

## Phiên bản 19.11

* Lệnh trạng thái mã hóa từ bộ điều khiển SPL (E ) sẽ thông báo trạng thái
  kết nối cho các bộ mã hóa đang hoạt động thay vì một bộ mã hóa đang được
  theo dõi ngầm.
* NVDA sẽ không còn tình trạng không làm gì hoặc phát âm thanh báo lỗi khi
  khởi động trong lúc một cửa sổ mã hóa đang có focus.

## Phiên bản 19.10/18.09.12-LTS

* Rút gọn thông điệp thông báo phiên bản cho Studio khi nó khởi động.
* Thông tin phiên bản cho Creator sẽ được thông báo khi nó khởi động.
* 19.10: lệnh tùy chỉnh có thể gán được cho lệnh trạng thái mã hóa từ SPL
  Controller (E) nên có thể dùng ở mọi nơi.
* Bước đầu hỗ trợ cho  bộ mã hóa AltaCast (Winamp plugin và phải được Studio
  nhận dạng). Các lệnh giống với bộ mã hóa SPL.

## Phiên bản 19.08.1

* Trong các bộ mã hóa SAM, NVDA sẽ không còn tình trạng không làm gì hoặc
  phát âm thanh báo lỗi nếu một bộ mã hóa bị xóa khi đang được theo dõi
  ngầm.

## Phiên bản 19.08/18.09.11-LTS

* 19.08: yêu cầu NVDA 2019.1 trở lên.
* 19.08: NVDA sẽ không còn tình trạng không làm gì hoặc phát âm thanh báo
  lỗi khi khởi động lại mà hộp thoại cài đặt Studio add-on còn mở.
* NVDA sẽ nhớ các thiết lập riêng biệt cho hồ sơ khi chuyển giữa các bản cài
  đặt, thậm chí là sau khi đổi tên hồ sơ được chọn hiện tại từ cài đặt
  add-on.
* NVDA sẽ không còn quên các thay đổi của các hồ sơ theo thời gian khi bấm
  nút Đồng ý để đóng cài đặt add-on. Lỗi này đã xuất hiện từ khi chuyển vào
  cài đặt nhiều trang trong nằm 2018.

## Phiên bản 19.07/18.09.10-LTS

* Đổi tên add-on từ "StationPlaylist Studio" thành "StationPlaylist" để mô
  tả tốt hơn các ứng dụng và tính năng được hỗ trợ bởi add-on này.
* Các cải tiến bảo mật bên trong.
* Nếu báo hiệu microphone hoặc các thiết lập truyền siêu dữ liệu bị thay đổi
  từ cài đặt add-on, NVDA sẽ không còn bị lỗi áp dụng các thiết lập đã thay
  đổi. Điều này khắc phục lỗi khi báo hiệu microphone không khởi động hoặc
  bị dừng ngay sau khi thay đổi các thiết lập  thông qua cài đặt add-on.

## Phiên bản 19.03/18.09.7-LTS

Phiên bản 19.06 hỗ trợ SPL Studio 5.20 trở lên.

* Bắt đầu hỗ trợ cho StationPlaylist Streamer.
* Khi đang chạy các ứng dụng Studio như Track Tool và Studio, nếu có một ứng
  dụng nhanh thứ hai được gọi chạy rồi tắt, NVDA sẽ không còn làm cho cấu
  hình Studio add-on thông báo lỗi và dừng hoạt động.
* Thêm nhãn cho nhiều tùy chọn trong hộp thoại SPL Encoder configuration.

## Phiên bản 19.04.1

* Khắc phục vài lỗi với việc thiết kế lại thông báo cột và bảng điểm danh
  sách phát trong cài đặt add-on, bao gồm các thay đổi để tùy chỉnh sắp xếp
  cột và bao gồm cả việc không có phản hồi khi lưu hay chuyển giữa các bản.

## Phiên bản 19.04/18.09.8-LTS

* Nhiều lệnh toàn cục như vào bảng điều khiển SPL và chuyển đến cửa sổ
  Studio sẽ bị tắt nếu chạy NVDA trong chế độ bảo vệ hay một ứng dụng từ
  Windows Store.
* 19.04: trong thông báo cột và bảng điểm danh sách phát (cài đặt add-on),
  các điều khiển bao gồm tùy chỉnh/sắp xếp cột sẽ hiện ra luôn thay vì phải
  bấm nút mở một hộp thoại để cấu hình các cài đặt này.
* Trong Creator, NVDA sẽ không còn phát âm thanh báo lỗi hoặc không làm gì
  khi focus ở một số danh sách nhất định.

## Phiên bản 19.03/18.09.7-LTS

* Bấm Control+NVDA+R để gọi lại các thiết lập đã lưu giờ đây cũng sẽ gọi lại
  các thiết lập của Studio add-on, và bấm lệnh này ba lần cũng sẽ khôi phục
  các cài đặt của Studio add-on về mặc định cùng với thiết lập của NVDA.
* Đổi tên hộp thoại cài đặt Studio add-on "Tùy chọn nâng cao" thành "Nâng
  cao".
* 19.03 (thử nghiệm): trong thông báo cột và bảng điểm danh sách phát (cài
  đặt add-on), các tùy chỉnh bao gồm tùy chỉnh/sắp xếp cột sẽ hiện ra luôn
  thay vì phải bấm nút mở một hộp thoại để cấu hình các cài đặt này.

## Phiên bản 19.02

* Gỡ bỏ tính năng độc lập kiểm tra cập nhật add-on, bao gồm lệnh kiểm tra
  cập nhật từ SPL Assistant (Control+Shift+U) và tùy chọn kiểm tra cập nhật
  add-on từ cài đặt add-on. Giờ đây, tính năng này sẽ được thực hiện bởi
  Add-on Updater (Cập nhật add-on).
* NVDA sẽ không còn tình trạng không làm gì hoặc phát âm thanh báo lỗi khi
  khoảng thời gian hoạt động của microphone được thiết lập, dùng để nhắc nhớ
  các phát thanh viên rằng microphone đang hoạt động bằng một tiếng beep
  ngắn.
* Khi khôi phục các cài đặt add-on từ hộp thoại cài đặt add-on / bảng khôi
  phục cài đặt, NVDA sẽ hỏi thêm một lần nữa nếu có một hồ sơ chuyển nhanh
  hay hồ sơ theo thời gian đang được kích hoạt.
* Sau khi khôi phục các cài đặt của Studio add-on, NvDA sẽ tắt hẹn giờ
  chuông báo microphone và thông báo trạng thái truyền siêu dữ liệu, tương
  tự như sau khi chuyển giữa các hồ sơ phát thanh.

## Phiên bản 19.01.1

* NVDA sẽ không còn thông báo "Đang theo dõi việcquét thư viện" sau khi đóng
  Studio trong vài trường hợp.

## Phiên bản 19.01/18.09.6-LTS

* Yêu cầu NVDA 2018.4 trở lên.
* Nhiều thay đổi mã nguồn để add-on tương thích hơn với Python 3.
* 19.01: vài thông điệp cho phiên dịch từ add-on này sẽ giống với thông điệp
  của NVDA.
* 19.01: tính năng kiểm tra cập nhật add-on không còn nữa. Thông điệp báo
  lỗi sẽ hiển thị khi dùng SPL Assistant, Control+Shift+U để kiểm tra cập
  nhật. Với các bản cập nhật trong tương lai, vui lòng dùng Add-on Updater.
* Cải thiện nhẹ hiệu suất vận hành khi dùng NVDA với các ứng dụng khác trong
  khi đã kích hoạt Voice Track Recorder. NVDA sẽ vẫn thể hiện các vấn đề
  hiệu suất khi dùng Studio và Voice Track Recorder được kích hoạt.
* Trong các bộ mã hóa, nếu một hộp thoại cài đặt mã hóa được mở
  (Alt+NVDA+0), NVDA sẽ hiện thông điệp báo lỗi nếu mở thêm hộp thoại cài
  đặt mã hóa khác.

## Phiên bản 18.12

* Những thay đổi bên trong để add-on tương thích hơn với các bản phát hành
  trong tương lai của NVDA.
* Sửa nhiều lỗi thông điệp nhanh của add-on trong tiếng Anh dù đã được dịch
  sang các ngôn ngữ khác.
* If using SPL Assistant to check for add-on updates (SPL Assistant,
  Control+Shift+U), NVDA will not install new add-on releases if they
  require a newer version of NVDA.
* Vài lệnh SPL Assistant giờ đây yêu cầu trình xem danh sách phát phải hiển
  thị, có một danh sách phát và trong vài trường hợp, phải đứng tại một
  track. Các lệnh chịu ảnh hưởng bao gồm thời gian còn lại (D), ảnh chụp
  danh sách phát (F8) và bảng điểm danh sách phát (Shift+F8).
* Lệnh xem thời gian còn lại của danh sách phát (SPL Assistant, D) giờ đây
  yêu cầu phải đứng tại  một track trong trình xem danh sách phát.
* Trong SAM Encoders, giờ bạn có thể dùng các lệnh điều hướng trong bảng
  (Control+Alt+các phím mũi tên) để xem lại nhiều thông tin trạng thái mã
  hóa.

## Phiên bản 18.11/18.09.5-LTS

Lưu ý: 18.11.1 thay thế 18.11 nhằm cung cấp những hỗ trợ đắc lực hơn cho
Studio 5.31.

* Bắt đầu hỗ trợ cho StationPlaylist Studio 5.31.
* Giờ bạn có thể thu thập các ảnh chụp (SPL Assistant, F8) và bảng điểm danh
  sách phát (SPL Assistant, Shift+F8) khi một danh sách phát được mở nhưng
  con trỏ không đứng ở tack đầu tiên.
* NVDA sẽ không còn tình trạng không làm gì hoặc phát âm thanh báo lỗi khi
  cố gắng thông báo trạng thái truyền siêu dữ liệu khi khởi độn Studio nếu
  đã được cấu hình như vậy.
* Nếu được cấu hình để thông báo trạng thái truyền siêu dữ liệu khi khởi
  động Studio, việc thông báo trạng thái metadata streaming sẽ không còn bỏ
  đi các thông báo thay đổi thanh trạng thái và ngược lại.

## Phiên bản 18.10.2/18.09.4-LTS

* Sửa lỗi không đóng được màn hình cài đặt add-on nếu đã bấm nút Áp dụng và
  và sau đó lại bấm nút Đồng ý hay Hủy.

## Phiên bản 18.10.1/18.09.3-LTS

* Giải quyết vài trục trặc liên quan đến tính năng thông báo kết nối bộ mã
  hóa, bao gồm việc không thông báo thông điệp trạng thái, không phát track
  đầu tiên được chọn hoặc không chuyển đến cửa sổ Studio khi đã kết
  nối. Những lỗi này gây ra bởi wxPython 4 (NVDA 2018.3 trở lên).

## Phiên bản 18.10

* Yêu cầu NVDA 2018.3 trở lên.
* Những thay đổi bên trong để add-on tương thích hơn với Python 3.

## Phiên bản 18.09.1-LTS

* Khi lấy thông tin bảng điểm danh sách phát ở định dạng bảng HTML, Các tiêu
  đề cột không còn bị chuyển thành dạng giống danh sách chuỗi của Python.

## Phiên bản 18.09-LTS

Phiên bản 18.09.x là loạt phát hành cuối cùng hỗ trợ Studio 5.10 và dựa trên
các công nghệ cũ, với 18.10 trở lên hỗ trợ Studio 5.11/5.20 và các tính năng
mới. Vài tính năng mới sẽ hỗ trợ ngược trở lại 18.09.x nếu cần.

* Khuyến khích dùng NVDA 2018.3 trở lên vì sử dụng wxPython 4.
* Màn hình cài đặt Add-on giờ đây đã hiển thị trên giao diện nhiều trang bắt
  nguồn từ NVDA 2018.2 trở lên.
* Test Drive Fast và Slow rings đã được gom lại thành kênh "development"
  (thử nghiệm), với tùy chọn cho người dùng các bản đang phát triển kiểm tra
  các tính năng thử nghiệm bằng cách chọn vào hộp kiểm các tính năng thử
  nghiệm trong cài đặt nâng cao của add-on. Người dùng ở kênh Test Drive
  Fast ring sẽ tiếp tục kiểm tra các tính năng thử nghiệm.
* Đã gỡ bỏ tính năng chọn các kênh  cập nhật add-on khác nhau từ cài đặt
  add-on. Người dùng muốn chuyển sang kênh phát hành khác phải vào trang
  cộng đồng NVDA add-on (addons.nvda-project.org), chọn StationPlaylist
  Studio rồi tải bản phát hành mong muốn.
* Các dấu kiểm để bao gồm cột cho việc thông báo cột và bảng điểm danh sách
  phát, kể cả các hộp kiểm cho truyền siêu dữ liệu cũng đã được chuyển sang
  dạng checkable (tạm dịch: có thể chọn).
* Khi chuyển qua lại giữa các bản cài đặt, NvDA sẽ nhớ các thiết lập hiện
  tại cho các cài đặt hồ sơ cụ thể (báo hiệu, thông báo cột, cài đặt cho
  truyền siêu dữ liệu).
* Thêm định dạng CSV (dùng dấu phẩy ngăn cách các giá trị) như một định dạng
  cho bảng điểm của danh sách phát.
* Bấm Control+NvDA+C để lưu thiết lập sẽ lưu luôn thiết lập của Studio
  add-on (yêu cầu NVDA 2018.3).

## Các bản phát hành cũ hơn

Vui lòng xem liên kết bản ghi các thay đổi để có thông tin về các bản phát
hành cũ của add-on.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
