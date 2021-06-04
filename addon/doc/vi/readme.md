# StationPlaylist #

* Tác giả: Geoff Shang, Joseph Lee và các cộng tác viên khác
* Tải về [phiên bản chính thức][1]
* NVDA compatibility: 2020.4 and beyond

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
  on GitHub. This add-on readme will list changes from version 20.09 (2020)
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
* Shift+F1: mở tài liệu hướng dẫn trực tuyến.

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

## Version 21.06

* NVDA will no longer do nothing or play error tones when trying to open
  various add-on dialogs such as encoder settings dialog. This is a critical
  fix required to support NVDA 2021.1.
* NVDA will no longer appear to do nothing or play error tones when trying
  to announce complete time (hours, minutes, seconds) from Studio (command
  unassigned). This affects NVDA 2021.1 or later.

## Version 21.04/20.09.7-LTS

* 21.04: NVDA 2020.4 or later is required.
* In encoders, NVDA no longer fails to announce date and time information
  when performing date/time command (NVDA+F12). This affects NVDA 2021.1 or
  later.

## Version 21.03/20.09.6-LTS

* Minimum Windows release requirement is now tied to NVDA releases.
* Removed feedback email command (Alt+NVDA+Hyphen). Please send feedback to
  add-on developers using the contact information provided from Add-ons
  Manager.
* 21.03: parts of the add-on source code now include type annotations.
* 21.03: made the add-on code more robust with help from Mypy (a Python
  static type checker). In particular, fixed several long-standing bugs such
  as NVDA not being able to reset add-on settings to defaults under some
  circumstances and attempting to save encoder settings when not
  loaded. Some prominent bug fixes were also backported to 20.09.6-LTS.
* Fixed numerous bugs with add-on welcome dialog (Alt+NVDA+F1 from Studio
  window), including multiple welcome dialogs being shown and NVDA appearing
  to do nothing or playing error tones when welcome dialog remains open
  after Studio exits.
* Fixed numerous bugs with track comments dialog (Alt+NVDA+C three times
  from a track in Studio), including an error tone heard when trying to save
  comments and many track comment dialogs appearing if Alt+NVDA+C is pressed
  many times. If track comments dialog is still shown after Studio is
  closed, comments will not be saved.
* Various column commands such as columns explorer (Control+NVDA+number row)
  in Studio tracks and encoder status announcements no longer gives
  erroneous results when performed after NVDA is restarted while focused on
  tracks or encoders. This affects NVDA 2020.4 or later.
* Fixed numerous issues with playlist snapshots (SPL Assistant, F8),
  including inability to obtain snapshot data and reporting wrong tracks as
  shortest or longest tracks.
* NVDA will no longer announce "0 items in the library" when Studio exits in
  the middle of a library scan.
* NVDA will no longer fail to save changes to encoder settings after errors
  are encountered when loading encoder settings and subsequently settings
  are reset to defaults.

## Version 21.01/20.09.5-LTS

Version 21.01 supports SPL Studio 5.30 and later.

* 21.01: NVDA 2020.3 or later is required.
* 21.01: column header inclusion setting from add-on settings has been
  removed. NVDA's own table column header setting will control column header
  announcements across SPL suite and encoders.
* Added a command to toggle screen versus custom column inclusion and order
  setting (NVDA+V). Note that this command is available only when focused on
  a track in Studio's playlist viewer.
* SPL Assistant and Controller layer help will be presented as a browse mode
  document instead of a dialog.
* NVDA will no longer stop announcing library scan progress if configured to
  announce scan progress while using a braille display.

## Version 20.11.1/20.09.4-LTS

* Initial support for StationPlaylist suite 5.50.
* Improvements to presentation of various add-on dialogs thanks to NVDA
  2020.3 features.

## Version 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 or later is required.
* 20.11: Resolved more coding style issues and potential bugs with Flake8.
* Fixed various issues with add-on welcome dialog (Alt+NVDA+F1 from Studio),
  including wrong command shown for add-on feedback (Alt+NVDA+Hyphen).
* 20.11: Column presentation format for track and encoder items across
  StationPlaylist suite (including SAM encoder) is now based on
  SysListView32 list item format.
* 20.11: NVDA will now announce column information for tracks throughout SPL
  suite regardless of "report object description" setting in NVDA's object
  presentation settings panel. For best experience, leave this setting on.
* 20.11: In Studio's playlist viewer, custom column order and inclusion
  setting will affect how track columns are presented when using object
  navigation to move between tracks, including current navigator object
  announcement.
* If vertical column announcement is set to a value other than "whichever
  column I'm reviewing", NVDA will no longer announce wrong column data
  after changing column position on screen via mouse.
* improved playlist transcripts (SPL Assistant, Shift+F8) presentation when
  viewing the transcript in HTML table or list format.
* 20.11: In encoders, encoder labels will be announced when performing
  object navigation commands in addition to pressing up or down arrow keys
  to move between encoders.
* In encoders, in addition to Alt+NVDA+number row 0, pressing F12 will also
  open encoder settings dialog for the selected encoder.

## Phiên bản 20.10/20.09.2-LTS

* Due to changes to encoder settings file format, installing an older
  version of this add-on after installing this version will cause
  unpredictable behavior.
* It is no longer necessary to restart NVDA with debug logging mode to read
  debug messages from log viewer. You can view debug messages if log level
  is set to "debug" from NVDA's general settings panel.
* In Studio's playlist viewer, NVDA will not include column headers if this
  setting is disabled from add-on settings and custom column order or
  inclusion settings are not defined.
* 20.10: column header inclusion setting from add-on settings is deprecated
  and will be removed in a future release. In the future NVDA's own table
  column header setting will control column header announcements across SPL
  suite and encoders.
* When SPL Studio is minimized to the system tray (notification area), NVDA
  will announce this fact when trying to switch to Studio from other
  programs either through a dedicated command or as a result of an encoder
  connecting.

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

## Các bản phát hành cũ hơn

Vui lòng xem liên kết bản ghi các thay đổi để có thông tin về các bản phát
hành cũ của add-on.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
