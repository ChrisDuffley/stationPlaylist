# StationPlaylist #

* Tác giả: Geoff Shang, Joseph Lee và các cộng tác viên khác
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* Tải về [phiên bản hỗ trợ lâu dài][3] - cho người dùng Studio 5.20
* NVDA tương thích: 2019.3 đến 2020.2

Gói add-on này cung cấp sự cải thiện cho việc sử dụng StationPlaylist Studio
và các ứng dụng StationPlaylist khác, cũng như cung cấp các tiện ích để điều
khiển Studio ở bất cứ đâu. Các ứng dụng được hỗ trợ bao gồm Studio, Creator,
Track Tool, VT Recorder và Streamer, cả các bộ mã hóa SAM, SPL và AltaCast.

Để biết thêm thông tin về add-on này, xem [hướng dẫn sử dụng add-on][4].

CÁC LƯU Ý QUAN TRỌNG:

* Add-on này yêu cầu bộ StationPlaylist 5.20 trở lên.
* Nếu dùng Windows 8 trở lên, hãy tắt chế độ giảm âm thanh để có trải nghiệm
  tốt nhất.
* Từ 2018, [bản ghi những thay đổi cho các bản phát hành cũ của add-on][5]
  sẽ được tìm thấy trên GitHub. Tập tin readme của add-on này sẽ liệt kê các
  thay đổi từ phiên bản 20.01 (2020 trở đi).
* Khi đang chạy Studio, bạn có thể lưu, gọi các thiết lập đã lưu hoặc khôi
  phục các thiết lập của add-on về mặc định bằng cách bấm Control+NVDA+C,
  Control+NVDA+R một lần, hoặc Control+NVDA+R ba lần. điều này cũng được áp
  dụng cho các thiết lập mã hóa - bạn có thể lưu và khôi phục (không gọi
  lại) các thiết lập mã hóa nếu đang sử dụng chúng.

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
  Remote VT và Track Tool): di chuyển đến cột trước / sau của track.
* Control+Alt+Home/End (khi đứng tại một track trong Studio, Creator, Remote
  VT và Track Tool): di chuyển đến cột đầu / cuối của track.
* Control+Alt+mũi tên lên / xuống (khi đứng tại một track trong Studio,
  Creator, Remote VTvà Track Tool): chuyển đến track trước hoặc kế và thông
  báo các cột cụ thể.
* Control+NVDA+1 đến 0 (khi đứng ở tại một track trong Studio, Creator (bao
  gồm Playlist Editor), Remote VT và Track Tool): thông báo nội dung cho một
  cột đã định. Bấm hai lần sẽ hiển thị thông tin trên cửa sổ duyệt tài liệu.
* Control+NVDA+- (trừ khi con trỏ ở một track trong Studio, Creator, Remote
  VT và Track Tool): hiển thị dữ liệu của tất cả các cột trong một track
  trên một cửa sổ ở chế độ duyệt.
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

* F9: kết nối bộ mã hóa đã chọn.
* F10 (chỉ khi dùng SAM encoder): ngắt kết nối bộ mã hóa đã chọn.
* Control+F9: kết nối tất cả bộ mã hóa.
* Control+F10 (chỉ khi dùng SAM encoder): ngắt kết nối tất cả các bộ mã hóa.
* F11: bật tắt chế độ để NVDA chuyển đến cửa sổ Studio cho bộ mã hóa được
  chọn nếu đã kết nối.
* Shift+F11: bật tắt chế độ để Studio sẽ phát track đầu tiên được chọn khi
  bộ mã hóa được kết nối đến một máy chủ đang phát.
* Control+F11: bật tắt chế độ theo dõi ngầm của bộ mã hóa được chọn.
* Control+F12: mở hộp thoại chọn bộ mã hóa đã xóa (sắp xếp lại các cài đặt
  của nhãn phát và các bộ mã hóa).
* Alt+NVDA+0: mở hộp thoại cài đặt mã hóa để cấu hình các tùy chọn như nhãn
  mã hóa.

Ngoài ra, có các lệnh để xem lại cột bao gồm:

* Control+NVDA+1: vị trí mã hóa.
* Control+NVDA+2: nhãn mã hóa.
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
* C (Shift+C trong kiểu phím lệnh của JAWS): tên của track đang phát.
* C (Kiểu phím lệnh JAWS): bật tắt cart explorer (chỉ trong trình xem danh
  sách phát).
* D (R trong kiểu phím lệnh của JAWS): thời lượng còn lại của danh sách phát
  (nếu có thông báo lỗi, di chuyển đến trình xem danh sách phát và thực hiện
  lệnh này).
* E: trạng thái truyền siêu dữ liệu.
* Shift+1 đến Shift+4, Shift+0: trạng thái của URL truyền siêu dữ liệu cụ
  thể (0 cho DSP encoder).
* F: tìm kiếm track (chỉ  khi ở trong trình xem danh sách phát).
* H: thời lượng phát nhạc của khung giờ hiện tại.
* Shift+H: thời lượng còn lại cho track của khung giờ hiện tại.
* I (L trong kiểu phím lệnh của JAWS): đếm lượt người nghe.
* K: chuyển đến track đã đánh dấu (chỉ khi ở trong trình xem danh sách
  phát).
* Control+K: chọn track hiện tại làm track đánh dấu (chỉ khi ở trong trình
  xem danh sách phát).
* L (Shift+L trong kiểu phím lệnh của JAWS): Line in.
* M: Microphone.
* N: tên của track kế được lên lịch.
* P: trạng thái phát nhạc (đang phát hay dừng).
* Shift+P: độ cao của track hiện tại.
* R (Shift+E trong kiểu phím lệnh của JAWS): bật / tắt thu ra tập tin.
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

