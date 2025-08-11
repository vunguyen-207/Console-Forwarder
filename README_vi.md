# Console Forwarder

## Tổng quan
Một script Python đơn giản thiết lập một bot Telegram có khả năng thực thi các lệnh shell từ xa thông qua lệnh `/cmd`. Mục đích chính của công cụ này là để bypass và đối phó với các hành động khả nghi từ những screen-sharers trong quá trình kiểm tra máy tính của bạn. Bạn có thể sử dụng bot này để chạy các lệnh trên PC của mình một cách an toàn và kín đáo.

Bằng cách thực thi lệnh qua Telegram, bạn tránh việc cấp toàn quyền điều khiển từ xa, giảm nguy cơ thay đổi trái phép hoặc lộ dữ liệu. Điều này đặc biệt hữu ích trong các tình huống khác nhau, chủ yếu tránh Screen-sharers.

**Lưu ý:** Sử dụng công cụ này một cách có trách nhiệm và đảm bảo bạn có quyền truy cập và thực thi lệnh trên máy. Công cụ này được tạo để chứng minh khái niệm và không nhằm mục đích sử dụng không hợp pháp.

## Tính năng
- Thực thi bất kỳ lệnh shell nào từ xa qua Telegram.
- Thiết lập đơn giản.
- Chạy nền để tránh bị phát hiện trong quá trình chia sẻ màn hình.
- Giới hạn tương tác chỉ ở đầu ra dòng lệnh, ngăn chặn thao túng trực quan.

## Yêu cầu
- Python 3.6 trở lên
- Token Bot Telegram (tạo qua [BotFather](https://t.me/botfather))
- Thư viện đã cài đặt: `python-telegram-bot` (cài qua `pip install python-telegram-bot`)

## Cài đặt
1. Sao chép repo:
   ```
   git clone https://github.com/vunguyen-207/Console-Forwarder/
   cd Console-Forwarder
   ```

2. Cài đặt các requirements:
   ```
   pip install -r requirements.txt
   ```

3. Chỉnh sửa script (`bot.py`) để thay thế `YourToken` và `YourChatID` bằng thông tin của bạn:
   - `YourToken`: Token bot Telegram của bạn.
   - `YourChatID`: ID cuộc trò chuyện mà bot sẽ phản hồi (ví dụ: cuộc trò chuyện cá nhân hoặc nhóm của bạn).

4. Chạy script:
   ```
   python bot.py
   ```

Để chạy ở chế độ nền:
- Trên Windows: Sử dụng `python bot.py` để chạy mà không hiển thị MD.
- Trên Linux/Mac: Sử dụng `nohup python bot.py &` hoặc chuyển đổi thành service.

Để hoạt động ẩn:
- Biên dịch thành executable bằng PyInstaller: `pyinstaller --onefile --noconsole bot.py`
- Thêm vào StartUp hoặc Task Scheduler để đảm bảo chạy ẩn, hoặc thực hiện bằng các cách khác nếu bạn biết.

## Cách sử dụng
1. Khởi động bot bằng cách chạy script.
2. Trong Telegram, gửi `/cmd <command>` đến bot.
   - Ví dụ: `/cmd dir` (trên Windows) hoặc `/cmd ls` (trên Linux).
3. Bot sẽ thực thi lệnh và trả lời với kết quả output.

Trong một phiên screen-share, bot sẽ chạy ẩn, cho phép bạn thực hiện các hành động mà không bị Screen-sharer nhìn thấy hoặc can thiệp trực tiếp.

## Cân nhắc bảo mật
- **Hãy code lại:** Đây là sản phẩm chứng minh khái niệm. Bạn cần recode lại để đảm bảo tính ẩn danh.
- **Kiểm soát truy cập:** Hạn chế ChatID chỉ cho những người đáng tin cậy.
- **Rủi ro lệnh:** Thực thi lệnh tùy ý có thể nguy hiểm; triển khai xác thực bổ sung nếu cần.
- **Đạo đức:** Công cụ này giúp tránh truy cập màn hình không cần thiết, nhưng hãy đảm bảo tuân thủ luật pháp và chính sách.

## Giấy phép
Giấy phép MIT - Xem [LICENSE](LICENSE) để biết chi tiết.

## Đóng góp
Hãy thoải mái tạo fork và gửi requests để cải thiện, chẳng hạn như thêm xác thực hoặc khác.

## Tuyên bố từ chối trách nhiệm
Công cụ này chỉ dành cho mục đích giáo dục và sử dụng hợp pháp. Mình không chịu trách nhiệm cho bất kỳ hành vi lạm dụng nào.
