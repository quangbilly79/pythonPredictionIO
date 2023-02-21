# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# The four text documents
quanLyTaiChinhSauKetHon = """
Quản lý tài chính sau kết hôn là vấn đề vô cùng quan trọng đối với bất cứ gia đình nào. Để xây dựng được một tổ ấm vững chắc thì các thành viên trong gia đình, đặc biệt là người vợ - tay hòm chìa khóa, phải biết quản lý chi tiêu trong gia đình hợp lý.

Có lẽ khi yêu, mọi thứ trong mắt đôi lứa ngọt ngào và hoàn hảo. Cuộc sống thật đẹp, đủ yêu thương là thừa hạnh phúc. Có điều, khi cùng chung sống dưới một mái nhà, những sự thật tưởng chừng giản đơn nhưng lại rất phũ phàng ập tới, ví dụ như:

- Anh kiếm tiền thì em phải đi chợ và nấu cơm, công bằng thế còn gì!

- Anh trả tiền nhà, sao em không thanh toán hoá đơn tiền điện?

- Phải làm thế nào để thu đủ bù chi đây?

Mâu thuẫn gia đình nảy sinh từ đây, rạn nứt tình cảm cũng bắt nguồn từ đấy. Một thực tế chẳng hề màu hồng mà bất cứ đôi vợ chồng mới cưới nào cũng từng trải qua. Vậy còn bạn, bạn đã sẵn sàng để đương đầu? Bạn đã có được những kỹ năng cần thiết hay chưa?

Với cuốn sách Mẹo quản lý tài chính sau kết hôn sẽ giúp bạn nắm bắt được bí quyết quản lý tài chính đơn giản nhưng vô cùng hiệu quả với các cặp vợ chồng, đặc biệt là cho những đôi mới cưới như:

- Lập kế hoạch tài chính cho tương lai

- Quản lý tài sản chung sau hôn nhân

- Tích luỹ tiền bạc cho kế hoạch sinh con

- Thăng bằng túi tiền trong thời khủng hoảng kinh tế
"""
yeuTrongTinhThucVoiOsho = """
“YÊU” TRONG TỈNH THỨC VỚI OSHO

Một chỉ dẫn “yêu không sợ hãi” đầy ngạc nhiên từ bậc thầy tâm linh Osho.

Những người đói khát trong nhu cầu, những người luôn kỳ vọng ở tình yêu chính là những người đau khổ nhất. Hai kẻ đói khát tìm thấy nhau trong một mối quan hệ yêu đương cùng những kỳ vọng người kia sẽ mang đến cho mình thứ mình cần – về cơ bản sẽ nhanh chóng thất vọng về nhau và cùng mang đến ngục tù khổ đau cho nhau. Trong cuốn sách Yêu, Osho - bậc thầy tâm linh, người được tôn vinh là một trong 1000 người kiến tạo của thế kỷ 20 – đã đưa ra những kiến giải sâu sắc về nhu cầu tâm lý có sức mạnh lớn nhất của nhân loại và “chỉ cho chúng ta cách trải nghiệm tình yêu”.

Trong “Yêu” (Tựa gốc: Being in Love), Osho dẫn người đọc vào một hành trình tìm hiểu táo bạo và đầy sôi nổi về “hiện tượng bí ẩn” mang tên tình yêu. “Điều bạn cần làm không phải là học cách yêu, mà là loại bỏ những cách đánh mất tình yêu”, ông mở đầu. Trước tiên, Osho đưa ra một danh sách những điều “không phải là tình yêu”. Ông phân tích những nhu cầu đi kèm tình yêu thương đã phá hủy tình yêu ra sao, điều này diễn ra kể từ khi con người mới chào đời cho đến khi trưởng thành. Những thói quen đòi hỏi, mong muốn sở hữu người khác, kỳ vọng vào người khác… đều tạo nên sự hủy diệt và xung đột trong mọi mối quan hệ tình cảm, bao gồm cả tình yêu. Theo ông, tình yêu không bao gồm cảm giác ghen tuông, chiếm hữu, cạnh tranh, phụ thuộc, hay việc đòi hỏi người mình yêu phải hoàn hảo. Những điều trên đều khởi nguồn từ cái tôi, và Osho cho rằng: “Khi bạn thật sự yêu ai đó, cái tôi của bạn bắt đầu tan chảy và biến mất”.

Thông qua từng chương của cuốn sách, bạn đọc nhận diện những dấu hiệu của một tình yêu đích thực: Sự cho đi và không chờ đợi được nhận lại, sự trưởng thành cá nhân, đặc biệt là sự tỉnh thức khi yêu. “Việc tỉnh táo nhận biết về bản thể của mình là sự khởi đầu của hành trình hướng tới tình yêu”.
"""
blogChoTamHon = """
Blog cho tâm hồn của Madisyn Taylor là cuốn sách dành cho mỗi ngày vui sống khỏe mạnh và toại nguyện.

Cuộc sống cho ta bao nhiêu niềm vui, tình yêu, ngày tươi sáng thì cũng đem đến ngần ấy đau khổ, buồn bã, chịu đựng. Thay vì đóng chặt cánh cửa trái tim, bạn hãy cương quyết mở rộng lòng mình để những cảm xúc tuôn trào. Hãy khai thác nguồn năng lượng thiêng liêng của tình yêu cuộc sống ẩn chứa trong bạn.

Trong hành trình đi tìm ý nghĩa cuộc sống, ta không thể tránh khỏi những thắc mắc về các vấn đề cơ bản như: Làm thế nào để xây dựng những mối quan hệ chân thành, sâu sắc và bền chặt? Làm thế nào để đương đầu và vượt qua những nỗi đau, những tổn thương trong tâm hồn? Làm thế nào để đạt được những mục tiêu ta hằng khao khát và làm sao để tìm ra lý tưởng cuộc đời mình?

Đúc kết từ kinh nghiệm sống của bản thân cùng nhiều ý tưởng khơi nguồn cảm hứng cho mọi người, tác giả Madisyn Taylor đã dựng nên một bức tranh tổng thể bao gồm những phương cách phát triển toàn diện nhằm khơi dậy nguồn ánh sáng cơ thể, tinh thần và trí tuệ. Những thông điệp từ tập sách này sẽ truyền cảm hứng, giúp bạn tạo lập một cuộc sống tự chủ và là động lực tinh thần hỗ trợ mạnh mẽ cgo bạn trong hành trình cuộc sống.
"""
noiVoiTuoiHaiMuoi = """
Nhất Hạnh mang đến cho bạn đọc một cảm giác ấm áp, chân thành nhưng cũng không kém phần mãnh liệt, sâu sắc.
Những lời chia sẻ của Thiền Sư thấm sâu vào lòng những người trẻ tuổi, khơi gợi những ước mơ hoài bão, khơi dậy sức sống dạt dào trong trái tim của họ, làm bừng cháy những yêu thương. Nói với tuổi hai mươi tìm thấy điểm đồng điệu trong lời thơ của Tố Hữu: "20 tuổi hồn quay trong gió bão/ gân đang xanh và thớ thịt căng da", và sức trẻ đó phải được tỏa sáng trong tình yêu và trách nhiệm với đất nước, trong lý tưởng và khát vọng, trong tình yêu và cuộc sống của mình.

Đọc Nói với tuổi hai mươi - Thích Nhất Hạnh để thấy rằng cuộc đời vô cùng cao quý và tươi đẹp, và các bạn trẻ, hãy sống sao cho khỏi sống hoài, sống phí, để sức trẻ căng tràn của các bạn sẽ hữu ích cho cuộc đời, cho thế gian và nhân loại.
"""
batMiVe12CungHoangDao = """
Theo phương Tây, 12 cung Hoàng Đạo là mười hai cung 30° của Hoàng Đạo, bắt đầu từ điểm xuân phân (một trong những giao điểm của Hoàng Đạo với Xích đạo thiên cầu), còn được gọi là Điểm Đầu của Bạch Dương.

Thứ tự của 12 cung Hoàng Đạo là Bạch Dương, Kim Ngưu, Song Tử, Cự Giải, Sư Tử, Xử Nữ, Thiên Bình, Thiên Yết, Nhân Mã, Ma Kết, Bảo Bình và Song Ngư.

Theo đó, mỗi một cung ứng với một Chòm Sao chiếu mệnh tạo nên 12 tính cách đa dạng, phong phú, không hòa quyện, không trộn lẫn. Dựa vào cung Hoàng Đạo tương ứng với ngày sinh nhật của mỗi người, ngoài việc đoán được tính cách của mỗi người, các nhà chiêm tinh học còn có thể dự đoán được một phần nào đó tương lai của họ trong một năm.
"""
lacMatCoDauXungHi = """
Cảnh Thiên khi xưa là một cô gái mù quáng liều lĩnh vì tình yêu. Sau khi ngã cầu thang rồi “đi đời nhà ma”, Cảnh Thiên tỉnh dậy và trở thành một con người hoàn toàn khác: quyến rũ tuyệt đỉnh, thông minh linh hoạt.

- Với kim chủ: biết co biết duỗi

- Với trà xanh: biết vả biết dìm

- Với "chồng yêu" đẹp trai tàn tật: biết xoa biết bóp

Chiến Lê Xuyên – cậu ba nhà họ Chiến – là người nắm mọi quyền hành trong gia tộc. Anh bị tai nạn nghiêm trọng tới mức tàn tật, phải cưới một cô vợ có tử vi phù hợp về để “thay đổi vận mệnh”.

---

Đêm đến, Cảnh Thiên mò sang phòng anh, bắt đầu cởi quần áo của anh.

Chiến Lê Xuyên: “Nhìn thấy cơ thể của mình, cô ta có biểu cảm gì thế hả?”

Cảnh Thiên: “Ôi gương mặt này! Body này! Nhất định phải cứu!”
"""
docs = [
    quanLyTaiChinhSauKetHon,
    yeuTrongTinhThucVoiOsho,
    blogChoTamHon,
    noiVoiTuoiHaiMuoi,
    batMiVe12CungHoangDao,
    lacMatCoDauXungHi
]

# Initialize the TfidfVectorizer
tfidf = TfidfVectorizer()

# Fit and transform the documents into a matrix of TF-IDF scores
tfidf_matrix = tfidf.fit_transform(docs)

# Calculate the cosine similarity between the first document and all other documents
cosine_similarities = np.dot(tfidf_matrix[0], tfidf_matrix.T).toarray()[0]

# Sort the documents based on their similarity scores
sorted_indices = np.argsort(-cosine_similarities)

# Print the similarity scores
for i in sorted_indices:
    print(f"Document {i+1} similarity score: {cosine_similarities[i]}")

# Document 1 similarity score: 0.9999999999999984
# Document 3 similarity score: 0.2236233790989697
# Document 2 similarity score: 0.20780040764561208
# Document 4 similarity score: 0.16920474178215164
# Document 6 similarity score: 0.15587904257112614
# Document 5 similarity score: 0.0936219137856442