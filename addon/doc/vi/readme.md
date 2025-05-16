# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Gói add-on này cung cấp sự cải thiện cho việc sử dụng StationPlaylist Studio
và các ứng dụng StationPlaylist khác, cũng như cung cấp các tiện ích để điều
khiển Studio ở bất cứ đâu. Các ứng dụng được hỗ trợ bao gồm Studio, Creator,
Track Tool, VT Recorder và Streamer, cả các bộ mã hóa SAM, SPL và AltaCast.

For more information about the add-on, read the [add-on guide][1].

CÁC LƯU Ý QUAN TRỌNG:

* This add-on requires StationPlaylist suite 5.50 or later.
* Some add-on features will be disabled or limited if NVDA is running in
  secure mode such as in logon screen.
* For best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][2] will be found
  on GitHub. This add-on readme will list changes from version 23.02 (2023)
  onwards.
* Khi đang chạy Studio, bạn có thể lưu, gọi các thiết lập đã lưu hoặc khôi
  phục các thiết lập của add-on về mặc định bằng cách bấm Control+NVDA+C,
  Control+NVDA+R một lần, hoặc Control+NVDA+R ba lần. điều này cũng được áp
  dụng cho các thiết lập mã hóa - bạn có thể lưu và khôi phục (không gọi
  lại) các thiết lập mã hóa nếu đang sử dụng chúng.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Các phím tắt

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA+Shift+F12 (vuốt lên hai ngón trong chế độ chạm của SPL) từ cửa sổ
  Studio: thông báo thời gian phát thanh như là 5 phút đến đầu giờ. Bấm hai
  lần sẽ thông báo số phút và giây đến đầu giờ.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 từ cửa sổ Creator's Playlist Editor và Remote VT playlist
  editor: thông báo thời gian đã lên lịch cho danh sách phát đã tải.
* Alt+NVDA+2 từ cửa sổ Playlist Editor của Creator và Remote VT playlist
  editor: thông báo tổng thời gian của danh sách phát.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 từ cửa sổ  Playlist Editor của Creator và Remote VT playlist
  editor: thông báo khi các track được chọn đã lên lịch phát.
* Alt+NVDA+4 từ cửa sổ Playlist Editor của Creator và Remote VT playlist
  editor: thông báo vòng xoay và phân loại đã kết hợp với danh sách phát đã
  tải.
* Control+NVDA+F from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward (does not support speak on demand).
* Shift+NVDA+R from Studio window: Steps through library scan announcement
  settings (does not support speak on demand).
* Control+Shift+X from Studio window: Steps through braille timer settings
  (does not support speak on demand).
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column (does not
  support speak on demand).
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns (does not support speak on demand).
* Control+NVDA+1 đến 0 (khi đứng ở tại một track trong Studio, Creator (bao
  gồm Playlist Editor), Remote VT và Track Tool): thông báo nội dung cho một
  cột đã định. Bấm hai lần sẽ hiển thị thông tin trên cửa sổ duyệt tài liệu.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Các lệnh chưa được gán thao tác

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesture you wish to use.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* SPL Controller layer (unavailable in secure mode).
* Announcing Studio status such as track playback from other programs
  (unavailable in secure mode).
* Announcing encoder connection status from any program (unavailable in
  secure mode).
* SPL Assistant layer từ SPL Studio.
* Thông báo giờ bao gồm giây từ SPL Studio.
* Thông báo nhiệt độ.
* Thông báo tên track kế nếu được lên lịch.
* Thông báo tựa đề của track đang phát.
* Đánh dấu track hiện tại làm track bắt đầu phân tích track theo thời gian.
* Thực hiện phân tích thời gian track.
* Chụp ảnh danh sách phát.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Những lệnh cho thêm khi dùng các bộ mã hóa

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: kết nối bộ mã hóa đã chọn.
* F10 (chỉ khi dùng SAM encoder): ngắt kết nối bộ mã hóa đã chọn.
* Control+F9: kết nối tất cả bộ mã hóa.
* Control+F10 (chỉ khi dùng SAM encoder): ngắt kết nối tất cả các bộ mã hóa.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: bật tắt chế độ để Studio sẽ phát track đầu tiên được chọn khi
  bộ mã hóa được kết nối đến một máy chủ đang phát.
* Control+F11: bật tắt chế độ theo dõi ngầm của bộ mã hóa được chọn.
* Control+F12: mở hộp thoại chọn bộ mã hóa đã xóa (sắp xếp lại các cài đặt
  của nhãn phát và các bộ mã hóa).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

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