## Phiên bản 20.09-LTS

Phiên bản 20.09.x là loạt phát hành cuối cùng hỗ trợ Studio 5.20 và dựa trên
các công nghệ cũ, các bản phát hành trong tương lai hỗ trợ Studio 5.30 và
thêm các tính năng gần đây của NVDA. Vài tính năng mới sẽ hỗ trợ ngược trở
lại 20.09.x nếu cần.

* Do các thay đổi trong NVDA, --các lệnh chuyển spl-configvolatile không còn
  dùng được để làm cho các thiết lập của add-on có thuộc tính chỉ đọc. Bạn
  có thể giả lập nó bằng cách bỏ chọn  hộp kiểm "Lưu cấu hình khi tắt NVDA"
  trong bảng cài đặt chung của NVDA.
* Đã gỡ bỏ cài đặt các tính năng thử nghiệm trong phân loại cài đặt nâng cao
  trong cài đặt add-on (Alt+NvDA+0), vốn được sử dụng cho người dùng các bản
  thử nghiệm kiểm tra các đoạn mã bleeding-edge.
* Các lệnh điều hướng bảng trong Studio giờ đã có trong danh sách track được
  tìm thấy theo yêu cầu của người nghe, chèn track và các màn hình khác.
* Nhiều lệnh điều hướng cột sẽ hoạt động như lệnh điều hướng trong bảng của
  NVDA. Bên cạnh việc đơn giản hóa các lệnh này, nó còn mang lại những lợi
  ích như dễ sử dụng hơn cho người nhìn kém.
* Các lệnh điều hướng cột theo chiều dọc (Control+Alt+mũi tên lên/xuống) giờ
  đã có trong Creator, trình biên tập danh sách phát, Remote VT và Track
  Tool.
* Lệnh xem cột của track (Control+NVDA+trừ) giờ đã có trong trình biên tập
  danh sách phát của Creator và Remote VT.
* Lệnh xem cột của track sẽ tuân thủ việc sắp xếp hiển thị cột trên màn
  hình.
* Trong SAM encoders, cải thiện khả năng phản hồi của NVDA khi bấm
  Control+F9 hay Control+F10 để kết nối hay ngắt kết nối tất cả bộ mã
  hóa. Có thể thấy kết quả của việc này trong việc tăng cấp độ khi thông báo
  thông tin bộ mã hóa được chọn.
* Trong SPL và các bộ mã hóa AltaCast, bấm F9 sẽ kết nối bộ mã hóa được
  chọn.

## Phiên bản 20.07

* Trong trình xem danh sách phát của Studio, NVDA sẽ không còn tình trạng
  không làm gì hoặc phát âm thanh báo lỗi khi nỗ lực xóa các track hay sau
  khi xóa một danh sách phát đã tại khi con trỏ ở tại trình xem danh sách
  phát.
* Khi tìm track trong hộp thoại chèn track của Studio, NVDA sẽ đọc kết quả
  tìm kiếm nếu tìm thấy chúng.
* NVDA sẽ không còn tình trạng không làm gì hoặc phát âm thanh báo lỗi khi
  chuyển đến một hồ sơ phát thanh mới tạo và lưu các thiết lập của add-on.
* Trong cài đặt mã hóa, "nhãn phát" đã được đổi tên thành "nhãn mã hóa".
* Đã gỡ bỏ lệnh riêng cho bộ nhãn phát (F12). Có thể quy định các nhãn mã
  hóa từ hộp thoại cài đặt mã hóa (Alt+NVDA+0).
* Con trỏ hệ thống sẽ không chuyển đến Studio dạng lặp đi lặp lại hay các
  track được chọn sẽ được phát khi một bộ mã hóa đang được theo dõi ngầm
  (Control+F11) cứ kết nối và ngắt kết nối.
* Trong SPL encoders, đã thêm lệnh Control+F9 để kết nối tất cả các bộ mã
  hóa (giống như lệnh F9).

## Phiên bản 20.06

* Giải quyết nhiều vấn đề về kiểu mã nguồn và các lỗi tiềm năng với Flake8.
* Sửa nhiều lỗi thông điệp nhanh hỗ trợ các bộ mã hóa trong tiếng Anh dù đã
  được dịch sang các ngôn ngữ khác.
* Tính năng các hồ sơ phát thanh theo thời gian  đã bị gỡ bỏ.
* Kiểu lệnh của Window-Eyes cho SPL Assistant đã bị gỡ bỏ. Những người dùng
  kiểu lệnh này sẽ phải chuyển sang kiểu lệnh của NVDA.
* Vì tính năng giảm âm của NVDA không có tác dụng với việc phát thanh từ
  Studio, trừ khi thiết lập vài thứ về phần cứng, hộp thoại nhắc nhớ tính
  năng này đã bị gỡ bỏ.
* Khi có lỗi trong các cài đặt mã hóa, không cần phải chuyển đến cửa sổ
  Studio để NVDA khôi phục các thiết lập về mặc định. Giờ đây bạn phải
  chuyển đến một bộ mã hóa từ cửa sổ các bộ mã hóa để NVDA khôi phục các
  thiết lập.
* Tên của hộp thoại cài đặt các bộ mã hóa cho SAM encoders giờ đây hiển thị
  định dạng mã hóa thay vì vị trí bộ mã hóa.

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

## Các bản phát hành cũ hơn

Vui lòng xem liên kết bản ghi các thay đổi để có thông tin về các bản phát
hành cũ của add-on.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
