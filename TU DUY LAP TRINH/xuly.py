import random
def motivation(text):
    quotes = ["Làm ít nhưng làm đều, rắn cũng thành rồng 💚","Không sao đâu, từ từ rồi cũng xong 🍃","Bắt đầu là đã thắng nửa chặng đường rồi 🌿"
              ,"Hôm nay làm nhẹ 1 task, mai chill gấp đôi 😎"
              ,"Cứ trườn từng chút, rắn cũng đến đích 🐍","Mọi việc đều bắt đầu từ một dòng ghi chú nhỏ 📝"
              ,"Ngày mai luôn tốt hơn nếu hôm nay chịu bắt đầu 🌿","Hôm nay không hoàn hảo cũng không sao, chỉ cần có cố gắng 💪"
              ,"Bình tĩnh, hít sâu, và làm từng việc một 🍀","Thành công là tổng hợp của những ngày nhỏ năng suất 🌱"
              ,"Mệt thì nghỉ, chứ đừng ngừng tiến 🐍💤","Ngày hôm nay là món quà — hãy dùng nó để tick thêm một task 🎁",
              "Mọi sự thay đổi bắt đầu từ hành động nhỏ 💚","Rắn ngoan chăm task, rắn được nghỉ sớm 🐍✨"]
    if text:
       quote = random.choice(quotes)
    return quote