The available commands are (most commands support speak on demand):

* A: tự động hóa.
* C (Shift+C trong kiểu phím lệnh của JAWS): tên của track đang phát.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R trong kiểu phím lệnh của JAWS): thời lượng còn lại của danh sách phát
  (nếu có thông báo lỗi, di chuyển đến trình xem danh sách phát và thực hiện
  lệnh này).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: trạng thái truyền siêu dữ liệu.
* Shift+1 đến Shift+4, Shift+0: trạng thái của URL truyền siêu dữ liệu cụ
  thể (0 cho DSP encoder).
* F: Find track (playlist viewer only, does not support speak on demand).
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
* O: Playlist hour over/under by.
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

Important: SPL Controller layer commands are disabled if NVDA is running in
secure mode.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* N: Turn microphone on without fade.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
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

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. Not all settings are available if NVDA is
running in secure mode.

## Hộp thoại hồ sơ phát thanh

Bạn có thể lưu các thiết lập cụ thể cho các chương trình biểu diễn cụ thể
vào các hồ sơ phát thanh. Chúng có thể được quản lý qua hộp thoại các hồ sơ
phát thanh SPL, có thể truy cập bằng cách bấm Alt+NVDA+P từ cửa sổ Studio.

## Chế độ chạm của SPL

If you are using Studio on a touchscreen computer with NVDA installed, you
can perform some Studio commands from the touchscreen. First use three
finger tap to switch to SPL mode, then use the touch commands listed above
to perform commands.

## Version 25.06-LTS

Version 25.06.x is the last release series to support Studio 5.x with future
releases requiring Studio 6.x. Some new features will be backported to
25.06.x if needed.

* NVDA will no longer forget to transfer broadcast profiles while updating
  the add-on (fixing a regression introduced in 25.05).
* Added a new command in SPL Assistant to announce playlist hour over/under
  by in minutes and seconds (O).
* In Studio, the command to step through library scan announcement settings
  has changed from Alt+NVDA+R to Shift+NVDA+R as the former command toggles
  remote access feature in NVDA 2025.1.
* NVDA will no longer play error tones or appear to do nothing when
  performing some SPL Assistant commands after resizing Studio window.
* The user interface for confirmation dialog shown when deleting broadcast
  profiles now resembles NVDA's configuration profile deletion interface.
* NVDA will recognize track column changes introduced in Creator and Track
  Tool 6.11.
* In columns explorer for Creator, "Date Restriction" column is now
  "Restrictions".
* NVDA will no longer play wrong carts when playing them via SPL Controller
  layer.

## Version 25.05

* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Moved ad-on wiki documents such as add-on changelog to the main code
  repository.
* Added close button to playlist snapshots, playlist transcripts, and SPL
  Assistant and Controller layer help screens (NVDA 2025.1 and later).
* NVDA will no longer do nothing or play error tones when announcing weather
  and temperature information in Studio 6.x (SPL Assistant, W).

## Version 25.01

* 64-bit Windows 10 21H2 (build 19044) or later is required.
* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.
* In Studio 6.10 and later, added a new command in SPL Assistant to announce
  control keys enabled/disabled status (Control+D).

## Version 24.03

* Compatible with NVDA 2024.1.
* NVDA 2023.3.3 or later is required.
* Support for StationPlaylist suite 6.10.
* Most commands support speak on demand (NVDA 2024.1) so announcements can
  be spoken in this mode.

## Version 24.01

* The commands for the Encoder Settings dialog for use with the SPL and SAM
  Encoders are now assignable, meaning that you can change them from their
  defaults under the StationPlaylist category in NVDA Menu > Preferences >
  Input Gestures. The ones that are not assignable are the connect and
  disconnect commands. Also, to prevent command conflicts and make much
  easier use of this command on remote servers, the default gesture for
  switching to Studio after connecting is now Control+Shift+F11 (previously
  just F11). All of these can of course still be toggled from the Encoder
  Settings dialog (NVDA+Alt+0 or F12).

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* In Studio's playlist viewer, NVDA will not announce column headers such as
  artist and title if table headers setting is set to either "rows and
  columns" or "columns" in NVDA's document formatting settings panel.

## Các bản phát hành cũ hơn

Please see the [changelog][2] for release notes for old add-on releases.

[1]:
https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
