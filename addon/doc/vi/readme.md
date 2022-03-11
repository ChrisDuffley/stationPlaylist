# StationPlaylist #

* Tác giả: Geoff Shang, Joseph Lee và các cộng tác viên khác
* Tải về [phiên bản chính thức][1]
* NVDA compatibility: 2021.3 and later

Gói add-on này cung cấp sự cải thiện cho việc sử dụng StationPlaylist Studio
và các ứng dụng StationPlaylist khác, cũng như cung cấp các tiện ích để điều
khiển Studio ở bất cứ đâu. Các ứng dụng được hỗ trợ bao gồm Studio, Creator,
Track Tool, VT Recorder và Streamer, cả các bộ mã hóa SAM, SPL và AltaCast.

For more information about the add-on, read the [add-on guide][2].

CÁC LƯU Ý QUAN TRỌNG:

* This add-on requires StationPlaylist suite 5.30 or later.
* Nếu dùng Windows 8 trở lên, hãy tắt chế độ giảm âm thanh để có trải nghiệm
  tốt nhất.
* Starting from 2018, [changelogs for old add-on releases][3] will be found
  on GitHub. This add-on readme will list changes from version 21.10 (2021)
  onwards.
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
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order.
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 từ cửa sổ Studio: mở hộp thoại cấu hình add-on của Studio.
* Alt+NVDA+P từ cửa sổ Studio: mở hộp thoại các hồ sơ phát thanh của Studio.
* Alt+NVDA+F1: mở hộp thoại chào mừng.

## Các lệnh chưa được gán thao tác

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesture you wish to use.

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
* Alt+NVDA+0 and F12: Opens encoder settings dialog to configure options
  such as encoder label.

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

## Bộ điều khiển SPL

Bộ điều khiển SPL là tập hợp các lệnh bạn có thể dùng để điều khiển SPL
Studio bất cứ đâu. Bấm các lệnh của bộ điều khiển SPL, và NVDA sẽ đọc, "bộ
điều khiển SPL." Bấm các phím lệnh khác để thực hiện nhiều cài đặt của
Studio như bật / tắt microphone hoặc phát track kế.

Các lệnh của bộ điều khiển SPL bao gồm:

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track.
* Shift+C: Title and duration of the upcoming track if any.
* E: Encoder connection status.
* I: Listener count.
* Q: Studio status information such as whether a track is playing,
  microphone is on and others.
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Layer help.

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

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

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

## Version 22.01

* If add-on specific command-line switches such as "--spl-configinmemory" is
  specified when starting NVDA, NVDA will no longer add the specified
  parameter each time NVDA and/or Studio runs. Restart NVDA to restore
  normal functionality (without command-line switches).

## Version 21.11

* Initial support for StationPlaylist suite 6.0.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Các bản phát hành cũ hơn

Vui lòng xem liên kết bản ghi các thay đổi để có thông tin về các bản phát
hành cũ của add-on.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
