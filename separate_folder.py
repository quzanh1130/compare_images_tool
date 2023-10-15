import os
import shutil
import json


def separate_folder(src_folder, dst_folder):
    # Duyệt qua tất cả các tệp trong thư mục nguồn
    for filename in os.listdir(src_folder):
        # Tách tên tệp và phần mở rộng
        name, ext = os.path.splitext(filename)

        # Tách phần trước và sau ký tự "_" trong tên tệp
        x1,x2,x3 = name.split("_")

        # Tạo một thư mục cho mỗi prefix duy nhất
        folder_path = os.path.join(dst_folder, x3)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Di chuyển tệp đến thư mục
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(folder_path, filename)
        shutil.move(src_path, dst_path)


def separate_text(input_file_path, output_file_path):
    # Mở tệp văn bản đầu vào để đọc và tạo tệp văn bản đầu ra để ghi
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        # Đọc từng dòng trong tệp đầu vào
        for line in input_file:
            # Phân tích dòng dữ liệu JSON
            data = json.loads(line)

            # Kiểm tra xem "user/angle" có tồn tại trong dữ liệu hay không
            if "user/angle" in data:
                # Lấy giá trị của "user/angle"
                value = data["user/angle"]

                # Ghi giá trị vào tệp đầu ra
                output_file.write(str(value) + "\n")
